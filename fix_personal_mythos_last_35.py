#!/usr/bin/env python3
"""Fix the final 35 dead links in Personal Mythos."""

import re
from pathlib import Path

PERSONAL_MYTHOS = Path("Library/The Seven Pillars of Understanding/Personal Mythos")

# Old Folklore paths in The Quest Object.md
OLD_FOLKLORE_PATHS_FINAL = {
    "Folklore/Fairy Tales/The Two Brothers": "The Two Brothers",
    "Folklore/Hero's Journey/Approach to the Inmost Cave": "Approach to the Inmost Cave",
    "Folklore/Hero's Journey/Crossing the First Threshold": "Crossing the First Threshold",
    "Folklore/Hero's Journey/Return with the Elixir": "Return with the Elixir",
    "Folklore/Hero's Journey/Tests, Allies, and Enemies": "Tests, Allies, and Enemies",
    "Folklore/Hero's Journey/The Call to Adventure": "The Call to Adventure",
    "Folklore/Hero's Journey/The Ordeal": "The Ordeal",
    "Folklore/Hero's Journey/The Reward": "The Reward",
    "Folklore/Hero's Journey/The Road Back": "The Road Back",
    "Folklore/Individuation Process/Confrontation with Shadow": "Confrontation with Shadow",
    "Folklore/Individuation Process/Confrontation with the Self": "Confrontation with the Self",
    "Folklore/Individuation Process/Ego Formation and Childhood": "Ego Formation and Childhood",
    "Folklore/Individuation Process/Encounter with Anima-Animus": "Encounter with Anima-Animus",
    "Folklore/Individuation Process/Integration and Wholeness": "Integration and Wholeness",
}

# Remaining Tarot cards
FINAL_TAROT_CARDS = {
    "The Magician": "The Magician (I)",
    "The High Priestess": "The High Priestess (II)",
    "The Lovers": "The Lovers (VI)",
    "The Hermit": "The Hermit (IX)",
    "The Chariot": "The Chariot (VII)",
}

# Logos fix
FINAL_LOGOS = {
    "Logos": "Core Foundations/Logos",
}

# Qabalah - convert to plain text
# Concepts to plain text
FINAL_TO_PLAIN = [
    "Qabalah", "Ego", "The Devouring Mother", "The Terrible Father", "Underworld",
]

def apply_last_35_fixes(content):
    """Fix last 35 dead links."""
    changes = 0
    
    # Old Folklore paths
    for old, new in OLD_FOLKLORE_PATHS_FINAL.items():
        pattern = rf'\[\[{re.escape(old)}(?:\|[^\]]+)?\]\]'
        count = len(re.findall(pattern, content))
        if count:
            content = re.sub(pattern, rf'[[{new}]]', content)
            changes += count
    
    # Tarot cards
    for old, new in FINAL_TAROT_CARDS.items():
        pattern = rf'\[\[{re.escape(old)}\]\]'
        count = len(re.findall(pattern, content))
        if count:
            content = re.sub(pattern, rf'[[{new}]]', content)
            changes += count
    
    # Logos
    for old, new in FINAL_LOGOS.items():
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

def main():
    total_files = 0
    total_changes = 0
    
    for md_file in sorted(PERSONAL_MYTHOS.rglob("*.md")):
        content = md_file.read_text()
        new_content, changes = apply_last_35_fixes(content)
        
        if changes > 0:
            md_file.write_text(new_content)
            print(f"✓ {md_file.relative_to(PERSONAL_MYTHOS)}: {changes} fixes")
            total_files += 1
            total_changes += changes
    
    print(f"\n{'='*60}")
    print(f"LAST 35 FIXES: {total_changes} fixes across {total_files} files")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
