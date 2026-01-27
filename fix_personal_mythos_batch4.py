#!/usr/bin/env python3
"""Fix Personal Mythos Batch 4: Final cleanup."""

import re
from pathlib import Path

PERSONAL_MYTHOS = Path("Library/The Seven Pillars of Understanding/Personal Mythos")

# Fix remaining gate formats
GATE_MANUAL_FIXES = {
    "Gate 29 (HD)": "Gate 29 - The Abysmal",
    "Gate 39 (HD)": "Gate 39 - Obstruction",
    "Gate 59 (HD)": "Gate 59 - Dispersion",
    "Gate 59: Intimacy": "Gate 59 - Dispersion",
}

# Fix old folklore path with footnote (edge case)
FOLKLORE_EDGE_FIX = {
    "Folklore/Jungian Archetypes/The Threshold Guardian[^1]": "Threshold Guardian",
}

# Minor mythology references
MINOR_MYTHOLOGY_TO_PLAIN = [
    "Slavic Mythology", "Sumerian Mythology", "West African Mythology",
    "The Hedge of Thorns", "The Seven Ravens",
]

# Archangel references (link to existing Angelology files)
ARCHANGEL_FIXES = {
    "Archangel Gabriel": "Gabriel",
    "Archangel Michael": "Michael",
    "Archangel Raphael": "Raphael",
    "Archangel Uriel": "Uriel",
    "Chamuel": "Kamael",  # Alternate spelling
}

# Astrology references
ASTROLOGY_TO_PLAIN = [
    "Ascendant (Rising Sign)", "Black Moon Lilith", "Ceres (asteroid)",
    "Juno (asteroid)", "Pallas Athena (asteroid)", "Vesta (asteroid)",
    "Vertex", "Lot of Fortune", "Part of Fortune",
]

# Alchemy terms (concepts, not entries)
ALCHEMY_TO_PLAIN_BATCH4 = [
    "Athanor", "Calcinatio", "Cauda Pavonis", "Opus Contra Naturam",
    "Rubificatio", "Citrinitas (Alchemy)", "Nigredo (Alchemy)",
]

# Fairy tales and stories
FAIRY_TALES_TO_PLAIN_BATCH4 = [
    "Cap O' Rushes", "Donkeyskin", "The Girl Without Hands",
    "The Golden Bird", "The Twelve Brothers", "The White Snake",
    "Brother and Sister", "The Six Swans", "The Snow Queen",
]

# HD Channels
HD_CHANNELS_TO_PLAIN = [
    "Channel 10-20", "Channel 20-34", "Channel 57-34",
]

# Jungian/Psychological concepts
JUNGIAN_TO_PLAIN_BATCH4 = [
    "Archetypes", "Archetype", "Complex", "Active Imagination",
    "Amplification", "Circumambulation", "Enantiodromia",
]

# Tarot/Qabalah references
TAROT_QABALAH_TO_PLAIN = [
    "Qabalah/Paths", "The Lightning Flash", "The Serpent Path",
]

# Mythology figures (concepts, not entries)
MYTHOLOGY_FIGURES_TO_PLAIN = [
    "Atropos", "Avalokiteshvara", "Clotho", "Demeter", "Lachesis",
    "Nephthys", "Tara", "Yemaya", "Oshun", "Oya",
]

# Alchemical/Hermetic symbols
SYMBOLS_TO_PLAIN = [
    "Caduceus", "Ouroboros", "Vesica Piscis",
]

# System references (forward references or meta-references)
SYSTEM_REFS_TO_PLAIN = [
    "INDEX - Personal Mythos Master List", "RUBRIC - Library Content Standard",
]

# Campbell/Hero's Journey specifics
CAMPBELL_TO_PLAIN = [
    "Belly of the Whale", "Refusal of Return", "Magic Flight",
    "Rescue from Without", "Master of Two Worlds",
]

# Miscellaneous
MISC_TO_PLAIN = [
    "Threshold Guardian", "Daemon", "Daimon", "Anima Figura",
    "Puella Aeterna", "Senex", "Seven-Coordinate Navigation",
]

def apply_fixes(content):
    """Apply all fixes."""
    changes = 0
    
    # Gate fixes
    for old, new in GATE_MANUAL_FIXES.items():
        pattern = rf'\[\[{re.escape(old)}(?:\|[^\]]+)?\]\]'
        count = len(re.findall(pattern, content))
        if count:
            content = re.sub(pattern, rf'[[{new}]]', content)
            changes += count
    
    # Folklore edge case
    for old, new in FOLKLORE_EDGE_FIX.items():
        pattern = rf'\[\[{re.escape(old)}\]\]'
        count = len(re.findall(pattern, content))
        if count:
            content = re.sub(pattern, rf'[[{new}]]', content)
            changes += count
    
    # Archangels
    for old, new in ARCHANGEL_FIXES.items():
        pattern = rf'\[\[{re.escape(old)}(?:\|[^\]]+)?\]\]'
        count = len(re.findall(pattern, content))
        if count:
            content = re.sub(pattern, rf'[[{new}]]', content)
            changes += count
    
    # Convert to plain text
    all_to_plain = (MINOR_MYTHOLOGY_TO_PLAIN + ASTROLOGY_TO_PLAIN + 
                   ALCHEMY_TO_PLAIN_BATCH4 + FAIRY_TALES_TO_PLAIN_BATCH4 +
                   HD_CHANNELS_TO_PLAIN + JUNGIAN_TO_PLAIN_BATCH4 +
                   TAROT_QABALAH_TO_PLAIN + MYTHOLOGY_FIGURES_TO_PLAIN +
                   SYMBOLS_TO_PLAIN + SYSTEM_REFS_TO_PLAIN +
                   CAMPBELL_TO_PLAIN + MISC_TO_PLAIN)
    
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
        new_content, changes = apply_fixes(content)
        
        if changes > 0:
            md_file.write_text(new_content)
            print(f"✓ {md_file.relative_to(PERSONAL_MYTHOS)}: {changes} fixes")
            total_files += 1
            total_changes += changes
    
    print(f"\n{'='*60}")
    print(f"BATCH 4 COMPLETE: {total_changes} fixes across {total_files} files")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
