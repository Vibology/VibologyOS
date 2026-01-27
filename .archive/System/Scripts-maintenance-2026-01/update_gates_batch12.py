#!/usr/bin/env python3
"""
Update Human Design Gates Batch 12 (Gates 34-44) with verification metadata.
"""

from pathlib import Path

GATE_FILES = [
    "Gate 34 - The Power of the Great.md",
    "Gate 35 - Progress.md",
    "Gate 36 - Darkening of the Light.md",
    "Gate 37 - The Family.md",
    "Gate 38 - Opposition.md",
    "Gate 39 - Obstruction.md",
    "Gate 40 - Deliverance.md",
    "Gate 41 - Decrease.md",
    "Gate 42 - Increase.md",
    "Gate 43 - Breakthrough.md",
    "Gate 44 - Coming to Meet.md"
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
    print("Updating Human Design Gates Batch 12 (34-44) YAML metadata...\n")
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
    print(f"\nCompleted: {updated_count}/11 files updated")

if __name__ == "__main__":
    main()
