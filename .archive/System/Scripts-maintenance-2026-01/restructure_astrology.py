#!/usr/bin/env python3
"""
Restructure Astrology files to match Semantic Section System.

Transformations:
1. OPENING: ## What is Astrology? -> ## Archetypal Essence
2. DEPTH: ## Psychological & Jungian Depth -> ## Psychological Depth
3. SHADOW: ## Evolved vs. Unevolved Expression -> ## Shadow Expression
4. SHADOW: ## Shadow and * (variants) -> ## Shadow Expression
5. PRACTICE: ## Invitation for Contemplation -> ## Interpretation Guide
6. PRACTICE: ## Practical Guidance -> ## Interpretation Guide
7. LINKS: ## Internal Links* -> ## Cross-References

Usage:
    python restructure_astrology.py --dry-run  # Preview
    python restructure_astrology.py            # Apply
"""

import re
import argparse
from pathlib import Path

ASTROLOGY_PATH = Path("/home/joe/VibologyOS/Library/The Seven Pillars of Understanding/Astrology")

def process_file(filepath, dry_run=True):
    """Process a single Astrology file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    changes = []

    # 1. OPENING: ## What is Astrology? -> ## Archetypal Essence
    if re.search(r'^## What is Astrology\?\s*$', content, re.MULTILINE):
        content = re.sub(r'^## What is Astrology\?\s*$', '## Archetypal Essence', content, flags=re.MULTILINE)
        changes.append("  ## What is Astrology? -> ## Archetypal Essence")

    # 2. DEPTH: ## Psychological & Jungian Depth -> ## Psychological Depth
    if re.search(r'^## Psychological & Jungian Depth\s*$', content, re.MULTILINE):
        content = re.sub(r'^## Psychological & Jungian Depth\s*$', '## Psychological Depth', content, flags=re.MULTILINE)
        changes.append("  ## Psychological & Jungian Depth -> ## Psychological Depth")

    # 3. SHADOW: ## Evolved vs. Unevolved Expression -> ## Shadow Expression
    if re.search(r'^## Evolved vs\. Unevolved Expression\s*$', content, re.MULTILINE):
        content = re.sub(r'^## Evolved vs\. Unevolved Expression\s*$', '## Shadow Expression', content, flags=re.MULTILINE)
        changes.append("  ## Evolved vs. Unevolved Expression -> ## Shadow Expression")

    # 4. SHADOW: Various "## Shadow and X" patterns -> ## Shadow Expression
    shadow_patterns = [
        r'^## Shadow and Inflation\s*$',
        r'^## Shadow and the Maternal Complex\s*$',
        r'^## Shadow and the Trickster\'s Trap\s*$',
        r'^## Shadow Expressions and the Martial Wound\s*$',
        r'^## Shadow Expressions.*$',
        r'^## Shadow and .*$',
    ]
    for pattern in shadow_patterns:
        if re.search(pattern, content, re.MULTILINE):
            content = re.sub(pattern, '## Shadow Expression', content, flags=re.MULTILINE)
            changes.append(f"  {pattern.replace('^', '').replace('$', '').replace(r'\s*', '')} -> ## Shadow Expression")
            break  # Only report one shadow rename per file

    # 5. PRACTICE: ## Invitation for Contemplation -> ## Interpretation Guide
    if re.search(r'^## Invitation for Contemplation\s*$', content, re.MULTILINE):
        content = re.sub(r'^## Invitation for Contemplation\s*$', '## Interpretation Guide', content, flags=re.MULTILINE)
        changes.append("  ## Invitation for Contemplation -> ## Interpretation Guide")

    # 6. PRACTICE: ## Practical Guidance -> ## Interpretation Guide
    if re.search(r'^## Practical Guidance\s*$', content, re.MULTILINE):
        content = re.sub(r'^## Practical Guidance\s*$', '## Interpretation Guide', content, flags=re.MULTILINE)
        changes.append("  ## Practical Guidance -> ## Interpretation Guide")

    # 7. LINKS: ## Internal Links & Related Concepts -> ## Cross-References
    if re.search(r'^## Internal Links.*$', content, re.MULTILINE):
        content = re.sub(r'^## Internal Links.*$', '## Cross-References', content, flags=re.MULTILINE)
        changes.append("  ## Internal Links* -> ## Cross-References")

    if content != original:
        if changes and not dry_run:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

    return changes

def main():
    parser = argparse.ArgumentParser(description='Restructure Astrology files')
    parser.add_argument('--dry-run', action='store_true',
                        help='Preview changes without writing')
    args = parser.parse_args()

    # Get all .md files recursively
    files = sorted(ASTROLOGY_PATH.rglob('*.md'))
    print(f"Found {len(files)} Astrology files\n")

    if args.dry_run:
        print("=== DRY RUN MODE ===\n")

    total_changed = 0
    for filepath in files:
        changes = process_file(filepath, dry_run=args.dry_run)
        if changes:
            total_changed += 1
            rel_path = filepath.relative_to(ASTROLOGY_PATH)
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
