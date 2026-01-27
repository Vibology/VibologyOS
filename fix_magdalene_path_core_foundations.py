#!/usr/bin/env python3
"""Fix Core Foundations paths in Magdalene Path files."""

import re
from pathlib import Path

MAGDALENE_PATH = Path("Library/The Seven Pillars of Understanding/The Magdalene Path")

# Remove the "Core Foundations/" prefix - files should link directly by name
CORE_FOUNDATIONS_FIXES = {
    "Core Foundations/Inner Authority and Strategy": "Inner Authority and Strategy",
    "Core Foundations/Seven-Coordinate Navigation": "Seven-Coordinate Navigation",
    "Core Foundations/Anima et Algorithm": "Anima et Algorithm",
    "Core Foundations/Vibology": "Vibology",
}

def fix_core_foundations(content):
    """Fix Core Foundations paths."""
    changes = 0
    
    for old, new in CORE_FOUNDATIONS_FIXES.items():
        pattern = rf'\[\[{re.escape(old)}(?:\|[^\]]+)?\]\]'
        count = len(re.findall(pattern, content))
        if count:
            content = re.sub(pattern, rf'[[{new}]]', content)
            changes += count
    
    return content, changes

def main():
    total_files = 0
    total_changes = 0
    
    for md_file in sorted(MAGDALENE_PATH.rglob("*.md")):
        content = md_file.read_text()
        new_content, changes = fix_core_foundations(content)
        
        if changes > 0:
            md_file.write_text(new_content)
            print(f"✓ {md_file.name}: {changes} fixes")
            total_files += 1
            total_changes += changes
    
    print(f"\n{'='*60}")
    print(f"CORE FOUNDATIONS FIX: {total_changes} fixes across {total_files} files")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
