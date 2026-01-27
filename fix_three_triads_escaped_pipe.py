#!/usr/bin/env python3
"""Fix The Three Triads links with escaped pipe."""

import re
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
    
    # Replace escaped pipe with normal pipe
    old_pattern = r'\[\[The Three Triads\\|'
    new_pattern = r'[[The Three Triads|'
    
    if old_pattern in content:
        new_content = content.replace(old_pattern, new_pattern)
        file_path.write_text(new_content)
        print(f"✓ {file_rel}: Fixed The Three Triads escaped pipe")
    else:
        print(f"  {file_rel}: No escaped pipe found")

print("\nDone")
