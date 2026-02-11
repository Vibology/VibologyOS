#!/usr/bin/env python3
"""
fix_dead_links.py — Batch-fix known dead wikilinks in Library/ and Synthesis/

Dry-run by default. Pass --apply to write changes.
Pass --verbose to see every individual replacement.

Usage:
    python3 System/Scripts/fix_dead_links.py              # dry-run
    python3 System/Scripts/fix_dead_links.py --apply      # write changes
    python3 System/Scripts/fix_dead_links.py --verbose    # show each replacement
"""

import argparse
import os
import re
import sys
from pathlib import Path

# ──────────────────────────────────────────────────────────────────────
# REPLACEMENT MAPPINGS
# Each entry: (dead_link_target, correct_target)
# Order matters within categories — longer/more-specific patterns first.
# ──────────────────────────────────────────────────────────────────────

# Cat 1: The Window → The Astrolabe
CAT1_WINDOW = [
    ("The Window", "The Astrolabe"),
]

# Cat 2: Tarot Major Arcana — add Roman numerals
CAT2_TAROT = [
    # Special cases first (spelling variants, "The" prefix mismatches)
    ("Judgment (XX)", "Judgement (XX)"),
    ("The Wheel of Fortune (X)", "Wheel of Fortune (X)"),
    ("The Wheel of Fortune", "Wheel of Fortune (X)"),
    ("Strength (VIII/XI)", "Strength (VIII)"),
    # Standard missing-numeral fixes (alphabetical)
    ("The Chariot", "The Chariot (VII)"),
    ("The Devil", "The Devil (XV)"),
    ("The Emperor", "The Emperor (IV)"),
    ("The Empress", "The Empress (III)"),
    ("The Fool", "The Fool (0)"),
    ("The Hanged Man", "The Hanged Man (XII)"),
    ("The Hermit", "The Hermit (IX)"),
    ("The Hierophant", "The Hierophant (V)"),
    ("The High Priestess", "The High Priestess (II)"),
    ("The Lovers", "The Lovers (VI)"),
    ("The Magician", "The Magician (I)"),
    ("The Moon", "The Moon (XVIII)"),
    ("The Star", "The Star (XVII)"),
    ("The Sun", "The Sun (XIX)"),
    ("The Tower", "The Tower (XVI)"),
    ("The World", "The World (XXI)"),
    ("Death", "Death (XIII)"),
    ("Judgement", "Judgement (XX)"),
    ("Justice", "Justice (XI)"),
    ("Strength", "Strength (VIII)"),
    ("Temperance", "Temperance (XIV)"),
]

# Cat 3: Jungian/pillar article mismatches
CAT3_JUNGIAN = [
    ("Transcendent Function", "The Transcendent Function"),
    ("Collective Unconscious", "The Collective Unconscious"),
    ("Individuation", "Individuation Process"),
    ("Shadow", "The Shadow"),
    ("Animus", "The Animus"),
    ("Anima", "The Anima"),
    ("Syzygy", "The Syzygy"),
    ("Persona", "The Persona"),
    ("Tarot", "The Tarot"),
]

# Cat 4: HD Centers — remove "Center" suffix
CAT4_CENTERS = [
    ("Heart Center (Ego/Will)", "Heart"),
    ("Heart (Ego) Center", "Heart"),
    ("Emotional Solar Plexus", "Solar Plexus"),
    ("Solar Plexus Center", "Solar Plexus"),
    ("Ego/Heart Center", "Heart"),
    ("Heart/Ego Center", "Heart"),
    ("Throat Center", "Throat"),
    ("Sacral Center", "Sacral"),
    ("Spleen Center", "Spleen"),
    ("Head Center", "Head"),
    ("Root Center", "Root"),
    ("Ajna Center", "Ajna"),
    ("The G Center", "G Center"),
]

# Cat 5: Planets — add glyphs
CAT5_PLANETS = [
    ("The Sun ☉", "Sun ☉"),
    ("The Moon ☽", "Moon ☽"),
    ("Jupiter", "Jupiter ♃"),
    ("Saturn", "Saturn ♄"),
    ("Venus", "Venus ♀"),
    ("Mars", "Mars ♂"),
    ("Sun", "Sun ☉"),
]

# Cat 6: Signs — add glyphs
CAT6_SIGNS = [
    ("Capricorn", "Capricorn ♑"),
    ("Aquarius", "Aquarius ♒"),
    ("Scorpio", "Scorpio ♏"),
    ("Libra", "Libra ♎"),
    ("Aries", "Aries ♈"),
]

# Cat 7: Sephiroth — remove parentheticals, fix spellings
CAT7_SEPHIROTH = [
    ("Gevurah (Severity)", "Geburah"),
    ("Geburah (Severity)", "Geburah"),
    ("Tiphareth (Beauty)", "Tiphareth"),
    ("Tiferet (Beauty)", "Tiphareth"),
    ("Chesed (Mercy)", "Chesed"),
    ("Binah (Understanding)", "Binah"),
    ("Kether (Crown)", "Kether"),
    ("Netzach (Victory)", "Netzach"),
    ("Yesod (Foundation)", "Yesod"),
    ("Malkuth (Kingdom)", "Malkuth"),
    ("Chokmah (Wisdom)", "Chokmah"),
    ("Da'ath (Knowledge)", "Daath"),
    ("Da'at (Knowledge)", "Daath"),
    ("Hod (Splendor)", "Hod"),
    ("Tiphereth", "Tiphareth"),
    ("Daat", "Daath"),
]

# Cat 8: Gates — expand short refs
# Single-digit gates need word boundary to avoid matching "Gate 12" etc.
CAT8_GATES_SINGLE = [
    ("Gate 1", "Gate 01 - The Creative"),
    ("Gate 6", "Gate 06 - Conflict"),
    ("Gate 8", "Gate 08 - Holding Together"),
]

CAT8_GATES_MULTI = [
    ("Gate 25 (Innocence)", "Gate 25 - Innocence"),
    ("Gate 12", "Gate 12 - Standstill"),
    ("Gate 16", "Gate 16 - Enthusiasm"),
    ("Gate 20", "Gate 20 - Contemplation"),
    ("Gate 23", "Gate 23 - Splitting Apart"),
    ("Gate 27", "Gate 27 - Nourishment"),
    ("Gate 31", "Gate 31 - Influence"),
    ("Gate 33", "Gate 33 - Retreat"),
    ("Gate 35", "Gate 35 - Progress"),
    ("Gate 36", "Gate 36 - Darkening of the Light"),
    ("Gate 45", "Gate 45 - Gathering Together"),
    ("Gate 50", "Gate 50 - The Cauldron"),
    ("Gate 55", "Gate 55 - Abundance"),
    ("Gate 56", "Gate 56 - The Wanderer"),
    ("Gate 62", "Gate 62 - Preponderance of the Small"),
]

# Cat 9: Miscellaneous
CAT9_MISC = [
    ("The Hermetic Order of the Golden Dawn", "The Hermetic Order of the Golden Dawn"),  # skip — already correct target name
    ("Encounter with Anima", "Encounter with Anima-Animus"),
    ("The Return with Elixir", "Return with the Elixir"),
    ("The Meeting with the Mentor", "Meeting the Mentor"),
    ("Anointing", "Anointing and Substituted Love"),
    ("The Four Worlds", "Four Worlds"),
    ("The Shekinah", "Shekinah"),
    ("The Middle Pillar", "Middle Pillar"),
    ("Four Quarters", "The Four Quarters"),
    ("Hero's Journey", "The Hero's Journey"),
    ("Golden Dawn", "The Hermetic Order of the Golden Dawn"),
    ("Tree of Life", "The Tree of Life"),
    ("Manifestors", "Manifestor"),
    ("BodyGraph", "The BodyGraph"),
    ("Zaphkiel", "Tzaphkiel"),
]

# Cat 10: Round 2 mechanical fixes
CAT10_ROUND2 = [
    # Gate name corrections
    ("Gate 33 - Privacy", "Gate 33 - Retreat"),
    ("Gate 62 - Details", "Gate 62 - Preponderance of the Small"),
    # Tarot naming
    ("Death (Card XIII)", "Death (XIII)"),
    ("Judgment", "Judgement (XX)"),
    # Jungian naming
    ("Self", "The Self"),
    ("Encounter with Animus", "Encounter with Anima-Animus"),
    ("Anima-Animus", "Encounter with Anima-Animus"),
    ("Trickster", "The Trickster"),
    # Alchemical
    ("The Alchemical Process", "Alchemical Stages"),
    # Protocol links (strip .md extension)
    ("PROTOCOL - Cross-System Synthesis.md", "PROTOCOL - Cross-System Synthesis"),
    ("PROTOCOL - Chart Data Acquisition.md", "PROTOCOL - Chart Data Acquisition"),
]


# ──────────────────────────────────────────────────────────────────────
# REGEX BUILDERS
# ──────────────────────────────────────────────────────────────────────

def escape_for_regex(text: str) -> str:
    """Escape special regex characters in link target text."""
    # Escape everything except letters, digits, spaces, and common Unicode
    return re.escape(text)


def build_standard_rule(dead: str, correct: str) -> tuple[re.Pattern, str]:
    """
    Build a regex that matches [[dead]], [[dead|alias]], [[dead#heading]]
    but NOT if the target already equals the correct form.

    Returns (compiled_pattern, replacement_template).
    """
    dead_esc = escape_for_regex(dead)

    # When correct is longer than dead (e.g., "Shadow" -> "The Shadow"),
    # use negative lookahead for the appended suffix to prevent double-fixing.
    # When correct is shorter or same length (e.g., "Hod (Splendor)" -> "Hod"),
    # the dead pattern itself is unique enough — no lookahead needed (the literal
    # dead text won't reappear after replacement).
    correction_suffix = correct[len(dead):] if len(correct) > len(dead) else ""

    if correction_suffix:
        lookahead = r'(?!' + re.escape(correction_suffix) + r')'
    else:
        lookahead = ''

    pattern = re.compile(
        r'\[\['
        + dead_esc
        + lookahead
        + r'((?:\#[^\]|]*)?(?:\|[^\]]*)?)'  # group 1: optional #heading and/or |alias
        + r'\]\]'
    )
    replacement = '[[' + correct + r'\1]]'
    return pattern, replacement


def build_exact_rule(dead: str, correct: str) -> tuple[re.Pattern, str]:
    """
    For cases where the dead link is a SUBSET of the correct target and we need
    strict boundary matching (e.g., [[Sun]] should not match [[The Sun (XIX)]]).

    Matches [[dead]], [[dead|...]], [[dead#...]] but NOT [[dead<more-text>...]]
    """
    dead_esc = escape_for_regex(dead)

    pattern = re.compile(
        r'\[\['
        + dead_esc
        + r'((?:\#[^\]|]*)?)' # group 1: optional #heading
        + r'(\|[^\]]*)?'      # group 2: optional |alias
        + r'\]\]'
    )
    replacement = '[[' + correct + r'\1\2]]'
    return pattern, replacement


def build_gate_single_digit_rule(dead: str, correct: str) -> tuple[re.Pattern, str]:
    """
    For single-digit gates: [[Gate 1]] must NOT match [[Gate 12]], [[Gate 16]], etc.
    Uses negative lookahead for additional digits.
    """
    dead_esc = escape_for_regex(dead)

    pattern = re.compile(
        r'\[\['
        + dead_esc
        + r'(?![0-9])'           # NOT followed by another digit
        + r'(?! - )'             # NOT already expanded (e.g., "Gate 1 - The Creative")
        + r'((?:\#[^\]|]*)?)'
        + r'(\|[^\]]*)?'
        + r'\]\]'
    )
    replacement = '[[' + correct + r'\1\2]]'
    return pattern, replacement


def build_gate_multi_digit_rule(dead: str, correct: str) -> tuple[re.Pattern, str]:
    """
    For multi-digit gates: [[Gate 12]] must NOT match if already expanded.
    """
    dead_esc = escape_for_regex(dead)

    pattern = re.compile(
        r'\[\['
        + dead_esc
        + r'(?! - )'             # NOT already expanded
        + r'((?:\#[^\]|]*)?)'
        + r'(\|[^\]]*)?'
        + r'\]\]'
    )
    replacement = '[[' + correct + r'\1\2]]'
    return pattern, replacement


# ──────────────────────────────────────────────────────────────────────
# BUILD ALL RULES
# ──────────────────────────────────────────────────────────────────────

def build_all_rules() -> list[tuple[str, str, re.Pattern, str]]:
    """
    Returns list of (category, dead_label, compiled_pattern, replacement).
    """
    rules = []

    def add_standard(cat: str, mappings: list[tuple[str, str]]):
        for dead, correct in mappings:
            if dead == correct:
                continue  # skip identity mappings
            pat, repl = build_standard_rule(dead, correct)
            rules.append((cat, dead, pat, repl))

    def add_exact(cat: str, mappings: list[tuple[str, str]]):
        for dead, correct in mappings:
            if dead == correct:
                continue
            pat, repl = build_exact_rule(dead, correct)
            rules.append((cat, dead, pat, repl))

    # Cat 1: Window → Astrolabe
    add_standard("Cat1-Window", CAT1_WINDOW)

    # Cat 2: Tarot — need careful ordering. Special cases first.
    # "The Wheel of Fortune (X)" before "The Wheel of Fortune"
    # Short names like "Death" need exact matching to avoid partial hits
    for dead, correct in CAT2_TAROT:
        if dead == correct:
            continue
        # These short names could match inside longer targets — use exact rules
        pat, repl = build_exact_rule(dead, correct)
        rules.append(("Cat2-Tarot", dead, pat, repl))

    # Cat 3: Jungian — short words like "Shadow", "Anima" need exact match
    add_exact("Cat3-Jungian", CAT3_JUNGIAN)

    # Cat 4: Centers — standard rules work (patterns are long enough)
    add_standard("Cat4-Centers", CAT4_CENTERS)

    # Cat 5: Planets — short names need exact match
    add_exact("Cat5-Planets", CAT5_PLANETS)

    # Cat 6: Signs — short names need exact match
    add_exact("Cat6-Signs", CAT6_SIGNS)

    # Cat 7: Sephiroth — standard works (parenthetical patterns are unique)
    add_standard("Cat7-Sephiroth", CAT7_SEPHIROTH)

    # Cat 8: Gates — special digit handling
    for dead, correct in CAT8_GATES_SINGLE:
        pat, repl = build_gate_single_digit_rule(dead, correct)
        rules.append(("Cat8-Gates", dead, pat, repl))

    for dead, correct in CAT8_GATES_MULTI:
        if dead == correct:
            continue
        pat, repl = build_gate_multi_digit_rule(dead, correct)
        rules.append(("Cat8-Gates", dead, pat, repl))

    # Cat 9: Misc — mixed; standard for most, exact for short ones
    for dead, correct in CAT9_MISC:
        if dead == correct:
            continue
        pat, repl = build_standard_rule(dead, correct)
        rules.append(("Cat9-Misc", dead, pat, repl))

    # Cat 10: Round 2 — exact match for short names, standard for longer ones
    for dead, correct in CAT10_ROUND2:
        if dead == correct:
            continue
        # Short single-word targets need exact matching
        if len(dead.split()) <= 2 and not dead.startswith("Gate") and not dead.startswith("PROTOCOL"):
            pat, repl = build_exact_rule(dead, correct)
        else:
            pat, repl = build_standard_rule(dead, correct)
        rules.append(("Cat10-Round2", dead, pat, repl))

    return rules


# ──────────────────────────────────────────────────────────────────────
# MAIN PROCESSING
# ──────────────────────────────────────────────────────────────────────

def process_file(filepath: Path, rules, apply: bool, verbose: bool) -> dict:
    """
    Process a single file. Returns stats dict.
    """
    stats = {"file": str(filepath), "replacements": 0, "details": []}

    try:
        content = filepath.read_text(encoding="utf-8")
    except (UnicodeDecodeError, PermissionError):
        return stats

    original = content
    for cat, dead_label, pattern, replacement in rules:
        new_content = pattern.sub(replacement, content)
        if new_content != content:
            count = len(pattern.findall(content))
            stats["replacements"] += count
            stats["details"].append((cat, dead_label, count))
            content = new_content

    if content != original:
        if apply:
            filepath.write_text(content, encoding="utf-8")

    return stats


def main():
    parser = argparse.ArgumentParser(description="Fix dead wikilinks in Library/ and Synthesis/")
    parser.add_argument("--apply", action="store_true", help="Write changes (default: dry-run)")
    parser.add_argument("--verbose", action="store_true", help="Show every replacement detail")
    args = parser.parse_args()

    # Resolve vault root (script lives in System/Scripts/)
    script_dir = Path(__file__).resolve().parent
    vault_root = script_dir.parent.parent

    scan_dirs = [vault_root / "Library", vault_root / "Synthesis"]
    for d in scan_dirs:
        if not d.exists():
            print(f"WARNING: Directory not found: {d}", file=sys.stderr)

    rules = build_all_rules()
    print(f"Loaded {len(rules)} replacement rules")
    print(f"Mode: {'APPLY' if args.apply else 'DRY-RUN'}")
    print(f"Scanning: {', '.join(str(d) for d in scan_dirs)}")
    print()

    # Collect all .md files
    md_files = []
    for scan_dir in scan_dirs:
        if scan_dir.exists():
            md_files.extend(sorted(scan_dir.rglob("*.md")))

    print(f"Found {len(md_files)} markdown files")
    print()

    total_replacements = 0
    total_files_changed = 0
    category_totals = {}

    for filepath in md_files:
        stats = process_file(filepath, rules, args.apply, args.verbose)
        if stats["replacements"] > 0:
            total_replacements += stats["replacements"]
            total_files_changed += 1
            rel = filepath.relative_to(vault_root)
            if args.verbose:
                print(f"  {rel}")
                for cat, dead_label, count in stats["details"]:
                    print(f"    [{cat}] [[{dead_label}]] × {count}")
            for cat, dead_label, count in stats["details"]:
                key = cat
                category_totals[key] = category_totals.get(key, 0) + count

    # Summary
    print("=" * 60)
    print(f"{'APPLIED' if args.apply else 'WOULD APPLY'}: {total_replacements} replacements across {total_files_changed} files")
    print()
    print("By category:")
    for cat in sorted(category_totals.keys()):
        print(f"  {cat}: {category_totals[cat]}")
    print("=" * 60)

    if not args.apply:
        print()
        print("This was a DRY RUN. Pass --apply to write changes.")


if __name__ == "__main__":
    main()
