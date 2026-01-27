#!/usr/bin/env python3
"""Absolute final cleanup: Fix remaining 105 dead links."""

import re
from pathlib import Path

PERSONAL_MYTHOS = Path("Library/The Seven Pillars of Understanding/Personal Mythos")

# Fix Logos path (wrong format)
LOGOS_FIX = {
    "Core Foundations/Logos": "Logos",
}

# Fix remaining Tarot cards without Roman numerals
TAROT_REMAINING = {
    "The Magician": "The Magician (I)",
    "The High Priestess": "The High Priestess (II)",
    "The Lovers": "The Lovers (VI)",
    "The Hermit": "The Hermit (IX)",
    "The Chariot": "The Chariot (VII)",
}

# Fix old HD paths
OLD_HD_PATHS = {
    "Human Design/Centers/Sacral Center": "Sacral",
    "Human Design/Gates/Gate 1 - The Creative": "Gate 01 - The Creative",
    "Human Design/Gates/Gate 2 - The Receptive": "Gate 02 - The Receptive",
}

# Fix old Tarot path
OLD_TAROT_PATH = {
    "The Tarot/The Tree of Life (Qabalah)": "Qabalah",
}

# Fix Spleen Authority
AUTHORITY_FIX = {
    "Spleen Authority": "Splenic Authority",
}

# Convert all remaining to plain text (all single-occurrence forward references)
ABSOLUTE_FINAL_TO_PLAIN = [
    # Concepts
    "Underworld", "Ego", "The Devouring Mother", "The Terrible Father",
    "Temenos", "Via Negativa", "Sacred Grove", "Initiation", "Liminality",
    "Repression", "libido", "Manifestation", "Intuition", "Instinct",
    "Quaternary", "Patience and Endurance", "Instinct Over Intellect",
    "Mother Archetype", "Separation Anxiety", "Helpful Instinct",
    "Negative Mother",
    
    # Mythology figures
    "Medusa", "Pandora", "Heracles", "Hera", "Kronos", "Hephaestus",
    
    # Mythology stories
    "The Odyssey", "The Epic of Gilgamesh", "Osiris Dismemberment",
    "Jonah and the Whale",
    
    # Fairy tale motifs
    "The Treasure from the Underworld", "The Helper Animal",
    "Sleeping Beauty (Briar Rose)", "The Wild Woman", "The Tower Imprisonment",
    "The Golden Hair", "The Secret Lover", "The Exile and Return",
    "The Healing Tears", "The Divine Twins", "The Enchanted Prince",
    "The Golden Object", "The Sacred Bargain", "The Well and Spring",
    "Mother Holle", "The Tower as Prison", "The Sorting Task",
    "The Hostile Sisters", "The Poisoned Apple", "Snow White and Rose Red",
    "The Thirteenth Fairy", "The Swan Maiden", "The Stolen Voice",
    "Homunculus", "The Loathly Lady", "Sovereignty Goddess",
    "The Doll", "The Talking Bird", "The Disguised Helper",
    "The Three Gifts", "The White Duck", "The Helpful Animals",
    "The Descent to the Underworld", "The Sacred Number Three",
    "The Jealous Goddess", "The Descent Motif",
    
    # Alchemy
    "The Red King", "Lust",
    
    # Astrology
    "Nodes of the Moon",
]

def apply_absolute_final_cleanup(content):
    """Apply absolute final cleanup."""
    changes = 0
    
    # Logos fix
    for old, new in LOGOS_FIX.items():
        pattern = rf'\[\[{re.escape(old)}(?:\|[^\]]+)?\]\]'
        count = len(re.findall(pattern, content))
        if count:
            content = re.sub(pattern, rf'[[{new}]]', content)
            changes += count
    
    # Tarot remaining
    for old, new in TAROT_REMAINING.items():
        pattern = rf'\[\[{re.escape(old)}\]\]'
        count = len(re.findall(pattern, content))
        if count:
            content = re.sub(pattern, rf'[[{new}]]', content)
            changes += count
    
    # Old HD paths
    for old, new in OLD_HD_PATHS.items():
        pattern = rf'\[\[{re.escape(old)}(?:\|[^\]]+)?\]\]'
        count = len(re.findall(pattern, content))
        if count:
            content = re.sub(pattern, rf'[[{new}]]', content)
            changes += count
    
    # Old Tarot path
    for old, new in OLD_TAROT_PATH.items():
        pattern = rf'\[\[{re.escape(old)}(?:\|[^\]]+)?\]\]'
        count = len(re.findall(pattern, content))
        if count:
            content = re.sub(pattern, rf'[[{new}]]', content)
            changes += count
    
    # Authority fix
    for old, new in AUTHORITY_FIX.items():
        pattern = rf'\[\[{re.escape(old)}(?:\|[^\]]+)?\]\]'
        count = len(re.findall(pattern, content))
        if count:
            content = re.sub(pattern, rf'[[{new}]]', content)
            changes += count
    
    # Convert to plain text
    for term in ABSOLUTE_FINAL_TO_PLAIN:
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
        new_content, changes = apply_absolute_final_cleanup(content)
        
        if changes > 0:
            md_file.write_text(new_content)
            print(f"✓ {md_file.relative_to(PERSONAL_MYTHOS)}: {changes} fixes")
            total_files += 1
            total_changes += changes
    
    print(f"\n{'='*60}")
    print(f"ABSOLUTE FINAL CLEANUP: {total_changes} fixes across {total_files} files")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
