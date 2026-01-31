# Initial Client Report Template

**Purpose:** Comprehensive archetypal portrait for new clients, synthesizing Western astrology, Human Design, and archetypal psychology.

**Output location:** `~/Business/Consultations/{Client Name}/`

---

## Pre-Generation Checklist

Before writing the report:

1. **Gather birth data:** Date, time (exact if possible), location
2. **Calculate charts:**
   ```bash
   cd ~/VibologyOS && source .venv/bin/activate

   # Astrology
   python3 System/Scripts/get_astro_data.py \
     --name "Name" --year YYYY --month M --day D \
     --hour H --minute M --lat LAT --lng LNG \
     --city "City" --nation "US" \
     --timezone "IANA/Timezone" --pretty > astrology.json

   # Human Design (start API if needed: cd System/humandesign_api && uvicorn humandesign.api:app --port 9021 &)
   python3 System/Scripts/get_hd_data.py \
     --name "Name" --year YYYY --month M --day D \
     --hour H --minute M --lat LAT --lng LNG --pretty > humandesign.json
   ```

3. **Generate graphics:**
   ```bash
   # Natal chart (Kerykeion generates in current directory)
   python3 -c "from kerykeion import AstrologicalSubject, KerykeionChartSVG; s = AstrologicalSubject('Name', YYYY, M, D, H, M, city='City', nation='US', lat=LAT, lng=LNG, tz_str='TZ', online=False); KerykeionChartSVG(s).makeSVG()"

   # Bodygraph (via chart renderer)
   python3 << 'EOF'
   import json, sys
   sys.path.insert(0, 'System/humandesign_api/src')
   from humandesign.services.chart_renderer import generate_bodygraph_image
   with open("humandesign.json") as f: hd = json.load(f)
   chart_data = {
       "general": {
           "energy_type": hd["type"]["energy_type"],
           "strategy": hd["type"]["strategy"],
           "inner_authority": hd["authority"]["inner_authority"],
           "profile": hd["profile"]["profile"],
           "inc_cross": hd["profile"]["incarnation_cross"],
           "definition": hd["definition"]["definition_type"],
           "defined_centers": hd["definition"]["defined_centers"],
           "variables": hd.get("variables", {})
       },
       "gates": {"prs": {"Planets": hd["gates"]["personality"]}, "des": {"Planets": hd["gates"]["design"]}},
       "channels": hd.get("channels", [])
   }
   with open("bodygraph.png", "wb") as f: f.write(generate_bodygraph_image(chart_data, fmt='png'))
   EOF
   ```

---

## Report Style Guidelines

**DO:**
- Write in accessible, plain English
- Address the client directly ("you," "your")
- Explain technical terms when first used
- Frame insights as patterns and possibilities, not fixed verdicts
- Include the graphic files by reference

**DO NOT:**
- Use YAML frontmatter
- Use wikilinks (no double brackets)
- Use excessive jargon without explanation
- Make definitive predictions
- Include technical data tables beyond a simple summary

---

## Report Structure

```markdown
# Initial Report: {Client Name}

*A portrait of your cosmic blueprint, synthesizing Western astrology, Human Design, and archetypal psychology.*

**Birth Data:** {Month Day, Year} at {Time} in {City, State/Country}

---

## Your Charts

Your natal chart and bodygraph are included with this report:
- **natal_chart.svg** — Your astrological birth chart showing planetary positions
- **bodygraph.png** — Your Human Design bodygraph showing energy centers and channels

---

## The Invitation

{2-3 paragraphs framing what this report offers. Not a verdict but a map. The client has lived these patterns—only they know how the symbols have manifested.}

---

## The Core Pattern

| Category | Your Configuration |
|----------|-------------------|
| **Sun Sign** | {Sign} ({Degree}) in the {House} House |
| **Moon Sign** | {Sign} ({Degree}) in the {House} House |
| **Rising Sign** | {Sign} ({Degree}) |
| **Human Design Type** | {Type} |
| **Strategy** | {Strategy} |
| **Authority** | {Authority} |
| **Profile** | {Profile} |
| **Life Theme** | {Incarnation Cross} |

---

## Part 1: Your Solar Story — What You're Here to Express

{Interpret Sun sign, house, and HD Conscious Sun gate. What is the conscious life mission? Use accessible language. Explain what Aquarius or Capricorn or whatever sign MEANS in practical terms.}

---

## Part 2: Your Emotional Landscape — What You Need to Feel Safe

{Interpret Moon sign, house, and emotional center definition (or openness). How does this person process emotion? What do they need to feel secure?}

---

## Part 3: Your Public Face — How Others First Experience You

{Interpret Rising sign, any planets conjunct Ascendant, and HD Profile. How do they meet the world? What's the first impression they give?}

---

## Part 4: Your Life Theme — What You're Here to Do

{Interpret HD Incarnation Cross and astrological North Node. The overarching life purpose. Connect the systems where they converge.}

---

## Part 5: Your Archetypes — The Mythic Patterns at Work

{Which archetypes and myths resonate with this configuration? Name 3-4 and explain why in accessible terms. Hero's Journey placement if relevant.}

---

## Part 6: The Shadow Territory — Growth Edges

{Challenging aspects, planets in detriment/fall, open centers that create conditioning vulnerability. Frame as invitations for growth, not defects.}

---

## Part 7: Practical Guidance

{Strategy and Authority explained in plain terms. Specific recommendations for working with open centers, challenging aspects, etc.}

---

## The Open Question

{End with what remains unknown. What would conversation with the client reveal? Leave space for their lived experience to complete the picture.}

---

## Verification

- Astrology calculated: {Date} via Kerykeion/Swiss Ephemeris
- Human Design calculated: {Date} via humandesign_api/Swiss Ephemeris

---

*"The privilege of a lifetime is to become who you truly are." — C.G. Jung*
```

---

## Files Generated

For each client report, the folder should contain:
- `astrology.json` — Raw natal chart data (permanent)
- `humandesign.json` — Raw HD data (permanent)
- `natal_chart.svg` — Astrological chart graphic
- `bodygraph.png` — Human Design bodygraph graphic
- `Initial Client Report.md` — The synthesis document
