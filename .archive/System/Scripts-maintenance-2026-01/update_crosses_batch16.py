#!/usr/bin/env python3
"""
Update Human Design Incarnation Crosses Batch 16 (files 21-40) with verification metadata.
"""

from pathlib import Path
import subprocess

def get_cross_files():
    """Get files 21-40 sorted alphabetically."""
    result = subprocess.run(
        ['find', '.', '-path', '*/Incarnation Crosses/*/*.md', '-type', 'f'],
        capture_output=True, text=True, cwd='.'
    )
    files = sorted(result.stdout.strip().split('\n'))
    return files[20:40]

def update_cross_yaml(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    new_lines = []
    updated = False
    for i, line in enumerate(lines):
        new_lines.append(line)
        if line.strip() == 'source_verified: true':
            if i + 1 < len(lines) and lines[i + 1].strip() != 'verified: true':
                new_lines.append('verified: true\n')
                updated = True
        if line.startswith('verification_date: 2026-01-23'):
            new_lines[-1] = 'verification_date: 2026-01-25\n'
            updated = True
    if updated:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
    return updated

def main():
    print("Updating Incarnation Crosses Batch 16 (files 21-40)...\n")
    cross_files = get_cross_files()
    updated_count = 0
    for file_path_str in cross_files:
        file_path = Path(file_path_str)
        if not file_path.exists():
            continue
        if update_cross_yaml(file_path):
            print(f"  ✓ {file_path.name}")
            updated_count += 1
    print(f"\nCompleted: {updated_count}/20 files updated")

if __name__ == "__main__":
    main()
