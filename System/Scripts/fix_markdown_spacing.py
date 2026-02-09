#!/usr/bin/env python3
"""Fix markdown spacing issues across the VibologyOS Library.

Ensures blank lines exist around horizontal rules (---) and after
frontmatter, so that standard markdown renderers display proper spacing.

Rules applied:
1. Blank line after frontmatter closing ---
2. Blank line before --- horizontal rules (not frontmatter)
3. Blank line after --- horizontal rules
4. Collapse 3+ consecutive blank lines to 2
"""

import os
import sys
from pathlib import Path


def is_hr_line(line: str) -> bool:
    """Check if a line is a horizontal rule (---, ***, ___)."""
    stripped = line.strip()
    if len(stripped) < 3:
        return False
    return (
        all(c == '-' for c in stripped) or
        all(c == '*' for c in stripped) or
        all(c == '_' for c in stripped)
    )


def fix_spacing(content: str) -> str:
    lines = content.split('\n')
    if not lines:
        return content

    result = []
    in_frontmatter = False
    frontmatter_closed = False
    in_code_block = False
    i = 0

    # Detect frontmatter
    has_frontmatter = lines[0].strip() == '---'

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Track code blocks (don't modify inside them)
        if stripped.startswith('```'):
            in_code_block = not in_code_block
            result.append(line)
            i += 1
            continue

        if in_code_block:
            result.append(line)
            i += 1
            continue

        # Track frontmatter
        if i == 0 and has_frontmatter:
            in_frontmatter = True
            result.append(line)
            i += 1
            continue

        if in_frontmatter and stripped == '---':
            in_frontmatter = False
            frontmatter_closed = True
            result.append(line)
            # Ensure blank line after frontmatter
            if i + 1 < len(lines) and lines[i + 1].strip() != '':
                result.append('')
            i += 1
            continue

        if in_frontmatter:
            result.append(line)
            i += 1
            continue

        # Handle horizontal rules
        if is_hr_line(stripped) and frontmatter_closed:
            # Ensure blank line before HR (if previous line isn't blank/start)
            if result and result[-1].strip() != '':
                result.append('')
            result.append(line)
            # Ensure blank line after HR
            if i + 1 < len(lines) and lines[i + 1].strip() != '':
                result.append('')
            i += 1
            continue

        # Handle headings - ensure blank line before heading
        if stripped.startswith('#') and not stripped.startswith('#!'):
            if result and result[-1].strip() != '':
                result.append('')
            result.append(line)
            i += 1
            continue

        result.append(line)
        i += 1

    # Collapse 3+ consecutive blank lines to 2
    collapsed = []
    blank_count = 0
    for line in result:
        if line.strip() == '':
            blank_count += 1
            if blank_count <= 2:
                collapsed.append(line)
        else:
            blank_count = 0
            collapsed.append(line)

    return '\n'.join(collapsed)


def process_library(library_path: str, dry_run: bool = False):
    library = Path(library_path)
    if not library.exists():
        print(f"Library not found: {library_path}")
        sys.exit(1)

    modified_count = 0
    total_count = 0
    skip_dirs = {'Fonts', '.DS_Store', 'The Window'}

    for md_file in sorted(library.rglob('*.md')):
        # Skip excluded directories
        if any(part in skip_dirs for part in md_file.parts):
            continue

        total_count += 1
        original = md_file.read_text(encoding='utf-8')
        fixed = fix_spacing(original)

        if fixed != original:
            modified_count += 1
            rel_path = md_file.relative_to(library)
            if dry_run:
                print(f"  WOULD FIX: {rel_path}")
            else:
                md_file.write_text(fixed, encoding='utf-8')
                print(f"  Fixed: {rel_path}")

    print(f"\n{'Would modify' if dry_run else 'Modified'}: {modified_count}/{total_count} files")


if __name__ == '__main__':
    library_path = os.path.expanduser('~/VibologyOS/Library')
    dry_run = '--dry-run' in sys.argv
    if dry_run:
        print("DRY RUN — no files will be modified\n")
    process_library(library_path, dry_run=dry_run)
