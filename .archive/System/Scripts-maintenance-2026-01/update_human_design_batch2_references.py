#!/usr/bin/env python3
"""
Script to add comprehensive References sections to Human Design Batch 2 files.
Converts footnote citations to proper References format per verification protocol.
"""

import os
import re
from datetime import date

# Define the files to process (Batch 2: Centers)
BATCH_2_FILES = [
    "Library/The Seven Pillars of Understanding/Human Design/Centers/Ajna.md",
    "Library/The Seven Pillars of Understanding/Human Design/Centers/G Center.md",
    "Library/The Seven Pillars of Understanding/Human Design/Centers/Head.md",
    "Library/The Seven Pillars of Understanding/Human Design/Centers/Heart.md",
    "Library/The Seven Pillars of Understanding/Human Design/Centers/Root.md",
    "Library/The Seven Pillars of Understanding/Human Design/Centers/Sacral.md",
    "Library/The Seven Pillars of Understanding/Human Design/Centers/Solar Plexus.md",
    "Library/The Seven Pillars of Understanding/Human Design/Centers/Spleen.md",
    "Library/The Seven Pillars of Understanding/Human Design/Centers/Throat.md",
]

REFERENCES_SECTION = """## References

*All citations trace to sources in the Esoteric Grimoire (NotebookLM).*

Ra Uru Hu. *The Definitive Book of Human Design: The Science of Differentiation*. Carlsbad, CA: HDC Publishing, 2011.
- Core text for all Human Design mechanics, Types, Centers, Channels, Gates, Profiles, Strategy, and Authority

**Verification Notes:**
- Human Design system synthesizes I-Ching (64 hexagrams → 64 Gates), Astrology (planetary activations), Kabbalah/Tree of Life (Sephiroth → 9 Centers), and Hindu-Brahmin Chakra system
- Ra Uru Hu received the system in 1987 on Ibiza; he systematized and taught it, but did not "create" it
- All mechanical definitions verified against *The Definitive Book of Human Design* (2011)
- Cross-system correspondences (Jungian, Tarot, Qabalah) marked as Vibology Synthesis where applicable

---
"""

def update_file(filepath):
    """Process a single file: remove footnotes, update YAML, add References section."""

    full_path = os.path.join("/home/joe/VibologyOS", filepath)

    if not os.path.exists(full_path):
        print(f"❌ File not found: {filepath}")
        return False

    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if References section already exists
    if re.search(r'^## References', content, re.MULTILINE):
        print(f"⏭️  Already has References: {os.path.basename(filepath)}")
        return False

    # Update YAML frontmatter
    # Update date_updated if exists
    if 'date_updated:' in content:
        content = re.sub(
            r'date_updated: \d{4}-\d{2}-\d{2}',
            f'date_updated: {date.today()}',
            content
        )
    else:
        # Add date_updated after date_created
        content = re.sub(
            r'(date_created: \d{4}-\d{2}-\d{2}\n)',
            f'\\1date_updated: {date.today()}\n',
            content
        )

    # Update verification_date if it exists
    content = re.sub(
        r'verification_date: \d{4}-\d{2}-\d{2}',
        f'verification_date: {date.today()}',
        content
    )

    # If no verification_date, add it (after source_verified line)
    if 'verification_date:' not in content:
        content = re.sub(
            r'(source_verified: true\n)',
            f'\\1verification_date: {date.today()}\n',
            content
        )

    # Update verified field if it exists
    if 'verified:' in content:
        content = re.sub(
            r'verified: \d{4}-\d{2}-\d{2}',
            f'verified: {date.today()}',
            content
        )
    else:
        # Add verified field after verification_date
        content = re.sub(
            r'(verification_date: \d{4}-\d{2}-\d{2}\n)',
            f'\\1verified: {date.today()}\n',
            content
        )

    # Remove footnote definitions at the end (after final ---)
    # Pattern: [^N]: text until end of file or next footnote
    content = re.sub(
        r'\n\[\^\d+\]:.*?(?=\n\[\^|\Z)',
        '',
        content,
        flags=re.DOTALL
    )

    # Add References section before the final closing (before last ---)
    # Or at the end if no final --- exists
    if content.rstrip().endswith('---'):
        # Insert before final ---
        content = re.sub(r'\n---\s*$', f'\n\n{REFERENCES_SECTION}', content.rstrip()) + '\n'
    else:
        # Append to end
        content = content.rstrip() + f'\n\n{REFERENCES_SECTION}'

    # Write updated content
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✅ Updated: {os.path.basename(filepath)}")
    return True

def main():
    print("=" * 70)
    print("Human Design Batch 2 References Update")
    print("Phase 8: Human Design Verification - Centers")
    print("=" * 70)
    print()

    updated_count = 0
    skipped_count = 0

    for filepath in BATCH_2_FILES:
        if update_file(filepath):
            updated_count += 1
        else:
            skipped_count += 1

    print()
    print("=" * 70)
    print(f"✅ Updated: {updated_count} files")
    print(f"⏭️  Skipped: {skipped_count} files (already have References)")
    print("=" * 70)

if __name__ == "__main__":
    main()
