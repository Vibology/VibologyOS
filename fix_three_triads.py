#!/usr/bin/env python3
"""Fix The Three Triads links with backslash."""

from pathlib import Path

ANGELOLOGY = Path("Library/The Seven Pillars of Understanding/Angelology")

files_to_fix = [
    "The Archangels/Michael.md",
    "The Archangels/Tzadkiel.md",
    "The Archangels/Tzaphkiel.md",
]

for file_rel in files_to_fix:
    file_path = ANGELOLOGY / file_rel
    content = file_path.read_text()
    
    # Replace the exact string
    if r"[[The Three Triads\]]" in content:
        new_content = content.replace(r"[[The Three Triads\]]", "[[The Three Triads]]")
        file_path.write_text(new_content)
        print(f"✓ {file_rel}: Fixed The Three Triads link")
    else:
        print(f"✗ {file_rel}: Link not found in expected format")

print("\nDone fixing The Three Triads links")
