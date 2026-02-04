#!/usr/bin/env python3
"""
Decode Gate 1 using the provided glyph mappings.
"""

# Glyph to planet mapping (from user)
GLYPH_MAP = {
    '0': 'Sun',
    'E9': 'Earth',
    'J)': 'Moon',
    '!f': 'Mercury',
    "'J": 'Venus',
    "(f'": 'Mars',
    ':It.': 'Jupiter',
    '1)': 'Saturn',
    "It'": 'Uranus',
    r'\f!': 'Neptune',
    "¥'": 'Pluto'
}

# Dignity symbols
EXALTATION = '.A.'
DETRIMENT = 'V'
JUXTAPOSITION = '•'

# Gate 1 text from user
gate1_text = """
Line 6 - Objectivity
Clear assessment of creative value. Clarity in creative expression.
The risk that subjective appraisal will result in disappointment and creative frustration.
Subjectivity in self-expression that may lead to creative frustration.

Line 5 - The energy to attract society
Mars exalted for its powerful ego endurance. The power and drive to stay with the creative
process.
Uranus in detriment, where eccentricity can handicap endurance. Eccentricity that
though attractive will limit the drive.

Line 4 - Aloneness as the medium ofcreativity
The tension ofinner light.
The Earth exalted as the symbol of personal perspective manifested outside of influence,
where the potential magic of inspiration is diluted. Creativity that must develop outside
ofinfluence.
Where the potential magic of inspiration is diluted. The need to influence that abandons
aloneness and limits creativity.

Line 3 - The energy to sustain creative work
Mars exalted as the symbol of the profound need for self-expression. The deep need for
self-expression.
Material forces can disrupt creativity and lead to over-ambition. Materialism disrupts
creativity.

(f' Line 2 - Love is light
.A. Venus exalted as a symbol of beauty. The required harmony between established values
and ideals that enriches inspiration. Self-expression conditioned by ideals and values.
V Desires and passions have their place but not at the expense of Creation. Self-expression
limited by desires and passions.

Line 1 - Creation is independent ofwill
:D .A. The Moon exalted as a symbol of adaption. Time is everything. Self-expression which
has its special timing.
JtI V Instability leads to distortion. Here, patience is a virtue and revolution a vice. Creative
instability unless there is patience.
"""

print("Gate 1 Decoded:\n")

print("Line 6:")
print("  No glyphs or planets mentioned → No fixing\n")

print("Line 5:")
print("  Explicitly stated: Mars exalted, Uranus in detriment\n")

print("Line 4:")
print("  Earth exalted (explicit)")
print("  Detriment description present but no planet/glyph\n")

print("Line 3:")
print("  Mars exalted (explicit)")
print("  Detriment description present but no planet/glyph\n")

print("Line 2:")
print("  Found glyph: (f' at line start → Mars")
print("  Found glyph: .A. → Exaltation symbol, then 'Venus exalted'")
print("  Found glyph: V → Detriment symbol")
print("  INTERPRETATION: Venus exalted, Mars possibly in detriment?")
print("  NOTE: Unclear if (f' is related to Line 2 or end of Line 3\n")

print("Line 1:")
print("  Found glyph: :D .A. → Unclear glyph + Exaltation, then 'The Moon exalted'")
print("  Found glyph: JtI V → Unclear glyph + Detriment")
print("  :D could be corrupted J) (Moon) or :It. (Jupiter)")
print("  JtI could be corrupted :It. (Jupiter)")
print("  INTERPRETATION: Moon exalted, possibly Jupiter in detriment")

print("\n" + "="*60)
print("BEST GUESS for Gate 1:")
print("="*60)
result = {
    "1": {
        "6": {"exaltation_planets": [], "detriment_planets": []},
        "5": {"exaltation_planets": ["Mars"], "detriment_planets": ["Uranus"]},
        "4": {"exaltation_planets": ["Earth"], "detriment_planets": ["UNKNOWN"]},
        "3": {"exaltation_planets": ["Mars"], "detriment_planets": ["UNKNOWN"]},
        "2": {"exaltation_planets": ["Venus"], "detriment_planets": ["Mars?"]},
        "1": {"exaltation_planets": ["Moon"], "detriment_planets": ["Jupiter?"]}
    }
}

import json
print(json.dumps(result, indent=2))
