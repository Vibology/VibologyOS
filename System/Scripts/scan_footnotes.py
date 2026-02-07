#!/usr/bin/env python3
"""
Scan Library for inline footnote coverage.

Reports:
- Files with inline footnotes ([^1], [^2]) but missing definitions
- Files with orphaned definitions but no inline references
- Overall coverage statistics
"""

import re
from pathlib import Path
from collections import defaultdict

LIBRARY_ROOT = Path(__file__).resolve().parent.parent.parent / "Library"

def scan_file(filepath):
    """
    Returns:
        inline_refs: set of footnote numbers used inline (e.g., {1, 2, 3})
        definitions: set of footnote numbers defined (e.g., {1, 2, 3})
    """
    try:
        content = filepath.read_text(encoding='utf-8')
    except Exception as e:
        return None, None, str(e)

    # Find inline references: [^1], [^2], etc.
    inline_pattern = r'\[\^(\d+)\](?!:)'  # Negative lookahead to exclude definitions
    inline_refs = set(map(int, re.findall(inline_pattern, content)))

    # Find definitions: [^1]: Source text
    def_pattern = r'^\[\^(\d+)\]:\s*.+$'
    definitions = set(map(int, re.findall(def_pattern, content, re.MULTILINE)))

    return inline_refs, definitions, None


def main():
    all_files = sorted(LIBRARY_ROOT.rglob("*.md"))

    # Exclude templates and WELCOME
    all_files = [
        f for f in all_files
        if not f.name.startswith("_") and f.name != "WELCOME.md"
    ]

    stats = {
        'total': len(all_files),
        'with_inline': 0,
        'with_definitions': 0,
        'complete': 0,  # Has inline refs AND matching definitions
        'orphaned_defs': 0,  # Has definitions but no inline refs
        'missing_defs': 0,  # Has inline refs but missing some definitions
    }

    orphaned_files = []
    missing_files = []

    for filepath in all_files:
        inline_refs, definitions, error = scan_file(filepath)

        if error:
            continue

        has_inline = len(inline_refs) > 0
        has_defs = len(definitions) > 0

        if has_inline:
            stats['with_inline'] += 1
        if has_defs:
            stats['with_definitions'] += 1

        # Check for mismatches
        if has_inline and has_defs and inline_refs == definitions:
            stats['complete'] += 1
        elif has_defs and not has_inline:
            stats['orphaned_defs'] += 1
            orphaned_files.append((filepath, definitions))
        elif has_inline and inline_refs != definitions:
            stats['missing_defs'] += 1
            missing = inline_refs - definitions
            missing_files.append((filepath, missing, inline_refs, definitions))

    # Report
    print("=" * 70)
    print("INLINE FOOTNOTE COVERAGE REPORT")
    print("=" * 70)
    print(f"\nTotal files scanned: {stats['total']}")
    print(f"\nFiles with inline footnotes: {stats['with_inline']} ({stats['with_inline']/stats['total']*100:.1f}%)")
    print(f"Files with definitions: {stats['with_definitions']} ({stats['with_definitions']/stats['total']*100:.1f}%)")
    print(f"Files with complete footnotes: {stats['complete']} ({stats['complete']/stats['total']*100:.1f}%)")
    print(f"\nFiles with orphaned definitions: {stats['orphaned_defs']}")
    print(f"Files with missing definitions: {stats['missing_defs']}")

    if missing_files:
        print(f"\n{'=' * 70}")
        print(f"FILES WITH MISSING DEFINITIONS ({len(missing_files)} files)")
        print("=" * 70)
        for filepath, missing, inline, defs in sorted(missing_files):
            rel_path = filepath.relative_to(LIBRARY_ROOT)
            print(f"\n{rel_path}")
            print(f"  Inline refs: {sorted(inline)}")
            print(f"  Definitions: {sorted(defs)}")
            print(f"  Missing: {sorted(missing)}")

    if orphaned_files:
        print(f"\n{'=' * 70}")
        print(f"FILES WITH ORPHANED DEFINITIONS ({len(orphaned_files)} files)")
        print("=" * 70)
        for filepath, defs in sorted(orphaned_files):
            rel_path = filepath.relative_to(LIBRARY_ROOT)
            print(f"\n{rel_path}")
            print(f"  Orphaned definitions: {sorted(defs)}")


if __name__ == "__main__":
    main()
