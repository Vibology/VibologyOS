#!/usr/bin/env python3
"""
Fix ACTUAL dead wikilinks in Astrology Signs files.
"""

import re
from pathlib import Path

SIGNS_DIR = Path("Library/The Seven Pillars of Understanding/Astrology/Signs")

WIKILINK_FIXES = {
    # HD Centers - correct names
    r'\[\[Ajna Center\]\]': '[[Ajna]]',
    r'\[\[G-Center\]\]': '[[G Center]]',

    # Tarot cards - add Roman numerals
    r'\[\[Temperance \(Tarot\)\]\]': '[[Temperance (XIV)|Temperance]]',
    r'\[\[The Chariot \(Tarot\)\]\]': '[[The Chariot (VII)|The Chariot]]',
}

def fix_wikilinks_in_file(filepath):
    """Fix wikilinks in a single file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    changes = []

    for pattern, replacement in WIKILINK_FIXES.items():
        matches = re.findall(pattern, content)
        if matches:
            content = re.sub(pattern, replacement, content)
            changes.append(f"  {pattern} → {replacement} ({len(matches)}x)")

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return changes
    return None

def main():
    """Process all Signs files."""
    print("Fixing ACTUAL dead wikilinks in Astrology Signs files...\n")

    files_changed = 0
    total_fixes = 0

    for md_file in sorted(SIGNS_DIR.glob("*.md")):
        changes = fix_wikilinks_in_file(md_file)
        if changes:
            files_changed += 1
            total_fixes += sum(1 for _ in changes)
            print(f"✓ {md_file.name}")
            for change in changes:
                print(change)
            print()

    print(f"\nSummary:")
    print(f"  Files changed: {files_changed}")
    print(f"  Total link types fixed: {total_fixes}")
    print(f"\nDone!")

if __name__ == "__main__":
    main()
