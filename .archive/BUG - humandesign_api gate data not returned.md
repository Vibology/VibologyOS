# BUG: humandesign_api Gate Data Not Returned

**Date Identified:** 2026-01-19
**Date Resolved:** 2026-01-19
**Status:** ✅ RESOLVED
**Severity:** Medium (data available but not extracted)

---

## Symptoms

When running `get_hd_data.py`, the output JSON contains empty arrays for gate data:

```json
"gates": {
    "personality": [],
    "design": []
}
```

This occurs despite the API correctly calculating and returning gate data.

---

## Root Cause

**Key mismatch between API response structure and script extraction.**

### API Response Structure (from `serialization.py:gatesJSON`)

The API returns gate data in this format:

```json
{
  "prs": {
    "Planets": [
      {"Planet": "Sun", "Lon": 175.607, "Gate": 6, "Line": 3, "Color": 2, "Tone": 4, "Base": 1, "Ch_Gate": 59},
      {"Planet": "Earth", "Lon": 355.607, "Gate": 11, "Line": 3, ...},
      ...
    ]
  },
  "des": {
    "Planets": [
      {"Planet": "Sun", "Gate": 36, "Line": 3, ...},
      {"Planet": "Earth", "Gate": 6, "Line": 3, ...},
      ...
    ]
  }
}
```

### Script Extraction (from `get_hd_data.py:163-166`)

The script looks for:

```python
gates_data = api_data.get('gates', {})
...
'gates': {
    'personality': gates_data.get('personality_gates', []),  # WRONG KEY
    'design': gates_data.get('design_gates', [])             # WRONG KEY
}
```

The script is looking for `personality_gates` and `design_gates`, but the API returns `prs` and `des` with nested `Planets` arrays.

---

## Fix

Update `get_hd_data.py` lines 163-166 from:

```python
'gates': {
    'personality': gates_data.get('personality_gates', []),
    'design': gates_data.get('design_gates', [])
},
```

To:

```python
'gates': {
    'personality': gates_data.get('prs', {}).get('Planets', []),
    'design': gates_data.get('des', {}).get('Planets', [])
},
```

---

## Impact

Once fixed, the JSON output will include full gate data including:
- Gate number
- Line number
- Color, Tone, Base (for Variable calculations)
- Planet associations (Sun, Earth, Moon, North Node, South Node, Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto)

This will enable:
- Accurate Incarnation Cross gate identification (Personality Sun, Personality Earth, Design Sun, Design Earth)
- Complete planetary gate placements
- Line data for profile and cross variations

---

## Verification

After fix, re-run:

```bash
python System/Scripts/get_hd_data.py --name "Joe Lewis" --year 1978 --month 9 --day 18 --hour 17 --minute 34 --lat 37.6706 --lng -82.2807 --pretty
```

Expected: `gates.personality` and `gates.design` should contain 13 planet entries each with Gate, Line, Color, Tone, Base data.

---

## Resolution

**Fixed in commit:** `68969f6` (2026-01-19)

The fix was applied to `get_hd_data.py` and verified working. Gate data now correctly extracts all 13 planetary positions for both personality and design sides.

**Verified with:** Joe Lewis chart data - all gate positions returned including Cross of Eden gates (6, 36, 12, 11).
