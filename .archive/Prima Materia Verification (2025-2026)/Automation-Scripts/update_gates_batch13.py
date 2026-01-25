#!/usr/bin/env python3
"""
Update Human Design Gates Batch 13 (Gates 45-54) with verification metadata.
"""

from pathlib import Path

GATE_FILES = [
    "Gate 45 - Gathering Together.md",
    "Gate 46 - Pushing Upward.md",
    "Gate 47 - Oppression.md",
    "Gate 48 - The Well.md",
    "Gate 49 - Revolution.md",
    "Gate 50 - The Cauldron.md",
    "Gate 51 - The Arousing.md",
    "Gate 52 - Keeping Still.md",
    "Gate 53 - Development.md",
    "Gate 54 - The Marrying Maiden.md"
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
    print("Updating Human Design Gates Batch 13 (45-54) YAML metadata...\n")
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

if __name__ == "__main__":
    main()
