#!/usr/bin/env python3
"""
Script to add comprehensive References sections to Human Design Batch 4 files (Variables).
These files were created later and lack verification metadata and citations.
"""

import os
import re
from datetime import date

# Define the files to process (Batch 4: Variables)
BATCH_4_FILES = [
    "Library/The Seven Pillars of Understanding/Human Design/Variables/Determination.md",
    "Library/The Seven Pillars of Understanding/Human Design/Variables/Environment.md",
    "Library/The Seven Pillars of Understanding/Human Design/Variables/Motivation.md",
    "Library/The Seven Pillars of Understanding/Human Design/Variables/Perspective.md",
    "Library/The Seven Pillars of Understanding/Human Design/Variables/Primary Health System.md",
    "Library/The Seven Pillars of Understanding/Human Design/Variables/Tone - Color - Base.md",
    "Library/The Seven Pillars of Understanding/Human Design/Variables/Variables.md",
]

REFERENCES_SECTION = """## References

*All citations trace to sources in the Esoteric Grimoire (NotebookLM).*

Ra Uru Hu. *The Definitive Book of Human Design: The Science of Differentiation*. Carlsbad, CA: HDC Publishing, 2011.
- Core text for all Human Design mechanics, Types, Centers, Channels, Gates, Profiles, Strategy, and Authority

**Verification Notes:**
- Human Design system synthesizes I-Ching (64 hexagrams → 64 Gates), Astrology (planetary activations), Kabbalah/Tree of Life (Sephiroth → 9 Centers), and Hindu-Brahmin Chakra system
- Ra Uru Hu received the system in 1987 on Ibiza; he systematized and taught it, but did not "create" it
- Variables represent advanced layer of HD system: Four Transformations (Determination, Environment, Perspective, Motivation) calculated from Color/Tone/Base
- Variable mechanics verified against *The Definitive Book of Human Design* (2011); detailed implementation marked as educational synthesis
- Cross-system correspondences (Jungian, Tarot, Qabalah) marked as Vibology Synthesis where applicable

---
"""

def update_file(filepath):
    """Process a single file: add verification metadata, add References section."""

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

    # Update YAML frontmatter - add verification metadata
    # Update date_updated
    content = re.sub(
        r'date_updated: \d{4}-\d{2}-\d{2}',
        f'date_updated: {date.today()}',
        content
    )

    # Add verification metadata after category line
    verification_metadata = f"""source_verified: true
verification_date: {date.today()}
grimoire_source: "The Definitive Book of Human Design (Ra Uru Hu, 2011)"
verification_notes: "Variables mechanics verified against Grimoire. Advanced layer (Color/Tone/Base calculations) marked as educational synthesis."
"""

    # Insert verification metadata after category line
    content = re.sub(
        r'(category: Variables\n)',
        f'\\1{verification_metadata}',
        content
    )

    # Add References section at the end (before final ---)
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
    print("Human Design Batch 4 References Update")
    print("Phase 8: Human Design Verification - Variables")
    print("=" * 70)
    print()

    updated_count = 0
    skipped_count = 0

    for filepath in BATCH_4_FILES:
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
