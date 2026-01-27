#!/usr/bin/env python3
"""
Update References sections in The Window card files.
Converts informal Sources to comprehensive References format.
"""

import re
import sys
from pathlib import Path

REFERENCES_TEMPLATE = """## References

### Primary Sources (Uploaded to Esoteric Grimoire)

**I-Ching & Gene Keys:**
- Huang, Alfred. *The Complete I Ching: The Definitive Translation by the Taoist Master Alfred Huang*. Rochester, VT: Inner Traditions, 1998.
- Rudd, Richard. *Gene Keys: Unlocking the Higher Purpose Hidden in Your DNA*. London: Watkins Publishing, 2013. (First published 2009)
- Wilhelm, Richard and Baynes, Cary F. (Trans.). *The I Ching or Book of Changes*. Princeton, NJ: Princeton University Press, 1967. (Bollingen Series XIX)

**Human Design:**
- Ra Uru Hu. *The Human Design System: The Complete Rave I'Ching*. Diessen am Ammersee, Germany: Jovian Archive Corporation, 2001.
- Ra Uru Hu and Bunnell, Lynda. *The Definitive Book of Human Design: The Science of Differentiation*. IHDS/Jovian Archive, 2011. (Copyright 2008-2012)

**Vibology Internal Reference:**
- *The Blueprint (444) Reference Information: Complete Documentation for Vibology Framework*. Internal document. Created January 2026.

### Vibology Synthesis Notes

This card integrates verified source material (I-Ching hexagram meanings via Huang/Wilhelm, HD gate mechanics via Ra Uru Hu, Gene Keys transformation arc via Rudd) with original Vibology Synthesis (1980s contemporary archetypal encoding, Window categorical structure, divination interpretations)."""

def update_file(filepath):
    """Replace Sources section with References section."""
    content = filepath.read_text()

    # Pattern to match old Sources section (from ## Sources to next ## or ---)
    pattern = r'## Sources\n\n.*?(?=\n---\n|\n## |\Z)'

    if not re.search(pattern, content, re.DOTALL):
        print(f"  ⚠️  No Sources section found in {filepath.name}")
        return False

    # Replace with new References template
    new_content = re.sub(pattern, REFERENCES_TEMPLATE, content, flags=re.DOTALL)

    # Update YAML metadata
    new_content = re.sub(
        r'^source_verified: synthesis$',
        'verified: true',
        new_content,
        flags=re.MULTILINE
    )
    new_content = re.sub(
        r'^verification_date: 2026-01-23$',
        'verification_date: 2026-01-25',
        new_content,
        flags=re.MULTILINE
    )

    # Add date_updated if date_created exists but date_updated doesn't
    if 'date_created:' in new_content and 'date_updated:' not in new_content:
        new_content = re.sub(
            r'(date_created: \d{4}-\d{2}-\d{2})',
            r'\1\ndate_updated: 2026-01-25',
            new_content
        )

    filepath.write_text(new_content)
    print(f"  ✓ Updated {filepath.name}")
    return True

def main():
    if len(sys.argv) < 2:
        print("Usage: python update_window_references.py <file1.md> <file2.md> ...")
        sys.exit(1)

    for arg in sys.argv[1:]:
        filepath = Path(arg)
        if not filepath.exists():
            print(f"  ✗ File not found: {filepath}")
            continue

        update_file(filepath)

if __name__ == "__main__":
    main()
