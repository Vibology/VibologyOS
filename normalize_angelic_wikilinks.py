#!/usr/bin/env python3
"""
Normalize wikilinks in Ten Angelic Orders files.
Fixes dead links by using proper Obsidian alias syntax: [[actual-file|display-text]]
"""

import os
import re
from pathlib import Path
from collections import defaultdict


def build_file_map():
    """Build comprehensive mapping of link text to actual file paths."""
    library_root = Path("Library/The Seven Pillars of Understanding")
    file_map = {}

    # Scan all markdown files
    for md_file in library_root.rglob("*.md"):
        rel_path = md_file.relative_to(library_root)
        filename_no_ext = md_file.stem
        file_map[filename_no_ext] = str(rel_path.as_posix())

        # Map short variations for Gates: "Gate 01 - The Creative" → "Gate 1"
        if filename_no_ext.startswith("Gate "):
            parts = filename_no_ext.split(" - ", 1)
            if len(parts) == 2:
                gate_num = parts[0].replace("Gate ", "").lstrip("0")
                file_map[f"Gate {gate_num}"] = str(rel_path.as_posix())

        # Map short variations for cards with numbers: "The Fool (0)" → "The Fool"
        if " (" in filename_no_ext and ")" in filename_no_ext:
            short_name = filename_no_ext.split(" (")[0]
            file_map[short_name] = str(rel_path.as_posix())

    # Add special mappings for ambiguous cases
    special_mappings = {
        # Tarot Major Arcana
        "Judgement": "The Tarot/Major Arcana/Judgement (XX).md",
        "Judgment": "The Tarot/Major Arcana/Judgement (XX).md",
        "Justice": "The Tarot/Major Arcana/Justice (VIII or XI).md",
        "Strength": "The Tarot/Major Arcana/Strength (VIII or XI).md",
        "Temperance": "The Tarot/Major Arcana/Temperance (XIV).md",
        "The World": "The Tarot/Major Arcana/The World (XXI).md",
        "The Wheel of Fortune": "The Tarot/Major Arcana/The Wheel of Fortune (X).md",
        "Wheel of Fortune": "The Tarot/Major Arcana/The Wheel of Fortune (X).md",

        # Qabalah - Sephiroth
        "Tree of Life": "The Tarot/Qabalah/Tree of Life.md",
        "Kether": "The Tarot/Qabalah/Kether.md",
        "Chokmah": "The Tarot/Qabalah/Chokmah.md",
        "Binah": "The Tarot/Qabalah/Binah.md",
        "Chesed": "The Tarot/Qabalah/Chesed.md",
        "Geburah": "The Tarot/Qabalah/Geburah.md",
        "Tiphareth": "The Tarot/Qabalah/Tiphareth.md",
        "Netzach": "The Tarot/Qabalah/Netzach.md",
        "Hod": "The Tarot/Qabalah/Hod.md",
        "Yesod": "The Tarot/Qabalah/Yesod.md",
        "Malkuth": "The Tarot/Qabalah/Malkuth.md",
        "Daath": "The Tarot/Qabalah/Daath.md",

        # Qabalah - Other concepts
        "Four Worlds": "The Tarot/Qabalah/Four Worlds.md",
        "Qlippoth": "The Tarot/Qabalah/Qlippoth.md",
        "Ein Sof": "The Tarot/Qabalah/Ain Soph Aur.md",  # Alternate spelling
        "Ain Soph": "The Tarot/Qabalah/Ain Soph Aur.md",  # Related concept
        "Pillar of Mercy": "The Tarot/Qabalah/Pillar of Mercy.md",
        "The Pillar of Mercy": "The Tarot/Qabalah/Pillar of Mercy.md",
        "Middle Pillar": "The Tarot/Qabalah/Middle Pillar.md",

        # Angelology
        "Angelology": "Angelology/Angelology.md",
        "The Three Triads": "Angelology/The Three Triads.md",
        "The Ten Angelic Orders": "Angelology/The Ten Angelic Orders/The Ten Angelic Orders.md",
        "The Archangels": "Angelology/The Archangels/The Archangels.md",

        # Pillars
        "Astrology": "Astrology/Astrology.md",
        "Human Design": "Human Design/Human Design.md",
        "The Tarot|Tarot": "The Tarot/The Tarot.md",  # Handle existing alias
    }

    file_map.update(special_mappings)
    return file_map


def extract_link_text(wikilink_content):
    """Extract the display text from a wikilink (handles existing aliases)."""
    if "|" in wikilink_content:
        # Already has alias: [[target|display]]
        return wikilink_content.split("|")[-1]
    else:
        # No alias: [[display]]
        return wikilink_content


def normalize_wikilinks(content, file_map):
    """Normalize all wikilinks in content."""
    wikilink_pattern = re.compile(r'\[\[([^\]]+)\]\]')
    changes = []

    def replace_link(match):
        original_link = match.group(1)
        link_text = extract_link_text(original_link)

        # Check if this link needs normalization
        if link_text in file_map:
            actual_file = file_map[link_text]
            actual_filename = Path(actual_file).stem

            # If the link text matches the actual filename, no alias needed
            if link_text == actual_filename:
                return f"[[{actual_filename}]]"
            else:
                # Use alias syntax: [[actual-file|display-text]]
                changes.append(f"  [[{link_text}]] → [[{actual_filename}|{link_text}]]")
                return f"[[{actual_filename}|{link_text}]]"
        else:
            # Link not found in map - leave unchanged but log it
            return match.group(0)

    new_content = wikilink_pattern.sub(replace_link, content)
    return new_content, changes


def process_angelic_order_files(file_map, dry_run=False):
    """Process all files in Ten Angelic Orders directory."""
    orders_dir = Path("Library/The Seven Pillars of Understanding/Angelology/The Ten Angelic Orders")

    if not orders_dir.exists():
        print(f"ERROR: Directory not found: {orders_dir}")
        return

    files_processed = []
    total_changes = 0

    for md_file in sorted(orders_dir.glob("*.md")):
        print(f"\n{'='*70}")
        print(f"Processing: {md_file.name}")
        print('='*70)

        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()

        new_content, changes = normalize_wikilinks(content, file_map)

        if changes:
            print(f"Changes ({len(changes)}):")
            for change in changes[:20]:  # Show first 20 changes
                print(change)
            if len(changes) > 20:
                print(f"  ... and {len(changes) - 20} more")

            if not dry_run:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"✓ Updated {md_file.name}")
            else:
                print(f"[DRY RUN] Would update {md_file.name}")

            files_processed.append(md_file.name)
            total_changes += len(changes)
        else:
            print("No changes needed.")

    return files_processed, total_changes


def main():
    print("="*70)
    print("WIKILINK NORMALIZATION SCRIPT")
    print("Ten Angelic Orders - Dead Link Resolution")
    print("="*70)

    # Build file map
    print("\nBuilding file mapping...")
    file_map = build_file_map()
    print(f"✓ Mapped {len(file_map)} files")

    # Process files
    print("\n" + "="*70)
    print("PROCESSING FILES")
    print("="*70)

    files_processed, total_changes = process_angelic_order_files(file_map, dry_run=False)

    # Summary
    print("\n" + "="*70)
    print("SUMMARY")
    print("="*70)
    print(f"Files processed: {len(files_processed)}")
    print(f"Total wikilinks normalized: {total_changes}")

    if files_processed:
        print("\nFiles updated:")
        for filename in files_processed:
            print(f"  - {filename}")


if __name__ == "__main__":
    main()
