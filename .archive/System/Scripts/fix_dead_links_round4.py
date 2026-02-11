#!/usr/bin/env python3
"""Fix dead wikilinks round 4: alias rewrites + unbracketing for new Category B entries."""

import os
import re

LIBRARY_ROOT = os.path.expanduser("~/VibologyOS/Library")
CORE_ROOT = os.path.expanduser("~/VibologyOS/Library/Core Foundations of Vibology")

# Alias rewrites: dead_link_text -> replacement (full wikilink)
ALIAS_FIXES = {
    # Astrology planets
    "[[Pluto]]": "[[Pluto ♇|Pluto]]",
    "[[Saturn]]": "[[Saturn ♄|Saturn]]",
    "[[The Moon]]": "[[Moon ☽|The Moon]]",
    "[[Mars]]": "[[Mars ♂|Mars]]",
    "[[Venus]]": "[[Venus ♀|Venus]]",
    "[[Neptune]]": "[[Neptune ♆|Neptune]]",
    "[[The Sun]]": "[[Sun ☉|The Sun]]",
    "[[Jupiter]]": "[[Jupiter ♃|Jupiter]]",
    "[[Uranus]]": "[[Uranus ♅|Uranus]]",
    # Astrology signs
    "[[Scorpio]]": "[[Scorpio ♏|Scorpio]]",
    "[[Cancer]]": "[[Cancer ♋|Cancer]]",
    "[[Virgo]]": "[[Virgo ♍|Virgo]]",
    "[[Libra]]": "[[Libra ♎|Libra]]",
    "[[Aries]]": "[[Aries ♈|Aries]]",
    "[[Capricorn]]": "[[Capricorn ♑|Capricorn]]",
    "[[Leo]]": "[[Leo ♌|Leo]]",
    # Tarot Major Arcana
    "[[The High Priestess]]": "[[The High Priestess (II)|The High Priestess]]",
    "[[Justice]]": "[[Justice (XI)|Justice]]",
    "[[The Empress]]": "[[The Empress (III)|The Empress]]",
    "[[The Hermit]]": "[[The Hermit (IX)|The Hermit]]",
    "[[The Hierophant]]": "[[The Hierophant (V)|The Hierophant]]",
    "[[The Magician]]": "[[The Magician (I)|The Magician]]",
    "[[The Wheel of Fortune (X)]]": "[[Wheel of Fortune (X)|The Wheel of Fortune]]",
    "[[Death]]": "[[Death (XIII)|Death]]",
    # Angelology
    "[[Celestial Hierarchy]]": "[[The Celestial Hierarchy|Celestial Hierarchy]]",
    "[[Angelic Orders]]": "[[The Ten Angelic Orders|Angelic Orders]]",
    "[[The Fallen Angels]]": "[[The Nine Orders of Fallen Angels|The Fallen Angels]]",
    "[[Archangel Michael]]": "[[Michael|Archangel Michael]]",
    "[[Archangel Raphael]]": "[[Raphael|Archangel Raphael]]",
    "[[Archangel Uriel]]": "[[Uriel|Archangel Uriel]]",
    # HD Centers
    "[[The Sacral Center]]": "[[Sacral|The Sacral Center]]",
    "[[The G Center]]": "[[G Center|The G Center]]",
    "[[The Spleen Center]]": "[[Spleen|The Spleen Center]]",
    "[[The Ajna Center]]": "[[Ajna|The Ajna Center]]",
    # HD Other
    "[[BodyGraph]]": "[[The BodyGraph|BodyGraph]]",
    "[[Channel 6-59 - Mating]]": "[[Channel 6-59 - Intimacy|Channel 6-59 - Mating]]",
    # HD Gates (zero-padded or article differences)
    "[[Gate 1 - The Creative]]": "[[Gate 01 - The Creative]]",
    "[[Gate 2 - The Receptive]]": "[[Gate 02 - The Receptive]]",
    "[[Gate 24 - Return]]": "[[Gate 24 - The Return]]",
    "[[Gate 28 - The Preponderance of the Great]]": "[[Gate 28 - Preponderance of the Great]]",
    "[[Gate 36 - The Darkening of the Light]]": "[[Gate 36 - Darkening of the Light]]",
    "[[Gate 62 - The Preponderance of the Small]]": "[[Gate 62 - Preponderance of the Small]]",
    # Qabalah
    "[[Qliphoth]]": "[[Qlippoth|Qliphoth]]",
    "[[Ain Soph]]": "[[Ain Soph Aur|Ain Soph]]",
    "[[Da'ath]]": "[[Daath|Da'ath]]",
    # Jungian
    "[[Psychological Types]]": "[[The Four Functions|Psychological Types]]",
}

# Unbracket: remove [[ ]] around these (no file exists)
UNBRACKET = [
    "Dionysus",
    "Heracles",
    "Medusa",
    "Odysseus",
    "Perseus",
    "Arachne",
    "Hephaestus",
    "Archangel Azrael",
    "Archangel Chamuel",
    "The Houses",
    "The Planets",
    "The Signs",
    "The Rave Mandala",
    "The Path of the Moon",
    "The Emerald Tablet",
    "The Descent",
    "The Return",
]


def process_file(filepath):
    """Apply all fixes to a single file. Returns (changed, alias_count, unbracket_count)."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    original = content
    alias_count = 0
    unbracket_count = 0

    # Apply alias fixes (exact string replacement)
    # Sort by length descending to avoid partial matches
    for dead, fixed in sorted(ALIAS_FIXES.items(), key=lambda x: -len(x[0])):
        if dead in content:
            # For [[Death]], make sure we don't match [[Death (XIII)]] etc.
            # We do exact string match, so [[Death]] won't match [[Death (XIII)]]
            count = content.count(dead)
            content = content.replace(dead, fixed)
            alias_count += count

    # Apply unbracket fixes
    for term in UNBRACKET:
        pattern = f"[[{term}]]"
        if pattern in content:
            count = content.count(pattern)
            content = content.replace(pattern, term)
            unbracket_count += count

    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return True, alias_count, unbracket_count
    return False, 0, 0


def main():
    total_files = 0
    changed_files = 0
    total_alias = 0
    total_unbracket = 0
    changed_list = []

    for root, dirs, files in os.walk(LIBRARY_ROOT):
        # Skip archive
        dirs[:] = [d for d in dirs if d != ".archive"]
        for fname in files:
            if not fname.endswith(".md"):
                continue
            filepath = os.path.join(root, fname)
            total_files += 1
            changed, ac, uc = process_file(filepath)
            if changed:
                changed_files += 1
                total_alias += ac
                total_unbracket += uc
                rel = os.path.relpath(filepath, os.path.expanduser("~/VibologyOS"))
                changed_list.append((rel, ac, uc))

    print(f"Scanned {total_files} files")
    print(f"Changed {changed_files} files")
    print(f"  Alias rewrites: {total_alias}")
    print(f"  Unbracketed: {total_unbracket}")
    print(f"  Total fixes: {total_alias + total_unbracket}")
    print()
    for path, ac, uc in sorted(changed_list):
        print(f"  {path}: {ac} alias, {uc} unbracket")


if __name__ == "__main__":
    main()
