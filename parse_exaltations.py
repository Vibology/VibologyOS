#!/usr/bin/env python3
"""
Parse exaltation and detriment data from Hexagram Line Descriptions text.
"""
import re
import json

# Planet names to search for
PLANETS = [
    'Sun', 'Moon', 'Earth', 'Mercury', 'Venus', 'Mars',
    'Jupiter', 'Saturn', 'Uranus', 'Neptune',
    'North Node', 'South Node'
]

def parse_hexagram_lines(text):
    """Parse the hexagram line descriptions and extract exaltation/detriment data."""

    data = {}

    # Split by gates
    gate_pattern = r'GATE (\d+):'
    gates = re.split(gate_pattern, text)

    # Process each gate (gates[0] is preamble, then alternating gate numbers and content)
    for i in range(1, len(gates), 2):
        gate_num = gates[i]
        gate_content = gates[i + 1] if i + 1 < len(gates) else ""

        # Initialize gate in data structure
        data[gate_num] = {}

        # Split by lines within the gate
        line_pattern = r'Line (\d) -'
        lines = re.split(line_pattern, gate_content)

        # Process each line (lines[0] is gate description, then alternating line nums and content)
        for j in range(1, len(lines), 2):
            line_num = lines[j]
            line_content = lines[j + 1] if j + 1 < len(lines) else ""

            # Initialize line data
            line_data = {
                "exaltation_planets": [],
                "detriment_planets": [],
                "juxtaposition_planets": [],
                "no_polarity": False
            }

            # Check for "no polarity" or "no specific planetary accent"
            if re.search(r'no (specific )?polarity|no specific planetary accent', line_content, re.IGNORECASE):
                line_data["no_polarity"] = True

            # Search for exaltations
            for planet in PLANETS:
                # Pattern: "Planet exalted" or "The Planet exalted"
                if re.search(rf'\b(the\s+)?{planet}\s+exalted\b', line_content, re.IGNORECASE):
                    if planet not in line_data["exaltation_planets"]:
                        line_data["exaltation_planets"].append(planet)

            # Search for detriments
            for planet in PLANETS:
                # Pattern: "Planet in detriment" or "Planet detriment"
                if re.search(rf'\b(the\s+)?{planet}\s+(in\s+)?detriment\b', line_content, re.IGNORECASE):
                    if planet not in line_data["detriment_planets"]:
                        line_data["detriment_planets"].append(planet)

            # Store the line data
            data[gate_num][line_num] = line_data

    return data

def main():
    # Read the extracted text file
    with open('hexagram_lines_raw.txt', 'r', encoding='utf-8') as f:
        text = f.read()

    # Parse the data
    dignity_data = parse_hexagram_lines(text)

    # Output to JSON
    with open('exaltations_detriments.json', 'w', encoding='utf-8') as f:
        json.dump(dignity_data, f, indent=2)

    # Print summary statistics
    total_lines = 0
    lines_with_exaltation = 0
    lines_with_detriment = 0
    lines_with_both = 0
    lines_no_polarity = 0

    for gate in dignity_data.values():
        for line in gate.values():
            total_lines += 1
            if line['no_polarity']:
                lines_no_polarity += 1
            if line['exaltation_planets']:
                lines_with_exaltation += 1
            if line['detriment_planets']:
                lines_with_detriment += 1
            if line['exaltation_planets'] and line['detriment_planets']:
                lines_with_both += 1

    print(f"Total lines: {total_lines}")
    print(f"Lines with exaltation: {lines_with_exaltation}")
    print(f"Lines with detriment: {lines_with_detriment}")
    print(f"Lines with both: {lines_with_both}")
    print(f"Lines with no polarity: {lines_no_polarity}")
    print(f"\nOutput written to: exaltations_detriments.json")

if __name__ == '__main__':
    main()
