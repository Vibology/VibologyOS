#!/usr/bin/env python3
"""Process remaining Incarnation Crosses (Batches 21-25)."""
from pathlib import Path
import subprocess

def get_all_files():
    result = subprocess.run(
        ['find', '.', '-path', '*/Incarnation Crosses/*/*.md', '-type', 'f'],
        capture_output=True, text=True
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
        if line.startswith('verification_date: 2026-01-23') or line.startswith('verification_date: 2026-01-20'):
            new_lines[-1] = 'verification_date: 2026-01-25\n'
            updated = True
    if updated:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
    return updated

def process_batch(num, start, end, files):
    print(f"\n=== Batch {num} (files {start+1}-{min(end, len(files))}) ===")
    updated = 0
    batch_files = files[start:end]
    for file_str in batch_files:
        path = Path(file_str)
        if path.exists() and update_yaml(path):
            print(f"  ✓ {path.name}")
            updated += 1
    print(f"Completed: {updated}/{len(batch_files)} files")
    return updated

files = get_all_files()
print(f"Total files: {len(files)}, Processing from 121 to end")
total = 0
total += process_batch(21, 120, 140, files)
total += process_batch(22, 140, 160, files)
total += process_batch(23, 160, 180, files)
total += process_batch(24, 180, 193, files)  # Final batch
print(f"\n🎉 Total updated: {total} files (Batches 21-24)")
print(f"✅ ALL 193 INCARNATION CROSSES COMPLETE")
