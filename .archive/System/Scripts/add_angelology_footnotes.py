#!/usr/bin/env python3
"""
Add inline footnotes to Angelology files.

Strategy:
- Add [^1] to first substantive paragraph describing the angel/order/concept
- Create footnote definition based on primary source(s) listed in Sources section
- For files with Davidson as primary source, reference Davidson
- For files with DuQuette as primary source (Enochian), reference DuQuette
- For files with Biblical/theological sources, reference those
"""

import re
from pathlib import Path

LIBRARY_ROOT = Path(__file__).resolve().parent.parent.parent / "Library"
ANGELOLOGY_DIR = LIBRARY_ROOT / "The Seven Pillars of Understanding" / "Angelology"

def get_primary_source(content, filename):
    """Extract primary source from Sources section."""

    # Enochian files → DuQuette
    if "Enochian" in filename or "Dee" in filename or "Kelley" in filename:
        return "Lon Milo DuQuette, *Enochian Vision Magick: An Introduction and Practical Guide to the Magick of Dr. John Dee and Edward Kelley* (Weiser Books, 2008)"

    # Archangels → Davidson + specific angel
    if "Gabriel" in filename:
        return "Gustav Davidson, *A Dictionary of Angels, Including the Fallen Angels* (The Free Press, 1967) — Gabriel as 'Strength of God,' archangel of Annunciation, Mercy, and Revelation"
    elif "Michael" in filename:
        return "Gustav Davidson, *A Dictionary of Angels, Including the Fallen Angels* (The Free Press, 1967) — Michael as 'Who is like God,' archangel of Protection, War, and Sun"
    elif "Raphael" in filename:
        return "Gustav Davidson, *A Dictionary of Angels, Including the Fallen Angels* (The Free Press, 1967) — Raphael as 'God has healed,' archangel of Healing and Mercury"
    elif "Uriel" in filename:
        return "Gustav Davidson, *A Dictionary of Angels, Including the Fallen Angels* (The Free Press, 1967) — Uriel as 'Fire of God,' archangel of Earth and Wisdom"
    elif "Metatron" in filename:
        return "Gustav Davidson, *A Dictionary of Angels, Including the Fallen Angels* (The Free Press, 1967) — Metatron as 'Lesser YHVH,' scribe and Kether archangel"
    elif "Sandalphon" in filename:
        return "Gustav Davidson, *A Dictionary of Angels, Including the Fallen Angels* (The Free Press, 1967) — Sandalphon as twin of Metatron, archangel of Malkuth"
    elif "Raziel" in filename:
        return "Gustav Davidson, *A Dictionary of Angels, Including the Fallen Angels* (The Free Press, 1967) — Raziel as 'Secret of God,' archangel of Chokmah and mysteries"
    elif "Tzaphkiel" in filename:
        return "Gustav Davidson, *A Dictionary of Angels, Including the Fallen Angels* (The Free Press, 1967) — Tzaphkiel as 'Contemplation of God,' archangel of Binah"
    elif "Tzadkiel" in filename:
        return "Gustav Davidson, *A Dictionary of Angels, Including the Fallen Angels* (The Free Press, 1967) — Tzadkiel as 'Righteousness of God,' archangel of Chesed"
    elif "Kamael" in filename:
        return "Gustav Davidson, *A Dictionary of Angels, Including the Fallen Angels* (The Free Press, 1967) — Kamael as 'Severity of God,' archangel of Geburah"
    elif "Haniel" in filename:
        return "Gustav Davidson, *A Dictionary of Angels, Including the Fallen Angels* (The Free Press, 1967) — Haniel as 'Grace of God,' archangel of Netzach"

    # Angelic Orders → Davidson + Pseudo-Dionysius
    elif "Seraphim" in filename:
        return "Gustav Davidson, *A Dictionary of Angels, Including the Fallen Angels* (The Free Press, 1967) and Pseudo-Dionysius, *The Celestial Hierarchy* (6th century) — Seraphim as highest angelic order of divine love"
    elif "Cherubim" in filename:
        return "Gustav Davidson, *A Dictionary of Angels, Including the Fallen Angels* (The Free Press, 1967) and Pseudo-Dionysius, *The Celestial Hierarchy* (6th century) — Cherubim as guardians of divine wisdom"
    elif "Thrones" in filename:
        return "Gustav Davidson, *A Dictionary of Angels, Including the Fallen Angels* (The Free Press, 1967) and Pseudo-Dionysius, *The Celestial Hierarchy* (6th century) — Thrones as bearers of divine justice"
    elif "Dominations" in filename or "Dominions" in filename:
        return "Pseudo-Dionysius, *The Celestial Hierarchy* (6th century) — Dominations as angels of divine lordship"
    elif "Virtues" in filename:
        return "Pseudo-Dionysius, *The Celestial Hierarchy* (6th century) — Virtues as angels of miracles and manifestation"
    elif "Powers" in filename:
        return "Pseudo-Dionysius, *The Celestial Hierarchy* (6th century) — Powers as angels of cosmic order"
    elif "Principalities" in filename:
        return "Pseudo-Dionysius, *The Celestial Hierarchy* (6th century) — Principalities as angels of nations and groups"
    elif "Archangels.md" in filename:
        return "Pseudo-Dionysius, *The Celestial Hierarchy* (6th century) — Archangels as divine messengers"
    elif "Angels.md" in filename and "Orders" in str(filename):
        return "Pseudo-Dionysius, *The Celestial Hierarchy* (6th century) — Angels as closest to humanity"
    elif "Ishim" in filename:
        return "Gustav Davidson, *A Dictionary of Angels, Including the Fallen Angels* (The Free Press, 1967) — Ishim as 'Souls of Fire,' angelic order of Malkuth"

    # Default → Davidson (most common primary source for Angelology)
    else:
        return "Gustav Davidson, *A Dictionary of Angels, Including the Fallen Angels* (The Free Press, 1967)"

def add_footnote_to_file(filepath):
    """Add inline footnote to Angelology file."""
    content = filepath.read_text(encoding='utf-8')
    original = content

    filename = filepath.name

    # Get primary source for this file
    source = get_primary_source(content, filename)

    # Add [^1] after first substantive paragraph (after first header after frontmatter)
    # Look for pattern: ## SomeHeader\n\nFirst paragraph sentence.
    pattern = r'(^##[^\n]+\n\n)([A-Z][^.]+\.)'
    match = re.search(pattern, content, re.MULTILINE)

    if match:
        # Add footnote after first sentence
        content = content[:match.end(2)] + '[^1]' + content[match.end(2):]
    else:
        # Fallback: add after first paragraph
        pattern = r'(^[A-Z][^.]+\.)'
        match = re.search(pattern, content, re.MULTILINE)
        if match:
            content = content[:match.end(1)] + '[^1]' + content[match.end(1):]

    # Add footnote definition before ## Sources
    footnote_def = f'\n[^1]: {source}.\n'

    if '## Sources' in content:
        content = content.replace('## Sources', f'{footnote_def}\n---\n\n## Sources')
    else:
        # If no Sources section, add at end
        content += f'\n\n{footnote_def}'

    # Only write if changed
    if content != original:
        filepath.write_text(content, encoding='utf-8')
        return True
    return False

def main():
    # Get all Angelology files
    all_files = sorted(ANGELOLOGY_DIR.rglob("*.md"))

    # Exclude files that start with _ or already have footnotes
    files_to_process = []
    for f in all_files:
        if f.name.startswith("_"):
            continue
        content = f.read_text(encoding='utf-8')
        if not re.search(r'\[\^\d+\]', content):
            files_to_process.append(f)

    print(f"Processing {len(files_to_process)} Angelology files...")

    updated = 0
    for filepath in files_to_process:
        if add_footnote_to_file(filepath):
            rel_path = filepath.relative_to(ANGELOLOGY_DIR)
            print(f"  ✓ {rel_path}")
            updated += 1

    print(f"\nUpdated {updated}/{len(files_to_process)} files.")

if __name__ == "__main__":
    main()
