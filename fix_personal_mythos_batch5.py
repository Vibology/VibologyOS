#!/usr/bin/env python3
"""Fix Personal Mythos Batch 5: Final remaining patterns."""

import re
from pathlib import Path

PERSONAL_MYTHOS = Path("Library/The Seven Pillars of Understanding/Personal Mythos")

# Archetype fixes
FINAL_ARCHETYPE_FIXES = {
    "The Trickster": "The Joker",
    "The Herald": "Threshold Guardian",
    "The Child": "The Divine Child",
    "The Sage": "The Wise Old Man",
    "The Innocent": "The Divine Child",
}

# HD fixes
HD_FINAL_FIXES = {
    "Solar Plexus Center": "Solar Plexus",
    "Splenic Center": "Spleen",
    "Undefined Centers": "Centers",
    "Defined vs Undefined Centers": "Centers",
    "Defined Head Center": "Head",
    "Manifestor Type": "Manifestor",
    "Tribal Circuit": "Human Design",
    "Not-Self": "Strategy",
}

# Tarot path fixes (long paths)
TAROT_PATH_PATTERNS = [
    (r'\[\[The Tarot/Major Arcana/(\d+) - ([^\]]+)\]\]', 
     lambda m: f"[[{m.group(2)}]]"),
]

# Tarot Roman numeral format fixes
TAROT_ROMAN_FIXES = {
    "0 - The Fool": "The Fool (0)",
    "I - The Magician": "The Magician (I)",
    "II - The High Priestess": "The High Priestess (II)",
    "III - The Empress": "The Empress (III)",
    "IV - The Emperor": "The Emperor (IV)",
    "V - The Hierophant": "The Hierophant (V)",
    "VI - The Lovers": "The Lovers (VI)",
    "VII - The Chariot": "The Chariot (VII)",
    "VIII - Strength": "Strength (VIII)",
    "IX - The Hermit": "The Hermit (IX)",
    "X - Wheel of Fortune": "Wheel of Fortune (X)",
    "XI - Justice": "Justice (XI)",
    "XII - The Hanged Man": "The Hanged Man (XII)",
    "XIII - Death": "Death (XIII)",
    "XIV - Temperance": "Temperance (XIV)",
    "XV - The Devil": "The Devil (XV)",
    "XVI - The Tower": "The Tower (XVI)",
    "XVII - The Star": "The Star (XVII)",
    "XVIII - The Moon": "The Moon (XVIII)",
    "XIX - The Sun": "The Sun (XIX)",
    "XX - Judgement": "Judgement (XX)",
    "XXI - The World": "The World (XXI)",
}

# Qabalah spelling fixes
QABALAH_FIXES = {
    "Tiphereth": "Tiphareth",
}

# Astrology fixes
ASTROLOGY_FINAL_FIXES = {
    "Descendant": "Astrology",
    "The Eighth House": "8th House",
    "The Twelfth House": "12th House",
    "Pluto Transits": "Pluto ♇",
}

# System reference fix
SYSTEM_FIXES = {
    "Core Foundations/Logos": "Logos",
}

# Fairy tale motifs and Campbell terms → plain text
MOTIFS_TO_PLAIN = [
    "The Awakening Kiss", "The Animal Helpers", "The Helpful Animal",
    "The Magic Object", "The Frog King", "Supernatural Aid",
    "Woman as Temptress", "The White Queen", "The Terrible Mother",
    "The Mother Complex", "The Wounded Healer", "The Dragon-Slayer",
    "Initiation Rites", "The Boon", "The Fisher King",
    "The Spirit in the Bottle", "The Labyrinth", "The Threshold",
    "The Quest", "The Redeemer", "The Golden Fleece", "The Reborn God",
    "The Individuated Self", "The Master of Two Worlds", "Ereshkigal",
    "The Treasure Hard to Attain", "Integration", "Sacred Marriage",
    "Vision Quest", "Iteratio", "The Seven Heavens", "The Ogdoad",
    "The Curse and Redemption", "The Recognition Token", "Lilith",
    "Putrefaction", "Fitcher's Bird", "Philomela and Procne",
    "Regression", "Danaë", "The Puella Aeterna", "Melusine",
    "The Fairy Godmother", "Inferior Function", "Eros and Logos",
    "Libido", "Inner Child", "Underworld", "Mystical Union",
    "Theosis",
]

def apply_fixes(content):
    """Apply all fixes."""
    changes = 0
    
    # Archetype fixes
    for old, new in FINAL_ARCHETYPE_FIXES.items():
        pattern = rf'\[\[{re.escape(old)}(?:\|[^\]]+)?\]\]'
        count = len(re.findall(pattern, content))
        if count:
            content = re.sub(pattern, rf'[[{new}]]', content)
            changes += count
    
    # HD fixes
    for old, new in HD_FINAL_FIXES.items():
        pattern = rf'\[\[{re.escape(old)}(?:\|[^\]]+)?\]\]'
        count = len(re.findall(pattern, content))
        if count:
            content = re.sub(pattern, rf'[[{new}]]', content)
            changes += count
    
    # Tarot path patterns
    for pattern_str, replacement_fn in TAROT_PATH_PATTERNS:
        matches = list(re.finditer(pattern_str, content))
        if matches:
            for match in reversed(matches):  # Process in reverse to maintain positions
                replacement = replacement_fn(match)
                content = content[:match.start()] + replacement + content[match.end():]
                changes += 1
    
    # Tarot Roman numeral fixes
    for old, new in TAROT_ROMAN_FIXES.items():
        pattern = rf'\[\[{re.escape(old)}\]\]'
        count = len(re.findall(pattern, content))
        if count:
            content = re.sub(pattern, rf'[[{new}]]', content)
            changes += count
    
    # Qabalah fixes
    for old, new in QABALAH_FIXES.items():
        pattern = rf'\[\[{re.escape(old)}(?:\|[^\]]+)?\]\]'
        count = len(re.findall(pattern, content))
        if count:
            content = re.sub(pattern, rf'[[{new}]]', content)
            changes += count
    
    # Astrology fixes
    for old, new in ASTROLOGY_FINAL_FIXES.items():
        pattern = rf'\[\[{re.escape(old)}(?:\|[^\]]+)?\]\]'
        count = len(re.findall(pattern, content))
        if count:
            content = re.sub(pattern, rf'[[{new}]]', content)
            changes += count
    
    # System fixes
    for old, new in SYSTEM_FIXES.items():
        pattern = rf'\[\[{re.escape(old)}(?:\|[^\]]+)?\]\]'
        count = len(re.findall(pattern, content))
        if count:
            content = re.sub(pattern, rf'[[{new}]]', content)
            changes += count
    
    # Convert motifs to plain text
    for term in MOTIFS_TO_PLAIN:
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
        new_content, changes = apply_fixes(content)
        
        if changes > 0:
            md_file.write_text(new_content)
            print(f"✓ {md_file.relative_to(PERSONAL_MYTHOS)}: {changes} fixes")
            total_files += 1
            total_changes += changes
    
    print(f"\n{'='*60}")
    print(f"BATCH 5 COMPLETE: {total_changes} fixes across {total_files} files")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
