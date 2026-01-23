#!/bin/bash

# Phase 3: Cohort B Human Design Verification Script
# Adds verification YAML to 33 HD files from 2026-01-08 batch
# Classification: synthesis (Grimoire mechanics + archetypal synthesis)

HD_FILES=(
  "Library/The Seven Pillars of Understanding/Human Design/Centers/Ajna.md"
  "Library/The Seven Pillars of Understanding/Human Design/Centers/G Center.md"
  "Library/The Seven Pillars of Understanding/Human Design/Centers/Head.md"
  "Library/The Seven Pillars of Understanding/Human Design/Centers/Heart.md"
  "Library/The Seven Pillars of Understanding/Human Design/Centers/Root.md"
  "Library/The Seven Pillars of Understanding/Human Design/Centers/Sacral.md"
  "Library/The Seven Pillars of Understanding/Human Design/Centers/Solar Plexus.md"
  "Library/The Seven Pillars of Understanding/Human Design/Centers/Spleen.md"
  "Library/The Seven Pillars of Understanding/Human Design/Centers/Throat.md"
  "Library/The Seven Pillars of Understanding/Human Design/Authority/Ego Authority.md"
  "Library/The Seven Pillars of Understanding/Human Design/Authority/Emotional Authority.md"
  "Library/The Seven Pillars of Understanding/Human Design/Authority/Mental Authority.md"
  "Library/The Seven Pillars of Understanding/Human Design/Authority/Sacral Authority.md"
  "Library/The Seven Pillars of Understanding/Human Design/Authority/Self-Projected Authority.md"
  "Library/The Seven Pillars of Understanding/Human Design/Authority/Splenic Authority.md"
  "Library/The Seven Pillars of Understanding/Human Design/Profiles/1-3 Investigator Martyr.md"
  "Library/The Seven Pillars of Understanding/Human Design/Profiles/1-4 Investigator Opportunist.md"
  "Library/The Seven Pillars of Understanding/Human Design/Profiles/2-4 Hermit Opportunist.md"
  "Library/The Seven Pillars of Understanding/Human Design/Profiles/2-5 Hermit Heretic.md"
  "Library/The Seven Pillars of Understanding/Human Design/Profiles/3-5 Martyr Heretic.md"
  "Library/The Seven Pillars of Understanding/Human Design/Profiles/3-6 Martyr Role Model.md"
  "Library/The Seven Pillars of Understanding/Human Design/Profiles/4-1 Opportunist Investigator.md"
  "Library/The Seven Pillars of Understanding/Human Design/Profiles/4-6 Opportunist Role Model.md"
  "Library/The Seven Pillars of Understanding/Human Design/Profiles/5-1 Heretic Investigator.md"
  "Library/The Seven Pillars of Understanding/Human Design/Profiles/5-2 Heretic Hermit.md"
  "Library/The Seven Pillars of Understanding/Human Design/Profiles/6-2 Role Model Hermit.md"
  "Library/The Seven Pillars of Understanding/Human Design/Profiles/6-3 Role Model Martyr.md"
  "Library/The Seven Pillars of Understanding/Human Design/Types/Generator.md"
  "Library/The Seven Pillars of Understanding/Human Design/Types/Manifestor.md"
  "Library/The Seven Pillars of Understanding/Human Design/Types/Projector.md"
  "Library/The Seven Pillars of Understanding/Human Design/Types/Reflector.md"
  "Library/The Seven Pillars of Understanding/Human Design/Strategy/Strategy.md"
  "Library/The Seven Pillars of Understanding/Human Design/Human Design.md"
)

VERIFICATION_YAML="source_verified: synthesis
verification_date: 2026-01-23
grimoire_source: \"Human Design (The Definitive Book, Complete Guide)\"
verification_notes: \"Core mechanics (gates, centers, profiles, authorities, types, strategy) verified against Grimoire. Synthesis includes archetypal interpretation, Jungian depth, cross-system correspondences.\""

count=0

for file in "${HD_FILES[@]}"; do
  filepath="/home/joe/VibologyOS/$file"

  if [ -f "$filepath" ]; then
    # Check if already verified
    if grep -q "source_verified:" "$filepath"; then
      echo "⚠️  Already verified: $file"
      continue
    fi

    # Check for date_created: 2026-01-08
    if ! grep -q "date_created: 2026-01-08" "$filepath"; then
      echo "⚠️  Wrong creation date: $file"
      continue
    fi

    # Add verification metadata after existing frontmatter
    awk -v yaml="$VERIFICATION_YAML" '
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
  else
    echo "❌ Not found: $file"
  fi
done

echo ""
echo "✅ Verification complete: $count files processed"
