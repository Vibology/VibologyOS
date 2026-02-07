#!/usr/bin/env python3
"""
Standardize endmatter structure across Library files.

Target structure:
1. ## Cross-References → {content} → ---
2. [^1]: source citation (footnotes ARE the sources) → ---

NO separate "## Sources" section - that would duplicate the footnote citations.
"""

import re
from pathlib import Path
from typing import Tuple, List

LIBRARY_ROOT = Path(__file__).resolve().parent.parent.parent / "Library"


def standardize_file(filepath: Path) -> Tuple[bool, str]:
    """
    Standardize endmatter for a single file.
    Returns (success, message)
    """
    try:
        content = filepath.read_text(encoding='utf-8')
        original = content

        # Skip templates/welcome
        if filepath.name.startswith("_") or filepath.name == "WELCOME.md":
            return False, "Skipped (template/welcome)"

        # Extract frontmatter
        frontmatter = ""
        frontmatter_match = re.match(r'^---\n(.*?\n)---\n', content, re.DOTALL)
        if frontmatter_match:
            frontmatter = frontmatter_match.group(0)
            content = content[frontmatter_match.end():]

        # Find all endmatter section markers
        sections = find_endmatter_sections(content)

        if not sections:
            return False, "No endmatter sections found"

        # Determine where body ends (before first endmatter section)
        first_section_pos = min(sec['start'] for sec in sections)
        body = content[:first_section_pos].rstrip()

        # Extract components from sections
        cross_refs = extract_section_content(content, sections, 'Cross-References')
        footnotes = extract_all_footnotes(content, sections)

        # Build standardized endmatter (NO Sources section)
        standardized = build_standardized_endmatter(cross_refs, footnotes)

        # Reconstruct file
        new_content = frontmatter + body + "\n\n" + standardized

        # Only write if changed
        if new_content != original:
            filepath.write_text(new_content, encoding='utf-8')
            return True, "Updated"
        else:
            return False, "No changes needed"

    except Exception as e:
        return False, f"Error: {str(e)}"


def find_endmatter_sections(content: str) -> List[dict]:
    """Find endmatter section headers and footnote definitions.

    Only recognizes:
    - ## Cross-References
    - ## Footnotes (will be removed)
    - ## Sources / ## References (will be removed)
    - [^N]: footnote definitions
    """
    sections = []

    # ONLY find endmatter-specific ## headers
    endmatter_headers = ['Cross-References', 'Footnotes', 'Sources', 'References']

    for header_name in endmatter_headers:
        pattern = rf'^## {re.escape(header_name)}$'
        for match in re.finditer(pattern, content, re.MULTILINE):
            sections.append({
                'type': 'header',
                'name': header_name,
                'start': match.start(),
                'end': match.end()
            })

    # Find all footnote definitions
    for match in re.finditer(r'^\[\^(\d+)\]:', content, re.MULTILINE):
        sections.append({
            'type': 'footnote',
            'number': int(match.group(1)),
            'start': match.start(),
            'end': match.end()
        })

    return sorted(sections, key=lambda x: x['start'])


def extract_section_content(content: str, sections: List[dict], section_name: str) -> str:
    """Extract content from a specific ## section."""
    # Find the section header
    section_idx = None
    for i, sec in enumerate(sections):
        if sec['type'] == 'header' and sec['name'] == section_name:
            section_idx = i
            break

    if section_idx is None:
        return ""

    # Find where content ends (next section or separator)
    start_pos = sections[section_idx]['end']
    end_pos = len(content)

    for i in range(section_idx + 1, len(sections)):
        next_sec = sections[i]
        if next_sec['type'] in ('header', 'footnote'):
            # Look backwards for separator before this section
            search_start = max(0, next_sec['start'] - 100)
            separator_matches = list(re.finditer(r'\n---\s*\n', content[search_start:next_sec['start']]))
            if separator_matches:
                end_pos = search_start + separator_matches[-1].start()
            else:
                end_pos = next_sec['start']
            break

    # Extract and clean content
    section_content = content[start_pos:end_pos].strip()
    # Remove leading/trailing separators
    section_content = re.sub(r'^---\s*', '', section_content)
    section_content = re.sub(r'\s*---$', '', section_content)

    return section_content.strip()


def extract_all_footnotes(content: str, sections: List[dict]) -> str:
    """Extract all footnote definitions (these ARE the sources)."""
    footnotes = []

    for sec in sections:
        if sec['type'] == 'footnote':
            # Find where this footnote definition ends
            pattern = r'^\[\^' + str(sec['number']) + r'\]:\s*(.+?)(?=^\[\^\d+\]:|^## |^---\s*$|$)'
            match = re.search(pattern, content[sec['start']:], re.MULTILINE | re.DOTALL)
            if match:
                footnote_text = match.group(1).strip()
                footnotes.append((sec['number'], f"[^{sec['number']}]: {footnote_text}"))

    if footnotes:
        footnotes.sort(key=lambda x: x[0])
        return "\n\n".join(f[1] for f in footnotes)

    return ""


def build_standardized_endmatter(cross_refs: str, footnotes: str) -> str:
    """Build standardized endmatter.

    Structure:
    1. ## Cross-References + content + separator
    2. Footnote definitions (NO header - these ARE the sources) + separator

    NO separate Sources section.
    """
    parts = []

    # 1. Cross-References
    if cross_refs:
        parts.append(f"## Cross-References\n\n{cross_refs}")
    else:
        parts.append("## Cross-References\n\n*See related entries within this pillar.*")

    parts.append("---")

    # 2. Footnotes (these ARE the sources)
    if footnotes:
        parts.append(footnotes)

    # 3. Final separator
    parts.append("---")

    return "\n\n".join(parts) + "\n"


def main():
    import sys

    if len(sys.argv) < 2:
        print("Usage: python3 standardize_endmatter.py <pillar_path>")
        print("Example: python3 standardize_endmatter.py 'The Seven Pillars of Understanding/The Astrolabe'")
        sys.exit(1)

    pillar_path = LIBRARY_ROOT / sys.argv[1]

    if not pillar_path.exists():
        print(f"Error: Path does not exist: {pillar_path}")
        sys.exit(1)

    # Get all markdown files in pillar
    files = sorted(pillar_path.rglob("*.md"))
    files = [f for f in files if not f.name.startswith("_")]

    print(f"Standardizing endmatter for {len(files)} files in {sys.argv[1]}...")
    print()

    updated = 0
    skipped = 0
    errors = 0

    for filepath in files:
        success, message = standardize_file(filepath)
        rel_path = filepath.relative_to(LIBRARY_ROOT)

        if success:
            print(f"  ✓ {rel_path}")
            updated += 1
        elif "Error" in message:
            print(f"  ✗ {rel_path} - {message}")
            errors += 1
        else:
            skipped += 1

    print()
    print(f"Results: {updated} updated, {skipped} skipped, {errors} errors")


if __name__ == "__main__":
    main()
