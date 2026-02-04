#!/usr/bin/env python3
"""
Parse exaltation/detriment data by mapping glyphs to planets.
"""
import re
import json
from pypdf import PdfReader
from collections import defaultdict

# Extract text
reader = PdfReader("Hexagram Line Descriptions.pdf")
full_text = ""
for page in reader.pages:
    full_text += page.extract_text() + "\n"

# Step 1: Build glyph mapping by finding cases where planet names ARE mentioned
# Pattern: [glyph characters] [planet name] exalted/detriment

PLANETS = ['Sun', 'Moon', 'Earth', 'Mercury', 'Venus', 'Mars',
           'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'North Node', 'South Node', 'Pluto']

glyph_to_planet = {}

# Find patterns like "Mars exalted" or "The Earth in detriment" and capture preceding glyphs
lines = full_text.split('\n')
for i, line in enumerate(lines):
    for planet in PLANETS:
        # Match: [some characters] The? Planet exalted/detriment
        pattern = rf'([^\w\s]{{1,5}})\s*(?:\.{{2,4}})?\s*(?:The\s+)?{planet}\s+(?:exalted|in detriment)'
        matches = re.finditer(pattern, line, re.IGNORECASE)
        for match in matches:
            glyph = match.group(1).strip()
            if glyph and len(glyph) <= 5:
                if glyph not in glyph_to_planet or glyph_to_planet[glyph] == planet:
                    glyph_to_planet[glyph] = planet

print("Glyph mappings discovered:")
for glyph, planet in sorted(glyph_to_planet.items(), key=lambda x: x[1]):
    print(f"  '{glyph}' -> {planet}")

# Now parse the full data using both explicit mentions AND glyph mappings
def parse_hexagram_data(text):
    data = {}

    # Split by gates
    gate_sections = re.split(r'GATE (\d+):', text)

    for i in range(1, len(gate_sections), 2):
        gate_num = gate_sections[i].strip()
        gate_content = gate_sections[i + 1] if i + 1 < len(gate_sections) else ""

        data[gate_num] = {}

        # Split by lines
        line_sections = re.split(r'Line (\d)\s*-', gate_content)

        for j in range(1, len(line_sections), 2):
            line_num = line_sections[j].strip()
            line_content = line_sections[j + 1] if j + 1 < len(line_sections) else ""

            line_data = {
                "exaltation_planets": [],
                "detriment_planets": [],
                "juxtaposition_planets": [],
                "no_polarity": False
            }

            # Check for no polarity
            if re.search(r'no (specific )?polarity|no specific planetary accent', line_content, re.IGNORECASE):
                line_data["no_polarity"] = True
                data[gate_num][line_num] = line_data
                continue

            # Method 1: Explicit planet names
            for planet in PLANETS:
                if re.search(rf'\b(the\s+)?{planet}\s+exalted\b', line_content, re.IGNORECASE):
                    if planet not in line_data["exaltation_planets"]:
                        line_data["exaltation_planets"].append(planet)

                if re.search(rf'\b(the\s+)?{planet}\s+(in\s+)?detriment\b', line_content, re.IGNORECASE):
                    if planet not in line_data["detriment_planets"]:
                        line_data["detriment_planets"].append(planet)

            # Method 2: Look for glyph patterns
            # Exaltation patterns: glyph followed by dots or triangle-up indicators
            for glyph, planet in glyph_to_planet.items():
                # Look for glyph + exaltation indicators
                if re.search(rf'{re.escape(glyph)}\s*[\.{{2,4}}|▲|.A.]', line_content):
                    if planet not in line_data["exaltation_planets"]:
                        line_data["exaltation_planets"].append(planet)

                # Look for glyph + detriment indicators
                if re.search(rf'{re.escape(glyph)}\s*[▼|V|\\l]', line_content):
                    if planet not in line_data["detriment_planets"]:
                        line_data["detriment_planets"].append(planet)

            data[gate_num][line_num] = line_data

    return data

# Parse the data
print("\nParsing hexagram data...")
data = parse_hexagram_data(full_text)

# Save to JSON
with open('exaltations_detriments_final.json', 'w') as f:
    json.dump(data, f, indent=2)

# Statistics
total_gates = len(data)
total_lines = sum(len(gate) for gate in data.values())
exalt_count = sum(1 for gate in data.values() for line in gate.values() if line['exaltation_planets'])
detri_count = sum(1 for gate in data.values() for line in gate.values() if line['detriment_planets'])
both_count = sum(1 for gate in data.values() for line in gate.values()
                 if line['exaltation_planets'] and line['detriment_planets'])
no_pol_count = sum(1 for gate in data.values() for line in gate.values() if line['no_polarity'])
none_count = sum(1 for gate in data.values() for line in gate.values()
                 if not line['exaltation_planets'] and not line['detriment_planets'] and not line['no_polarity'])

print(f"\nStatistics:")
print(f"Total gates: {total_gates}")
print(f"Total lines: {total_lines}")
print(f"Lines with exaltation: {exalt_count}")
print(f"Lines with detriment: {detri_count}")
print(f"Lines with both: {both_count}")
print(f"Lines with no polarity: {no_pol_count}")
print(f"Lines with no fixing: {none_count}")
print(f"\nSaved to: exaltations_detriments_final.json")
