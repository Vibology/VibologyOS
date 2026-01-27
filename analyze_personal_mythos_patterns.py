#!/usr/bin/env python3
"""Analyze dead link patterns in Personal Mythos."""

import re
from pathlib import Path
from collections import Counter

LIBRARY = Path("Library/The Seven Pillars of Understanding")
PERSONAL_MYTHOS = LIBRARY / "Personal Mythos"

def normalize_filename(name):
    """Normalize filename for comparison."""
    return name.replace(".md", "").strip()

def extract_wikilinks(content):
    """Extract all wikilinks from content."""
    pattern = r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]'
    return re.findall(pattern, content)

def build_library_index():
    """Build index of all Library files."""
    index = {}
    for md_file in LIBRARY.rglob("*.md"):
        normalized = normalize_filename(md_file.stem)
        index[normalized] = str(md_file.stem)
    return index

def categorize_dead_link(link, library_index):
    """Categorize a dead link by type."""
    
    # Old Folklore paths
    if link.startswith("Folklore/Jungian Archetypes/"):
        archetype = link.split("/")[-1]
        return ("old_folklore_path", archetype)
    
    # Long Seven Pillars paths
    if link.startswith("The Seven Pillars of Understanding/"):
        parts = link.split("/")
        if len(parts) >= 4:
            target = parts[-1]
            return ("long_path", target)
    
    # Centers with "Center" suffix
    if link.endswith(" Center"):
        base = link.replace(" Center", "")
        if base in ["Emotional Solar Plexus", "Sacral", "Root", "Throat", "Ajna", "G", "Heart", "Spleen", "Head"]:
            return ("center_suffix", base)
    
    # Tarot cards (common names)
    tarot_cards = ["The Fool", "The Magician", "The High Priestess", "The Empress", "The Emperor",
                   "The Hierophant", "The Lovers", "The Chariot", "Strength", "The Hermit",
                   "Wheel of Fortune", "Justice", "The Hanged Man", "Death", "Temperance",
                   "The Devil", "The Tower", "The Star", "The Moon", "The Sun", "Judgement", "Judgment", "The World"]
    if link in tarot_cards or link.replace("Judgement", "Judgment") in tarot_cards:
        return ("tarot_card", link)
    
    # Gate references
    if link.startswith("Gate "):
        return ("gate_reference", link)
    
    # Hexagram references
    if link.startswith("Hexagram "):
        return ("hexagram", link)
    
    # Mythology references
    if any(word in link for word in ["Mythology", "Zeus", "Apollo", "Athena", "Persephone", "Dionysus", "Odin", "Thor", "Ra", "Isis", "Inanna", "Psyche"]):
        return ("mythology", link)
    
    # External systems
    external_systems = ["Qabalah", "Buddhism", "Taoism", "Christianity", "Christian Mysticism", "Kabbalah", "I-Ching"]
    if link in external_systems:
        return ("external_system", link)
    
    # Alchemical terms
    alchemical = ["Coniunctio", "Mortificatio", "Solve et Coagula", "The Philosopher's Stone", 
                  "The Unus Mundus", "Unus Mundus", "The Hermaphrodite", "The Hieros Gamos"]
    if link in alchemical:
        return ("alchemical_term", link)
    
    # Archetype variants (without path)
    archetypes = ["The Hero", "The Self", "The Shadow", "The Anima", "The Animus", "The Divine Child",
                  "The Great Mother", "The Wise Old Man", "The Wise Old Woman", "The Joker", "The Persona",
                  "The Shapeshifter", "The Threshold Guardian"]
    if link in archetypes:
        # Check if it exists without "The" prefix
        without_the = link.replace("The ", "")
        if normalize_filename(without_the) in library_index:
            return ("missing_the_prefix", link)
        return ("archetype_variant", link)
    
    # Hero's Journey stages
    hj_stages = ["Call to Adventure", "Refusal of the Call", "Meeting the Mentor", "Crossing the Threshold",
                 "Tests Allies and Enemies", "Approach to the Inmost Cave", "The Ordeal", "The Reward",
                 "The Road Back", "The Resurrection", "Return with the Elixir", "Freedom to Live"]
    if link in hj_stages:
        return ("hero_journey_stage", link)
    
    # Individuation stages
    if link.startswith("Encounter with ") or link in ["Self", "Persona Development", "Ego Formation"]:
        return ("individuation_stage", link)
    
    # Internal cross-references
    if link in ["Personal Mythos", "Hero's Journey", "Alchemical Stages", "Jungian Archetypes", "World Mythology"]:
        return ("internal_section", link)
    
    return ("other", link)

def main():
    library_index = build_library_index()
    
    # Collect all dead links
    all_dead_links = []
    
    for md_file in PERSONAL_MYTHOS.rglob("*.md"):
        content = md_file.read_text()
        wikilinks = extract_wikilinks(content)
        for link in wikilinks:
            normalized = normalize_filename(link)
            if normalized not in library_index:
                all_dead_links.append(link)
    
    # Categorize
    categories = Counter()
    by_category = {}
    
    for link in all_dead_links:
        cat, detail = categorize_dead_link(link, library_index)
        categories[cat] += 1
        if cat not in by_category:
            by_category[cat] = []
        by_category[cat].append(link)
    
    # Print results
    print("\n" + "="*70)
    print("DEAD LINK PATTERN ANALYSIS")
    print("="*70)
    
    for cat, count in categories.most_common():
        print(f"\n{cat.upper().replace('_', ' ')}: {count} instances")
        # Show unique examples
        unique = sorted(set(by_category[cat]))[:15]
        for ex in unique:
            print(f"  - [[{ex}]]")
        if len(set(by_category[cat])) > 15:
            print(f"  ... and {len(set(by_category[cat])) - 15} more")
    
    print("\n" + "="*70)
    print(f"TOTAL CATEGORIES: {len(categories)}")
    print(f"TOTAL DEAD LINKS: {len(all_dead_links)}")
    print("="*70)

if __name__ == "__main__":
    main()
