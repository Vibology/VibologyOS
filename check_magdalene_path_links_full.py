#!/usr/bin/env python3
"""Scan The Magdalene Path for dead wikilinks (checking entire Library)."""

import re
from pathlib import Path

LIBRARY_ROOT = Path("Library")
MAGDALENE_PATH = LIBRARY_ROOT / "The Seven Pillars of Understanding" / "The Magdalene Path"

def normalize_filename(name):
    return name.replace(".md", "").strip()

def extract_wikilinks(content):
    pattern = r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]'
    return re.findall(pattern, content)

def build_library_index():
    """Build index of ALL files in Library directory."""
    index = {}
    for md_file in LIBRARY_ROOT.rglob("*.md"):
        normalized = normalize_filename(md_file.stem)
        index[normalized] = str(md_file.relative_to(LIBRARY_ROOT))
    return index

def main():
    library_index = build_library_index()
    
    dead_links_by_file = {}
    
    for md_file in sorted(MAGDALENE_PATH.rglob("*.md")):
        content = md_file.read_text()
        wikilinks = extract_wikilinks(content)
        
        dead_links = []
        for link in wikilinks:
            normalized = normalize_filename(link)
            if normalized not in library_index:
                dead_links.append(link)
        
        if dead_links:
            dead_links_by_file[md_file.name] = dead_links
    
    # Print results
    total_files = len(dead_links_by_file)
    total_links = sum(len(links) for links in dead_links_by_file.values())
    
    if total_files == 0:
        print("="*70)
        print("THE MAGDALENE PATH - ZERO DEAD LINKS! ✅")
        print("="*70)
        return
    
    print("="*70)
    print("THE MAGDALENE PATH - DEAD LINK SCAN (FULL LIBRARY)")
    print("="*70)
    
    for filename in sorted(dead_links_by_file.keys()):
        dead_links = dead_links_by_file[filename]
        print(f"\n{filename}: {len(dead_links)} dead links")
        for link in sorted(set(dead_links)):
            print(f"  - [[{link}]]")
    
    print("\n" + "="*70)
    print(f"TOTAL: {total_files} files with {total_links} dead links")
    print("="*70)

if __name__ == "__main__":
    main()
