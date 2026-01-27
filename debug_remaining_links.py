#!/usr/bin/env python3
"""Debug: Show actual wikilinks in problem files."""

import re
from pathlib import Path

PERSONAL_MYTHOS = Path("Library/The Seven Pillars of Understanding/Personal Mythos")

def extract_wikilinks(content):
    pattern = r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]'
    return re.findall(pattern, content)

problem_files = [
    "Fairy Tales/The Quest Object.md",
    "Fairy Tales/The Youngest Child.md",
    "Hero's Journey/Approach to the Inmost Cave.md",
    "Individuation Process/Encounter with Anima-Animus.md",
    "Jungian Archetypes/The Animus.md",
    "Jungian Archetypes/The Wise Old Man.md",
]

for file_rel in problem_files:
    file_path = PERSONAL_MYTHOS / file_rel
    if not file_path.exists():
        print(f"MISSING: {file_rel}")
        continue
    
    content = file_path.read_text()
    wikilinks = extract_wikilinks(content)
    
    # Check for the specific dead links we're looking for
    dead_links = []
    targets = ["The Chariot", "The Magician", "The Hermit", "The High Priestess", 
               "The Lovers", "Ego", "The Devouring Mother", "The Terrible Father",
               "Underworld", "Core Foundations/Logos", "Logos"]
    
    for link in wikilinks:
        if link in targets:
            dead_links.append(link)
    
    if dead_links:
        print(f"\n{file_rel}: {len(dead_links)} dead links")
        for link in dead_links:
            # Find context
            for i, line in enumerate(content.split('\n'), 1):
                if f"[[{link}]]" in line or f"[[{link}|" in line:
                    print(f"  Line {i}: [[{link}]]")
                    print(f"    Context: {line.strip()[:100]}")
                    break
