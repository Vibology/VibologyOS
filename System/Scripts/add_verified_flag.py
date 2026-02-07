#!/usr/bin/env python3
"""
Add 'verified: true' flag to Astrology files that have source_verified but not verified.
Updates YAML frontmatter, preserving all other fields.
"""

import re
from pathlib import Path

def add_verified_flag(file_path):
    """Add verified: true to YAML if source_verified exists but verified doesn't."""
    content = file_path.read_text()

    # Check if already has verified: true
    if re.search(r'^verified:\s*true', content, re.MULTILINE):
        return False, "Already has verified: true"

    # Check if has source_verified: true
    if not re.search(r'^source_verified:\s*true', content, re.MULTILINE):
        return False, "No source_verified: true"

    # Find the frontmatter
    parts = content.split('---', 2)
    if len(parts) < 3:
        return False, "No valid frontmatter"

    frontmatter = parts[1]
    body = parts[2]

    # Add verified: true after date_updated (or at end if not found)
    lines = frontmatter.strip().split('\n')
    new_lines = []
    verified_added = False

    for line in lines:
        new_lines.append(line)
        if line.startswith('date_updated:') and not verified_added:
            new_lines.append('verified: true')
            verified_added = True

    # If date_updated not found, add before source_verified
    if not verified_added:
        final_lines = []
        for line in new_lines:
            if line.startswith('source_verified:'):
                final_lines.append('verified: true')
            final_lines.append(line)
        new_lines = final_lines

    new_content = '---\n' + '\n'.join(new_lines) + '\n---' + body
    file_path.write_text(new_content)

    return True, "Added verified: true"

def main():
    repo_root = Path(__file__).parent.parent.parent
    astrology_dir = repo_root / "Library/The Seven Pillars of Understanding/Astrology"

    signs_dir = astrology_dir / "Signs"
    houses_dir = astrology_dir / "Houses"

    updated_files = []
    skipped_files = []

    for directory in [signs_dir, houses_dir]:
        if not directory.exists():
            continue

        for file_path in directory.glob("*.md"):
            success, message = add_verified_flag(file_path)
            if success:
                updated_files.append(file_path.name)
                print(f"✓ {file_path.name}: {message}")
            else:
                skipped_files.append(file_path.name)
                print(f"- {file_path.name}: {message}")

    print(f"\nSummary:")
    print(f"  Updated: {len(updated_files)}")
    print(f"  Skipped: {len(skipped_files)}")

if __name__ == "__main__":
    main()
