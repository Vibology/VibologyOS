#!/usr/bin/env python3
"""
Restructure Personal Mythos files to match Semantic Section System.

Transformations:
1. Remove "Section X:" prefixes (## Section 1: X -> ## X)
2. Remove "X." numeric prefixes (## 1. X -> ## X)
3. Remove Roman numeral prefixes (## I. X -> ## X)
4. OPENING: ## Foundational Material -> ## Overview
5. DATA: ## Core Correspondences -> ## Archetypal Cast
6. DEPTH: ## Synthesis Notes/Subsections -> ## Jungian Analysis
7. DEPTH: ## Psychological Dynamics & Transformation -> ## Jungian Analysis
8. SHADOW: ## Gender Dynamics -> ## Shadow Dynamics
9. PRACTICE: ## Practical Application & Shadow Work -> ## Practical Application
10. SOURCES: ## Sources & Further Reading -> ## Sources

Usage:
    python restructure_personal_mythos.py --dry-run  # Preview
    python restructure_personal_mythos.py            # Apply
"""

import re
import argparse
from pathlib import Path

PERSONAL_MYTHOS_PATH = Path("/home/joe/VibologyOS/Library/The Seven Pillars of Understanding/Personal Mythos")

def process_file(filepath, dry_run=True):
    """Process a single Personal Mythos file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    changes = []

    # 1. Remove "Section X:" prefixes (e.g., ## Section 1: Foundational -> ## Foundational)
    pattern = r'^## Section \d+:\s*(.+)$'
    matches = re.findall(pattern, content, re.MULTILINE)
    if matches:
        content = re.sub(pattern, r'## \1', content, flags=re.MULTILINE)
        changes.append(f"  Removed 'Section X:' prefixes ({len(matches)} sections)")

    # 2. Remove "X." numeric prefixes (e.g., ## 1. Foundational -> ## Foundational)
    pattern = r'^## \d+\.\s+(.+)$'
    matches = re.findall(pattern, content, re.MULTILINE)
    if matches:
        content = re.sub(pattern, r'## \1', content, flags=re.MULTILINE)
        changes.append(f"  Removed 'X.' prefixes ({len(matches)} sections)")

    # 3. Remove Roman numeral prefixes (## I. X -> ## X, ## V. X -> ## X)
    pattern = r'^## ([IVXLC]+)\.\s+(.+)$'
    matches = re.findall(pattern, content, re.MULTILINE)
    if matches:
        content = re.sub(pattern, r'## \2', content, flags=re.MULTILINE)
        changes.append(f"  Removed Roman numeral prefixes ({len(matches)} sections)")

    # 4. OPENING: ## Foundational Material -> ## Overview
    if re.search(r'^## Foundational Material\s*$', content, re.MULTILINE):
        content = re.sub(r'^## Foundational Material\s*$', '## Overview', content, flags=re.MULTILINE)
        changes.append("  ## Foundational Material -> ## Overview")

    # 5. DATA: ## Core Correspondences -> ## Archetypal Cast
    if re.search(r'^## Core Correspondences\s*$', content, re.MULTILINE):
        content = re.sub(r'^## Core Correspondences\s*$', '## Archetypal Cast', content, flags=re.MULTILINE)
        changes.append("  ## Core Correspondences -> ## Archetypal Cast")

    # 6. DEPTH: ## Synthesis Notes -> ## Jungian Analysis
    if re.search(r'^## Synthesis Notes\s*$', content, re.MULTILINE):
        content = re.sub(r'^## Synthesis Notes\s*$', '## Jungian Analysis', content, flags=re.MULTILINE)
        changes.append("  ## Synthesis Notes -> ## Jungian Analysis")

    # 6b. DEPTH: ## Synthesis Subsections -> ## Jungian Analysis
    if re.search(r'^## Synthesis Subsections\s*$', content, re.MULTILINE):
        content = re.sub(r'^## Synthesis Subsections\s*$', '## Jungian Analysis', content, flags=re.MULTILINE)
        changes.append("  ## Synthesis Subsections -> ## Jungian Analysis")

    # 6c. DEPTH: ## Psychological Dynamics & Transformation -> ## Jungian Analysis
    if re.search(r'^## Psychological Dynamics & Transformation\s*$', content, re.MULTILINE):
        content = re.sub(r'^## Psychological Dynamics & Transformation\s*$', '## Jungian Analysis', content, flags=re.MULTILINE)
        changes.append("  ## Psychological Dynamics & Transformation -> ## Jungian Analysis")

    # 7. SHADOW: ## Gender Dynamics -> ## Shadow Dynamics
    if re.search(r'^## Gender Dynamics\s*$', content, re.MULTILINE):
        content = re.sub(r'^## Gender Dynamics\s*$', '## Shadow Dynamics', content, flags=re.MULTILINE)
        changes.append("  ## Gender Dynamics -> ## Shadow Dynamics")

    # 8. PRACTICE: ## Practical Application & Shadow Work -> ## Practical Application
    if re.search(r'^## Practical Application & Shadow Work\s*$', content, re.MULTILINE):
        content = re.sub(r'^## Practical Application & Shadow Work\s*$', '## Practical Application', content, flags=re.MULTILINE)
        changes.append("  ## Practical Application & Shadow Work -> ## Practical Application")

    # 9. SOURCES: ## Sources & Further Reading -> ## Sources
    if re.search(r'^## Sources & Further Reading\s*$', content, re.MULTILINE):
        content = re.sub(r'^## Sources & Further Reading\s*$', '## Sources', content, flags=re.MULTILINE)
        changes.append("  ## Sources & Further Reading -> ## Sources")

    if content != original:
        if changes and not dry_run:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

    return changes

def main():
    parser = argparse.ArgumentParser(description='Restructure Personal Mythos files')
    parser.add_argument('--dry-run', action='store_true',
                        help='Preview changes without writing')
    args = parser.parse_args()

    # Get all .md files recursively
    files = sorted(PERSONAL_MYTHOS_PATH.rglob('*.md'))
    print(f"Found {len(files)} Personal Mythos files\n")

    if args.dry_run:
        print("=== DRY RUN MODE ===\n")

    total_changed = 0
    for filepath in files:
        changes = process_file(filepath, dry_run=args.dry_run)
        if changes:
            total_changed += 1
            rel_path = filepath.relative_to(PERSONAL_MYTHOS_PATH)
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
