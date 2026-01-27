#!/usr/bin/env python3
"""Fix Angelology dead links - Batch 1: Major patterns."""

import re
from pathlib import Path

ANGELOLOGY = Path("Library/The Seven Pillars of Understanding/Angelology")

# Fix old Folklore paths
FOLKLORE_FIXES = {
    "Folklore/Jungian Archetypes/The Self": "The Self",
    "Folklore/Jungian Archetypes/The Hero": "The Hero",
    "Folklore/Jungian Archetypes/The Great Mother": "The Great Mother",
    "Folklore/Jungian Archetypes/The Animus": "The Animus",
}

# Fix HD Center references
HD_CENTER_FIXES = {
    "Ajna Center": "Ajna",
    "G-Center": "G Center",
    "Head Center": "Head",
    "Heart Center": "Heart",
    "Root Center": "Root",
    "Sacral Center": "Sacral",
    "Spleen Center": "Spleen",
    "Throat Center": "Throat",
    "Defined G-Center": "G Center",
    "Undefined G-Center": "G Center",
    "Defined Head Center": "Head",
    "Undefined Head Center": "Head",
    "Defined vs. Undefined Centers": "Centers",
    "Defined vs. Undefined Heart": "Heart",
}

# Fix The Nine → The Ten Angelic Orders
ORDERS_FIX = {
    "The Nine Angelic Orders": "The Ten Angelic Orders",
}

# Fix Astrology paths
ASTROLOGY_FIXES = {
    "Astrology/Planets/Mercury # ☿": "Mercury ☿",
}

# Fix Tarot cards
TAROT_FIXES = {
    "Justice (VIII or XI)": "Justice (XI)",
    "Strength (VIII or XI)": "Strength (VIII)",
    "The Wheel of Fortune (X)": "Wheel of Fortune (X)",
}

# Fix long Seven Pillars paths
def fix_long_paths(content):
    """Fix long Seven Pillars paths."""
    pattern = r'\[\[The Seven Pillars of Understanding/[^/]+/[^/]+/[^/]+/([^/\]]+)/Overview\]\]'
    matches = re.findall(pattern, content)
    changes = len(matches)
    if changes:
        # These are House overviews - convert to plain text
        content = re.sub(pattern, r'\1', content)
    return content, changes

# Fix section anchor escapes (backslash before closing bracket)
def fix_escaped_brackets(content):
    """Fix escaped brackets in wikilinks."""
    pattern = r'\[\[([^\]]+)\\\]\]'
    matches = re.findall(pattern, content)
    changes = len(matches)
    if changes:
        content = re.sub(pattern, r'[[\1]]', content)
    return content, changes

# Convert to plain text - Gene Keys, I-Ching, Hexagrams
GENE_KEYS_CHING_TO_PLAIN = []
# Pattern match for these

# Convert mythology figures to plain text
MYTHOLOGY_TO_PLAIN = [
    "Kali", "Sekhmet", "Morrigan", "Rudra", "Horus", "Indra", "Marduk", "Mithra",
    "Thor", "Asclepius", "Dhanvantari", "Chiron", "Lakshmi", "Odin", "Osiris",
    "Ptah", "Vishnu", "Ananke", "Neith", "Nut", "Shakti", "Themis", "Urd",
    "Anubis", "Hecate", "Amun-Ra", "Athena", "Durga", "Manjushri", "Brahma",
    "Ma'at", "Agni",
]

# Convert HD-specific concepts to plain text
HD_TO_PLAIN = [
    "Manifesting Generator", "Strategy and Authority", "Defined G-Center",
    "Undefined G-Center", "Mars and the Heart Center", "Venus and the Spleen Center",
]

# Convert forward references to plain text
FORWARD_REFS_TO_PLAIN = [
    "Annunciation", "Psychopomp", "Liminal Space", "Sevens", "First House",
    "Mars Correspondences", "Fifth House", "Dragon-Slayers Across Traditions",
    "Full Humanity Full Divinity", "Solar Deities and Light-Bringers",
    "Solar Return", "Sword of Discrimination", "The Dragon as Shadow",
    "The Sacred Well", "Vertical Ascent", "Warriors of the Spirit",
    "1 Enoch", "The Book of Tobit", "Hermes Psychopompos", "The Psychopomp",
    "The Wounded Healer", "Gnosis", "Sophia", "Completion", "Completion of the Work",
    "Earth", "Embodiment", "Incarnation", "Princesses (Pages)", "The Body as Temple",
    "Chamuel", "Jophiel", "Zadkiel", "Jupiter Return",
    "Jupiter Return and the Sovereignty Initiation", "The Heart as Throne",
    "The King/Queen", "Saturn Return", "Saturn Return at 29",
    "The Throat as Manifestation Gateway", "Coniunctio", "Katabasis",
    "Pentacles Suit", "The Philosopher's Stone", "Bodhisattvas", "Daimon",
    "Discernment", "Genius", "Intuition", "Ishta Devata", "Kiraman Katibin",
    "Spirit Guide", "Subtle Listening", "Yidam", "Numinous Encounter", "The Voice",
    "Vocation", "Chakra System", "Fixed Signs", "I-Ching", "Mythology",
    "Precession of the Equinoxes", "The Zodiac", "Authority vs. Tyranny - The Domination Paradox",
    "Chesed and Jupiter - The Expansive Father", "The G-Center as Throne - Sovereignty in Human Design",
    "The Sovereign", "The Wise Father", "Mars transits", "The Sword Archetype",
    "The Warrior Archetype", "Ancestral Spirits", "Anima Mundi",
    "Belonging and Identity", "Collective Unconscious", "Cultural Archetypes",
    "Genius Loci", "Landvaettir", "Lokapalas", "Orisha", "Seventh House",
    "The Guardian of Nations", "Amesha Spentas", "Dark Night of the Soul",
    "Fixed Stars", "Muqarrabun", "Mystical Union", "Primum Mobile", "Theosis",
    "Trisagion", "Conscious", "Individuation", "Transpersonal", "Unconscious",
    "The Norns", "The Superego", "Charites", "Christ Consciousness",
    "Grace as Unearned Gift", "Integration", "Miracles and Divine Intervention",
    "Paramitas", "Siddhis", "Transcendent Function", "Valkyries", "Ashim",
    "Archangels of the Sephiroth", "Apotheosis", "Primum Mobile",
]

# Gene Keys → plain text
def convert_gene_keys(content):
    """Convert Gene Keys references to plain text."""
    pattern = r'\[\[Gene Keys\]\]'
    count = len(re.findall(pattern, content))
    if count:
        content = re.sub(pattern, 'Gene Keys', content)
    return content, count

# Hexagram → plain text
def convert_hexagrams(content):
    """Convert Hexagram references to plain text."""
    pattern = r'\[\[Hexagram [^\]]+\]\]'
    matches = re.findall(pattern, content)
    if matches:
        for match in set(matches):
            content = content.replace(match, match[2:-2])  # Remove [[ and ]]
    return content, len(matches)

def apply_fixes(content):
    """Apply all fixes."""
    total_changes = 0
    
    # 1. Fix Folklore paths
    for old, new in FOLKLORE_FIXES.items():
        pattern = rf'\[\[{re.escape(old)}(?:\|[^\]]+)?\]\]'
        count = len(re.findall(pattern, content))
        if count:
            content = re.sub(pattern, rf'[[{new}]]', content)
            total_changes += count
    
    # 2. Fix HD Centers
    for old, new in HD_CENTER_FIXES.items():
        pattern = rf'\[\[{re.escape(old)}(?:\|[^\]]+)?\]\]'
        count = len(re.findall(pattern, content))
        if count:
            content = re.sub(pattern, rf'[[{new}]]', content)
            total_changes += count
    
    # 3. Fix Orders name
    for old, new in ORDERS_FIX.items():
        pattern = rf'\[\[{re.escape(old)}(?:\|[^\]]+)?\]\]'
        count = len(re.findall(pattern, content))
        if count:
            content = re.sub(pattern, rf'[[{new}]]', content)
            total_changes += count
    
    # 4. Fix Astrology paths
    for old, new in ASTROLOGY_FIXES.items():
        pattern = rf'\[\[{re.escape(old)}(?:\|[^\]]+)?\]\]'
        count = len(re.findall(pattern, content))
        if count:
            content = re.sub(pattern, rf'[[{new}]]', content)
            total_changes += count
    
    # 5. Fix Tarot cards
    for old, new in TAROT_FIXES.items():
        pattern = rf'\[\[{re.escape(old)}(?:\|[^\]]+)?\]\]'
        count = len(re.findall(pattern, content))
        if count:
            content = re.sub(pattern, rf'[[{new}]]', content)
            total_changes += count
    
    # 6. Fix long paths
    content, changes = fix_long_paths(content)
    total_changes += changes
    
    # 7. Fix escaped brackets
    content, changes = fix_escaped_brackets(content)
    total_changes += changes
    
    # 8. Convert Gene Keys
    content, changes = convert_gene_keys(content)
    total_changes += changes
    
    # 9. Convert Hexagrams
    content, changes = convert_hexagrams(content)
    total_changes += changes
    
    # 10. Convert to plain text - all categories
    all_to_plain = MYTHOLOGY_TO_PLAIN + HD_TO_PLAIN + FORWARD_REFS_TO_PLAIN
    for term in all_to_plain:
        pattern = rf'\[\[{re.escape(term)}\]\]'
        count = len(re.findall(pattern, content))
        if count:
            content = re.sub(pattern, term, content)
            total_changes += count
    
    return content, total_changes

def main():
    total_files = 0
    total_changes = 0
    
    for md_file in sorted(ANGELOLOGY.rglob("*.md")):
        content = md_file.read_text()
        new_content, changes = apply_fixes(content)
        
        if changes > 0:
            md_file.write_text(new_content)
            rel_path = md_file.relative_to(ANGELOLOGY)
            print(f"✓ {rel_path}: {changes} fixes")
            total_files += 1
            total_changes += changes
    
    print(f"\n{'='*60}")
    print(f"ANGELOLOGY BATCH 1: {total_changes} fixes across {total_files} files")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
