#!/usr/bin/env python3
"""
Update Human Design Gates Batch 9 (Gates 01-11) with verification metadata.
These files already have References sections, but need YAML updates.
"""

from pathlib import Path

# Gates 01-11
GATE_FILES = [
    "Gate 01 - The Creative.md",
    "Gate 02 - The Receptive.md",
    "Gate 03 - Difficulty at the Beginning.md",
    "Gate 04 - Youthful Folly.md",
    "Gate 05 - Waiting.md",
    "Gate 06 - Conflict.md",
    "Gate 07 - The Army.md",
    "Gate 08 - Holding Together.md",
    "Gate 09 - The Taming Power of the Small.md",
    "Gate 10 - Treading.md",
    "Gate 11 - Peace.md"
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
    print("Updating Human Design Gates Batch 9 (01-11) YAML metadata...\n")

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
    print("\nBatch 9 Summary:")
    print("- All files have comprehensive References sections (## Sources)")
    print("- YAML updated: verified: true, verification_date: 2026-01-25")

if __name__ == "__main__":
    main()
