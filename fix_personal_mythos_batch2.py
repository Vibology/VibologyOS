#!/usr/bin/env python3
"""Fix Personal Mythos Batch 2: Gates, Internal Refs, Folklore paths."""

import re
from pathlib import Path

PERSONAL_MYTHOS = Path("Library/The Seven Pillars of Understanding/Personal Mythos")

# Gate mappings (single digit → zero-padded)
GATE_NAMES = {
    1: "The Creative", 2: "The Receptive", 3: "Difficulty at the Beginning",
    4: "Youthful Folly", 5: "Waiting", 6: "Conflict", 7: "The Army",
    8: "Holding Together", 9: "The Taming Power of the Small", 10: "Treading",
    11: "Peace", 12: "Standstill", 13: "The Fellowship of Man",
    14: "Possession in Great Measure", 15: "Modesty", 16: "Enthusiasm",
    17: "Following", 18: "Work on What Has Been Spoilt", 19: "Approach",
    20: "Contemplation", 21: "Biting Through", 22: "Grace",
    23: "Splitting Apart", 24: "The Return", 25: "Innocence",
    26: "The Taming Power of the Great", 27: "Nourishment",
    28: "Preponderance of the Great", 29: "The Abysmal", 30: "The Clinging Fire",
    31: "Influence", 32: "Duration", 33: "Retreat", 34: "The Power of the Great",
    35: "Progress", 36: "Darkening of the Light", 37: "The Family",
    38: "Opposition", 39: "Obstruction", 40: "Deliverance", 41: "Decrease",
    42: "Increase", 43: "Breakthrough", 44: "Coming to Meet",
    45: "Gathering Together", 46: "Pushing Upward", 47: "Oppression",
    48: "The Well", 49: "Revolution", 50: "The Cauldron", 51: "The Arousing",
    52: "Keeping Still", 53: "Development", 54: "The Marrying Maiden",
    55: "Abundance", 56: "The Wanderer", 57: "The Gentle", 58: "The Joyous",
    59: "Dispersion", 60: "Limitation", 61: "Inner Truth",
    62: "Preponderance of the Small", 63: "After Completion",
    64: "Before Completion",
}

# Individuation stages
INDIVIDUATION_FIXES = {
    "Encounter with Anima and Animus": "Encounter with Anima-Animus",
    "Encounter with Animus": "Encounter with Anima-Animus",
}

# Internal section references
INTERNAL_FIXES = {
    "Alchemical Stages": "Personal Mythos",  # Parent overview
    "Hero's Journey": "The Hero's Journey",  # Actual file name
}

# Old Folklore World Mythology paths
FOLKLORE_MYTHOLOGY_FIXES = {
    "Folklore/World Mythology/African Diaspora Mythology": "African Diaspora Mythology",
    "Folklore/World Mythology/Buddhist Cosmology": "Buddhist Cosmology",
    "Folklore/World Mythology/Celtic Mythology": "Celtic Mythology",
    "Folklore/World Mythology/Egyptian Mythology": "Egyptian Mythology",
    "Folklore/World Mythology/Greek Mythology": "Greek Mythology",
    "Folklore/World Mythology/Hindu Mythology": "Hindu Mythology",
    "Folklore/World Mythology/Japanese Mythology": "Japanese Mythology",
    "Folklore/World Mythology/Mesopotamian Mythology": "Mesopotamian Mythology",
    "Folklore/World Mythology/Native American Mythology": "Native American Mythology",
    "Folklore/World Mythology/Norse Mythology": "Norse Mythology",
    "Folklore/World Mythology/Slavic and Eastern European Mythology": "Slavic and Eastern European Mythology",
    "Folklore/World Mythology/Taoist Mythology": "Taoist Mythology",
    "Folklore/Fairy Tales/Rapunzel": "Rapunzel",
}

# Archetype variants
ARCHETYPE_FIXES = {
    "The Wise Old Woman": "Wise Old Man",  # No separate file for Old Woman
}

# Hero's Journey stage fixes
HERO_JOURNEY_FIXES = {
    "Call to Adventure": "The Call to Adventure",
    "Crossing the Threshold": "Crossing the First Threshold",
    "Freedom to Live": "Return with the Elixir",  # Final stage
}

# Simple archetype name fixes (remove "The" when file doesn't have it)
SIMPLE_ARCHETYPE_FIXES = {
    "World Mythology": "Personal Mythos",  # Parent overview file
    "Anima and Animus": "Encounter with Anima-Animus",  # Individuation stage
}

def fix_gates(content):
    """Fix gate references."""
    changes = 0
    
    # Pattern 1: [[Gate N]] → [[Gate 0N - Name]] (single digit)
    for num in range(1, 10):
        pattern = rf'\[\[Gate {num}\]\]'
        replacement = f'[[Gate 0{num} - {GATE_NAMES[num]}]]'
        count = len(re.findall(pattern, content))
        if count:
            content = re.sub(pattern, replacement, content)
            changes += count
    
    # Pattern 2: [[Gate NN]] → [[Gate NN - Name]] (double digit)
    for num in range(10, 65):
        pattern = rf'\[\[Gate {num}\]\]'
        replacement = f'[[Gate {num} - {GATE_NAMES[num]}]]'
        count = len(re.findall(pattern, content))
        if count:
            content = re.sub(pattern, replacement, content)
            changes += count
    
    # Pattern 3: [[Gate N - Wrong Name]] → [[Gate 0N - Correct Name]]
    for num in range(1, 10):
        pattern = rf'\[\[Gate {num} - [^\]]+\]\]'
        replacement = f'[[Gate 0{num} - {GATE_NAMES[num]}]]'
        count = len(re.findall(pattern, content))
        if count:
            content = re.sub(pattern, replacement, content)
            changes += count
    
    # Pattern 4: [[Gate NN - Wrong Name]] → [[Gate NN - Correct Name]]
    for num in range(10, 65):
        pattern = rf'\[\[Gate {num} - [^\]]+\]\]'
        replacement = f'[[Gate {num} - {GATE_NAMES[num]}]]'
        count = len(re.findall(pattern, content))
        if count:
            content = re.sub(pattern, replacement, content)
            changes += count
    
    return content, changes

def fix_other_patterns(content):
    """Fix other patterns."""
    changes = 0
    
    # Individuation stages
    for old, new in INDIVIDUATION_FIXES.items():
        pattern = rf'\[\[{re.escape(old)}(?:\|[^\]]+)?\]\]'
        count = len(re.findall(pattern, content))
        if count:
            content = re.sub(pattern, rf'[[{new}]]', content)
            changes += count
    
    # Internal sections
    for old, new in INTERNAL_FIXES.items():
        pattern = rf'\[\[{re.escape(old)}(?:\|[^\]]+)?\]\]'
        count = len(re.findall(pattern, content))
        if count:
            content = re.sub(pattern, rf'[[{new}]]', content)
            changes += count
    
    # Folklore paths
    for old, new in FOLKLORE_MYTHOLOGY_FIXES.items():
        pattern = rf'\[\[{re.escape(old)}(?:\|[^\]]+)?\]\]'
        count = len(re.findall(pattern, content))
        if count:
            content = re.sub(pattern, rf'[[{new}]]', content)
            changes += count
    
    # Archetype variants
    for old, new in ARCHETYPE_FIXES.items():
        pattern = rf'\[\[{re.escape(old)}(?:\|[^\]]+)?\]\]'
        count = len(re.findall(pattern, content))
        if count:
            content = re.sub(pattern, rf'[[{new}]]', content)
            changes += count
    
    # Hero's Journey stages
    for old, new in HERO_JOURNEY_FIXES.items():
        pattern = rf'\[\[{re.escape(old)}(?:\|[^\]]+)?\]\]'
        count = len(re.findall(pattern, content))
        if count:
            content = re.sub(pattern, rf'[[{new}]]', content)
            changes += count
    
    # Simple fixes
    for old, new in SIMPLE_ARCHETYPE_FIXES.items():
        pattern = rf'\[\[{re.escape(old)}(?:\|[^\]]+)?\]\]'
        count = len(re.findall(pattern, content))
        if count:
            content = re.sub(pattern, rf'[[{new}]]', content)
            changes += count
    
    return content, changes

def main():
    total_files = 0
    total_changes = 0
    
    for md_file in sorted(PERSONAL_MYTHOS.rglob("*.md")):
        content = md_file.read_text()
        
        # Apply fixes
        content, gate_changes = fix_gates(content)
        content, other_changes = fix_other_patterns(content)
        
        changes = gate_changes + other_changes
        
        if changes > 0:
            md_file.write_text(content)
            print(f"✓ {md_file.relative_to(PERSONAL_MYTHOS)}: {changes} fixes")
            total_files += 1
            total_changes += changes
    
    print(f"\n{'='*60}")
    print(f"BATCH 2 COMPLETE: {total_changes} fixes across {total_files} files")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
