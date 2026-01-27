#!/usr/bin/env python3
"""Scan Personal Mythos files for dead wikilinks."""

import re
from pathlib import Path
from collections import defaultdict

LIBRARY = Path("Library/The Seven Pillars of Understanding")
PERSONAL_MYTHOS = LIBRARY / "Personal Mythos"

def normalize_filename(name):
    """Normalize filename for comparison."""
    return name.replace(".md", "").strip()

def extract_wikilinks(content):
    """Extract all wikilinks from content."""
    # Match [[link]] or [[link|display]]
    pattern = r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]'
    return re.findall(pattern, content)

def build_library_index():
    """Build index of all Library files."""
    index = {}
    for md_file in LIBRARY.rglob("*.md"):
        rel_path = md_file.relative_to(LIBRARY)
        normalized = normalize_filename(md_file.stem)
        index[normalized] = str(rel_path)
    return index

def check_file(file_path, library_index):
    """Check a single file for dead links."""
    content = file_path.read_text()
    wikilinks = extract_wikilinks(content)
    
    dead_links = []
    for link in wikilinks:
        normalized = normalize_filename(link)
        if normalized not in library_index:
            dead_links.append(link)
    
    return dead_links

def main():
    library_index = build_library_index()
    
    # Group by subdirectory
    by_section = defaultdict(list)
    
    for md_file in sorted(PERSONAL_MYTHOS.rglob("*.md")):
        dead_links = check_file(md_file, library_index)
        if dead_links:
            rel_path = md_file.relative_to(PERSONAL_MYTHOS)
            section = rel_path.parts[0] if len(rel_path.parts) > 1 else "root"
            by_section[section].append((md_file.name, dead_links))
    
    # Print results
    total_files = 0
    total_links = 0
    
    for section in sorted(by_section.keys()):
        files = by_section[section]
        section_links = sum(len(links) for _, links in files)
        print(f"\n{'='*60}")
        print(f"{section.upper()} ({len(files)} files, {section_links} dead links)")
        print(f"{'='*60}")
        
        for filename, dead_links in files:
            print(f"\n{filename}: {len(dead_links)} dead links")
            for link in sorted(set(dead_links)):
                print(f"  - [[{link}]]")
        
        total_files += len(files)
        total_links += section_links
    
    print(f"\n{'='*60}")
    print(f"TOTAL: {total_files} files with {total_links} dead links")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
