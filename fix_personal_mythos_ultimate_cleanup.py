#!/usr/bin/env python3
"""Ultimate cleanup: Convert all remaining forward references to plain text."""

import re
from pathlib import Path

PERSONAL_MYTHOS = Path("Library/The Seven Pillars of Understanding/Personal Mythos")

# Astrology qualifier fixes
ASTROLOGY_QUALIFIER_FIXES = {
    "Saturn (Astrology)": "Saturn ♄",
    "Pluto (Astrology)": "Pluto ♇",
    "Moon (Astrology)": "Moon ☽",
}

# Tarot qualifier fixes
TAROT_QUALIFIER_FIXES = {
    "The High Priestess (Tarot)": "The High Priestess (II)",
    "The Moon (Tarot)": "The Moon (XVIII)",
    "The Star (Tarot)": "The Star (XVII)",
}

# Alchemy qualifier fixes
ALCHEMY_QUALIFIER_FIXES = {
    "Rubedo (Alchemy)": "Rubedo",
}

# Simple wikilink fixes
SIMPLE_WIKILINK_FIXES = {
    "Logos": "Core Foundations/Logos",
    "The Magician": "The Magician (I)",
    "The High Priestess": "The High Priestess (II)",
    "The Lovers": "The Lovers (VI)",
}

# Individuation Process variations
INDIVIDUATION_FIXES = {
    "The Individuation Process": "Individuation Process",
}

# Everything else → plain text (all remaining forward references)
ULTIMATE_TO_PLAIN = [
    # Jungian/Psychological
    "Underworld", "Ego", "The Devouring Mother", "The Terrible Father",
    "Moral Inflation", "Shadow Possession", "Scapegoating", 
    "Participation Mystique", "Object Permanence", "God-Image",
    "Teleology", "Persona Identification", "Imposter Syndrome",
    "Self-Reflection", "Shadow Confrontation", "Shadow Recognition vs. Integration",
    
    # Mythology
    "White Painted Woman", "The Dying and Rising God", "Minotaur",
    "Wasteland", "Yggdrasil", "Mara", "Osiris", "Hermes Trismegistus",
    
    # Hero's Journey variations
    "The Hero's Return", "Road Back", "The Return with the Elixir",
    "The Freedom to Live", "Treasure Hard to Attain", "The Elixir of Immortality",
    
    # Astrology
    "Pluto Square Pluto", "Nodes", "Lunar Cycles", "The Seven Classical Planets",
    
    # Alchemy
    "Lapis Philosophorum", "Soma", "Shamanic Dismemberment", "Katabasis",
    
    # General concepts
    "Muse", "Mandala", "Generativity", "Life Review", "The Elder Initiation",
    
    # HD
    "Manifesting Generator", "Sacral-Solar Plexus Connection", "Split Definition",
    
    # Symbolism
    "Undines", "The Sword", "The Scales", "Mercury/Hermes", "The Lover",
    "The Ancestor", "Jacob's Ladder", "The Ladder of Jacob",
    
    # Religious/Mystical
    "Islamic Mysticism", "Jewish Mysticism", "Seven Chakras", "Kundalini",
    "Sacred Geometry",
    
    # Numbers
    "The Seven as Cycle", "The Number Three", "The Number Four", 
    "The Number Eight", "The Number Twelve", "The Quaternary",
    
    # Fairy tale motifs (comprehensive list)
    "Iron Hans", "The Goose Girl at the Well", "The Enchanted Castle",
    "The Sacrificial Daughter", "The Three Sisters", "The Magic Rose",
    "The Dead Mother", "The Transformed Bride", "Vasalisa the Wise",
    "The Bloody Key", "The Predatory Husband", "The Rescuing Brothers",
    "The Robber Bridegroom", "Mr. Fox", "The White Dove",
    "The Devouring Witch", "The Gingerbread House", "Sibling Bond",
    
    # Other
    "The I-Ching",
]

def apply_ultimate_cleanup(content):
    """Apply ultimate cleanup."""
    changes = 0
    
    # Astrology qualifiers
    for old, new in ASTROLOGY_QUALIFIER_FIXES.items():
        pattern = rf'\[\[{re.escape(old)}(?:\|[^\]]+)?\]\]'
        count = len(re.findall(pattern, content))
        if count:
            content = re.sub(pattern, rf'[[{new}]]', content)
            changes += count
    
    # Tarot qualifiers
    for old, new in TAROT_QUALIFIER_FIXES.items():
        pattern = rf'\[\[{re.escape(old)}(?:\|[^\]]+)?\]\]'
        count = len(re.findall(pattern, content))
        if count:
            content = re.sub(pattern, rf'[[{new}]]', content)
            changes += count
    
    # Alchemy qualifiers
    for old, new in ALCHEMY_QUALIFIER_FIXES.items():
        pattern = rf'\[\[{re.escape(old)}(?:\|[^\]]+)?\]\]'
        count = len(re.findall(pattern, content))
        if count:
            content = re.sub(pattern, rf'[[{new}]]', content)
            changes += count
    
    # Simple wikilink fixes
    for old, new in SIMPLE_WIKILINK_FIXES.items():
        pattern = rf'\[\[{re.escape(old)}\]\]'
        count = len(re.findall(pattern, content))
        if count:
            content = re.sub(pattern, rf'[[{new}]]', content)
            changes += count
    
    # Individuation fixes
    for old, new in INDIVIDUATION_FIXES.items():
        pattern = rf'\[\[{re.escape(old)}(?:\|[^\]]+)?\]\]'
        count = len(re.findall(pattern, content))
        if count:
            content = re.sub(pattern, rf'[[{new}]]', content)
            changes += count
    
    # Convert to plain text
    for term in ULTIMATE_TO_PLAIN:
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
        new_content, changes = apply_ultimate_cleanup(content)
        
        if changes > 0:
            md_file.write_text(new_content)
            print(f"✓ {md_file.relative_to(PERSONAL_MYTHOS)}: {changes} fixes")
            total_files += 1
            total_changes += changes
    
    print(f"\n{'='*60}")
    print(f"ULTIMATE CLEANUP: {total_changes} fixes across {total_files} files")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
