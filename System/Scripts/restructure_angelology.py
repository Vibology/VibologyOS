#!/usr/bin/env python3
"""
Restructure Angelology files to match Semantic Section System.

Transformations:
1. Remove Roman numeral prefixes (## I. X -> ## X)
2. OPENING: ## Overview, ## Introduction*, ## What is Angelology? -> ## Essence
3. DATA: ## Foundational Material -> ## Correspondences
4. PRACTICE: ## Practical Application, ## Practical Mysticism*, ## How to Work with* -> ## Invocation
5. SHADOW: ## Shadow and Distortion*, ## The Shadow of* -> ## Fallen Aspect
6. LINKS: ## Internal Links*, ## *Internal Links* -> ## Cross-References
7. REMOVE: ## Keywords*, ## *Keywords and Themes

Usage:
    python restructure_angelology.py --dry-run  # Preview
    python restructure_angelology.py            # Apply
"""

import os
import re
import argparse
from pathlib import Path

ANGELOLOGY_PATH = Path("/home/joe/VibologyOS/Library/The Seven Pillars of Understanding/Angelology")

def process_file(filepath, dry_run=True):
    """Process a single Angelology file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    changes = []

    # 1. Remove Roman numeral prefixes from H2 sections
    # Match ## I. through ## XXII. (covers all cases found)
    roman_pattern = r'^## ([IVXLC]+)\. (.+)$'
    roman_matches = re.findall(roman_pattern, content, re.MULTILINE)
    if roman_matches:
        content = re.sub(roman_pattern, r'## \2', content, flags=re.MULTILINE)
        changes.append(f"  Removed Roman numerals from {len(roman_matches)} section(s)")

    # 2. OPENING slot transformations
    # ## Overview -> ## Essence
    if re.search(r'^## Overview\s*$', content, re.MULTILINE):
        content = re.sub(r'^## Overview\s*$', '## Essence', content, flags=re.MULTILINE)
        changes.append("  ## Overview -> ## Essence")

    # ## Introduction (plain) -> ## Essence
    if re.search(r'^## Introduction\s*$', content, re.MULTILINE):
        content = re.sub(r'^## Introduction\s*$', '## Essence', content, flags=re.MULTILINE)
        changes.append("  ## Introduction -> ## Essence")

    # ## Introduction: X -> ## Essence
    pattern = r'^## Introduction:.*$'
    if re.search(pattern, content, re.MULTILINE):
        content = re.sub(pattern, '## Essence', content, flags=re.MULTILINE)
        changes.append("  ## Introduction:* -> ## Essence")

    # ## What is Angelology? -> ## Essence
    if re.search(r'^## What is Angelology\?\s*$', content, re.MULTILINE):
        content = re.sub(r'^## What is Angelology\?\s*$', '## Essence', content, flags=re.MULTILINE)
        changes.append("  ## What is Angelology? -> ## Essence")

    # 3. DATA slot transformations
    # ## Foundational Material -> ## Correspondences
    if re.search(r'^## Foundational Material\s*$', content, re.MULTILINE):
        content = re.sub(r'^## Foundational Material\s*$', '## Correspondences', content, flags=re.MULTILINE)
        changes.append("  ## Foundational Material -> ## Correspondences")

    # 4. PRACTICE slot transformations
    # ## Practical Application -> ## Invocation
    if re.search(r'^## Practical Application\s*$', content, re.MULTILINE):
        content = re.sub(r'^## Practical Application\s*$', '## Invocation', content, flags=re.MULTILINE)
        changes.append("  ## Practical Application -> ## Invocation")

    # ## Practical Mysticism (and variants) -> ## Invocation
    pattern = r'^## Practical Mysticism.*$'
    if re.search(pattern, content, re.MULTILINE):
        content = re.sub(pattern, '## Invocation', content, flags=re.MULTILINE)
        changes.append("  ## Practical Mysticism* -> ## Invocation")

    # ## How to Work with X -> ## Invocation
    pattern = r'^## How to Work with.*$'
    if re.search(pattern, content, re.MULTILINE):
        content = re.sub(pattern, '## Invocation', content, flags=re.MULTILINE)
        changes.append("  ## How to Work with* -> ## Invocation")

    # ## Practical Magical Operations -> ## Invocation
    if re.search(r'^## Practical Magical Operations\s*$', content, re.MULTILINE):
        content = re.sub(r'^## Practical Magical Operations\s*$', '## Invocation', content, flags=re.MULTILINE)
        changes.append("  ## Practical Magical Operations -> ## Invocation")

    # 5. SHADOW slot transformations
    # ## Shadow and Distortion (and variants) -> ## Fallen Aspect
    pattern = r'^## Shadow and Distortion.*$'
    if re.search(pattern, content, re.MULTILINE):
        content = re.sub(pattern, '## Fallen Aspect', content, flags=re.MULTILINE)
        changes.append("  ## Shadow and Distortion* -> ## Fallen Aspect")

    # ## The Shadow of X -> ## Fallen Aspect
    pattern = r'^## The Shadow of.*$'
    if re.search(pattern, content, re.MULTILINE):
        content = re.sub(pattern, '## Fallen Aspect', content, flags=re.MULTILINE)
        changes.append("  ## The Shadow of* -> ## Fallen Aspect")

    # 6. LINKS slot transformations
    # ## Internal Links (and variants) -> ## Cross-References
    pattern = r'^## (?:Internal Links|.*Internal Links.*)\s*$'
    if re.search(pattern, content, re.MULTILINE):
        content = re.sub(pattern, '## Cross-References', content, flags=re.MULTILINE)
        changes.append("  ## *Internal Links* -> ## Cross-References")

    # 7. Remove Keywords sections
    # ## Keywords and Themes (and variants)
    # Match the section header and all content until the next ## or end of file
    pattern = r'\n## (?:Keywords and Themes|Keywords)\s*\n(?:(?!##).)*?(?=\n##|\Z)'
    if re.search(pattern, content, re.DOTALL):
        content = re.sub(pattern, '\n', content, flags=re.DOTALL)
        changes.append("  Removed ## Keywords* section")

    # 8. Additional cleanup: ## Cross-System Correspondences appears in some files
    # Keep it for now as it maps to Pillar Integration or can stay as subsection

    # 9. Cleanup: ## Individual Order Entries, ## Individual Archangel Entries
    # These are navigation sections - keep them but could demote to H3 in future

    # 10. ## The Gift of X -> ## The Gift of Integration (standardize)
    pattern = r'^## The Gift of (?!Integration).*$'
    matches = re.findall(pattern, content, re.MULTILINE)
    if matches:
        content = re.sub(pattern, '## The Gift of Integration', content, flags=re.MULTILINE)
        changes.append(f"  ## The Gift of* -> ## The Gift of Integration ({len(matches)} instance(s))")

    # 11. ## A Prayer to X -> keep but note for potential consolidation under Invocation
    # (These are good content, will handle manually if needed)

    if content != original:
        if changes and not dry_run:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

    return changes

def main():
    parser = argparse.ArgumentParser(description='Restructure Angelology files')
    parser.add_argument('--dry-run', action='store_true',
                        help='Preview changes without writing')
    args = parser.parse_args()

    # Get all .md files recursively
    files = sorted(ANGELOLOGY_PATH.rglob('*.md'))
    print(f"Found {len(files)} Angelology files\n")

    if args.dry_run:
        print("=== DRY RUN MODE ===\n")

    total_changed = 0
    for filepath in files:
        changes = process_file(filepath, dry_run=args.dry_run)
        if changes:
            total_changed += 1
            rel_path = filepath.relative_to(ANGELOLOGY_PATH)
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
