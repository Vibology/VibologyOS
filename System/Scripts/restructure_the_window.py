#!/usr/bin/env python3
"""
Restructure The Window files to match Semantic Section System.

Transformations:
1. OPENING: ## Card Symbolism & Meaning -> ## Core Domain
2. OPENING: ## Portal Symbolism & Meaning -> ## Core Domain
3. OPENING: ## House Symbolism & Meaning -> ## Core Domain
4. DEPTH: ## Synthesis & Integration -> ## Synthesis Notes
5. PRACTICE: ## Divination Meanings -> ## Oracle Reading
6. PRACTICE: ## Divinatory Meaning -> ## Oracle Reading
7. PRACTICE: ## Divination Use -> ## Oracle Reading
8. DATA: ## Cross-System Correspondences -> ## Correspondences

Usage:
    python restructure_the_window.py --dry-run  # Preview
    python restructure_the_window.py            # Apply
"""

import re
import argparse
from pathlib import Path

WINDOW_PATH = Path("/home/joe/VibologyOS/Library/The Seven Pillars of Understanding/The Window")

def process_file(filepath, dry_run=True):
    """Process a single Window file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    changes = []

    # 1. OPENING: ## Card Symbolism & Meaning -> ## Core Domain
    if re.search(r'^## Card Symbolism & Meaning\s*$', content, re.MULTILINE):
        content = re.sub(r'^## Card Symbolism & Meaning\s*$', '## Core Domain', content, flags=re.MULTILINE)
        changes.append("  ## Card Symbolism & Meaning -> ## Core Domain")

    # 2. OPENING: ## Portal Symbolism & Meaning -> ## Core Domain
    if re.search(r'^## Portal Symbolism & Meaning\s*$', content, re.MULTILINE):
        content = re.sub(r'^## Portal Symbolism & Meaning\s*$', '## Core Domain', content, flags=re.MULTILINE)
        changes.append("  ## Portal Symbolism & Meaning -> ## Core Domain")

    # 3. OPENING: ## House Symbolism & Meaning -> ## Core Domain
    if re.search(r'^## House Symbolism & Meaning\s*$', content, re.MULTILINE):
        content = re.sub(r'^## House Symbolism & Meaning\s*$', '## Core Domain', content, flags=re.MULTILINE)
        changes.append("  ## House Symbolism & Meaning -> ## Core Domain")

    # 4. DEPTH: ## Synthesis & Integration -> ## Synthesis Notes
    if re.search(r'^## Synthesis & Integration\s*$', content, re.MULTILINE):
        content = re.sub(r'^## Synthesis & Integration\s*$', '## Synthesis Notes', content, flags=re.MULTILINE)
        changes.append("  ## Synthesis & Integration -> ## Synthesis Notes")

    # 5. PRACTICE: ## Divination Meanings -> ## Oracle Reading
    if re.search(r'^## Divination Meanings\s*$', content, re.MULTILINE):
        content = re.sub(r'^## Divination Meanings\s*$', '## Oracle Reading', content, flags=re.MULTILINE)
        changes.append("  ## Divination Meanings -> ## Oracle Reading")

    # 6. PRACTICE: ## Divinatory Meaning -> ## Oracle Reading
    if re.search(r'^## Divinatory Meaning\s*$', content, re.MULTILINE):
        content = re.sub(r'^## Divinatory Meaning\s*$', '## Oracle Reading', content, flags=re.MULTILINE)
        changes.append("  ## Divinatory Meaning -> ## Oracle Reading")

    # 7. PRACTICE: ## Divination Use -> ## Oracle Reading
    if re.search(r'^## Divination Use\s*$', content, re.MULTILINE):
        content = re.sub(r'^## Divination Use\s*$', '## Oracle Reading', content, flags=re.MULTILINE)
        changes.append("  ## Divination Use -> ## Oracle Reading")

    # 8. DATA: ## Cross-System Correspondences -> ## Correspondences
    if re.search(r'^## Cross-System Correspondences\s*$', content, re.MULTILINE):
        content = re.sub(r'^## Cross-System Correspondences\s*$', '## Correspondences', content, flags=re.MULTILINE)
        changes.append("  ## Cross-System Correspondences -> ## Correspondences")

    if content != original:
        if changes and not dry_run:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

    return changes

def main():
    parser = argparse.ArgumentParser(description='Restructure The Window files')
    parser.add_argument('--dry-run', action='store_true',
                        help='Preview changes without writing')
    args = parser.parse_args()

    # Get all .md files recursively
    files = sorted(WINDOW_PATH.rglob('*.md'))
    print(f"Found {len(files)} Window files\n")

    if args.dry_run:
        print("=== DRY RUN MODE ===\n")

    total_changed = 0
    for filepath in files:
        changes = process_file(filepath, dry_run=args.dry_run)
        if changes:
            total_changed += 1
            rel_path = filepath.relative_to(WINDOW_PATH)
            print(f"{rel_path}")
            for change in changes:
                print(change)
            print()

    print("=" * 50)
    print(f"Files {'to be ' if args.dry_run else ''}modified: {total_changed}")
    if args.dry_run:
        print("\n[DRY RUN] No files modified. Run without --dry-run to apply.")
    else:
        print(f"\n[COMPLETE] {total_changed} files updated.")

if __name__ == "__main__":
    main()
