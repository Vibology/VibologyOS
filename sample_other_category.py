#!/usr/bin/env python3
"""Sample the OTHER category to see what's in there."""

import re
from pathlib import Path
from collections import Counter

LIBRARY = Path("Library/The Seven Pillars of Understanding")
PERSONAL_MYTHOS = LIBRARY / "Personal Mythos"

def normalize_filename(name):
    return name.replace(".md", "").strip()

def extract_wikilinks(content):
    pattern = r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]'
    return re.findall(pattern, content)

def build_library_index():
    index = {}
    for md_file in LIBRARY.rglob("*.md"):
        normalized = normalize_filename(md_file.stem)
        index[normalized] = True
    return index

library_index = build_library_index()

# Collect OTHER category links
other_links = Counter()

for md_file in PERSONAL_MYTHOS.rglob("*.md"):
    content = md_file.read_text()
    wikilinks = extract_wikilinks(content)
    
    for link in wikilinks:
        normalized = normalize_filename(link)
        if normalized not in library_index:
            # Check if it falls into known categories
            is_known_cat = False
            
            if link == "Self":
                is_known_cat = True
            if link.startswith("Hexagram ") or link.startswith("Gate "):
                is_known_cat = True
            if link in ["Coniunctio", "Mortificatio", "Solve et Coagula", "The Hermaphrodite", 
                       "The Hieros Gamos", "The Philosopher's Stone", "The Unus Mundus", "Unus Mundus"]:
                is_known_cat = True
            if any(myth in link for myth in ["Mythology", "Aphrodite", "Athena", "Psyche", "Dionysus",
                                            "Persephone", "Demeter", "Inanna", "Odin", "Cupid"]):
                is_known_cat = True
            if link.startswith("Folklore/"):
                is_known_cat = True
            
            if not is_known_cat:
                other_links[link] += 1

# Print top 100
print("\n" + "="*70)
print("OTHER CATEGORY - TOP 100 MOST FREQUENT")
print("="*70)

for link, count in other_links.most_common(100):
    print(f"{count:3d}  [[{link}]]")

print(f"\n{'='*70}")
print(f"TOTAL UNIQUE OTHER LINKS: {len(other_links)}")
print(f"TOTAL OTHER INSTANCES: {sum(other_links.values())}")
print("="*70)
