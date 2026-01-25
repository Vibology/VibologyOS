#!/usr/bin/env python3
"""
Update References sections in Tarot Major Arcana files.
Converts old footnote-style Sources to new References format with full bibliographic details.
"""

import re
import sys
from pathlib import Path

REFERENCES_TEMPLATE = """## References

### Primary Sources (Uploaded to Esoteric Grimoire)

- Waite, Arthur Edward. *The Pictorial Key to the Tarot: Being Fragments of a Secret Tradition under the Veil of Divination*. London: William Rider & Son, Ltd., 1910.
- Wang, Robert. *The Qabalistic Tarot: A Textbook of Mystical Philosophy*. York Beach, Maine: Samuel Weiser, Inc., 1983.

### Secondary Sources (Referenced via Primary Sources)

- Crowley, Aleister. *The Book of Thoth*. New York: Samuel Weiser, Inc., 1974. (Originally published in *The Equinox*, Vol. III, No. V, 1944) — Referenced via Wang 1983

### Vibology Synthesis Notes

Interpretive commentary sections (RWS symbolism analysis, synthesis notes, personal observations) represent original Vibology Synthesis anchored to verified source material."""

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

    filepath.write_text(new_content)
    print(f"  ✓ Updated {filepath.name}")
    return True

def main():
    if len(sys.argv) < 2:
        print("Usage: python update_tarot_references.py <file1.md> <file2.md> ...")
        sys.exit(1)

    for arg in sys.argv[1:]:
        filepath = Path(arg)
        if not filepath.exists():
            print(f"  ✗ File not found: {filepath}")
            continue

        update_file(filepath)

if __name__ == "__main__":
    main()
