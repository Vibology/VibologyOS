#!/usr/bin/env python3
"""
Add inline footnotes to Personal Mythos files.

Strategy:
- Detect primary source based on file content and location
- Add [^1] to first substantive paragraph
- Create tailored footnote definition
"""

import re
from pathlib import Path

LIBRARY_ROOT = Path(__file__).resolve().parent.parent.parent / "Library"
PERSONAL_MYTHOS_DIR = LIBRARY_ROOT / "The Seven Pillars of Understanding" / "Personal Mythos"

def get_primary_source(filepath, content):
    """Determine primary source based on file path and content."""

    rel_path = str(filepath.relative_to(PERSONAL_MYTHOS_DIR))
    filename = filepath.name

    # Jungian Archetypes
    if "Jungian" in rel_path:
        if "Shadow" in filename:
            return "C.G. Jung, *Collected Works* Vol. 9i: *The Archetypes and the Collective Unconscious* (Princeton University Press) — The Shadow archetype as repressed, inferior aspects of personality"
        elif "Anima" in filename:
            return "C.G. Jung, *Collected Works* Vol. 9ii: *Aion: Researches into the Phenomenology of the Self* (Princeton University Press) — The Anima as unconscious feminine principle in male psyche"
        elif "Animus" in filename:
            return "C.G. Jung, *Collected Works* Vol. 9ii: *Aion* (Princeton University Press) — The Animus as unconscious masculine principle in female psyche"
        elif "Self" in filename:
            return "C.G. Jung, *Collected Works* Vol. 9ii: *Aion* (Princeton University Press) — The Self as archetype of wholeness, center and circumference of the psyche"
        elif "Persona" in filename:
            return "C.G. Jung, *Collected Works* Vol. 7: *Two Essays on Analytical Psychology* (Princeton University Press) — The Persona as social mask, compromise between individual and society"
        else:
            return "C.G. Jung, *Collected Works* (Bollingen Series XX, Princeton University Press) — Jungian archetypal psychology"

    # Alchemical Stages
    elif "Alchemical" in rel_path:
        if "Nigredo" in filename:
            return "C.G. Jung, *Collected Works* Vol. 12: *Psychology and Alchemy* (Princeton University Press, par. 334) — Nigredo as blackening, decomposition of prima materia, psychological death preceding transformation"
        elif "Albedo" in filename:
            return "C.G. Jung, *Collected Works* Vol. 12: *Psychology and Alchemy* (Princeton University Press) — Albedo as whitening, purification stage following Nigredo"
        elif "Citrinitas" in filename:
            return "C.G. Jung, *Collected Works* Vol. 12: *Psychology and Alchemy* (Princeton University Press) — Citrinitas as yellowing, solar consciousness emerging"
        elif "Rubedo" in filename:
            return "C.G. Jung, *Collected Works* Vol. 12: *Psychology and Alchemy* (Princeton University Press) — Rubedo as reddening, final stage of integration and wholeness"
        elif "Calcination" in filename:
            return "Edward F. Edinger, *Anatomy of the Psyche: Alchemical Symbolism in Psychotherapy* (Open Court, 1985) — Calcination as burning away ego structures through fire"
        elif "Dissolution" in filename:
            return "Edward F. Edinger, *Anatomy of the Psyche* (Open Court, 1985) — Dissolution as softening rigid structures through water"
        elif "Separation" in filename:
            return "Edward F. Edinger, *Anatomy of the Psyche* (Open Court, 1985) — Separation as discriminating pure from impure"
        elif "Conjunction" in filename:
            return "Edward F. Edinger, *Anatomy of the Psyche* (Open Court, 1985) — Conjunction as union of opposites"
        elif "Fermentation" in filename:
            return "Edward F. Edinger, *Anatomy of the Psyche* (Open Court, 1985) — Fermentation as spiritual inspiration following putrefaction"
        elif "Distillation" in filename:
            return "Edward F. Edinger, *Anatomy of the Psyche* (Open Court, 1985) — Distillation as purification through repeated heating and cooling"
        elif "Coagulation" in filename:
            return "Edward F. Edinger, *Anatomy of the Psyche* (Open Court, 1985) — Coagulation as solidification of volatile spirit into permanent form"
        else:
            return "C.G. Jung, *Collected Works* Vol. 12: *Psychology and Alchemy* (Princeton University Press) — Alchemical transformation stages"

    # Fairy Tales
    elif "Fairy Tales" in rel_path:
        return "Grimm Brothers, *The Complete Fairy Tales* and Marie-Louise von Franz, *The Interpretation of Fairy Tales* (Shambhala, 1970) — Jungian analysis of archetypal patterns in fairy tales"

    # Hero's Journey
    elif "Hero" in rel_path or "Monomyth" in filename:
        return "Joseph Campbell, *The Hero with a Thousand Faces* (Pantheon Books, 1949) — The monomyth structure of archetypal hero narratives"

    # Individuation
    elif "Individuation" in filename:
        return "C.G. Jung, *Collected Works* Vol. 7: *Two Essays on Analytical Psychology* (Princeton University Press) — Individuation as the process of psychological integration and self-realization"

    # World Mythology - Greek
    elif "Greek Mythology" in rel_path:
        if "Zeus" in filename:
            return "Hesiod, *Theogony* (c. 700 BCE) and Homer, *Iliad* and *Odyssey* — Classical sources for Zeus as sky-father and king of gods"
        elif "Athena" in filename:
            return "Hesiod, *Theogony* and Homeric *Hymn to Athena* — Athena as goddess of wisdom, born from Zeus's head"
        elif "Apollo" in filename:
            return "Homeric *Hymn to Apollo* and classical sources — Apollo as god of light, music, prophecy, and rational order"
        elif "Artemis" in filename:
            return "Homeric *Hymn to Artemis* and classical sources — Artemis as virgin goddess of hunt, wilderness, and moon"
        elif "Aphrodite" in filename:
            return "Hesiod, *Theogony* and Homeric *Hymn to Aphrodite* — Aphrodite as goddess of love, beauty, and desire"
        elif "Hermes" in filename:
            return "Homeric *Hymn to Hermes* — Hermes as trickster, messenger, guide of souls"
        elif "Dionysus" in filename:
            return "Euripides, *The Bacchae* and classical sources — Dionysus as god of wine, ecstasy, and transformation"
        elif "Hades" in filename:
            return "Homer, *Iliad* and *Odyssey*, and classical sources — Hades as god of the underworld and lord of the dead"
        elif "Persephone" in filename:
            return "Homeric *Hymn to Demeter* — Persephone's abduction and descent to underworld"
        elif "Prometheus" in filename:
            return "Hesiod, *Theogony* and Aeschylus, *Prometheus Bound* — Prometheus as fire-bringer and rebel consciousness"
        else:
            return "Classical Greek sources (Hesiod, Homer, Homeric Hymns) and mythological encyclopedias"

    # World Mythology - Egyptian
    elif "Egyptian Mythology" in rel_path:
        if "Isis" in filename:
            return "Plutarch, *Isis and Osiris* (c. 100 CE) — Isis as great mother goddess and magician"
        elif "Osiris" in filename:
            return "Plutarch, *Isis and Osiris* — Osiris as god of death, resurrection, and vegetation"
        elif "Thoth" in filename:
            return "Egyptian sources and *Hermetica* — Thoth as god of wisdom, writing, and magic"
        else:
            return "Egyptian mythological texts and Plutarch, *Isis and Osiris*"

    # World Mythology - Mesopotamian
    elif "Mesopotamian" in rel_path:
        if "Inanna" in filename:
            return "*The Descent of Inanna* (Sumerian myth, c. 1900-1600 BCE) — Inanna's descent to the underworld and return"
        else:
            return "Mesopotamian mythological texts (Sumerian, Akkadian, Babylonian)"

    # Coniunctio
    elif "Coniunctio" in filename:
        return "C.G. Jung, *Collected Works* Vol. 14: *Mysterium Coniunctionis* (Princeton University Press) — The coniunctio as alchemical union of opposites, psychic wholeness"

    # Enantiodromia
    elif "Enantiodromia" in filename:
        return "C.G. Jung, *Collected Works* Vol. 6: *Psychological Types* (Princeton University Press) — Enantiodromia as transformation into opposite, psychic reversal"

    # Mandala
    elif "Mandala" in filename:
        return "C.G. Jung, *Collected Works* Vol. 9i: *The Archetypes and the Collective Unconscious* (Princeton University Press) — Mandala as symbol of the Self, psychic totality"

    # Unus Mundus
    elif "Unus Mundus" in filename:
        return "C.G. Jung, *Collected Works* Vol. 14: *Mysterium Coniunctionis* (Princeton University Press) — Unus Mundus as the unified reality underlying psyche and matter"

    # Four Functions
    elif "Four Functions" in filename or "Psychological Types" in filename:
        return "C.G. Jung, *Collected Works* Vol. 6: *Psychological Types* (Princeton University Press) — The four psychological functions: thinking, feeling, sensation, intuition"

    # Default
    else:
        return "Primary sources listed in References section"

def add_footnote_to_file(filepath):
    """Add inline footnote to Personal Mythos file."""
    content = filepath.read_text(encoding='utf-8')
    original = content

    # Get primary source
    source = get_primary_source(filepath, content)

    # Add [^1] after first substantive paragraph
    # Look for first paragraph after frontmatter/headers
    pattern = r'(^##[^\n]+\n\n)([A-Z][^.]+\.)'
    match = re.search(pattern, content, re.MULTILINE)

    if match:
        content = content[:match.end(2)] + '[^1]' + content[match.end(2):]
    else:
        # Fallback: after first paragraph
        pattern = r'(^[A-Z][^.]+\.)'
        match = re.search(pattern, content, re.MULTILINE)
        if match:
            content = content[:match.end(1)] + '[^1]' + content[match.end(1):]

    # Add footnote definition before ## Sources or ## References
    footnote_def = f'\n[^1]: {source}.\n'

    if '## Sources' in content:
        content = content.replace('## Sources', f'{footnote_def}\n---\n\n## Sources')
    elif '## References' in content:
        content = content.replace('## References', f'{footnote_def}\n---\n\n## References')
    else:
        content += f'\n\n{footnote_def}'

    # Only write if changed
    if content != original:
        filepath.write_text(content, encoding='utf-8')
        return True
    return False

def main():
    # Get all Personal Mythos files
    all_files = sorted(PERSONAL_MYTHOS_DIR.rglob("*.md"))

    # Exclude files that start with _ or already have footnotes
    files_to_process = []
    for f in all_files:
        if f.name.startswith("_"):
            continue
        content = f.read_text(encoding='utf-8')
        if not re.search(r'\[\^\d+\]', content):
            files_to_process.append(f)

    print(f"Processing {len(files_to_process)} Personal Mythos files...")

    updated = 0
    for filepath in files_to_process:
        if add_footnote_to_file(filepath):
            rel_path = filepath.relative_to(PERSONAL_MYTHOS_DIR)
            print(f"  ✓ {rel_path}")
            updated += 1

    print(f"\nUpdated {updated}/{len(files_to_process)} files.")

if __name__ == "__main__":
    main()
