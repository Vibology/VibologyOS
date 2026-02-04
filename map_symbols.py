#!/usr/bin/env python3
"""
Map the symbol patterns to planet names by examining known cases.
"""
import re

# Read the text
with open('hexagram_lines_raw.txt', 'r') as f:
    text = f.read()

# Find all unique symbol patterns before "exalted" or "detriment"
# Pattern: symbol characters followed by planet name and exalted/detriment
pattern = r'([^\n]{1,10}?)\s+(The\s+)?(Sun|Moon|Earth|Mercury|Venus|Mars|Jupiter|Saturn|Uranus|Neptune|North Node|South Node)\s+(exalted|in detriment)'

matches = re.findall(pattern, text, re.IGNORECASE)

# Group by symbol pattern
symbol_map = {}
for match in matches:
    symbol = match[0].strip()
    planet = match[2]
    dignity = match[3]
    
    if symbol not in symbol_map:
        symbol_map[symbol] = []
    symbol_map[symbol].append((planet, dignity))

print("Symbol patterns found:")
for symbol, planets in sorted(symbol_map.items()):
    print(f"\n'{symbol}':")
    for planet, dignity in planets[:5]:  # Show first 5 examples
        print(f"  {planet} {dignity}")
