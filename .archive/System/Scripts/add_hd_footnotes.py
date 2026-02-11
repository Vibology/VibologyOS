#!/usr/bin/env python3
"""
Add inline footnotes to Human Design files that reference sources but lack inline citations.

Strategy:
1. For overview files (Human Design.md, Centers.md, Gates.md, Profiles.md, Tone-Color-Base.md):
   - Add [^1] to first substantive paragraph referencing HD mechanics

2. For channel files (Channel 24-61, Channel 25-51):
   - Add [^1] to "Ra's Definition" section or first mechanical description

3. For profile file (4-1 Opportunist Investigator):
   - Add [^1] to profile mechanics description

All files use same footnote:
[^1]: Ra Uru Hu, *The Definitive Book of Human Design: The Science of Differentiation*
      (HDC Publishing, 2011) — Core mechanics for [specific topic].
"""

import re
from pathlib import Path

LIBRARY_ROOT = Path(__file__).resolve().parent.parent.parent / "Library"
HD_DIR = LIBRARY_ROOT / "The Seven Pillars of Understanding" / "Human Design"

# Files to process (manually identified from list)
FILES_TO_PROCESS = [
    "Centers/Centers.md",
    "Channels/Channel 24-61 - Awareness.md",
    "Channels/Channel 25-51 - Initiation.md",
    "Gates/Gates.md",
    "Human Design.md",
    "Profiles/4-1 Opportunist Investigator.md",
    "Profiles/Profiles.md",
    "Variables/Tone - Color - Base.md",
]

def add_footnote_to_file(filepath):
    """Add inline footnote to HD file based on content type."""
    content = filepath.read_text(encoding='utf-8')
    original = content

    filename = filepath.name

    # Determine topic for footnote definition
    if "Channel" in filename:
        topic = "channel mechanics and circuitry analysis"
        # Add [^1] after first substantive sentence in file (after frontmatter)
        # Look for first paragraph after "---" that describes mechanics
        pattern = r'(## .*?\n\n)(.*?Human Design.*?\.)'
        match = re.search(pattern, content, re.DOTALL)
        if match:
            content = content.replace(match.group(2), match.group(2) + '[^1]', 1)

    elif filename == "Human Design.md":
        topic = "all Human Design mechanics (Types, Centers, Channels, Gates, Profiles, Strategy, Authority)"
        # Add after first substantive claim about HD system
        pattern = r'(Human Design is a synthesis.*?differentiation\.)'
        match = re.search(pattern, content, re.DOTALL)
        if match:
            content = content.replace(match.group(1), match.group(1) + '[^1]', 1)

    elif filename == "Centers.md":
        topic = "the nine Centers as energy hubs"
        # Add after definition of Centers
        pattern = r'(The nine Centers are the nine energy hubs.*?BodyGraph\.)'
        match = re.search(pattern, content, re.DOTALL)
        if match:
            content = content.replace(match.group(1), match.group(1) + '[^1]', 1)

    elif filename == "Gates.md":
        topic = "the 64 Gates as hexagram activations"
        # Add after definition of Gates
        pattern = r'(The 64 Gates are the sixty-four.*?expression\.)'
        match = re.search(pattern, content, re.DOTALL)
        if match:
            content = content.replace(match.group(1), match.group(1) + '[^1]', 1)

    elif filename == "Profiles.md":
        topic = "the 12 Profiles as archetypal life themes"
        # Add after definition of Profiles
        pattern = r'(The Profile is the costume.*?incarnation\.)'
        match = re.search(pattern, content, re.DOTALL)
        if match:
            content = content.replace(match.group(1), match.group(1) + '[^1]', 1)

    elif "4-1" in filename:
        topic = "Profile mechanics (4/1 Opportunist/Investigator)"
        # Add after profile description
        pattern = r'(The 4/1 Profile.*?network\.)'
        match = re.search(pattern, content, re.DOTALL)
        if match:
            content = content.replace(match.group(1), match.group(1) + '[^1]', 1)

    elif "Tone" in filename or "Color" in filename or "Base" in filename:
        topic = "Variables (Tone, Color, Base) as advanced HD mechanics"
        # Add after description of Tone-Color-Base
        pattern = r'(Tone, Color, and Base.*?mechanics\.)'
        match = re.search(pattern, content, re.DOTALL)
        if match:
            content = content.replace(match.group(1), match.group(1) + '[^1]', 1)
    else:
        topic = "Human Design mechanics"
        return False  # Skip if unrecognized

    # Add footnote definition before ## Sources
    footnote_def = f'\n[^1]: Ra Uru Hu, *The Definitive Book of Human Design: The Science of Differentiation* (HDC Publishing, 2011) — {topic.capitalize()}.\n'

    if '## Sources' in content:
        content = content.replace('## Sources', f'{footnote_def}\n---\n\n## Sources')
    else:
        content += f'\n{footnote_def}'

    # Only write if changed
    if content != original:
        filepath.write_text(content, encoding='utf-8')
        return True
    return False

def main():
    print(f"Processing {len(FILES_TO_PROCESS)} Human Design files...")

    updated = 0
    for file_path in FILES_TO_PROCESS:
        full_path = HD_DIR / file_path
        if full_path.exists():
            if add_footnote_to_file(full_path):
                print(f"  ✓ {file_path}")
                updated += 1
            else:
                print(f"  - {file_path} (no changes)")
        else:
            print(f"  ✗ {file_path} (not found)")

    print(f"\nUpdated {updated}/{len(FILES_TO_PROCESS)} files.")

if __name__ == "__main__":
    main()
