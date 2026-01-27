#!/usr/bin/env python3
"""Fix Personal Mythos Batch 6: Convert remaining forward references to plain text."""

import re
from pathlib import Path

PERSONAL_MYTHOS = Path("Library/The Seven Pillars of Understanding/Personal Mythos")

# Tarot card fixes (simple names)
TAROT_SIMPLE_FIXES = {
    "The Magician": "The Magician (I)",
    "The High Priestess": "The High Priestess (II)",
    "The Lovers": "The Lovers (VI)",
    "The Wheel of Fortune (X)": "Wheel of Fortune (X)",
}

# Simple cross-references that exist
SIMPLE_FIXES = {
    "Logos": "Core Foundations/Logos",  # Need full path
    "Threshold Guardian": "The Threshold Guardian",  # Add "The"
}

# All remaining concepts → plain text (forward references)
ALL_TO_PLAIN = [
    # Jungian/Psychological concepts
    "Underworld", "The Coniunctio", "The Father Wound", "The Wounded King",
    "Kronos Devouring His Children", "Peter Pan Syndrome", "Sacred Fool",
    "Shapeshifting", "Zero Point", "Wry Schizophrenia", "Puer/Puella",
    "Ego", "The Devouring Mother", "The Terrible Father", "Terrible Mother",
    "Threshold Experience", "Exposure Therapy", "Rite of Passage",
    "The Belly of the Beast", "The Forest", "The River Styx", "The Crone",
    "Post-Traumatic Growth", "Generativity vs. Stagnation", "Logotherapy",
    "Somatic Healing", "Narrative Therapy", "Threshold", "The Exile",
    "The Pregnancy", "Dismemberment", "PTSD", "Ego Death",
    "regressive restoration of the persona", "Numinous", "Hubris",
    "Comfort Zone", "Homeostasis",
    
    # Campbell/Hero's Journey
    "Meeting with the Mentor", "Refusal of the Return", "The Magic Flight",
    "Crossing the Return Threshold", "The Return Threshold", "The Monomyth",
    
    # Fairy tales and stories
    "The Little Mermaid", "The Flying Dutchman", "Jack and the Beanstalk",
    "Puss in Boots", "The Golden Goose", "The Brave Little Tailor",
    "The Sleeping Beauty", "Parsifal",
    
    # HD concepts
    "Individual Circuitry", "The Whole Chart", "Profile",
    "Personality Crystal", "Design Crystal", "Conscious Sun",
    "Defined Centers", "Defined Ego/Heart Center", "Open Head Center",
    "Open Ajna Center", "Reflector Type", "Undefined G Center",
    "Line 6 - Role Model", "Line 3 - Martyr", "Line 5 - Heretic",
    "The Superior Personality",
    
    # Qabalah
    "Path 26 - Ayin", "Path 13 - Gimel", "Da'ath", "The Cherubim",
    "The Hermetic Tradition", "The Caduceus",
    
    # Astrology
    "Midheaven", "Sun Sign", "Midheaven (MC)", "The Fourth House",
    "First Saturn Return", "Moon in Cancer",
    
    # Mythology
    "Heimdallr", "Loki", "Tiresias", "Sol Invictus", "Lila",
    "Duat", "Sage",
    
    # Other
    "Gnostic Texts", "Sulfur", "Multiplication", "Five Hindrances",
    "The Village", "The Hearth", "The Twelve Archetypes",
    "House of the Spirit",
]

def apply_final_fixes(content):
    """Apply final fixes."""
    changes = 0
    
    # Tarot fixes
    for old, new in TAROT_SIMPLE_FIXES.items():
        pattern = rf'\[\[{re.escape(old)}\]\]'
        count = len(re.findall(pattern, content))
        if count:
            content = re.sub(pattern, rf'[[{new}]]', content)
            changes += count
    
    # Simple fixes
    for old, new in SIMPLE_FIXES.items():
        pattern = rf'\[\[{re.escape(old)}\]\]'
        count = len(re.findall(pattern, content))
        if count:
            content = re.sub(pattern, rf'[[{new}]]', content)
            changes += count
    
    # Convert to plain text
    for term in ALL_TO_PLAIN:
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
        new_content, changes = apply_final_fixes(content)
        
        if changes > 0:
            md_file.write_text(new_content)
            print(f"✓ {md_file.relative_to(PERSONAL_MYTHOS)}: {changes} fixes")
            total_files += 1
            total_changes += changes
    
    print(f"\n{'='*60}")
    print(f"BATCH 6 FINAL COMPLETE: {total_changes} fixes across {total_files} files")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
