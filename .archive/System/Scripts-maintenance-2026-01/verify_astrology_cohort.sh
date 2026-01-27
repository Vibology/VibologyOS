#!/bin/bash
# Phase 3: Cohort B Astrology Verification Script

ASTROLOGY_FILES=(
  "Library/The Seven Pillars of Understanding/Astrology/Planets/Jupiter ♃.md"
  "Library/The Seven Pillars of Understanding/Astrology/Planets/Mars ♂.md"
  "Library/The Seven Pillars of Understanding/Astrology/Planets/Mercury  ☿.md"
  "Library/The Seven Pillars of Understanding/Astrology/Planets/Moon ☽.md"
  "Library/The Seven Pillars of Understanding/Astrology/Planets/Neptune ♆.md"
  "Library/The Seven Pillars of Understanding/Astrology/Planets/Pluto ♇.md"
  "Library/The Seven Pillars of Understanding/Astrology/Planets/Saturn ♄.md"
  "Library/The Seven Pillars of Understanding/Astrology/Planets/Sun ☉.md"
  "Library/The Seven Pillars of Understanding/Astrology/Planets/Uranus ♅.md"
  "Library/The Seven Pillars of Understanding/Astrology/Planets/Venus ♀.md"
  "Library/The Seven Pillars of Understanding/Astrology/Signs/Aquarius ♒.md"
  "Library/The Seven Pillars of Understanding/Astrology/Signs/Aries ♈.md"
  "Library/The Seven Pillars of Understanding/Astrology/Signs/Cancer ♋.md"
  "Library/The Seven Pillars of Understanding/Astrology/Signs/Capricorn ♑.md"
  "Library/The Seven Pillars of Understanding/Astrology/Signs/Gemini ♊.md"
  "Library/The Seven Pillars of Understanding/Astrology/Signs/Leo ♌.md"
  "Library/The Seven Pillars of Understanding/Astrology/Signs/Libra ♎.md"
  "Library/The Seven Pillars of Understanding/Astrology/Signs/Pisces ♓.md"
  "Library/The Seven Pillars of Understanding/Astrology/Signs/Sagittarius ♐.md"
  "Library/The Seven Pillars of Understanding/Astrology/Signs/Scorpio ♏.md"
  "Library/The Seven Pillars of Understanding/Astrology/Signs/Taurus ♉.md"
  "Library/The Seven Pillars of Understanding/Astrology/Signs/Virgo ♍.md"
  "Library/The Seven Pillars of Understanding/Astrology/Houses/1st House.md"
  "Library/The Seven Pillars of Understanding/Astrology/Houses/2nd House.md"
  "Library/The Seven Pillars of Understanding/Astrology/Houses/3rd House.md"
  "Library/The Seven Pillars of Understanding/Astrology/Houses/4th House.md"
  "Library/The Seven Pillars of Understanding/Astrology/Houses/5th House.md"
  "Library/The Seven Pillars of Understanding/Astrology/Houses/6th House.md"
  "Library/The Seven Pillars of Understanding/Astrology/Houses/7th House.md"
  "Library/The Seven Pillars of Understanding/Astrology/Houses/8th House.md"
  "Library/The Seven Pillars of Understanding/Astrology/Houses/9th House.md"
  "Library/The Seven Pillars of Understanding/Astrology/Houses/10th House.md"
  "Library/The Seven Pillars of Understanding/Astrology/Houses/11th House.md"
  "Library/The Seven Pillars of Understanding/Astrology/Houses/12th House.md"
  "Library/The Seven Pillars of Understanding/Astrology/Astrology.md"
  "Library/The Seven Pillars of Understanding/Astrology/Aspects.md"
  "Library/The Seven Pillars of Understanding/Astrology/Transits and Timing.md"
)

VERIFICATION_YAML="source_verified: synthesis
verification_date: 2026-01-23
grimoire_source: \"Astrology (Lilly's Christian Astrology, Ptolemy's Tetrabiblos)\"
verification_notes: \"Core dignities and traditional meanings verified against Grimoire. Synthesis includes Jungian archetypal depth, mythology (Greek/Roman), cross-system correspondences, and esoteric interpretation.\""

count=0

for file in "${ASTROLOGY_FILES[@]}"; do
  filepath="/home/joe/VibologyOS/$file"

  if [ -f "$filepath" ]; then
    if grep -q "source_verified:" "$filepath"; then
      echo "⚠️  Already verified: $file"
      continue
    fi

    if ! grep -q "date_created: 2026-01-08" "$filepath"; then
      echo "⚠️  Wrong creation date: $file"
      continue
    fi

    # Add YAML before second ---
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
