# Dignity Data Extraction Archive (February 2026)

This directory contains temporary files from the Human Design dignity data extraction project completed on February 3-4, 2026.

## Project Summary

Extracted comprehensive exaltation/detriment dignity data for all 64 gates (384 lines total) from the IHDS source material. The final merged data is in the root directory as `exaltations_detriments.json`.

## Archived Files

### Individual Gate Files (64 files)
- `gate_1_complete.json` through `gate_64_complete.json`
- Each file contains dignity data for one gate (6 lines)
- All merged into final `exaltations_detriments.json`

### Parsing Scripts (5 files)
- `decode_gate1.py` - Initial test script for Gate 1
- `map_symbols.py` - Symbol mapping utilities
- `parse_exaltations.py` - Main extraction script
- `parse_pdf_detailed.py` - Detailed PDF parsing
- `parse_with_glyphs.py` - Glyph-aware parsing

### Old Data Versions (3 files)
- `exaltations_detriments_v2.json` - Second iteration (54KB)
- `exaltations_detriments_final.json` - Third iteration (62KB)
- `gate_1_manual.json` - Manual extraction test for Gate 1

### Raw Extraction Data
- `hexagram_lines_raw.txt` - Raw text extracted from PDF
- `hexagram_pages/` - 68 PNG images (individual PDF pages)
- `Hexagram Line Descriptions.pdf` - Source PDF document

### Debug Files
- `correct.png` - Reference bodygraph image used for validation

## Final Output

**Location:** `/Users/joe/VibologyOS/exaltations_detriments.json`
**Size:** 72KB
**Date:** February 4, 2026
**Format:** JSON with gate → line → {exaltation_planets, detriment_planets, juxtaposition_planets, no_polarity}

## Verification Status

✅ All 64 gates extracted (100%)
✅ All 384 lines verified (100%)
✅ Data integrated into humandesign_api
✅ Dignity rendering implemented and tested

## Related Commits

- VibologyOS: Multiple commits Feb 3-4, 2026
- humandesign_api: Multiple commits Feb 4, 2026
- See git log for complete history

---
**Archived:** February 4, 2026
**Reason:** Extraction complete, temporary files no longer needed for active development
