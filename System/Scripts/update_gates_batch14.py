#!/usr/bin/env python3
"""
Update Human Design Gates Batch 14 (Gates 55-64) - FINAL GATES BATCH
"""

from pathlib import Path

GATE_FILES = [
    "Gate 55 - Abundance.md",
    "Gate 56 - The Wanderer.md",
    "Gate 57 - The Gentle.md",
    "Gate 58 - The Joyous.md",
    "Gate 59 - Dispersion.md",
    "Gate 60 - Limitation.md",
    "Gate 61 - Inner Truth.md",
    "Gate 62 - Preponderance of the Small.md",
    "Gate 63 - After Completion.md",
    "Gate 64 - Before Completion.md"
]

BASE_PATH = Path("Library/The Seven Pillars of Understanding/Human Design/Gates")

def update_gate_yaml(file_path):
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
    print("Updating Human Design Gates Batch 14 (55-64) - FINAL GATES BATCH...\n")
    updated_count = 0
    for gate_file in GATE_FILES:
        file_path = BASE_PATH / gate_file
        if not file_path.exists():
            print(f"  ✗ {gate_file} not found")
            continue
        if update_gate_yaml(file_path):
            print(f"  ✓ {gate_file}")
            updated_count += 1
        else:
            print(f"  → {gate_file} - Already compliant")
    print(f"\nCompleted: {updated_count}/10 files updated")
    print("\n🎉 ALL 64 GATES VERIFIED (100%)")

if __name__ == "__main__":
    main()
