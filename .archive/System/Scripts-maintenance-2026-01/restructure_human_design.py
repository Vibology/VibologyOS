#!/usr/bin/env python3
"""
Restructure Human Design files to match Semantic Section System.

Transformations:
1. OPENING: ## Ra's Mechanical Definition -> ## Ra's Definition
2. OPENING: ## Definition -> ## Ra's Definition
3. SHADOW: ## Conditioning and Not-Self Patterns -> ## Not-Self Patterns
4. PRACTICE: ## Strategy and Authority Integration -> ## Strategy Integration
5. PRACTICE: ## Practical Guidance -> ## Strategy Integration

Usage:
    python restructure_human_design.py --dry-run  # Preview
    python restructure_human_design.py            # Apply
"""

import re
import argparse
from pathlib import Path

HD_PATH = Path("/home/joe/VibologyOS/Library/The Seven Pillars of Understanding/Human Design")

def process_file(filepath, dry_run=True):
    """Process a single Human Design file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    changes = []

    # 1. OPENING: ## Ra's Mechanical Definition -> ## Ra's Definition
    if re.search(r"^## Ra's Mechanical Definition\s*$", content, re.MULTILINE):
        content = re.sub(r"^## Ra's Mechanical Definition\s*$", "## Ra's Definition", content, flags=re.MULTILINE)
        changes.append("  ## Ra's Mechanical Definition -> ## Ra's Definition")

    # 2. OPENING: ## Definition -> ## Ra's Definition
    if re.search(r'^## Definition\s*$', content, re.MULTILINE):
        content = re.sub(r'^## Definition\s*$', "## Ra's Definition", content, flags=re.MULTILINE)
        changes.append("  ## Definition -> ## Ra's Definition")

    # 3. SHADOW: ## Conditioning and Not-Self Patterns -> ## Not-Self Patterns
    if re.search(r'^## Conditioning and Not-Self Patterns\s*$', content, re.MULTILINE):
        content = re.sub(r'^## Conditioning and Not-Self Patterns\s*$', '## Not-Self Patterns', content, flags=re.MULTILINE)
        changes.append("  ## Conditioning and Not-Self Patterns -> ## Not-Self Patterns")

    # 4. PRACTICE: ## Strategy and Authority Integration -> ## Strategy Integration
    if re.search(r'^## Strategy and Authority Integration\s*$', content, re.MULTILINE):
        content = re.sub(r'^## Strategy and Authority Integration\s*$', '## Strategy Integration', content, flags=re.MULTILINE)
        changes.append("  ## Strategy and Authority Integration -> ## Strategy Integration")

    # 5. PRACTICE: ## Practical Guidance -> ## Strategy Integration
    if re.search(r'^## Practical Guidance\s*$', content, re.MULTILINE):
        content = re.sub(r'^## Practical Guidance\s*$', '## Strategy Integration', content, flags=re.MULTILINE)
        changes.append("  ## Practical Guidance -> ## Strategy Integration")

    # 6. DATA: ## Cross-System Correspondences -> ## Correspondences
    if re.search(r'^## Cross-System Correspondences\s*$', content, re.MULTILINE):
        content = re.sub(r'^## Cross-System Correspondences\s*$', '## Correspondences', content, flags=re.MULTILINE)
        changes.append("  ## Cross-System Correspondences -> ## Correspondences")

    # 7. Remove ## Keywords section (redundant with YAML tags)
    pattern = r'\n## Keywords\s*\n(?:(?!##).)*?(?=\n##|\Z)'
    if re.search(pattern, content, re.DOTALL):
        content = re.sub(pattern, '\n', content, flags=re.DOTALL)
        changes.append("  Removed ## Keywords section")

    if content != original:
        if changes and not dry_run:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

    return changes

def main():
    parser = argparse.ArgumentParser(description='Restructure Human Design files')
    parser.add_argument('--dry-run', action='store_true',
                        help='Preview changes without writing')
    args = parser.parse_args()

    # Get all .md files recursively
    files = sorted(HD_PATH.rglob('*.md'))
    print(f"Found {len(files)} Human Design files\n")

    if args.dry_run:
        print("=== DRY RUN MODE ===\n")

    total_changed = 0
    for filepath in files:
        changes = process_file(filepath, dry_run=args.dry_run)
        if changes:
            total_changed += 1
            rel_path = filepath.relative_to(HD_PATH)
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
