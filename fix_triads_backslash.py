#!/usr/bin/env python3
"""Fix The Three Triads links with trailing backslash."""

import re
from pathlib import Path

ANGELOLOGY = Path("Library/The Seven Pillars of Understanding/Angelology")

def fix_triads_links(content):
    """Fix malformed The Three Triads links."""
    # Pattern: [[The Three Triads\|anything]]
    pattern = r'\[\[The Three Triads\\(\|[^\]]+)?\]\]'
    
    def replace_match(match):
        alias_part = match.group(1) if match.group(1) else ""
        return f'[[The Three Triads{alias_part}]]'
    
    new_content = re.sub(pattern, replace_match, content)
    changes = len(re.findall(pattern, content))
    return new_content, changes

total_changes = 0
for md_file in sorted(ANGELOLOGY.rglob("*.md")):
    content = md_file.read_text()
    new_content, changes = fix_triads_links(content)
    
    if changes > 0:
        md_file.write_text(new_content)
        rel_path = md_file.relative_to(ANGELOLOGY)
        print(f"✓ {rel_path}: {changes} fixes")
        total_changes += changes

print(f"\nTotal: {total_changes} fixes")
