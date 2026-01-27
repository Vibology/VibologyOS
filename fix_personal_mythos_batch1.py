#!/usr/bin/env python3
"""Fix batch-repairable dead links in Personal Mythos - Batch 1."""

import re
from pathlib import Path

PERSONAL_MYTHOS = Path("Library/The Seven Pillars of Understanding/Personal Mythos")

# Pattern 1: Old Folklore paths
FOLKLORE_FIXES = {
    "Folklore/Jungian Archetypes/The Anima": "Anima",
    "Folklore/Jungian Archetypes/The Animus": "Animus",
    "Folklore/Jungian Archetypes/The Divine Child": "Divine Child",
    "Folklore/Jungian Archetypes/The Great Mother": "Great Mother",
    "Folklore/Jungian Archetypes/The Hero": "Hero",
    "Folklore/Jungian Archetypes/The Joker": "Joker",
    "Folklore/Jungian Archetypes/The Persona": "Persona",
    "Folklore/Jungian Archetypes/The Self": "Self",
    "Folklore/Jungian Archetypes/The Shadow": "Shadow",
    "Folklore/Jungian Archetypes/The Shapeshifter": "Shapeshifter",
    "Folklore/Jungian Archetypes/The Threshold Guardian": "Threshold Guardian",
    "Folklore/Jungian Archetypes/The Wise Old Man": "Wise Old Man",
    "Folklore/Jungian Archetypes/The Wise Old Woman": "Wise Old Woman",
}

# Pattern 2: Long Seven Pillars paths
LONG_PATH_FIXES = {
    "The Seven Pillars of Understanding/Personal Mythos/Jungian Archetypes/The Anima": "Anima",
    "The Seven Pillars of Understanding/Personal Mythos/Jungian Archetypes/The Animus": "Animus",
    "The Seven Pillars of Understanding/Personal Mythos/Jungian Archetypes/The Divine Child": "Divine Child",
    "The Seven Pillars of Understanding/Personal Mythos/Jungian Archetypes/The Great Mother": "Great Mother",
    "The Seven Pillars of Understanding/Personal Mythos/Jungian Archetypes/The Hero": "Hero",
    "The Seven Pillars of Understanding/Personal Mythos/Jungian Archetypes/The Joker": "Joker",
    "The Seven Pillars of Understanding/Personal Mythos/Jungian Archetypes/The Persona": "Persona",
    "The Seven Pillars of Understanding/Personal Mythos/Jungian Archetypes/The Self": "Self",
    "The Seven Pillars of Understanding/Personal Mythos/Jungian Archetypes/The Shadow": "Shadow",
    "The Seven Pillars of Understanding/Personal Mythos/Jungian Archetypes/The Shapeshifter": "Shapeshifter",
    "The Seven Pillars of Understanding/Personal Mythos/Jungian Archetypes/The Threshold Guardian": "Threshold Guardian",
    "The Seven Pillars of Understanding/The Window/The Twelve Archetypes/The Divine Child": "Divine Child",
    "The Seven Pillars of Understanding/The Window/The Twelve Archetypes/The Great Mother": "Great Mother",
    "The Seven Pillars of Understanding/The Window/The Twelve Archetypes/The Hero": "Hero",
    "The Seven Pillars of Understanding/The Window/The Twelve Archetypes/The Joker": "Joker",
    "The Seven Pillars of Understanding/The Window/The Twelve Archetypes/The Persona": "Persona",
}

# Pattern 3: Tarot cards (add Roman numerals using display alias)
TAROT_FIXES = {
    "The Fool": "0 - The Fool|The Fool (0)",
    "The Magician": "1 - The Magician|The Magician (I)",
    "The High Priestess": "2 - The High Priestess|The High Priestess (II)",
    "The Empress": "3 - The Empress|The Empress (III)",
    "The Emperor": "4 - The Emperor|The Emperor (IV)",
    "The Hierophant": "5 - The Hierophant|The Hierophant (V)",
    "The Lovers": "6 - The Lovers|The Lovers (VI)",
    "The Chariot": "7 - The Chariot|The Chariot (VII)",
    "Strength": "8 - Strength|Strength (VIII)",
    "The Hermit": "9 - The Hermit|The Hermit (IX)",
    "Wheel of Fortune": "10 - Wheel of Fortune|Wheel of Fortune (X)",
    "Justice": "11 - Justice|Justice (XI)",
    "The Hanged Man": "12 - The Hanged Man|The Hanged Man (XII)",
    "Death": "13 - Death|Death (XIII)",
    "Temperance": "14 - Temperance|Temperance (XIV)",
    "The Devil": "15 - The Devil|The Devil (XV)",
    "The Tower": "16 - The Tower|The Tower (XVI)",
    "The Star": "17 - The Star|The Star (XVII)",
    "The Moon": "18 - The Moon|The Moon (XVIII)",
    "The Sun": "19 - The Sun|The Sun (XIX)",
    "Judgement": "20 - Judgement|Judgement (XX)",
    "Judgment": "20 - Judgement|Judgment (XX)",
    "The World": "21 - The World|The World (XXI)",
}

# Pattern 4: Center suffix removal
CENTER_FIXES = {
    "Ajna Center": "Ajna",
    "G-Center": "G Center",
    "Head Center": "Head",
    "Root Center": "Root",
    "Sacral Center": "Sacral",
    "Spleen Center": "Spleen",
    "Throat Center": "Throat",
    "Emotional Solar Plexus": "Solar Plexus",
}

# Pattern 5: External systems → plain text (remove wikilink)
EXTERNAL_TO_PLAIN = ["Buddhism", "Christian Mysticism", "Christianity", "Qabalah", "Taoism", "Kabbalah", "I-Ching"]

# Pattern 6: Hexagrams → plain text (not in Library)
# Match pattern: [[Hexagram...]] → plain text

def fix_wikilink(content):
    """Fix wikilinks in content."""
    changes = 0
    
    # Fix 1: Old Folklore paths
    for old, new in FOLKLORE_FIXES.items():
        pattern = rf'\[\[{re.escape(old)}(?:\|([^\]]+))?\]\]'
        matches = re.findall(pattern, content)
        if matches:
            content = re.sub(pattern, rf'[[{new}]]', content)
            changes += len(matches)
    
    # Fix 2: Long paths
    for old, new in LONG_PATH_FIXES.items():
        pattern = rf'\[\[{re.escape(old)}(?:\|([^\]]+))?\]\]'
        matches = re.findall(pattern, content)
        if matches:
            content = re.sub(pattern, rf'[[{new}]]', content)
            changes += len(matches)
    
    # Fix 3: Tarot cards
    for old, new in TAROT_FIXES.items():
        # Only fix if it's exactly [[The Card]] (no existing alias)
        pattern = rf'\[\[{re.escape(old)}\]\]'
        matches = re.findall(pattern, content)
        if matches:
            content = re.sub(pattern, rf'[[{new}]]', content)
            changes += len(matches)
    
    # Fix 4: Centers
    for old, new in CENTER_FIXES.items():
        pattern = rf'\[\[{re.escape(old)}(?:\|([^\]]+))?\]\]'
        matches = re.findall(pattern, content)
        if matches:
            content = re.sub(pattern, rf'[[{new}]]', content)
            changes += len(matches)
    
    # Fix 5: External systems → plain text
    for term in EXTERNAL_TO_PLAIN:
        pattern = rf'\[\[{re.escape(term)}\]\]'
        matches = re.findall(pattern, content)
        if matches:
            content = re.sub(pattern, term, content)
            changes += len(matches)
    
    # Fix 6: Hexagrams → plain text
    pattern = r'\[\[(Hexagram [^\]]+)\]\]'
    matches = re.findall(pattern, content)
    if matches:
        content = re.sub(pattern, r'\1', content)
        changes += len(matches)
    
    return content, changes

def main():
    total_files = 0
    total_changes = 0
    
    for md_file in sorted(PERSONAL_MYTHOS.rglob("*.md")):
        content = md_file.read_text()
        new_content, changes = fix_wikilink(content)
        
        if changes > 0:
            md_file.write_text(new_content)
            print(f"✓ {md_file.relative_to(PERSONAL_MYTHOS)}: {changes} fixes")
            total_files += 1
            total_changes += changes
    
    print(f"\n{'='*60}")
    print(f"BATCH 1 COMPLETE: {total_changes} fixes across {total_files} files")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
