#!/usr/bin/env python3
"""
scan_dead_links.py — Find dead wikilinks in Library/ and Synthesis/

Extracts all [[Target]], [[Target|alias]], [[Target#heading]] links,
resolves them against actual .md files in the vault, and reports dead links.

Usage:
    python3 System/Scripts/scan_dead_links.py              # summary + dead links
    python3 System/Scripts/scan_dead_links.py --by-target   # group by dead target
    python3 System/Scripts/scan_dead_links.py --by-file     # group by source file
"""

import argparse
import os
import re
from collections import defaultdict
from pathlib import Path

WIKILINK_RE = re.compile(r'\[\[([^\]]+?)\]\]')


def build_file_index(vault_root: Path) -> set[str]:
    """Build a set of all note titles (filenames without .md extension)."""
    titles = set()
    for md_file in vault_root.rglob("*.md"):
        titles.add(md_file.stem)
    return titles


def extract_links(filepath: Path) -> list[tuple[int, str, str]]:
    """
    Extract wikilinks from a file.
    Returns list of (line_number, raw_match, resolved_target).
    """
    links = []
    try:
        content = filepath.read_text(encoding="utf-8")
    except (UnicodeDecodeError, PermissionError):
        return links

    for i, line in enumerate(content.splitlines(), 1):
        # Skip YAML frontmatter
        if i == 1 and line.strip() == "---":
            continue

        for match in WIKILINK_RE.finditer(line):
            raw = match.group(1)
            # Extract target: strip |alias and #heading
            # Handle \| first (Obsidian's escaped pipe in markdown tables)
            target = raw.split("\\|")[0].split("|")[0].split("#")[0].strip()
            if target:
                links.append((i, raw, target))

    return links


def main():
    parser = argparse.ArgumentParser(description="Scan for dead wikilinks")
    parser.add_argument("--by-target", action="store_true",
                        help="Group results by dead target")
    parser.add_argument("--by-file", action="store_true",
                        help="Group results by source file")
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    vault_root = script_dir.parent.parent

    scan_dirs = [vault_root / "Library", vault_root / "Synthesis"]

    # Build index of all existing note titles
    file_index = build_file_index(vault_root)

    # Collect all .md files to scan
    md_files = []
    for scan_dir in scan_dirs:
        if scan_dir.exists():
            md_files.extend(sorted(scan_dir.rglob("*.md")))

    total_links = 0
    total_dead = 0
    dead_by_target = defaultdict(list)  # target -> [(file, line, raw)]
    dead_by_file = defaultdict(list)    # file -> [(line, target, raw)]

    for filepath in md_files:
        links = extract_links(filepath)
        total_links += len(links)
        rel = filepath.relative_to(vault_root)

        for line_no, raw, target in links:
            if target not in file_index:
                total_dead += 1
                dead_by_target[target].append((str(rel), line_no, raw))
                dead_by_file[str(rel)].append((line_no, target, raw))

    # Output
    print(f"Scanned {len(md_files)} files, found {total_links} wikilinks, {total_dead} dead")
    print(f"Unique dead targets: {len(dead_by_target)}")
    print()

    if args.by_target:
        print("=" * 70)
        print("DEAD LINKS BY TARGET (sorted by occurrence count)")
        print("=" * 70)
        for target, occurrences in sorted(dead_by_target.items(),
                                           key=lambda x: -len(x[1])):
            print(f"\n[[{target}]] ({len(occurrences)} occurrences)")
            for filepath, line_no, raw in occurrences:
                print(f"  {filepath}:{line_no}")

    elif args.by_file:
        print("=" * 70)
        print("DEAD LINKS BY FILE")
        print("=" * 70)
        for filepath, dead_links in sorted(dead_by_file.items()):
            print(f"\n{filepath} ({len(dead_links)} dead links)")
            for line_no, target, raw in sorted(dead_links):
                print(f"  :{line_no}  [[{target}]]")

    else:
        # Default: summary table of dead targets sorted by count
        print("=" * 70)
        print(f"{'Dead Target':<55} {'Count':>5}")
        print("-" * 70)
        for target, occurrences in sorted(dead_by_target.items(),
                                           key=lambda x: (-len(x[1]), x[0])):
            display = target if len(target) <= 53 else target[:50] + "..."
            pad = max(0, 49 - len(display))
            print(f"  [[{display}]]{' ' * pad} {len(occurrences):>5}")
        print("-" * 70)
        print(f"  {'TOTAL':<53} {total_dead:>5}")


if __name__ == "__main__":
    main()
