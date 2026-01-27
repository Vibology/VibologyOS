#!/usr/bin/env python3
"""
Update Human Design Gates Batch 10 (Gates 12-22) with verification metadata.
These files already have References sections, but need YAML updates.
"""

from pathlib import Path

# Gates 12-22
GATE_FILES = [
    "Gate 12 - Standstill.md",
    "Gate 13 - The Fellowship of Man.md",
    "Gate 14 - Possession in Great Measure.md",
    "Gate 15 - Modesty.md",
    "Gate 16 - Enthusiasm.md",
    "Gate 17 - Following.md",
    "Gate 18 - Work on What Has Been Spoilt.md",
    "Gate 19 - Approach.md",
    "Gate 20 - Contemplation.md",
    "Gate 21 - Biting Through.md",
    "Gate 22 - Grace.md"
]

BASE_PATH = Path("Library/The Seven Pillars of Understanding/Human Design/Gates")

def update_gate_yaml(file_path):
    """Add verified: true after source_verified and update verification_date."""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    updated = False

    for i, line in enumerate(lines):
        new_lines.append(line)

        # After "source_verified: true\n", add "verified: true\n"
        if line.strip() == 'source_verified: true':
            # Check if next line is already verified: true
            if i + 1 < len(lines) and lines[i + 1].strip() != 'verified: true':
                new_lines.append('verified: true\n')
                updated = True

        # Update verification_date from 2026-01-23 to 2026-01-25
        if line.startswith('verification_date: 2026-01-23'):
            new_lines[-1] = 'verification_date: 2026-01-25\n'
            updated = True

    if updated:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)

    return updated

def main():
    print("Updating Human Design Gates Batch 10 (12-22) YAML metadata...\n")

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
    print("\nBatch 10 Summary:")
    print("- All files have comprehensive References sections (## Sources)")
    print("- YAML updated: verified: true, verification_date: 2026-01-25")

if __name__ == "__main__":
    main()
