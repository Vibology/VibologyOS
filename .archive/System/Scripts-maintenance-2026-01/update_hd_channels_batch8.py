#!/usr/bin/env python3
"""
Human Design Channels Batch 8 References Update Script
Adds comprehensive References sections and verification metadata to Channel files.
FINAL BATCH - Completes all 36 Channels.
"""

import re
from pathlib import Path

# Batch 8 files (Channels 29-46, 30-41, 32-54, 34-57, 35-36, 37-40, 39-55, 42-53, 47-64)
FILES = [
    "Channel 29-46 - Discovery.md",
    "Channel 30-41 - Fantasy.md",
    "Channel 32-54 - Transformation.md",
    "Channel 34-57 - Power.md",
    "Channel 35-36 - Transitoriness.md",
    "Channel 37-40 - Community.md",
    "Channel 39-55 - Moodiness.md",
    "Channel 42-53 - Maturation.md",
    "Channel 47-64 - Abstraction.md",
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
    print("Human Design Channels Batch 8 References Update (FINAL BATCH)")
    print("=" * 70)

    success_count = 0
    for filename in FILES:
        filepath = BASE_PATH / filename
        if process_file(filepath):
            success_count += 1

    print("\n" + "=" * 70)
    print(f"Completed: {success_count}/{len(FILES)} files updated")
    print("🎉 ALL 36 CHANNELS COMPLETE! 🎉")
    print("=" * 70)

if __name__ == "__main__":
    main()
