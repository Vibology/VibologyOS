#!/usr/bin/env python3
"""Fix dead wikilinks - Round 3: Alias fixes + bracket removals.

Category A: Rewrite as piped links to existing files
Category C: Scholar/author references → plain text
Category D: Noise/meta → plain text
Category E: Codex archetype names → plain text (or alias where clear target exists)
Category F: Low-value singles → plain text
"""

import os
import re
import sys
from pathlib import Path

VAULT = Path(os.path.expanduser("~/VibologyOS"))
LIBRARY = VAULT / "Library"

# Track changes
changes_made = []
files_modified = set()

# ============================================================
# CATEGORY A: ALIAS FIXES (dead link → piped link to existing file)
# ============================================================
# Format: (dead_pattern, replacement)
# These use exact string matching on the wikilink content

ALIAS_FIXES = {
    # HD Circuits → Channels.md section anchors
    "Collective Logic Circuit": "Channels#Collective Logic Circuit|Collective Logic Circuit",
    "Individual Centering Circuit": "Channels#Individual Centering Circuit|Individual Centering Circuit",
    "Individual Knowing Circuit": "Channels#Individual Knowing Circuit|Individual Knowing Circuit",
    "Tribal Ego Circuit": "Channels#Tribal Ego Circuit|Tribal Ego Circuit",
    "Collective Abstract Circuit": "Channels#Collective Sensing (Abstract) Circuit|Collective Abstract Circuit",
    "Collective Sensing/Abstract Circuit": "Channels#Collective Sensing (Abstract) Circuit|Collective Sensing/Abstract Circuit",
    "Tribal Circuit": "Channels#3. Tribal Circuit|Tribal Circuit",
    "Tribal Defense Circuit": "Channels#Tribal Defense Circuit|Tribal Defense Circuit",
    "Collective Sensing Circuit": "Channels#Collective Sensing (Abstract) Circuit|Collective Sensing Circuit",
    "Collective Sharing Circuit": "Channels#2. Collective Circuit|Collective Sharing Circuit",
    "Individual Circuit": "Channels#1. Individual Circuit|Individual Circuit",

    # Archetype aliases
    "The Trickster": "The Joker|The Trickster",
    "Trickster Archetype": "The Joker|Trickster Archetype",
    "The Mother Archetype": "The Great Mother|The Mother Archetype",
    "The Child Archetype": "The Divine Child|The Child Archetype",
    "The Hermit Archetype": "The Hermit (IX)|The Hermit Archetype",
    "King-Queen Archetype": "The Syzygy|King-Queen Archetype",
    "The Guardian Archetype": "The Threshold Guardian|The Guardian Archetype",
    "The Holy Fool": "The Joker|The Holy Fool",
    "The Kore": "Persephone|The Kore",
    "The Sage": "The Wise Old Man|The Sage",
    "The Elder": "The Senex|The Elder",
    "The Elder Archetype": "The Senex|The Elder Archetype",
    "Wise Old Man-Woman": "The Wise Old Man|Wise Old Man-Woman",
    "Eternal Youth": "Puer and Puella|Eternal Youth",
    "Death and Rebirth Archetype": "Death and Resurrection|Death and Rebirth Archetype",
    "The Devouring Father": "The Senex|The Devouring Father",

    # Jungian concept aliases
    "Archetypes": "Jungian Archetypes|Archetypes",

    # HD aliases
    "Manifesting Generator": "Generator|Manifesting Generator",
    "Defined Sacral": "Sacral|Defined Sacral",

    # Angelology aliases
    "The Nine Orders of Angels": "The Ten Angelic Orders|The Nine Orders of Angels",
    "The Seven Archangels": "The Seven Planetary Archangels|The Seven Archangels",
    "Kerubim": "Cherubim|Kerubim",
    "Archangel Correspondence - Moon": "Gabriel|Lunar Archangel",
    "Archangel Correspondence - Sun": "Michael|Solar Archangel",
    "Archangel Correspondence - Venus": "Haniel|Venus Archangel",
    "Hierarchical Consciousness": "The Celestial Hierarchy|Hierarchical Consciousness",

    # Qabalah aliases
    "EHEIEH": "Eheieh|EHEIEH",
    "Qabalistic Cross": "Lesser Banishing Ritual of the Pentagram|Qabalistic Cross",

    # Tarot aliases
    "Eight of Disks (Prudence)": "Eight of Pentacles|Eight of Disks (Prudence)",
    "Four of Disks (Power)": "Four of Pentacles|Four of Disks (Power)",
    "Four of Swords (Truce)": "Four of Swords|Four of Swords (Truce)",
    "The Major Arcana": "The Fool's Journey|The Major Arcana",

    # Astrology aliases
    "essential dignity": "Planetary Condition|essential dignity",
    "Dignities & Rulerships": "Planetary Condition|Dignities & Rulerships",
    "Mars Archetype": "Mars ♂|Mars Archetype",
    "Saturn Archetype": "Saturn ♄|Saturn Archetype",
    "Saturn Return": "Saturn ♄|Saturn Return",

    # Mythology aliases
    "Hermes/Mercury": "Hermes|Hermes/Mercury",
    "Hermes/Mercury Archetype": "Hermes|Hermes/Mercury Archetype",

    # Codex alias
    "The Receptive (02)": "02 - The Receptive|The Receptive (02)",

    # Planet aliases
    "Luna": "Moon ☽|Luna",
}

# ============================================================
# SPECIAL COMPOUND FIXES (need regex or multi-link replacement)
# ============================================================
COMPOUND_FIXES = {
    # [[Chesed & Geburah]] → [[Chesed]] & [[Geburah]]
    "[[Chesed & Geburah]]": "[[Chesed]] & [[Geburah]]",
    # [[Anima and Animus]] → [[The Anima|Anima]] and [[The Animus|Animus]]
    "[[Anima and Animus]]": "[[The Anima|Anima]] and [[The Animus|Animus]]",
    # [[Strategy and Authority]] → [[Strategy]] and [[Authority]]
    "[[Strategy and Authority]]": "[[Strategy]] and [[Authority]]",
    # Full path Uriel link → simple link
    "[[The Seven Pillars of Understanding/Angelology/The Archangels/Uriel]]": "[[Uriel]]",
}

# ============================================================
# CATEGORY C: SCHOLAR/AUTHOR REFERENCES → plain text
# ============================================================
SCHOLARS = [
    "Gustav Davidson",
    "Robert Wang",
    "Plotinus",
    "Thomas Aquinas",
    "Carl Jung",
    "Pseudo-Dionysius the Areopagite",
    "Dante Alighieri",
    "Dante",
    "Aldous Huxley",
    "Aristotle",
    "Cicero",
    "Gregory the Great",
    "Ibn Arabi",
    "Maimonides",
    "Meister Eckhart",
    "Plato",
    "Proclus",
    "Shankara",
    "Thomas Heywood",
    "Ezekiel",
]

# ============================================================
# CATEGORY D: NOISE/META → plain text
# ============================================================
NOISE = [
    "wikilinks",
    "wikilink",
    "Double bracket",
]
# Note: [[Relevant Entry]] is only in a template — leave it alone

# ============================================================
# CATEGORY E: CODEX/ASTROLABE ARCHETYPE NAMES → plain text
# ============================================================
ARCHETYPE_NAMES = [
    "The Oracle Archetype",
    "The Phoenix",
    "The Apprentice",
    "The Artist",
    "The Body",
    "The Builder Archetype",
    "The Dancer",
    "The Descent Archetype",
    "The Dionysian Archetype",
    "The Dreamer Archetype",
    "The Healer Archetype",
    "The Hearth",
    "The Lightning",
    "The Mountain Sage",
    "The Philosophical Mercury",
    "The Prophet",
    "The Provider",
    "The Sabbath",
    "The Seeker",
    "The Skeptic Archetype",
    "The Source",
    "The Sovereign",
    "The Sovereign Archetype",
    "The Tyrant",
    "The Warrior",
    "The Warrior Archetype",
    "The Witness",
    "The Witness Archetype",
    "The Wounded Healer",
    "Lover Archetype",
    "Scribe Archetype",
    "Everyman Archetype",
    "Eros Archetype",
    "Eros Function",
    "The King Archetype",
]

# ============================================================
# CATEGORY F: LOW-VALUE SINGLES → plain text
# ============================================================
LOW_VALUE = [
    "Advaita Vedanta",
    "Ahriman",
    "Chiron",
    "Elements",
    "Envy",
    "Fire Signs",
    "Fixed Signs",
    "Mutable Signs",
    "Fixation",
    "Fragmentation",
    "Gratitude",
    "Hexagrams",
    "Humility",
    "Integrity",
    "Kali",
    "Libido",
    "Loki",
    "Mazloth",
    "Mithras",
    "Oracles",
    "Perseus",
    "Planetary Hours",
    "Planetary Spheres",
    "Possession",
    "Pride",
    "Psalms",
    "Sufism",
    "Virgin Mary",
    "Yod",
    "Gene Keys",
    "Shadow-Gift-Siddhi",
    "Golden Path",
    "Puer Aeternus",
    "Nephthys",  # Will be Category B eventually, but remove dead link for now
    "Psychological Types",
    "The Four Functions",
    "Unus Mundus",
    "Mandala",
    "Enantiodromia",
    "Coniunctio",
    "Neoplatonism",
    "Hermeticism",
    "The Dark Night of the Soul",
]
# NOTE: Category B items (Athena, Hera, etc.) are NOT in this list — they stay as dead links
# until content is created for them. Some Cat B items that are lower priority are included
# above to clear them now (Nephthys, Psychological Types, etc. can be re-linked when created).

# Wait — let me reconsider. Category B items that will get content created should keep
# their wikilinks so they auto-resolve when files are created. Let me remove the Cat B
# items from LOW_VALUE that the user said they'd create.

# Actually the user said to do alias fixes and bracket removals FIRST, then the 20 new
# content items later. So I should NOT remove brackets from the 20 Cat B items.
# Let me remove items that are in Cat B from the bracket-removal lists.

CAT_B_ITEMS = {
    "Athena", "Hera", "Demeter", "Hecate", "Eros", "Hestia",
    "Osiris", "Horus", "Set", "Nephthys",
    "Lilith",
    "Coniunctio", "Enantiodromia", "Mandala", "Psychological Types",
    "The Four Functions", "Unus Mundus",
    "The Dark Night of the Soul", "Hermeticism", "Neoplatonism",
}

# Remove Cat B items from LOW_VALUE
LOW_VALUE = [x for x in LOW_VALUE if x not in CAT_B_ITEMS]

# Build combined bracket-removal set (C + D + E + F minus B)
BRACKET_REMOVALS = set()
for lst in [SCHOLARS, NOISE, ARCHETYPE_NAMES, LOW_VALUE]:
    for item in lst:
        if item not in CAT_B_ITEMS:
            BRACKET_REMOVALS.add(item)


def process_file(filepath):
    """Process a single markdown file for all fixes."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except (UnicodeDecodeError, PermissionError):
        return

    original = content
    file_changes = []

    # 1. Apply compound fixes (exact string replacement)
    for old, new in COMPOUND_FIXES.items():
        if old in content:
            content = content.replace(old, new)
            file_changes.append(f"  COMPOUND: {old} → {new}")

    # 2. Apply alias fixes
    # Match [[exact dead link text]] and replace with [[alias target]]
    for dead_text, alias_target in ALIAS_FIXES.items():
        # Match [[dead_text]] but NOT [[something|dead_text]] (already aliased)
        # and NOT [[dead_text#section]] (already has anchor)
        pattern = r'\[\[' + re.escape(dead_text) + r'\]\]'
        replacement = f'[[{alias_target}]]'
        matches = re.findall(pattern, content)
        if matches:
            content = re.sub(pattern, replacement, content)
            file_changes.append(f"  ALIAS ({len(matches)}x): [[{dead_text}]] → [[{alias_target}]]")

    # 3. Apply bracket removals
    # Match [[dead_text]] and replace with just dead_text
    for dead_text in BRACKET_REMOVALS:
        pattern = r'\[\[' + re.escape(dead_text) + r'\]\]'
        matches = re.findall(pattern, content)
        if matches:
            content = re.sub(pattern, dead_text, content)
            file_changes.append(f"  UNBRACKET ({len(matches)}x): [[{dead_text}]] → {dead_text}")

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        files_modified.add(str(filepath))
        changes_made.extend([str(filepath)] + file_changes)


def main():
    # Process all .md files in vault (Library, Synthesis, System)
    scan_dirs = [
        VAULT / "Library",
        VAULT / "Synthesis",
        VAULT / "System",
    ]

    file_count = 0
    for scan_dir in scan_dirs:
        if not scan_dir.exists():
            continue
        for filepath in scan_dir.rglob("*.md"):
            process_file(filepath)
            file_count += 1

    # Print summary
    print(f"Scanned {file_count} files")
    print(f"Modified {len(files_modified)} files")
    print(f"Total changes: {len([c for c in changes_made if c.startswith('  ')])}")
    print()

    if changes_made:
        # Group by file
        current_file = None
        for line in changes_made:
            if not line.startswith("  "):
                current_file = line
                print(f"\n{os.path.relpath(current_file, VAULT)}")
            else:
                print(line)

    # Summary by type
    alias_count = sum(1 for c in changes_made if "ALIAS" in c)
    unbracket_count = sum(1 for c in changes_made if "UNBRACKET" in c)
    compound_count = sum(1 for c in changes_made if "COMPOUND" in c)
    print(f"\n{'='*60}")
    print(f"ALIAS fixes: {alias_count}")
    print(f"UNBRACKET fixes: {unbracket_count}")
    print(f"COMPOUND fixes: {compound_count}")
    print(f"Total: {alias_count + unbracket_count + compound_count}")


if __name__ == "__main__":
    main()
