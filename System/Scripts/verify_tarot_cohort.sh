#!/bin/bash

# Phase 3: Cohort B Tarot Verification Script
# Adds verification YAML to 23 Tarot files from 2026-01-08 batch
# Classification: synthesis (Grimoire Qabalah + divinatory synthesis)

TAROT_FILES=(
  "Library/The Seven Pillars of Understanding/The Tarot/Major Arcana/0 - The Fool.md"
  "Library/The Seven Pillars of Understanding/The Tarot/Major Arcana/1 - The Magician.md"
  "Library/The Seven Pillars of Understanding/The Tarot/Major Arcana/2 - The High Priestess.md"
  "Library/The Seven Pillars of Understanding/The Tarot/Major Arcana/3 - The Empress.md"
  "Library/The Seven Pillars of Understanding/The Tarot/Major Arcana/4 - The Emperor.md"
  "Library/The Seven Pillars of Understanding/The Tarot/Major Arcana/5 - The Hierophant.md"
  "Library/The Seven Pillars of Understanding/The Tarot/Major Arcana/6 - The Lovers.md"
  "Library/The Seven Pillars of Understanding/The Tarot/Major Arcana/7 - The Chariot.md"
  "Library/The Seven Pillars of Understanding/The Tarot/Major Arcana/8 - Strength.md"
  "Library/The Seven Pillars of Understanding/The Tarot/Major Arcana/9 - The Hermit.md"
  "Library/The Seven Pillars of Understanding/The Tarot/Major Arcana/10 - Wheel of Fortune.md"
  "Library/The Seven Pillars of Understanding/The Tarot/Major Arcana/11 - Justice.md"
  "Library/The Seven Pillars of Understanding/The Tarot/Major Arcana/12 - The Hanged Man.md"
  "Library/The Seven Pillars of Understanding/The Tarot/Major Arcana/13 - Death.md"
  "Library/The Seven Pillars of Understanding/The Tarot/Major Arcana/14 - Temperance.md"
  "Library/The Seven Pillars of Understanding/The Tarot/Major Arcana/15 - The Devil.md"
  "Library/The Seven Pillars of Understanding/The Tarot/Major Arcana/16 - The Tower.md"
  "Library/The Seven Pillars of Understanding/The Tarot/Major Arcana/17 - The Star.md"
  "Library/The Seven Pillars of Understanding/The Tarot/Major Arcana/18 - The Moon.md"
  "Library/The Seven Pillars of Understanding/The Tarot/Major Arcana/19 - The Sun.md"
  "Library/The Seven Pillars of Understanding/The Tarot/Major Arcana/20 - Judgement.md"
  "Library/The Seven Pillars of Understanding/The Tarot/Major Arcana/21 - The World.md"
  "Library/The Seven Pillars of Understanding/The Tarot/The Tarot.md"
)

VERIFICATION_YAML="source_verified: synthesis
verification_date: 2026-01-23
grimoire_source: \"Tarot (Qabalistic Tarot, Pictorial Key, Golden Dawn)\"
verification_notes: \"Core Qabalistic correspondences (Hebrew letters, paths, zodiacal/planetary attributions) verified against Grimoire. Synthesis includes RWS and Thoth divinatory meanings, alchemical stages, Jungian archetypal interpretation.\""

count=0

for file in "${TAROT_FILES[@]}"; do
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
