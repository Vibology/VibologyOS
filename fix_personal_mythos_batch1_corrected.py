#!/usr/bin/env python3
"""Fix batch-repairable dead links in Personal Mythos - Batch 1 CORRECTED."""

import re
from pathlib import Path

PERSONAL_MYTHOS = Path("Library/The Seven Pillars of Understanding/Personal Mythos")

# Pattern 3: Tarot cards - CORRECTED to match actual filenames
TAROT_FIXES = {
    # First, fix the broken ones we just created (number prefix format)
    "1 - The Magician": "The Magician (I)",
    "2 - The High Priestess": "The High Priestess (II)",
    "3 - The Empress": "The Empress (III)",
    "4 - The Emperor": "The Emperor (IV)",
    "5 - The Hierophant": "The Hierophant (V)",
    "6 - The Lovers": "The Lovers (VI)",
    "7 - The Chariot": "The Chariot (VII)",
    "8 - Strength": "Strength (VIII)",
    "9 - The Hermit": "The Hermit (IX)",
    "10 - Wheel of Fortune": "Wheel of Fortune (X)",
    "11 - Justice": "Justice (XI)",
    "12 - The Hanged Man": "The Hanged Man (XII)",
    "13 - Death": "Death (XIII)",
    "14 - Temperance": "Temperance (XIV)",
    "15 - The Devil": "The Devil (XV)",
    "16 - The Tower": "The Tower (XVI)",
    "17 - The Star": "The Star (XVII)",
    "18 - The Moon": "The Moon (XVIII)",
    "19 - The Sun": "The Sun (XIX)",
    "20 - Judgement": "Judgement (XX)",
    "21 - The World": "The World (XXI)",
    "0 - The Fool": "The Fool (0)",
    # Now fix the originals that still exist
    "The Fool": "The Fool (0)",
    "The Magician": "The Magician (I)",
    "The High Priestess": "The High Priestess (II)",
    "The Empress": "The Empress (III)",
    "The Emperor": "The Emperor (IV)",
    "The Hierophant": "The Hierophant (V)",
    "The Lovers": "The Lovers (VI)",
    "The Chariot": "The Chariot (VII)",
    "Strength": "Strength (VIII)",
    "The Hermit": "The Hermit (IX)",
    "Wheel of Fortune": "Wheel of Fortune (X)",
    "Justice": "Justice (XI)",
    "The Hanged Man": "The Hanged Man (XII)",
    "Death": "Death (XIII)",
    "Temperance": "Temperance (XIV)",
    "The Devil": "The Devil (XV)",
    "The Tower": "The Tower (XVI)",
    "The Star": "The Star (XVII)",
    "The Moon": "The Moon (XVIII)",
    "The Sun": "The Sun (XIX)",
    "Judgement": "Judgement (XX)",
    "Judgment": "Judgement (XX)",  # Handle alternate spelling
    "The World": "The World (XXI)",
}

def fix_tarot_links(content):
    """Fix Tarot card links."""
    changes = 0
    
    for old, new in TAROT_FIXES.items():
        # Match [[old]] or [[old|anything]]
        pattern = rf'\[\[{re.escape(old)}(?:\|[^\]]+)?\]\]'
        matches = re.findall(pattern, content)
        if matches:
            content = re.sub(pattern, rf'[[{new}]]', content)
            changes += len(matches)
    
    return content, changes

def main():
    total_files = 0
    total_changes = 0
    
    for md_file in sorted(PERSONAL_MYTHOS.rglob("*.md")):
        content = md_file.read_text()
        new_content, changes = fix_tarot_links(content)
        
        if changes > 0:
            md_file.write_text(new_content)
            print(f"✓ {md_file.relative_to(PERSONAL_MYTHOS)}: {changes} fixes")
            total_files += 1
            total_changes += changes
    
    print(f"\n{'='*60}")
    print(f"TAROT CORRECTION: {total_changes} fixes across {total_files} files")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
