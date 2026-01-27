#!/usr/bin/env python3
"""Fix Personal Mythos Batch 3: Archetype names and common patterns."""

import re
from pathlib import Path

PERSONAL_MYTHOS = Path("Library/The Seven Pillars of Understanding/Personal Mythos")

# Archetype name fixes (add "The" prefix)
ARCHETYPE_NAME_FIXES = {
    # Only fix when NOT already part of "The X" (to avoid breaking "The Great Mother")
    "Great Mother": "The Great Mother",
    "Divine Child": "The Divine Child",
    "Animus": "The Animus",
    "Anima": "The Anima",
    "Hero": "The Hero",
    "Shadow": "The Shadow",
    "Persona": "The Persona",
    "Joker": "The Joker",
    "Shapeshifter": "The Shapeshifter",
    "Wise Old Man": "The Wise Old Man",
    "Self": "The Self",  # Individuation stage
    "Trickster": "The Joker",  # Alternate name for Joker archetype
    "Mentor": "The Wise Old Man",  # Hero's Journey naming
    "Herald": "Threshold Guardian",  # Another HJ archetype
}

# Fairy tale titles (many don't have Library entries, convert to plain text)
FAIRY_TALES_TO_PLAIN = [
    "Sleeping Beauty", "The Handless Maiden", "Rumpelstiltskin", "Baba Yaga",
    "Vasilisa the Beautiful", "Vasilisa", "East of the Sun, West of the Moon",
    "The Juniper Tree", "Little Red Riding Hood", "The Goose Girl",
    "Allerleirauh", "Parzival", "The Glass Coffin", "The Water of Life",
]

# Jungian concepts (convert to plain text - not individual Library entries)
JUNGIAN_TO_PLAIN = [
    "Individuation", "Projection", "Ego", "The Ego", "Syzygy",
    "Collective Unconscious", "Ego-Self Axis", "Puer Aeternus",
    "Mother Complex", "Animus Possession", "Shadow Integration",
    "The Devouring Mother", "The Terrible Father", "Wise Old Woman",
    "Psychopomp", "The Psychopomp", "Sublimation", "Anticipatory Anxiety",
]

# Hero's Journey stage variations
HERO_JOURNEY_FIXES2 = {
    "Ordeal": "The Ordeal",
    "Tests, Allies, Enemies": "Tests, Allies, and Enemies",
    "Tests, Allies and Enemies": "Tests, Allies, and Enemies",
    "Resurrection": "The Resurrection",
    "The Mentor": "Meeting the Mentor",
    "Mentor": "Meeting the Mentor",
    "The Road of Trials": "Tests, Allies, and Enemies",
    "Atonement with the Father": "The Ordeal",  # Campbell's term
    "The Belly of the Whale": "Crossing the First Threshold",  # Campbell's term
    "The Ultimate Boon": "The Reward",  # Campbell's term
    "Meeting with the Goddess": "The Reward",  # Campbell's term
    "The Meeting with the Goddess": "The Reward",
    "The Reward (Seizing the Sword)": "The Reward",
    "Ordinary World": "The Ordinary World",
    "Special World": "Tests, Allies, and Enemies",  # Act 2
    "Apotheosis": "The Resurrection",  # Campbell's term
}

# Alchemy terms (concepts, not entries)
ALCHEMY_TO_PLAIN = [
    "Coniunctio", "Mortificatio", "Solve et Coagula", "The Hermaphrodite",
    "The Hieros Gamos", "Hieros Gamos", "The Philosopher's Stone", "Philosopher's Stone",
    "The Unus Mundus", "Unus Mundus", "Prima Materia", "Separatio", "Solutio",
    "Coagulatio", "Mercurius", "Albedo (Alchemy)", "Alchemical Tradition",
]

# Astrology fixes
ASTROLOGY_FIXES = {
    "Astrology/Planets/Mercury # ☿": "Mercury ☿",
    "Chiron": "Astrology",  # Not in Library, link to parent
    "Saturn Return": "Saturn ♄",
    "South Node": "Astrology",
    "North Node": "Astrology",
    "Ascendant": "Astrology",
    "10th House (Midheaven)": "10th House",
}

# Mythology stories (concepts, not entries)
MYTHOLOGY_TO_PLAIN = [
    "Aphrodite and Psyche", "Psyche and Eros", "Cupid and Psyche",
    "Demeter and Persephone", "Persephone and Demeter", "Persephone's Descent",
    "Hades and Persephone", "Inanna's Descent", "Odin's Sacrifice",
    "Orpheus and Eurydice", "Perseus and Medusa",
    "Chinese Mythology", "Biblical Mythology", "Christian Mythology",
    "Arthurian Legend",
]

# HD concepts
HD_TO_PLAIN = [
    "Tribal Circuitry", "Open Centers", "Generators", "Manifestors",
]

# Tarot path fix
TAROT_PATH_FIXES = {
    "The Tarot/Major Arcana/00 - The Fool": "The Fool (0)",
}

# Miscellaneous fixes
MISC_FIXES = {
    "The Frog Prince": "Frog Prince",
    "The Wheel of Fortune": "Wheel of Fortune (X)",
    "Judgment (XX)": "Judgement (XX)",
    "Logos": "Core Foundations/Logos",  # Wrong path
    "Transcendent Function": "The Transcendent Function",
    "Personal Myth": "Personal Mythos",
    "The Personal Myth": "Personal Mythos",
    "Anima and Animus": "The Anima",  # Link to first one
    "The Anima and Animus": "The Anima",
    "Anima/Animus": "The Anima",
}

# Archetype-related concepts (plain text)
ARCHETYPE_CONCEPTS_TO_PLAIN = [
    "The Dragon", "The Wasteland", "The Grail", "The Phoenix",
    "The Animal Bridegroom", "The Poisoned Gift", "The Impossible Task",
    "The Magic Mirror", "The Sacred Marriage", "The Underworld", "Underworld",
    "Abandonment in the Forest", "Dark Night of the Soul", "Midlife Crisis",
    "The Road Back", "Eros", "Kali", "Athena", "Dionysus", "Azrael",
    "Amphitrite", "Objective Psyche", "Anima Mundi", "Uroboros",
    "Animal Totems", "Ancestor",
]

def fix_archetype_names(content):
    """Fix archetype names."""
    changes = 0
    
    for old, new in ARCHETYPE_NAME_FIXES.items():
        # Only fix [[Old]], not [[The Old]] or part of longer names
        pattern = rf'\[\[{re.escape(old)}\]\]'
        count = len(re.findall(pattern, content))
        if count:
            content = re.sub(pattern, rf'[[{new}]]', content)
            changes += count
    
    return content, changes

def fix_other_refs(content):
    """Fix other reference patterns."""
    changes = 0
    
    # Hero's Journey
    for old, new in HERO_JOURNEY_FIXES2.items():
        pattern = rf'\[\[{re.escape(old)}(?:\|[^\]]+)?\]\]'
        count = len(re.findall(pattern, content))
        if count:
            content = re.sub(pattern, rf'[[{new}]]', content)
            changes += count
    
    # Astrology
    for old, new in ASTROLOGY_FIXES.items():
        pattern = rf'\[\[{re.escape(old)}(?:\|[^\]]+)?\]\]'
        count = len(re.findall(pattern, content))
        if count:
            content = re.sub(pattern, rf'[[{new}]]', content)
            changes += count
    
    # Tarot paths
    for old, new in TAROT_PATH_FIXES.items():
        pattern = rf'\[\[{re.escape(old)}(?:\|[^\]]+)?\]\]'
        count = len(re.findall(pattern, content))
        if count:
            content = re.sub(pattern, rf'[[{new}]]', content)
            changes += count
    
    # Misc fixes
    for old, new in MISC_FIXES.items():
        pattern = rf'\[\[{re.escape(old)}(?:\|[^\]]+)?\]\]'
        count = len(re.findall(pattern, content))
        if count:
            content = re.sub(pattern, rf'[[{new}]]', content)
            changes += count
    
    return content, changes

def convert_to_plain(content):
    """Convert concepts to plain text."""
    changes = 0
    
    all_to_plain = (FAIRY_TALES_TO_PLAIN + JUNGIAN_TO_PLAIN + ALCHEMY_TO_PLAIN + 
                   MYTHOLOGY_TO_PLAIN + HD_TO_PLAIN + ARCHETYPE_CONCEPTS_TO_PLAIN)
    
    for term in all_to_plain:
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
        
        # Apply fixes
        content, arch_changes = fix_archetype_names(content)
        content, ref_changes = fix_other_refs(content)
        content, plain_changes = convert_to_plain(content)
        
        changes = arch_changes + ref_changes + plain_changes
        
        if changes > 0:
            md_file.write_text(content)
            print(f"✓ {md_file.relative_to(PERSONAL_MYTHOS)}: {changes} fixes ({arch_changes} arch, {ref_changes} refs, {plain_changes} plain)")
            total_files += 1
            total_changes += changes
    
    print(f"\n{'='*60}")
    print(f"BATCH 3 COMPLETE: {total_changes} fixes across {total_files} files")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
