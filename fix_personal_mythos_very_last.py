#!/usr/bin/env python3
"""Fix the very last remaining dead links with proper alias handling."""

import re
from pathlib import Path

PERSONAL_MYTHOS = Path("Library/The Seven Pillars of Understanding/Personal Mythos")

# Tarot cards - match with or without aliases
TAROT_FIXES_WITH_ALIASES = {
    "The Magician": "The Magician (I)",
    "The High Priestess": "The High Priestess (II)",
    "The Lovers": "The Lovers (VI)",
    "The Hermit": "The Hermit (IX)",
    "The Chariot": "The Chariot (VII)",
}

# Logos path fix
LOGOS_PATH_FIX = {
    "Core Foundations/Logos": "Logos",
}

# Concepts to plain text
CONCEPTS_TO_PLAIN = ["Ego", "The Devouring Mother", "The Terrible Father", "Underworld"]

def fix_with_alias(content):
    """Fix wikilinks that may have aliases."""
    changes = 0
    
    # Tarot cards - handle both [[card]] and [[card|anything]]
    for old, new in TAROT_FIXES_WITH_ALIASES.items():
        # Match [[old]] or [[old|anything]]
        pattern = rf'\[\[{re.escape(old)}(?:\|[^\]]+)?\]\]'
        matches = list(re.finditer(pattern, content))
        if matches:
            # Replace in reverse order to preserve positions
            for match in reversed(matches):
                # Preserve the display text if there was an alias
                full_match = match.group(0)
                if '|' in full_match:
                    # Extract display text
                    display = full_match.split('|')[1].rstrip(']')
                    replacement = f'[[{new}|{display}'
                else:
                    replacement = f'[[{new}]]'
                
                content = content[:match.start()] + replacement + content[match.end():]
                changes += 1
    
    # Logos path fix
    for old, new in LOGOS_PATH_FIX.items():
        pattern = rf'\[\[{re.escape(old)}(?:\|[^\]]+)?\]\]'
        count = len(re.findall(pattern, content))
        if count:
            content = re.sub(pattern, rf'[[{new}]]', content)
            changes += count
    
    # Concepts to plain text - handle both with and without aliases
    for term in CONCEPTS_TO_PLAIN:
        # Match [[term]] or [[term|anything]]
        pattern = rf'\[\[{re.escape(term)}(?:\|[^\]]+)?\]\]'
        matches = list(re.finditer(pattern, content))
        if matches:
            # Replace in reverse order
            for match in reversed(matches):
                # Use the original term (not the alias)
                content = content[:match.start()] + term + content[match.end():]
                changes += 1
    
    return content, changes

def main():
    total_files = 0
    total_changes = 0
    
    problem_files = [
        "Fairy Tales/The Quest Object.md",
        "Fairy Tales/The Youngest Child.md",
        "Hero's Journey/Approach to the Inmost Cave.md",
        "Individuation Process/Encounter with Anima-Animus.md",
        "Jungian Archetypes/The Animus.md",
        "Jungian Archetypes/The Wise Old Man.md",
    ]
    
    for file_rel in problem_files:
        file_path = PERSONAL_MYTHOS / file_rel
        if not file_path.exists():
            continue
        
        content = file_path.read_text()
        new_content, changes = fix_with_alias(content)
        
        if changes > 0:
            file_path.write_text(new_content)
            print(f"✓ {file_rel}: {changes} fixes")
            total_files += 1
            total_changes += changes
    
    print(f"\n{'='*60}")
    print(f"VERY LAST FIXES: {total_changes} fixes across {total_files} files")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
