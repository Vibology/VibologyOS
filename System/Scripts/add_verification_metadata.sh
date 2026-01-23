#!/bin/bash
# Add verification metadata to Incarnation Cross files
# Usage: bash add_verification_metadata.sh

VERIFICATION_DATE="2026-01-23"
GRIMOIRE_SOURCE="Human Design/Incarnation Crosses"
SOURCE_VERIFIED="pre-verified"

# Find all Incarnation Cross markdown files
CROSS_DIR="Library/The Seven Pillars of Understanding/Human Design/Incarnation Crosses"

echo "Adding verification metadata to Incarnation Cross files..."
echo "Target directory: $CROSS_DIR"
echo ""

# Counter
count=0

# Process each file
while IFS= read -r file; do
    # Check if file already has source_verified field
    if grep -q "^source_verified:" "$file"; then
        echo "SKIP (already verified): $file"
        continue
    fi

    # Add verification fields before the closing --- of YAML frontmatter
    # Find the line number of the second --- (closing YAML)
    closing_line=$(awk '/^---$/{n++; if(n==2){print NR; exit}}' "$file")

    if [ -z "$closing_line" ]; then
        echo "ERROR (no YAML frontmatter): $file"
        continue
    fi

    # Insert verification fields before the closing ---
    sed -i "${closing_line}i\\
source_verified: $SOURCE_VERIFIED\\
verification_date: $VERIFICATION_DATE\\
grimoire_source: \"$GRIMOIRE_SOURCE\"" "$file"

    count=$((count + 1))
    echo "UPDATED: $file"

done < <(find "$CROSS_DIR" -name "*.md" -type f | sort)

echo ""
echo "==================================="
echo "Verification metadata added to $count files"
echo "==================================="
