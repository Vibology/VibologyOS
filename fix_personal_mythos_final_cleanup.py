#!/usr/bin/env python3
"""Final cleanup: Fix last Tarot cards and remaining edge cases."""

import re
from pathlib import Path

PERSONAL_MYTHOS = Path("Library/The Seven Pillars of Understanding/Personal Mythos")

# Last Tarot cards
LAST_TAROT_FIXES = {
    "The Chariot": "The Chariot (VII)",
    "The Hermit": "The Hermit (IX)",
    "The High Priestess": "The High Priestess (II)",
    "The Lovers": "The Lovers (VI)",
    "The Magician": "The Magician (I)",
}

# Core Foundations path fix
PATH_FIXES = {
    "Core Foundations/Logos": "Logos",
}

# Remaining concepts to plain text
FINAL_TO_PLAIN = [
    "Chemical Wedding", "Christ Mythos", "Christ's Resurrection",
    "Chronos", "Chronos Devouring His Children", "Cronus",
    "Compensatory Function", "Conjunctions", "Conscious Death",
    "Curiosity as Initiation",
]

def apply_cleanup(content):
    changes = 0
    
    # Tarot
    for old, new in LAST_TAROT_FIXES.items():
        pattern = rf'\[\[{re.escape(old)}\]\]'
        count = len(re.findall(pattern, content))
        if count:
            content = re.sub(pattern, rf'[[{new}]]', content)
            changes += count
    
    # Paths
    for old, new in PATH_FIXES.items():
        pattern = rf'\[\[{re.escape(old)}\]\]'
        count = len(re.findall(pattern, content))
        if count:
            content = re.sub(pattern, rf'[[{new}]]', content)
            changes += count
    
    # Plain text
    for term in FINAL_TO_PLAIN:
        pattern = rf'\[\[{re.escape(term)}\]\]'
        count = len(re.findall(pattern, content))
        if count:
            content = re.sub(pattern, term, content)
            changes += count
    
    return content, changes

total_files = 0
total_changes = 0

for md_file in sorted(PERSONAL_MYTHOS.rglob("*.md")):
    content = md_file.read_text()
    new_content, changes = apply_cleanup(content)
    
    if changes > 0:
        md_file.write_text(new_content)
        print(f"✓ {md_file.relative_to(PERSONAL_MYTHOS)}: {changes} fixes")
        total_files += 1
        total_changes += changes

print(f"\n{'='*60}")
print(f"FINAL CLEANUP: {total_changes} fixes across {total_files} files")
print(f"{'='*60}")
