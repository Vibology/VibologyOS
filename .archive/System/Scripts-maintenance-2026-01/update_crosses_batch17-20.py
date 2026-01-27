#!/usr/bin/env python3
"""Process Incarnation Crosses Batches 17-20 (files 41-120) efficiently."""
from pathlib import Path
import subprocess

def get_all_cross_files():
    result = subprocess.run(
        ['find', '.', '-path', '*/Incarnation Crosses/*/*.md', '-type', 'f'],
        capture_output=True, text=True, cwd='.'
    )
    return sorted(result.stdout.strip().split('\n'))

def update_yaml(file_path):
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

def process_batch(batch_num, start, end, files):
    print(f"\n=== Batch {batch_num} (files {start+1}-{end}) ===")
    updated = 0
    for file_str in files[start:end]:
        path = Path(file_str)
        if path.exists() and update_yaml(path):
            print(f"  ✓ {path.name}")
            updated += 1
    print(f"Completed: {updated}/{end-start} files")
    return updated

files = get_all_cross_files()
total = 0
total += process_batch(17, 40, 60, files)
total += process_batch(18, 60, 80, files)
total += process_batch(19, 80, 100, files)
total += process_batch(20, 100, 120, files)
print(f"\n✅ Total updated: {total}/80 files (Batches 17-20)")
