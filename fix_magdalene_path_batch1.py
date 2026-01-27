#!/usr/bin/env python3
"""Fix The Magdalene Path dead links - Batch 1."""

import re
from pathlib import Path

MAGDALENE_PATH = Path("Library/The Seven Pillars of Understanding/The Magdalene Path")

# Fix "The Magdalene Path Overview" → "The Magdalene Path"
OVERVIEW_FIX = {
    "The Magdalene Path Overview": "The Magdalene Path",
}

# Fix section anchor links - remove the anchor portion
# Pattern: [[File#Section]] → [[File]]
def remove_section_anchors(content):
    """Remove section anchors from wikilinks."""
    # Match [[Something#Anchor]] or [[Something#Anchor|Display]]
    pattern = r'\[\[([^#\]]+)#[^\]|]+(\|[^\]]+)?\]\]'
    
    def replace_anchor(match):
        file_part = match.group(1)
        alias_part = match.group(2) if match.group(2) else ""
        return f'[[{file_part}{alias_part}]]'
    
    new_content = re.sub(pattern, replace_anchor, content)
    changes = len(re.findall(pattern, content))
    return new_content, changes

# Fix Tarot cards
TAROT_FIXES = {
    "The Star": "The Star (XVII)",
    "The Moon": "The Moon (XVIII)",
    "The High Priestess": "The High Priestess (II)",
    "The Lovers": "The Lovers (VI)",
    "Death": "Death (XIII)",
    "The Hanged Man": "The Hanged Man (XII)",
    "Temperance": "Temperance (XIV)",
    "The Devil": "The Devil (XV)",
    "The Emperor": "The Emperor (IV)",
    "The Empress": "The Empress (III)",
    "The Sun": "The Sun (XIX)",
    "The World": "The World (XXI)",
    "The Universe": "The World (XXI)",  # Thoth deck name
    "Wheel of Fortune": "Wheel of Fortune (X)",
}

# Fix Jungian Archetypes references (they're already standalone files)
# Just remove the "Jungian Archetypes#" prefix
def fix_jungian_archetype_refs(content):
    """Fix Jungian Archetypes references."""
    pattern = r'\[\[Jungian Archetypes#(The [^\]|]+)(\|[^\]]+)?\]\]'
    
    def replace_jungian(match):
        archetype = match.group(1)
        alias_part = match.group(2) if match.group(2) else ""
        return f'[[{archetype}{alias_part}]]'
    
    new_content = re.sub(pattern, replace_jungian, content)
    changes = len(re.findall(pattern, content))
    return new_content, changes

# Fix Core Foundations references
CORE_FOUNDATIONS_FIXES = {
    "Inner Authority and Strategy": "Core Foundations/Inner Authority and Strategy",
    "Seven-Coordinate Navigation": "Core Foundations/Seven-Coordinate Navigation",
    "Anima et Algorithm": "Core Foundations/Anima et Algorithm",
    "Vibology": "Core Foundations/Vibology",
}

# Fix Angelology references
ANGELOLOGY_FIXES = {
    "The Seraphim": "Seraphim",
}

# Convert forward references to plain text
FORWARD_REFS_TO_PLAIN = [
    "Sophia", "Theosis", "Mystical Union", "Enochian System Overview",
    "Folklore", "Saturn",
]

def apply_fixes(content):
    """Apply all fixes."""
    total_changes = 0
    
    # 1. Remove section anchors
    content, changes = remove_section_anchors(content)
    total_changes += changes
    
    # 2. Fix Jungian Archetypes
    content, changes = fix_jungian_archetype_refs(content)
    total_changes += changes
    
    # 3. Fix Overview name
    for old, new in OVERVIEW_FIX.items():
        pattern = rf'\[\[{re.escape(old)}(?:\|[^\]]+)?\]\]'
        count = len(re.findall(pattern, content))
        if count:
            content = re.sub(pattern, rf'[[{new}]]', content)
            total_changes += count
    
    # 4. Fix Tarot cards
    for old, new in TAROT_FIXES.items():
        pattern = rf'\[\[{re.escape(old)}\]\]'
        count = len(re.findall(pattern, content))
        if count:
            content = re.sub(pattern, rf'[[{new}]]', content)
            total_changes += count
    
    # 5. Fix Core Foundations
    for old, new in CORE_FOUNDATIONS_FIXES.items():
        pattern = rf'\[\[{re.escape(old)}(?:\|[^\]]+)?\]\]'
        count = len(re.findall(pattern, content))
        if count:
            content = re.sub(pattern, rf'[[{new}]]', content)
            total_changes += count
    
    # 6. Fix Angelology
    for old, new in ANGELOLOGY_FIXES.items():
        pattern = rf'\[\[{re.escape(old)}(?:\|[^\]]+)?\]\]'
        count = len(re.findall(pattern, content))
        if count:
            content = re.sub(pattern, rf'[[{new}]]', content)
            total_changes += count
    
    # 7. Convert forward refs to plain text
    for term in FORWARD_REFS_TO_PLAIN:
        pattern = rf'\[\[{re.escape(term)}\]\]'
        count = len(re.findall(pattern, content))
        if count:
            content = re.sub(pattern, term, content)
            total_changes += count
    
    return content, total_changes

def main():
    total_files = 0
    total_changes = 0
    
    for md_file in sorted(MAGDALENE_PATH.rglob("*.md")):
        content = md_file.read_text()
        new_content, changes = apply_fixes(content)
        
        if changes > 0:
            md_file.write_text(new_content)
            print(f"✓ {md_file.name}: {changes} fixes")
            total_files += 1
            total_changes += changes
    
    print(f"\n{'='*60}")
    print(f"MAGDALENE PATH BATCH 1: {total_changes} fixes across {total_files} files")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
