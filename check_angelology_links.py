#!/usr/bin/env python3
"""Scan Angelology for dead wikilinks."""

import re
from pathlib import Path
from collections import defaultdict

LIBRARY_ROOT = Path("Library")
ANGELOLOGY = LIBRARY_ROOT / "The Seven Pillars of Understanding" / "Angelology"

def normalize_filename(name):
    return name.replace(".md", "").strip()

def extract_wikilinks(content):
    pattern = r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]'
    return re.findall(pattern, content)

def build_library_index():
    index = {}
    for md_file in LIBRARY_ROOT.rglob("*.md"):
        normalized = normalize_filename(md_file.stem)
        index[normalized] = str(md_file.relative_to(LIBRARY_ROOT))
    return index

def main():
    library_index = build_library_index()
    
    dead_links_by_file = defaultdict(list)
    
    for md_file in sorted(ANGELOLOGY.rglob("*.md")):
        content = md_file.read_text()
        wikilinks = extract_wikilinks(content)
        
        for link in wikilinks:
            normalized = normalize_filename(link)
            if normalized not in library_index:
                dead_links_by_file[md_file.relative_to(ANGELOLOGY)].append(link)
    
    # Print results
    total_files = len(dead_links_by_file)
    total_links = sum(len(links) for links in dead_links_by_file.values())
    
    if total_files == 0:
        print("="*70)
        print("ANGELOLOGY - ZERO DEAD LINKS! ✅")
        print("="*70)
        return
    
    print("="*70)
    print("ANGELOLOGY - DEAD LINK SCAN")
    print("="*70)
    
    # Group by section
    sections = defaultdict(list)
    for file_path, links in sorted(dead_links_by_file.items()):
        section = str(file_path.parent) if file_path.parent != Path('.') else "root"
        sections[section].append((file_path.name, links))
    
    for section in sorted(sections.keys()):
        files = sections[section]
        section_total = sum(len(links) for _, links in files)
        print(f"\n{section.upper()} ({len(files)} files, {section_total} dead links)")
        print("="*70)
        
        for filename, links in files:
            print(f"\n{filename}: {len(links)} dead links")
            for link in sorted(set(links)):
                print(f"  - [[{link}]]")
    
    print("\n" + "="*70)
    print(f"TOTAL: {total_files} files with {total_links} dead links")
    print("="*70)

if __name__ == "__main__":
    main()
