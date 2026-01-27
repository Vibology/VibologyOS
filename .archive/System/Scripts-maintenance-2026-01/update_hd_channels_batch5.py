#!/usr/bin/env python3
"""
Human Design Channels Batch 5 References Update Script
Adds comprehensive References sections and verification metadata to Channel files.
"""

import re
from pathlib import Path

# Batch 5 files (Channels 1-8, 2-14, 3-60, 4-63, 5-15, 6-59, 7-31, 9-52, 10-20)
FILES = [
    "Channel 1-8 - Inspiration.md",
    "Channel 2-14 - The Beat.md",
    "Channel 3-60 - Mutation.md",
    "Channel 4-63 - Logic.md",
    "Channel 5-15 - Rhythm.md",
    "Channel 6-59 - Intimacy.md",
    "Channel 7-31 - The Alpha.md",
    "Channel 9-52 - Concentration.md",
    "Channel 10-20 - Awakening.md",
]

BASE_PATH = Path.home() / "VibologyOS/Library/The Seven Pillars of Understanding/Human Design/Channels"

REFERENCES_SECTION = """
## References

**Primary Source:**
- Ra Uru Hu, *The Definitive Book of Human Design: The Science of Differentiation* (HDC Publishing, 2011)

**Cross-System Sources:**
- Richard Rudd, *The Gene Keys: Unlocking the Higher Purpose Hidden in Your DNA* (Gene Keys Publishing, 2013)
- Alfred Huang, *The Complete I Ching: The Definitive Translation* (Inner Traditions, 1998)

**Verification Note:**
All channel mechanics, circuitry analysis, and Ra's teachings are sourced from *The Definitive Book of Human Design* (2011). Gene Keys correspondences are from Rudd (2013). I-Ching hexagram correlations are from Huang (1998). Cross-system synthesis (Tarot, Qabalah, Jungian psychology) and biological/somatic interpretations represent **Vibology Synthesis**—integrations drawing upon verified HD mechanics but extending into archetypal and interdisciplinary correspondences.
"""

def update_yaml_frontmatter(content: str) -> str:
    """Add verification metadata to YAML frontmatter."""
    # Find the YAML block
    yaml_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if not yaml_match:
        print("  ⚠️  No YAML frontmatter found")
        return content

    yaml_content = yaml_match.group(1)
    rest_of_content = content[yaml_match.end():]

    # Check if verification fields already exist
    if 'verified:' in yaml_content:
        print("  ✓ Verification metadata already exists")
        return content

    # Add verification metadata
    verification_metadata = """verified: true
verification_date: 2026-01-25
source_verified: Esoteric Grimoire"""

    updated_yaml = f"---\n{yaml_content}\n{verification_metadata}\n---\n"
    return updated_yaml + rest_of_content

def add_references_section(content: str) -> str:
    """Add References section at the end if it doesn't exist."""
    if '## References' in content:
        print("  ✓ References section already exists")
        return content

    # Add References before the final quote (if exists) or at the very end
    final_quote_pattern = r'\n---\n\n\*".*?"\*\n*$'
    final_quote_match = re.search(final_quote_pattern, content, re.DOTALL)

    if final_quote_match:
        # Insert References before the final quote
        insert_pos = final_quote_match.start()
        updated_content = content[:insert_pos] + "\n" + REFERENCES_SECTION.strip() + "\n" + content[insert_pos:]
    else:
        # Append at the end
        updated_content = content.rstrip() + "\n\n" + REFERENCES_SECTION.strip() + "\n"

    print("  ✓ Added References section")
    return updated_content

def process_file(filepath: Path) -> bool:
    """Process a single file."""
    print(f"\nProcessing: {filepath.name}")

    if not filepath.exists():
        print(f"  ❌ File not found: {filepath}")
        return False

    # Read file
    content = filepath.read_text(encoding='utf-8')

    # Update YAML
    content = update_yaml_frontmatter(content)

    # Add References section
    content = add_references_section(content)

    # Write back
    filepath.write_text(content, encoding='utf-8')
    print(f"  ✅ Completed: {filepath.name}")
    return True

def main():
    print("=" * 70)
    print("Human Design Channels Batch 5 References Update")
    print("=" * 70)

    success_count = 0
    for filename in FILES:
        filepath = BASE_PATH / filename
        if process_file(filepath):
            success_count += 1

    print("\n" + "=" * 70)
    print(f"Completed: {success_count}/{len(FILES)} files updated")
    print("=" * 70)

if __name__ == "__main__":
    main()
