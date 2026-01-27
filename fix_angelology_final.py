#!/usr/bin/env python3
"""Fix final 6 Angelology dead links."""

import re
from pathlib import Path

ANGELOLOGY = Path("Library/The Seven Pillars of Understanding/Angelology")

# Fix escaped bracket at end
def fix_trailing_escaped_bracket(content):
    """Fix [[Link\]] → [[Link]]"""
    pattern = r'\[\[([^\]]+)\\\]\]'
    count = len(re.findall(pattern, content))
    if count:
        content = re.sub(pattern, r'[[\1]]', content)
    return content, count

# Convert long Window path and Sword reference to plain text
LONG_PATHS_TO_PLAIN = [
    "The Seven Pillars of Understanding/The Window/The Six Lower Houses/House of the Sea/Overview",
    "The Sword of Discrimination",
]

def apply_final_fixes(content):
    """Apply final fixes."""
    total_changes = 0
    
    # 1. Fix trailing escaped brackets
    content, changes = fix_trailing_escaped_bracket(content)
    total_changes += changes
    
    # 2. Convert long paths to plain text
    for term in LONG_PATHS_TO_PLAIN:
        pattern = rf'\[\[{re.escape(term)}\]\]'
        count = len(re.findall(pattern, content))
        if count:
            # Extract just the last part for display
            if "House of the Sea" in term:
                content = re.sub(pattern, "House of the Sea", content)
            else:
                content = re.sub(pattern, term.split("/")[-1], content)
            total_changes += count
    
    return content, total_changes

def main():
    total_files = 0
    total_changes = 0
    
    for md_file in sorted(ANGELOLOGY.rglob("*.md")):
        content = md_file.read_text()
        new_content, changes = apply_final_fixes(content)
        
        if changes > 0:
            md_file.write_text(new_content)
            rel_path = md_file.relative_to(ANGELOLOGY)
            print(f"✓ {rel_path}: {changes} fixes")
            total_files += 1
            total_changes += changes
    
    print(f"\n{'='*60}")
    print(f"ANGELOLOGY FINAL: {total_changes} fixes across {total_files} files")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
