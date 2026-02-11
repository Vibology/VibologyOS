#!/usr/bin/env python3
"""
Add inline footnote citations to Tarot Major Arcana cards that have orphaned definitions.

Pattern:
- [^1] = Waite citations (traditional meanings, reversed meanings)
- [^2] = Wang citations (Qabalistic/Golden Dawn correspondences)
"""

import re
from pathlib import Path

LIBRARY_ROOT = Path(__file__).resolve().parent.parent.parent / "Library"

# Files to process
TAROT_CARDS = [
    "The Seven Pillars of Understanding/The Tarot/Major Arcana/The Devil (XV).md",
    "The Seven Pillars of Understanding/The Tarot/Major Arcana/The Hanged Man (XII).md",
    "The Seven Pillars of Understanding/The Tarot/Major Arcana/The Moon (XVIII).md",
    "The Seven Pillars of Understanding/The Tarot/Major Arcana/The Sun (XIX).md",
    "The Seven Pillars of Understanding/The Tarot/Major Arcana/The Tower (XVI).md",
    "The Seven Pillars of Understanding/The Tarot/Major Arcana/The World (XXI).md",
]


def add_citations_to_card(filepath: Path) -> bool:
    """Add inline citations to a single card."""
    content = filepath.read_text(encoding='utf-8')
    original = content

    # Pattern 1: Waite's traditional meanings
    content = re.sub(
        r"(According to Waite'?s? \*Pictorial Key to the Tarot\*[^.]+\.)",
        r"\1[^1]",
        content
    )

    # Pattern 2: Waite's reversed meanings
    content = re.sub(
        r"(\*\*Reversed\*\*, Waite identifies[^.]+\.)",
        r"\1[^1]",
        content
    )

    # Pattern 3: Golden Dawn titles (Wang source)
    content = re.sub(
        r"(The Golden Dawn gives [^.]+\.)",
        r"\1[^2]",
        content
    )

    # Pattern 4: "for a man/woman/maid" divination meanings (Waite)
    content = re.sub(
        r'([""]for a [^"]+[""][^.]*\.)',
        r'\1[^1]',
        content
    )

    if content != original:
        filepath.write_text(content, encoding='utf-8')
        return True
    return False


def main():
    updated = 0
    for card_path in TAROT_CARDS:
        filepath = LIBRARY_ROOT / card_path
        if filepath.exists():
            if add_citations_to_card(filepath):
                print(f"  ✓ {filepath.name}")
                updated += 1
        else:
            print(f"  ✗ Not found: {filepath.name}")

    print(f"\nUpdated: {updated}/{len(TAROT_CARDS)} cards")


if __name__ == "__main__":
    main()
