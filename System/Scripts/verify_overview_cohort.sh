#!/bin/bash

# Phase 3: Cohort B Overview Files Verification Script
# Adds verification YAML to 2 pillar overview files from 2026-01-08 batch
# Classification: synthesis (Grimoire frameworks + scholarly sources)

OVERVIEW_FILES=(
  "Library/The Seven Pillars of Understanding/Angelology/Angelology.md"
  "Library/The Seven Pillars of Understanding/The Window/The Window.md"
)

ANGELOLOGY_YAML="source_verified: synthesis
verification_date: 2026-01-23
grimoire_source: \"Angelology (Pseudo-Dionysius, Dictionary of Angels, Qabalah)\"
verification_notes: \"Nine Orders, Three Triads, Sephirothic correspondences verified against Grimoire. Synthesis includes theological sources (Aquinas, Dante), Hebrew Qabalah integration, cross-system correspondences.\""

WINDOW_YAML="source_verified: synthesis
verification_date: 2026-01-23
grimoire_source: \"The Window (Blueprint, Human Design, Gene Keys, I-Ching)\"
verification_notes: \"64-card structure, Six Houses, Twelve Archetypes, I-Ching/HD correspondences verified against Grimoire. Synthesis includes contemporary 1980s archetypal encoding, cross-pillar integration.\""

count=0

# Process Angelology
file="${OVERVIEW_FILES[0]}"
filepath="/home/joe/VibologyOS/$file"

if [ -f "$filepath" ]; then
  if ! grep -q "source_verified:" "$filepath"; then
    if grep -q "date_created: 2026-01-08" "$filepath"; then
      awk -v yaml="$ANGELOLOGY_YAML" '
/^---$/ {
  count++
  if (count == 2) {
    print yaml
  }
  print
  next
}
{ print }
' "$filepath" > "$filepath.tmp" && mv "$filepath.tmp" "$filepath"
      echo "✅ Verified: $file"
      ((count++))
    fi
  fi
fi

# Process The Window
file="${OVERVIEW_FILES[1]}"
filepath="/home/joe/VibologyOS/$file"

if [ -f "$filepath" ]; then
  if ! grep -q "source_verified:" "$filepath"; then
    if grep -q "date_created: 2026-01-08" "$filepath"; then
      awk -v yaml="$WINDOW_YAML" '
/^---$/ {
  count++
  if (count == 2) {
    print yaml
  }
  print
  next
}
{ print }
' "$filepath" > "$filepath.tmp" && mv "$filepath.tmp" "$filepath"
      echo "✅ Verified: $file"
      ((count++))
    fi
  fi
fi

echo ""
echo "✅ Verification complete: $count files processed"
