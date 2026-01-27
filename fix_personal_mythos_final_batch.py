#!/usr/bin/env python3
"""Final comprehensive cleanup of remaining Personal Mythos dead links."""

import re
from pathlib import Path

PERSONAL_MYTHOS = Path("Library/The Seven Pillars of Understanding/Personal Mythos")

# Fix old Folklore paths that were missed
OLD_FOLKLORE_ALCHEMY = {
    "Folklore/Alchemical Stages/Albedo": "Albedo",
    "Folklore/Alchemical Stages/Coniunctio": "Conjunction",
    "Folklore/Alchemical Stages/Nigredo": "Nigredo",
    "Folklore/Alchemical Stages/Rubedo": "Rubedo",
    "Folklore/Alchemical Stages/Separatio": "Separation",
}

OLD_FOLKLORE_FAIRY_TALES = {
    "Folklore/Fairy Tales/Beauty and the Beast": "Beauty and the Beast",
    "Folklore/Fairy Tales/Bluebeard": "Bluebeard",
    "Folklore/Fairy Tales/Cinderella": "Cinderella",
    "Folklore/Fairy Tales/Frog Prince": "Frog Prince",
    "Folklore/Fairy Tales/Hansel and Gretel": "Hansel and Gretel",
    "Folklore/Fairy Tales/Snow White": "Snow White",
    "Folklore/Fairy Tales/Rapunzel": "Rapunzel",
    "Folklore/Fairy Tales/The Wicked Stepmother": "The Wicked Stepmother",
}

# Tarot fix
TAROT_DEATH_FIX = {
    "Death (Tarot)": "Death (XIII)",
}

# HD variations
HD_VARIATIONS = {
    "Defined G-Center": "G Center",
    "Ego-Heart Center": "Heart",
    "Defined Sacral": "Sacral",
}

# Convert everything else to plain text
ALL_REMAINING_TO_PLAIN = [
    # HD Channels
    "Channel 27-50", "Channel 27-50: Preservation", "Channel 51-25", "Channel 59-6",
    
    # Fairy tale motifs
    "House of the Flame", "House of the Land", "House of the Sea",
    
    # Alchemy
    "The Chemical Wedding",
    
    # Psychological
    "Negative Mother Complex", "Ego Death and Rebirth", "Depression",
    "Ego Integrity vs. Despair", "Empty Shell Syndrome", "First Half of Life",
    "Second Half of Life", "Compensatory Function",
    
    # Mythology/Religious
    "Dante's Divine Comedy", "Fisher King", "Christ's Resurrection",
    
    # Concepts
    "Death and Rebirth", "Diamond Body", "Ego",
]

def apply_final_comprehensive_fixes(content):
    """Apply all final fixes."""
    changes = 0
    
    # Old Folklore alchemy paths
    for old, new in OLD_FOLKLORE_ALCHEMY.items():
        pattern = rf'\[\[{re.escape(old)}(?:\|[^\]]+)?\]\]'
        count = len(re.findall(pattern, content))
        if count:
            content = re.sub(pattern, rf'[[{new}]]', content)
            changes += count
    
    # Old Folklore fairy tale paths
    for old, new in OLD_FOLKLORE_FAIRY_TALES.items():
        pattern = rf'\[\[{re.escape(old)}(?:\|[^\]]+)?\]\]'
        count = len(re.findall(pattern, content))
        if count:
            content = re.sub(pattern, rf'[[{new}]]', content)
            changes += count
    
    # Tarot Death fix
    for old, new in TAROT_DEATH_FIX.items():
        pattern = rf'\[\[{re.escape(old)}(?:\|[^\]]+)?\]\]'
        count = len(re.findall(pattern, content))
        if count:
            content = re.sub(pattern, rf'[[{new}]]', content)
            changes += count
    
    # HD variations
    for old, new in HD_VARIATIONS.items():
        pattern = rf'\[\[{re.escape(old)}(?:\|[^\]]+)?\]\]'
        count = len(re.findall(pattern, content))
        if count:
            content = re.sub(pattern, rf'[[{new}]]', content)
            changes += count
    
    # Convert to plain text
    for term in ALL_REMAINING_TO_PLAIN:
        pattern = rf'\[\[{re.escape(term)}\]\]'
        count = len(re.findall(pattern, content))
        if count:
            content = re.sub(pattern, term, content)
            changes += count
    
    return content, changes

def main():
    total_files = 0
    total_changes = 0
    
    for md_file in sorted(PERSONAL_MYTHOS.rglob("*.md")):
        content = md_file.read_text()
        new_content, changes = apply_final_comprehensive_fixes(content)
        
        if changes > 0:
            md_file.write_text(new_content)
            print(f"✓ {md_file.relative_to(PERSONAL_MYTHOS)}: {changes} fixes")
            total_files += 1
            total_changes += changes
    
    print(f"\n{'='*60}")
    print(f"FINAL COMPREHENSIVE CLEANUP: {total_changes} fixes across {total_files} files")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
