#!/usr/bin/env python3
"""
Add inline footnotes to Tarot Major Arcana files.

Converts inline citations (Waite 1910), (Wang 1983), (Wang 1983 cites Crowley)
to footnote format [^1], [^2], [^3].

Pattern:
- First (Waite 1910) → [^1]
- All (Wang 1983) → [^2]
- All (Wang 1983 cites Crowley) → [^2] (same source)
"""

import re
from pathlib import Path

LIBRARY_ROOT = Path(__file__).resolve().parent.parent.parent / "Library"
TAROT_DIR = LIBRARY_ROOT / "The Seven Pillars of Understanding" / "The Tarot" / "Major Arcana"

# Footnote definitions to add before ## Sources section
FOOTNOTE_DEFS = """
[^1]: Waite, Arthur Edward. *The Pictorial Key to the Tarot: Being Fragments of a Secret Tradition under the Veil of Divination*. London: William Rider & Son, Ltd., 1910. — Traditional upright and reversed meanings, symbolic interpretations.

[^2]: Wang, Robert. *The Qabalistic Tarot: A Textbook of Mystical Philosophy*. York Beach, Maine: Samuel Weiser, Inc., 1983. — Qabalistic correspondences, Golden Dawn tradition, Crowley's *Book of Thoth* references.
"""

def process_file(filepath):
    """Convert inline citations to footnotes."""
    content = filepath.read_text(encoding='utf-8')
    original = content

    # Replace citations with footnotes
    # (Waite 1910) → [^1]
    content = re.sub(r'\(Waite 1910\)', '[^1]', content)

    # (Wang 1983 cites Crowley) → [^2]
    content = re.sub(r'\(Wang 1983 cites Crowley\)', '[^2]', content)

    # (Wang 1983) → [^2]
    content = re.sub(r'\(Wang 1983\)', '[^2]', content)

    # Add footnote definitions before ## Sources section
    if '## Sources' in content:
        content = content.replace('## Sources', f'{FOOTNOTE_DEFS.strip()}\n\n---\n\n## Sources')
    else:
        # If no Sources section, add at end
        content += f'\n\n{FOOTNOTE_DEFS.strip()}\n'

    # Only write if changed
    if content != original:
        filepath.write_text(content, encoding='utf-8')
        return True
    return False

def main():
    tarot_files = sorted(TAROT_DIR.glob("*.md"))

    # Exclude files that already have footnotes (The Fool)
    files_to_process = []
    for f in tarot_files:
        content = f.read_text(encoding='utf-8')
        if not re.search(r'\[\^\d+\]', content):
            files_to_process.append(f)

    print(f"Processing {len(files_to_process)} Tarot Major Arcana files...")

    updated = 0
    for filepath in files_to_process:
        if process_file(filepath):
            print(f"  ✓ {filepath.name}")
            updated += 1
        else:
            print(f"  - {filepath.name} (no changes)")

    print(f"\nUpdated {updated}/{len(files_to_process)} files.")

if __name__ == "__main__":
    main()
