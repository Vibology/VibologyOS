#!/usr/bin/env python3
import re
import os
from pathlib import Path

SIGNS_DIR = Path("Library/The Seven Pillars of Understanding/Astrology/Signs")

def find_file_in_library(target_name):
    """Search for a file in Library directory."""
    # Try exact match first
    for root, dirs, files in os.walk("Library"):
        if f"{target_name}.md" in files:
            return True
    return False

def extract_target(wikilink):
    """Extract target from wikilink (before any |)."""
    match = re.match(r'\[\[([^|\]]+)', wikilink)
    if match:
        return match.group(1)
    return None

def main():
    dead_links = {}
    
    for md_file in sorted(SIGNS_DIR.glob("*.md")):
        with open(md_file, 'r') as f:
            content = f.read()
        
        wikilinks = re.findall(r'\[\[[^\]]+\]\]', content)
        
        for link in wikilinks:
            target = extract_target(link)
            if target and not find_file_in_library(target):
                if target not in dead_links:
                    dead_links[target] = []
                dead_links[target].append(md_file.name)
    
    if dead_links:
        print("DEAD LINKS FOUND:\n")
        for target, files in sorted(dead_links.items()):
            print(f"[[{target}]]")
            for fname in files:
                print(f"  - {fname}")
            print()
    else:
        print("No dead links found.")

if __name__ == "__main__":
    main()
