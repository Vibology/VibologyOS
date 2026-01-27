#!/usr/bin/env python3
"""Fix the final 3 Logos references - convert to plain text."""

import re
from pathlib import Path

PERSONAL_MYTHOS = Path("Library/The Seven Pillars of Understanding/Personal Mythos")

files_to_fix = [
    "Individuation Process/Encounter with Anima-Animus.md",
    "Jungian Archetypes/The Animus.md",
    "Jungian Archetypes/The Wise Old Man.md",
]

def fix_logos(content):
    """Convert [[Logos]] to plain text."""
    pattern = r'\[\[Logos\]\]'
    count = len(re.findall(pattern, content))
    if count:
        content = re.sub(pattern, 'Logos', content)
        return content, count
    return content, 0

total_changes = 0
for file_rel in files_to_fix:
    file_path = PERSONAL_MYTHOS / file_rel
    content = file_path.read_text()
    new_content, changes = fix_logos(content)
    
    if changes > 0:
        file_path.write_text(new_content)
        print(f"✓ {file_rel}: {changes} fixes")
        total_changes += changes

print(f"\n{'='*60}")
print(f"LOGOS FINAL FIX: {total_changes} fixes")
print(f"{'='*60}")
