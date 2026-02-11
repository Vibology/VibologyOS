#!/usr/bin/env python3
"""
List all Library files that have no inline footnotes.

These files have References/Sources sections but no inline citations.
Phase 3: Add inline footnotes to these files.
"""

import re
from pathlib import Path

LIBRARY_ROOT = Path(__file__).resolve().parent.parent.parent / "Library"

def has_footnotes(filepath):
    """Check if file has any inline footnote references."""
    try:
        content = filepath.read_text(encoding='utf-8')
    except Exception:
        return None

    # Find inline references: [^1], [^2], etc.
    inline_pattern = r'\[\^(\d+)\](?!:)'
    inline_refs = re.findall(inline_pattern, content)

    return len(inline_refs) > 0

def main():
    all_files = sorted(LIBRARY_ROOT.rglob("*.md"))

    # Exclude templates and WELCOME
    all_files = [
        f for f in all_files
        if not f.name.startswith("_") and f.name != "WELCOME.md"
    ]

    files_without_footnotes = []

    for filepath in all_files:
        if not has_footnotes(filepath):
            files_without_footnotes.append(filepath)

    # Group by pillar
    by_pillar = {}
    for filepath in files_without_footnotes:
        rel_path = filepath.relative_to(LIBRARY_ROOT)
        parts = rel_path.parts

        if parts[0] == "The Seven Pillars of Understanding":
            pillar = parts[1] if len(parts) > 1 else "Unknown"
        else:
            pillar = parts[0] if len(parts) > 0 else "Unknown"

        if pillar not in by_pillar:
            by_pillar[pillar] = []
        by_pillar[pillar].append(rel_path)

    # Report
    print("=" * 70)
    print(f"FILES WITHOUT INLINE FOOTNOTES: {len(files_without_footnotes)} files")
    print("=" * 70)

    for pillar in sorted(by_pillar.keys()):
        files = by_pillar[pillar]
        print(f"\n{pillar} ({len(files)} files)")
        print("-" * 70)
        for f in sorted(files):
            print(f"  {f}")

if __name__ == "__main__":
    main()
