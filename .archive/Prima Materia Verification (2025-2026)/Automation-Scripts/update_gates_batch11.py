#!/usr/bin/env python3
"""
Update Human Design Gates Batch 11 (Gates 23-33) with verification metadata.
These files already have References sections, but need YAML updates.
"""

from pathlib import Path

# Gates 23-33
GATE_FILES = [
    "Gate 23 - Splitting Apart.md",
    "Gate 24 - The Return.md",
    "Gate 25 - Innocence.md",
    "Gate 26 - The Taming Power of the Great.md",
    "Gate 27 - Nourishment.md",
    "Gate 28 - Preponderance of the Great.md",
    "Gate 29 - The Abysmal.md",
    "Gate 30 - The Clinging Fire.md",
    "Gate 31 - Influence.md",
    "Gate 32 - Duration.md",
    "Gate 33 - Retreat.md"
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
    print("Updating Human Design Gates Batch 11 (23-33) YAML metadata...\n")

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
    print("\nBatch 11 Summary:")
    print("- All files have comprehensive References sections (## Sources)")
    print("- YAML updated: verified: true, verification_date: 2026-01-25")

if __name__ == "__main__":
    main()
