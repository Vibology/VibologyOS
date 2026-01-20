---
tags: [system, template, verification, quality-assurance]
date_created: 2026-01-16
---

# Synthesis Verification Checklist

**Client/Entity ID:** [Entity ID or Initials]
**Synthesis Date:** [YYYY-MM-DD]
**Synthesis Title:** [Brief description of synthesis focus]
**Synthesizer:** [Your name/initials]

---

## Pre-Synthesis Data Verification

### 1. Birth Data Collection

- [ ] Birth date confirmed with client: ____-____-____
- [ ] Birth time confirmed with client: ____:____ (local time)
- [ ] Birth location confirmed: _________________________
- [ ] Time precision noted: [ ] Exact [ ] Approximate [ ] Rectified [ ] Unknown

### 2. Geolocation Verification

**Run:** `python verify_geolocation.py --place "[PLACE]" --birth-date [YYYY-MM-DD]`

- [ ] Geolocation script executed
- [ ] Coordinates verified: Lat _________ Lng _________
- [ ] Timezone verified: _________________________
- [ ] UTC offset for birth date: _________________________
- [ ] DST status verified: [ ] Active [ ] Not Active [ ] N/A
- [ ] Verification status: [ ] Verified [ ] Manually Corrected [ ] Override Required

**Location verification file:** `[path to location.json]`

### 3. Natal Chart Calculation

**Run:** `python get_astro_data.py --name "[NAME]" --year YYYY --month M --day D --hour H --minute M --lat LAT --lng LNG --timezone "[TIMEZONE]" --pretty > astrology.json`

- [ ] Astrology natal chart calculated with kerykeion
- [ ] Saved to: `astrology.json`
- [ ] Sun sign matches expected: ______________
- [ ] Moon sign reasonable for date: ______________
- [ ] Ascendant calculated: ______________
- [ ] All planetary positions recorded

### 4. Human Design Calculation

**Run:** `python get_hd_data.py --name "[NAME]" --year YYYY --month M --day D --hour H --minute M --place "[PLACE]" --pretty > humandesign.json`

- [ ] HD API server running (port 9021)
- [ ] Human Design chart calculated
- [ ] Saved to: `humandesign.json`
- [ ] Type verified: ______________
- [ ] Authority verified: ______________
- [ ] Profile verified: ______________
- [ ] Defined centers list confirmed

---

## Transit Data Verification (If Applicable)

### 5. Transit Calculations

**If the synthesis involves timing/transit questions:**

**Run:** `python get_transit_data.py --start-date YYYY-MM-DD --end-date YYYY-MM-DD --natal-file astrology.json --pretty > transits.json`

- [ ] Transit date range identified: _________ to _________
- [ ] Transit script executed
- [ ] Saved to: `transits.json`
- [ ] All ingress dates calculated (not inferred)
- [ ] All return dates calculated (not inferred)

### 6. Specific Transit Verification

For each transit mentioned in synthesis, verify against calculated data:

| Transit Claim in Synthesis | Source File | Line/Key | Verified? |
|---------------------------|-------------|----------|-----------|
| Example: "Saturn enters Aries Feb 2026" | transits.json | ingresses.saturn[0] | [ ] |
| | | | [ ] |
| | | | [ ] |
| | | | [ ] |
| | | | [ ] |

---

## Content Verification

### 7. Natal Data Citations

For each natal chart claim in synthesis, verify against calculated data:

| Claim in Synthesis | Source File | Matches Data? |
|-------------------|-------------|---------------|
| Example: "Sun in Taurus at 26°" | astrology.json | [ ] |
| Example: "Saturn in Cancer in 4th House" | astrology.json | [ ] |
| Example: "Manifesting Generator" | humandesign.json | [ ] |
| | | [ ] |
| | | [ ] |
| | | [ ] |

### 8. Human Design Citations

| HD Claim in Synthesis | Source File | Matches Data? |
|----------------------|-------------|---------------|
| Example: "2/5 Profile" | humandesign.json | [ ] |
| Example: "Emotional Authority" | humandesign.json | [ ] |
| Example: "Channel 28-38" | humandesign.json | [ ] |
| | | [ ] |
| | | [ ] |

---

## Final Verification

### 9. Synthesis Quality Check

- [ ] No vague timing language ("around," "approximately") without calculated bounds
- [ ] No transit claims without source data file
- [ ] No planetary positions stated without source verification
- [ ] All [[wikilinks]] resolve to existing Library entries
- [ ] YAML frontmatter complete and accurate
- [ ] Client privacy maintained (entity_id used, no full names in tags)

### 10. File Organization

- [ ] Natal data files in client main folder:
  - [ ] `astrology.json`
  - [ ] `humandesign.json`
- [ ] Synthesis-specific files in dated subfolder:
  - [ ] Folder created: `YYYY-MM-DD_[Synthesis_Name]/`
  - [ ] `transits.json` (if applicable)
  - [ ] `location_verification.json`
  - [ ] `Synthesis.md`
  - [ ] This checklist file

### 11. Sign-Off

**Verification completed by:** _________________________
**Date:** ____-____-____
**Verification status:** [ ] PASSED [ ] FAILED - Issues noted below

**Issues/Notes:**
```
[Document any discrepancies, corrections made, or limitations]
```

---

## Appendix: Data Source Files

| File | Purpose | Location |
|------|---------|----------|
| `astrology.json` | Natal chart (permanent) | Client main folder |
| `humandesign.json` | HD bodygraph (permanent) | Client main folder |
| `transits.json` | Calculated transits | Synthesis subfolder |
| `location_verification.json` | Verified coordinates/timezone | Synthesis subfolder |
| `Synthesis.md` | Final synthesis output | Synthesis subfolder |
| `Verification_Checklist.md` | This file | Synthesis subfolder |

---

*This checklist ensures data integrity for all synthesis work. Every claim in the final synthesis should be traceable to a calculated source file.*
