#!/usr/bin/env python3
"""
Restructure Tarot files to match Semantic Section System.

Transformations:
1. OPENING: ## Core Correspondences -> ## Qabalistic Position
2. OPENING: ## Introduction -> ## Qabalistic Position
3. DEPTH: ## Synthesis Notes -> ## Esoteric Interpretation
4. PRACTICE: ## Divination Meanings -> ## Divination Use
5. DATA: ## Cross-System Correspondences -> ## Correspondences

Usage:
    python restructure_tarot.py --dry-run  # Preview
    python restructure_tarot.py            # Apply
"""

import re
import argparse
from pathlib import Path

TAROT_PATH = Path("/home/joe/VibologyOS/Library/The Seven Pillars of Understanding/The Tarot")

def process_file(filepath, dry_run=True):
    """Process a single Tarot file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    changes = []

    # 1. OPENING: ## Core Correspondences -> ## Qabalistic Position
    if re.search(r'^## Core Correspondences\s*$', content, re.MULTILINE):
        content = re.sub(r'^## Core Correspondences\s*$', '## Qabalistic Position', content, flags=re.MULTILINE)
        changes.append("  ## Core Correspondences -> ## Qabalistic Position")

    # 2. OPENING: ## Introduction -> ## Qabalistic Position
    if re.search(r'^## Introduction\s*$', content, re.MULTILINE):
        content = re.sub(r'^## Introduction\s*$', '## Qabalistic Position', content, flags=re.MULTILINE)
        changes.append("  ## Introduction -> ## Qabalistic Position")

    # 3. DEPTH: ## Synthesis Notes -> ## Esoteric Interpretation
    if re.search(r'^## Synthesis Notes\s*$', content, re.MULTILINE):
        content = re.sub(r'^## Synthesis Notes\s*$', '## Esoteric Interpretation', content, flags=re.MULTILINE)
        changes.append("  ## Synthesis Notes -> ## Esoteric Interpretation")

    # 4. PRACTICE: ## Divination Meanings -> ## Divination Use
    if re.search(r'^## Divination Meanings\s*$', content, re.MULTILINE):
        content = re.sub(r'^## Divination Meanings\s*$', '## Divination Use', content, flags=re.MULTILINE)
        changes.append("  ## Divination Meanings -> ## Divination Use")

    # 5. DATA: ## Cross-System Correspondences -> ## Correspondences
    if re.search(r'^## Cross-System Correspondences\s*$', content, re.MULTILINE):
        content = re.sub(r'^## Cross-System Correspondences\s*$', '## Correspondences', content, flags=re.MULTILINE)
        changes.append("  ## Cross-System Correspondences -> ## Correspondences")

    if content != original:
        if changes and not dry_run:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

    return changes

def main():
    parser = argparse.ArgumentParser(description='Restructure Tarot files')
    parser.add_argument('--dry-run', action='store_true',
                        help='Preview changes without writing')
    args = parser.parse_args()

    # Get all .md files recursively
    files = sorted(TAROT_PATH.rglob('*.md'))
    print(f"Found {len(files)} Tarot files\n")

    if args.dry_run:
        print("=== DRY RUN MODE ===\n")

    total_changed = 0
    for filepath in files:
        changes = process_file(filepath, dry_run=args.dry_run)
        if changes:
            total_changed += 1
            rel_path = filepath.relative_to(TAROT_PATH)
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
