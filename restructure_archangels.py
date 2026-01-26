#!/usr/bin/env python3
"""
Restructure Archangel Files to Canonical Semantic Section System

Transforms all 11 archangel files to match the canonical structure defined in
System/Templates/_MANIFEST-Angelology.md:

1. ## Essence (OPENING)
2. ## Correspondences (DATA)
3. ## Theological Depth (DEPTH)
4. ## Fallen Aspect (SHADOW)
5. ## Invocation (PRACTICE)
6. ## Cross-References (LINKS)
7. ## Sources (SOURCES)
"""

import re
from pathlib import Path
from typing import List, Tuple, Dict

# Base directory
BASE_DIR = Path("/home/joe/VibologyOS/Library/The Seven Pillars of Understanding/Angelology/The Archangels")

# Files to restructure
ARCHANGEL_FILES = [
    "Gabriel.md", "Raphael.md", "Michael.md", "Uriel.md",
    "Metatron.md", "Raziel.md", "Tzaphkiel.md", "Tzadkiel.md",
    "Kamael.md", "Haniel.md", "Sandalphon.md"
]

# Sections that should be converted to Theological Depth subsections
THEOLOGICAL_DEPTH_PATTERNS = [
    (r"^## (The )?Qabalistic (Context|Attribution|Integration):?.*", "### Qabalistic Context"),
    (r"^## (.+)in Mystical and Esoteric Tradition", "### Mystical and Esoteric Tradition"),
    (r"^## (The )?Tarot:.*", "### Tarot Correspondences"),
    (r"^## Element:.*", "### Elemental Attribution"),
    (r"^## Planetary Correspondence:.*", "### Planetary Correspondence"),
    (r"^## Iconography and Symbolism", "### Iconography and Symbolism"),
    (r"^## Function in Divine Economy", "### Function in Divine Economy"),
    (r"^## Human Consciousness Parallel:.*", "### Human Consciousness Parallel"),
    (r"^## Mythology and Cross-Tradition Parallels", "### Mythology and Cross-Tradition Parallels"),
    (r"^## Jungian and Psychological Dimension", "### Jungian and Psychological Dimension"),
    (r"^## (The )?Gift of Integration:.*", "### The Gift of Integration"),
    (r"^## .+and the Other Archangels", "### Relationships with Other Archangels"),
]

def parse_markdown_structure(filepath: Path) -> Tuple[str, str, List[Dict]]:
    """
    Parse markdown file into structure with proper hierarchy.

    Returns:
        - YAML frontmatter
        - Title section (H1 + subtitle)
        - List of H2 sections with their content
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract YAML frontmatter
    yaml_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if yaml_match:
        frontmatter = yaml_match.group(0)
        content_after_yaml = content[len(frontmatter):]
    else:
        frontmatter = ""
        content_after_yaml = content

    # Extract H1 title and subtitle
    title_match = re.match(r'^(# .+?\n)(\*.+?\*\n)?(\n---\n)?', content_after_yaml, re.DOTALL)
    if title_match:
        title_section = title_match.group(0)
        content_after_title = content_after_yaml[len(title_section):]
    else:
        title_section = ""
        content_after_title = content_after_yaml

    # Extract opening content (before first ##)
    opening_match = re.match(r'^((?:(?!^## ).)*)', content_after_title, re.DOTALL | re.MULTILINE)
    opening_content = opening_match.group(1).strip() if opening_match else ""

    # Split by H2 sections
    h2_pattern = re.compile(r'^## (.+?)$', re.MULTILINE)
    h2_positions = [(m.start(), m.group(1)) for m in h2_pattern.finditer(content_after_title)]

    sections = []
    for i, (pos, heading) in enumerate(h2_positions):
        next_pos = h2_positions[i+1][0] if i+1 < len(h2_positions) else len(content_after_title)
        section_content = content_after_title[pos:next_pos]
        sections.append({
            'heading': heading,
            'content': section_content
        })

    return frontmatter, title_section, opening_content, sections

def extract_essence_from_correspondences(content: str) -> Tuple[str, str]:
    """
    Extract opening paragraphs from Correspondences section to use as Essence.

    Returns: (essence_content, remaining_correspondences_content)
    """
    # Remove the ## Correspondences heading
    content_without_heading = re.sub(r'^## [^\n]+\n+', '', content, count=1)

    # Find first ### subsection
    first_subsection = re.search(r'^###\s', content_without_heading, re.MULTILINE)

    if first_subsection:
        # Everything before first ### is essence
        essence = content_without_heading[:first_subsection.start()].strip()
        remaining = content_without_heading[first_subsection.start():]
        return essence, remaining
    else:
        # No subsections, entire content is essence
        return content_without_heading.strip(), ""

def categorize_section(heading: str, content: str) -> Tuple[str, str]:
    """
    Categorize a section and return (category, converted_content).

    Categories: correspondences, theological_depth, fallen_aspect, invocation,
                cross_references, sources
    """
    h2_line = f"## {heading}"

    # Check for exact matches first
    if heading == "Fallen Aspect" or "Fallen Aspect" in heading:
        return "fallen_aspect", content

    if heading == "Invocation" or "Invocation" in heading:
        return "invocation", content

    if heading == "Cross-References":
        return "cross_references", content

    if heading == "Sources":
        return "sources", content

    if heading == "Correspondences" or heading == "Core Correspondences":
        return "correspondences", content

    # Special case: "A Prayer to [Archangel]" belongs in Invocation
    if heading.startswith("A Prayer to "):
        # Move to Invocation as subsection
        converted = content.replace(f"## {heading}", f"### {heading}", 1)
        return "invocation", converted

    # Special case: "Cross-System Correspondences" could be either
    # Theological Depth or kept separate - routing to Theological Depth
    if "Cross-System" in heading:
        converted = content.replace(f"## {heading}", f"### {heading}", 1)
        return "theological_depth", converted

    # Check Theological Depth patterns
    for pattern, replacement in THEOLOGICAL_DEPTH_PATTERNS:
        if re.match(pattern, h2_line):
            # Convert ## to ### for subsection
            converted = content.replace(f"## {heading}", replacement, 1)
            return "theological_depth", converted

    # Default: if not recognized, treat as Theological Depth subsection
    return "theological_depth", content.replace(f"## {heading}", f"### {heading}", 1)

def restructure_file(filepath: Path, dry_run: bool = True):
    """Restructure a single archangel file."""
    print(f"\n{'='*80}")
    print(f"Processing: {filepath.name}")
    print('='*80)

    frontmatter, title_section, opening_content, sections = parse_markdown_structure(filepath)

    # Categorize sections
    categorized = {
        'essence': '',
        'correspondences': [],
        'theological_depth': [],
        'fallen_aspect': [],
        'invocation': [],
        'cross_references': [],
        'sources': []
    }

    # Extract essence from opening content or first Correspondences section
    if opening_content:
        categorized['essence'] = opening_content
    else:
        # Look for Correspondences section and extract opening paragraphs
        for section in sections:
            if section['heading'] in ['Correspondences', 'Core Correspondences']:
                essence, remaining = extract_essence_from_correspondences(section['content'])
                if essence:
                    categorized['essence'] = essence
                # Update section content to only include remaining parts
                section['content'] = f"## {section['heading']}\n\n{remaining}" if remaining else ""
                break

    for section in sections:
        if not section['content']:  # Skip if content was moved to essence
            continue
        category, converted_content = categorize_section(section['heading'], section['content'])
        categorized[category].append(converted_content)

    # Build output
    output = []

    # 1. Frontmatter
    output.append(frontmatter)

    # 2. Title
    if title_section:
        output.append(title_section)

    # 3. ESSENCE (opening content before first H2 or extracted from Correspondences)
    if categorized['essence']:
        output.append("\n## Essence\n\n")
        output.append(categorized['essence'])
        output.append("\n")

    # 4. CORRESPONDENCES
    if categorized['correspondences']:
        output.append("\n---\n## Correspondences\n\n")
        for content in categorized['correspondences']:
            # Remove the H2 heading line (already added above)
            content_clean = re.sub(r'^## [^\n]+\n', '', content, count=1)
            output.append(content_clean)

    # 5. THEOLOGICAL DEPTH
    if categorized['theological_depth']:
        output.append("\n---\n## Theological Depth\n\n")
        for content in categorized['theological_depth']:
            # Content already has ### headings from conversion
            output.append(content)

    # 6. FALLEN ASPECT
    if categorized['fallen_aspect']:
        output.append("\n---\n")
        for content in categorized['fallen_aspect']:
            output.append(content)

    # 7. INVOCATION
    if categorized['invocation']:
        output.append("\n---\n")
        for content in categorized['invocation']:
            output.append(content)

    # 8. CROSS-REFERENCES
    if categorized['cross_references']:
        output.append("\n---\n")
        for content in categorized['cross_references']:
            output.append(content)

    # 9. SOURCES
    if categorized['sources']:
        output.append("\n---\n")
        for content in categorized['sources']:
            output.append(content)

    final_output = ''.join(output)

    # Report
    if dry_run:
        print(f"\n[DRY RUN] Would write {len(final_output)} characters to {filepath.name}")
        print("\nSection summary:")
        print(f"  - Essence: {'present' if categorized['essence'] else 'empty'}")
        print(f"  - Correspondences: {len(categorized['correspondences'])} H2 sections")
        print(f"  - Theological Depth: {len(categorized['theological_depth'])} H2 sections")
        print(f"  - Fallen Aspect: {len(categorized['fallen_aspect'])} H2 sections")
        print(f"  - Invocation: {len(categorized['invocation'])} H2 sections")
        print(f"  - Cross-References: {len(categorized['cross_references'])} H2 sections")
        print(f"  - Sources: {len(categorized['sources'])} H2 sections")

        # Show which sections went where
        print("\nSection routing:")
        for section in sections:
            if not section['content']:
                print(f"  '{section['heading']}' → essence (extracted)")
            else:
                category, _ = categorize_section(section['heading'], section['content'])
                print(f"  '{section['heading']}' → {category}")
    else:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(final_output)
        print(f"\n✓ Successfully restructured {filepath.name}")

def main():
    """Main execution."""
    import sys

    dry_run = '--dry-run' in sys.argv or '-n' in sys.argv
    test_mode = '--test' in sys.argv

    if dry_run:
        print("\n" + "="*80)
        print("DRY RUN MODE - No files will be modified")
        print("="*80)

    if test_mode:
        # Test on just Gabriel first
        files_to_process = ["Gabriel.md"]
        print("\n" + "="*80)
        print("TEST MODE - Processing only Gabriel.md")
        print("="*80)
    else:
        files_to_process = ARCHANGEL_FILES

    for filename in files_to_process:
        filepath = BASE_DIR / filename
        if filepath.exists():
            try:
                restructure_file(filepath, dry_run=dry_run)
            except Exception as e:
                print(f"\n✗ ERROR processing {filename}: {e}")
                import traceback
                traceback.print_exc()
        else:
            print(f"\n✗ File not found: {filepath}")

    print("\n" + "="*80)
    print("Processing complete!")
    print("="*80)

    if dry_run:
        print("\nTo apply changes, run without --dry-run flag:")
        print("  python3 restructure_archangels.py")
        print("\nTo test on Gabriel only:")
        print("  python3 restructure_archangels.py --test --dry-run")
    else:
        print("\nAll files have been restructured.")
        print("Review changes with: git diff")

if __name__ == '__main__':
    main()
