#!/usr/bin/env python3
"""Analyze remaining 233 dead links to categorize what can be fixed."""

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
    """Build comprehensive index of all Library files."""
    index = {}
    for md_file in LIBRARY.rglob("*.md"):
        normalized = normalize_filename(md_file.stem)
        index[normalized] = str(md_file.relative_to(LIBRARY))
    return index

def categorize_remaining(link, library_index):
    """Categorize each remaining dead link."""
    
    # Check if it's close to an existing file (fuzzy match)
    link_lower = link.lower()
    
    # HD Channels - check format
    if link.startswith("Channel "):
        return ("hd_channel", link)
    
    # HD Profiles
    if re.match(r'Line \d', link):
        return ("hd_profile_line", link)
    
    # Fairy tales
    fairy_tales = ["Snow Queen", "Six Swans", "Twelve Brothers", "White Snake", 
                   "Golden Bird", "Girl Without Hands", "Donkeyskin"]
    if any(tale in link for tale in fairy_tales):
        return ("fairy_tale", link)
    
    # Mythology figures
    if any(myth in link for myth in ["Cronus", "Chronos", "Loki", "Heimdallr", "Tiresias"]):
        return ("mythology_figure", link)
    
    # Astrology
    if "House" in link and any(num in link for num in ["Fourth", "Eighth", "Twelfth"]):
        return ("astrology_house", link)
    
    # Qabalah
    if link.startswith("Path ") and " - " in link:
        return ("qabalah_path", link)
    
    # Alchemy terms
    alchemy = ["Chemical Wedding", "Multiplication", "Opus"]
    if any(term in link for term in alchemy):
        return ("alchemy", link)
    
    # Psychological/Jungian
    psych = ["Compensatory", "Inferior Function", "Complex", "Regression", "Libido"]
    if any(term in link for term in psych):
        return ("psychological", link)
    
    # Mythology/Religious
    if any(term in link for term in ["Christ", "Gnostic", "Duat", "Sol Invictus"]):
        return ("mythology_religious", link)
    
    # Fairy tale motifs
    motifs = ["House of", "Curse and", "Spirit in", "Recognition Token"]
    if any(motif in link for motif in motifs):
        return ("fairy_tale_motif", link)
    
    # General concepts
    return ("other", link)

def main():
    library_index = build_library_index()
    
    # Collect all remaining dead links
    remaining_links = []
    file_count = Counter()
    
    for md_file in PERSONAL_MYTHOS.rglob("*.md"):
        content = md_file.read_text()
        wikilinks = extract_wikilinks(content)
        
        file_dead_links = []
        for link in wikilinks:
            normalized = normalize_filename(link)
            if normalized not in library_index:
                remaining_links.append(link)
                file_dead_links.append(link)
        
        if file_dead_links:
            file_count[md_file.relative_to(PERSONAL_MYTHOS)] = len(file_dead_links)
    
    # Categorize
    categories = Counter()
    by_category = {}
    
    for link in remaining_links:
        cat, detail = categorize_remaining(link, library_index)
        categories[cat] += 1
        if cat not in by_category:
            by_category[cat] = []
        by_category[cat].append(link)
    
    # Print results
    print("\n" + "="*70)
    print("REMAINING 233 DEAD LINKS - CATEGORIZED")
    print("="*70)
    
    for cat, count in categories.most_common():
        print(f"\n{cat.upper().replace('_', ' ')}: {count} instances")
        unique = sorted(set(by_category[cat]))[:20]
        for ex in unique:
            print(f"  - [[{ex}]]")
        if len(set(by_category[cat])) > 20:
            print(f"  ... and {len(set(by_category[cat])) - 20} more")
    
    print("\n" + "="*70)
    print("FILES WITH MOST REMAINING DEAD LINKS:")
    print("="*70)
    for file_path, count in file_count.most_common(10):
        print(f"{count:3d}  {file_path}")
    
    print("\n" + "="*70)
    print(f"TOTAL REMAINING: {len(remaining_links)} dead links")
    print(f"UNIQUE LINKS: {len(set(remaining_links))}")
    print("="*70)

if __name__ == "__main__":
    main()
