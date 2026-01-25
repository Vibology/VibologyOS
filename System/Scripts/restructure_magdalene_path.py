#!/usr/bin/env python3
"""
Restructure Magdalene Path files to match Semantic Section System.

Transforms:
1. ## Introduction: X -> ## Core Teaching (OPENING)
2. ## Historical Context: X -> ## Gospel Foundation (DATA) + demote subsections
3. ## Shadows of X -> ## Kenotic Descent (SHADOW)
4. ## Keywords -> REMOVE (content in YAML tags)
5. Keep ## Cross-References, ## Sources (already correct)

Usage:
    python restructure_magdalene_path.py --dry-run  # Preview
    python restructure_magdalene_path.py            # Apply
"""

import os
import re
import argparse
from pathlib import Path

MAGDALENE_PATH = Path("/home/joe/VibologyOS/Library/The Seven Pillars of Understanding/The Magdalene Path")

def process_file(filepath, dry_run=True):
    """Process a single Magdalene Path file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    changes = []

    # 1. Rename Introduction sections to Core Teaching
    pattern = r'^## Introduction:.*$'
    if re.search(pattern, content, re.MULTILINE):
        content = re.sub(pattern, '## Core Teaching', content, flags=re.MULTILINE)
        changes.append("  ## Introduction:* -> ## Core Teaching")

    # 2. Rename "Historical Context:" sections to "Gospel Foundation"
    pattern = r'^## Historical Context:.*$'
    if re.search(pattern, content, re.MULTILINE):
        content = re.sub(pattern, '## Gospel Foundation', content, flags=re.MULTILINE)
        changes.append("  ## Historical Context:* -> ## Gospel Foundation")

    # 3. Rename "Shadows of X" to "Kenotic Descent"
    pattern = r'^## Shadows of .*$'
    if re.search(pattern, content, re.MULTILINE):
        content = re.sub(pattern, '## Kenotic Descent', content, flags=re.MULTILINE)
        changes.append("  ## Shadows of* -> ## Kenotic Descent")

    # 4. Rename "Part III: Shadows of the Path" to "Kenotic Descent"
    pattern = r'^## Part III: Shadows of the Path\s*$'
    if re.search(pattern, content, re.MULTILINE):
        content = re.sub(pattern, '## Kenotic Descent', content, flags=re.MULTILINE)
        changes.append("  ## Part III: Shadows -> ## Kenotic Descent")

    # 5. Rename "The Mechanics:" sections to "Mystical Depth"
    pattern = r'^## The Mechanics:.*$'
    if re.search(pattern, content, re.MULTILINE):
        content = re.sub(pattern, '## Mystical Depth', content, flags=re.MULTILINE)
        changes.append("  ## The Mechanics:* -> ## Mystical Depth")

    # 6. Remove ## Keywords section entirely (content is in YAML tags)
    pattern = r'\n## Keywords\n+\*\*[^*]+\*\*\n*---\n'
    if re.search(pattern, content):
        content = re.sub(pattern, '\n---\n', content)
        changes.append("  Removed ## Keywords section")

    # Also handle Keywords without the bold formatting
    pattern = r'\n## Keywords\n+[^\n#]+\n*---\n'
    if re.search(pattern, content):
        content = re.sub(pattern, '\n---\n', content)
        changes.append("  Removed ## Keywords section (variant)")

    # 7. Rename "Cross-System Correspondences" to be under a semantic parent
    # For Magdalene Path, this becomes part of "Mystical Depth"
    # But since it often appears at the end before Cross-References, we can rename it
    pattern = r'^## Cross-System Correspondences\s*$'
    if re.search(pattern, content, re.MULTILINE):
        content = re.sub(pattern, '## Pillar Integration', content, flags=re.MULTILINE)
        changes.append("  ## Cross-System Correspondences -> ## Pillar Integration")

    # 8. Rename various practice-related sections to "Spiritual Practice"
    for old_name in [
        r'## Core Practices',
        r'## Practices of the Bridal Chamber',
        r'## Practical Anointing',
        r'## Daily Practices:.*',
        r'## Practices at Each Stage.*',
        r'## Relationship Practices.*',
    ]:
        if re.search(f'^{old_name}$', content, re.MULTILINE):
            # Don't rename these - they're good subsections
            # But we could wrap them under a "Spiritual Practice" header if needed
            pass

    if changes and not dry_run:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

    return changes

def main():
    parser = argparse.ArgumentParser(description='Restructure Magdalene Path files')
    parser.add_argument('--dry-run', action='store_true',
                        help='Preview changes without writing')
    args = parser.parse_args()

    files = sorted(MAGDALENE_PATH.glob('*.md'))
    print(f"Found {len(files)} Magdalene Path files\n")

    if args.dry_run:
        print("=== DRY RUN MODE ===\n")

    total_changed = 0
    for filepath in files:
        changes = process_file(filepath, dry_run=args.dry_run)
        if changes:
            total_changed += 1
            print(f"{filepath.name}")
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
