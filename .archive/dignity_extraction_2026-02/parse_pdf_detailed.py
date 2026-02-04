#!/usr/bin/env python3
"""
Parse PDF directly with better character encoding for planet glyphs.
"""
import re
import json
from pypdf import PdfReader

# Planet names
PLANETS = ['Sun', 'Moon', 'Earth', 'Mercury', 'Venus', 'Mars',
           'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'North Node', 'South Node']

def extract_pdf_text(pdf_path):
    """Extract text from PDF with better encoding."""
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def parse_line_entry(line_content):
    """Parse a single line entry to extract planet dignities."""
    data = {
        "exaltation_planets": [],
        "detriment_planets": [],
        "juxtaposition_planets": [],
        "no_polarity": False
    }

    # Check for no polarity
    if re.search(r'no (specific )?polarity|no specific planetary accent', line_content, re.IGNORECASE):
        data["no_polarity"] = True
        return data

    # Split into sentences/phrases
    sentences = re.split(r'[.!?]\s+', line_content)

    for sentence in sentences:
        # Look for explicit "Planet exalted" pattern
        for planet in PLANETS:
            if re.search(rf'\b(the\s+)?{planet}\s+exalted\b', sentence, re.IGNORECASE):
                if planet not in data["exaltation_planets"]:
                    data["exaltation_planets"].append(planet)

            # Look for "Planet in detriment" pattern
            if re.search(rf'\b(the\s+)?{planet}\s+(in\s+)?detriment\b', sentence, re.IGNORECASE):
                if planet not in data["detriment_planets"]:
                    data["detriment_planets"].append(planet)

    return data

def parse_hexagram_data(text):
    """Parse all hexagram lines from text."""
    data = {}

    # Split by gates
    gate_sections = re.split(r'GATE (\d+):', text)

    # Process each gate
    for i in range(1, len(gate_sections), 2):
        gate_num = gate_sections[i].strip()
        gate_content = gate_sections[i + 1] if i + 1 < len(gate_sections) else ""

        data[gate_num] = {}

        # Split by lines (Line 1 through Line 6)
        line_sections = re.split(r'Line (\d)\s*-', gate_content)

        # Process each line
        for j in range(1, len(line_sections), 2):
            line_num = line_sections[j].strip()
            line_content = line_sections[j + 1] if j + 1 < len(line_sections) else ""

            # Parse this line
            data[gate_num][line_num] = parse_line_entry(line_content)

    return data

def main():
    print("Extracting text from PDF...")
    text = extract_pdf_text("Hexagram Line Descriptions.pdf")

    print("Parsing hexagram data...")
    data = parse_hexagram_data(text)

    # Save to JSON
    with open('exaltations_detriments_v2.json', 'w') as f:
        json.dump(data, f, indent=2)

    # Statistics
    total_lines = sum(len(gate) for gate in data.values())
    exalt_count = sum(1 for gate in data.values() for line in gate.values() if line['exaltation_planets'])
    detri_count = sum(1 for gate in data.values() for line in gate.values() if line['detriment_planets'])
    both_count = sum(1 for gate in data.values() for line in gate.values()
                     if line['exaltation_planets'] and line['detriment_planets'])
    no_pol_count = sum(1 for gate in data.values() for line in gate.values() if line['no_polarity'])

    print(f"\nStatistics:")
    print(f"Total gates: {len(data)}")
    print(f"Total lines: {total_lines}")
    print(f"Lines with exaltation: {exalt_count}")
    print(f"Lines with detriment: {detri_count}")
    print(f"Lines with both: {both_count}")
    print(f"Lines with no polarity: {no_pol_count}")
    print(f"\nSaved to: exaltations_detriments_v2.json")

if __name__ == '__main__':
    main()
