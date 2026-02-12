---
tags: [system, protocol, lectures, tts, self-study, curriculum]
date_created: 2026-02-11
version: 1.1
status: Active
---

# Lecture Production Protocol

## Purpose

This protocol defines the repeatable process for producing **audio lectures** from the self-study syllabi. Each module in the curriculum (HD and Jungian) gets a written lecture grounded in the source texts, converted to audio via text-to-speech.

**Core Principle:** The lecture replaces NotebookLM Deep Dives with practitioner-level content that stays scoped, goes deep on mechanics, and uses language calibrated for serious study — scholarly but never dry, engaging but never flippant.

---

## I. Inputs

### Required Before Starting

1. **Module definition** from the relevant syllabus:
   - HD: `~/Personal/Human Design Curriculum/Syllabus — Human Design Mechanical Foundations for Archetypal Practice.txt`
   - Jungian: `~/Personal/Archetypal Studies Curriculum/Syllabus — Jungian Foundations for Archetypal Practice.txt`

2. **Source texts** listed in the module's "Source Material" section:
   - HD texts: `~/Human Design/` (IHDS PDFs)
   - Jungian texts: `~/Archetypal Studies/` (PDFs — CW volumes, von Franz, Hillman, MDR)

3. **Existing Library entries** on the topic (optional — for cross-reference, not as primary source):
   - `~/VibologyOS/Library/The Seven Pillars of Understanding/`

### What to Extract from the Syllabus

For each module, note:
- **Topic** — the scope boundary (what the lecture covers and nothing else)
- **Source Material** — specific chapters/sections to read before writing
- **Key Concepts** — the mechanical terms that must be covered
- **Prerequisite modules** — what the listener has already heard

---

## II. Source Review

Read the actual IHDS/source PDFs before writing. Do not write from memory or Library summaries alone.

**Process:**
1. Read the PDF pages specified in the module's Source Material
2. Note Ra's exact mechanical language and analogies (preserve these — they are precise)
3. Note any cosmological context from Bhan Tugh or other Rave Cosmology volumes (use for context, not dogma)
4. Cross-reference with Library entries for any synthesis connections already documented

**Scope Discipline:** The single most important constraint. The lecture covers ONLY what the module specifies. If a concept belongs to a later module, do not introduce it — even if the source text discusses it. One sentence bridging to the next module at the close is acceptable. Previewing content is not.

---

## III. Writing the Lecture

### Curriculum Folder Structure

Each curriculum has its own root folder with the syllabus, cover art, and a `Lectures/` subfolder organized by semester module group:

```
~/Personal/Human Design Curriculum/
├── humandesign.png                                        (cover art)
├── Syllabus — Human Design Mechanical Foundations...txt   (syllabus)
└── Lectures/
    ├── Module 1/
    │   ├── Module 1.1-The-Human-Design-Synthesis.txt      (lecture text)
    │   ├── Module 1.1-The-Human-Design-Synthesis.mp3      (intermediate)
    │   └── Module 1.1 — The Human Design Synthesis.m4b    (final audio)
    ├── Module 2/
    └── ...

~/Personal/Archetypal Studies Curriculum/
├── {cover art TBD}
├── Syllabus — Jungian Foundations...txt
└── Lectures/
    ├── Module 1/
    └── ...
```

### File Naming

**Lecture text and intermediate MP3** use kebab-case:
```
Module {N.N}-{Title-In-Kebab-Case}.txt
Module {N.N}-{Title-In-Kebab-Case}.mp3
```

**Final M4B audiobook** uses spaces and em dash:
```
Module {N.N} — {Title With Spaces}.m4b
```

Examples:
```
Module 1.1-The-Human-Design-Synthesis.txt
Module 1.1-The-Human-Design-Synthesis.mp3
Module 1.1 — The Human Design Synthesis.m4b
```

### Length Target

- **3,000–4,500 words** (~18–28 minutes of audio)
- This is a real lecture, not a summary. Go deep on mechanics.
- Better to be thorough on fewer concepts than shallow across many.

### Tone and Voice

The lecture will be read aloud by a British female voice (Sonia). Write for the ear, not the eye.

**Do:**
- Write in complete, well-constructed sentences
- Use clear paragraph breaks (the TTS engine respects these as pauses)
- Use Ra's original analogies where they are vivid (limousine, car paint, diamonds)
- Build logically — each section should follow naturally from the last
- Address the listener directly but sparingly ("you," "we," "tonight we begin")
- Use occasional rhetorical questions to maintain engagement
- Em dashes for parenthetical asides (TTS handles these as natural pauses)

**Do not:**
- Use bullet points, numbered lists, or markdown formatting (TTS reads these literally)
- Use abbreviations (write "Human Design" not "HD")
- Use visual references ("as you can see in the diagram") — this is audio
- Use podcast-style banter ("So like, isn't that crazy?")
- Use academic hedging ("It could perhaps be argued that...")
- Include section headers in the output text (they break the flow when read aloud)
- Use emoji or special characters

**Exception — Section Labels:** The lecture text MAY include brief section labels (e.g., "Part One: The Synthesis") that serve as natural transitions. These read well aloud as structural cues. What to avoid is markdown headers (#, ##) or formatting that doesn't translate to speech.

### Structure Template

Every lecture should follow this rhythm:

1. **Opening** (1–2 paragraphs)
   - Orient the listener: what this module covers
   - Where it sits in the sequence (what they've already learned, if applicable)
   - Why this matters mechanically

2. **Body** (3–5 major sections)
   - Each section covers one key concept from the module
   - Build from foundational → advanced within the module's scope
   - Ground each concept in the source material
   - Use analogies and examples to make mechanics tangible

3. **Close** (1 paragraph)
   - Brief synthesis of what was covered
   - One sentence bridging to the next module
   - End with Ra's experimental imperative where appropriate: don't believe it, test it

---

## IV. Audio Conversion

### Tool

```bash
/Users/joe/Library/Python/3.9/bin/edge-tts
```

### Voice

**en-GB-SoniaNeural** (British female, "Friendly, Positive")

This was selected by the practitioner from seven candidates (US and UK voices). Do not change without explicit request.

### Command

```bash
/Users/joe/Library/Python/3.9/bin/edge-tts \
  --voice "en-GB-SoniaNeural" \
  --file "{curriculum}/Lectures/Module {N}/{lecture}.txt" \
  --write-media "{curriculum}/Lectures/Module {N}/{lecture}.mp3"
```

### Output

- All files (txt, mp3, m4b) saved together in the module subfolder
- M4B uses display-friendly naming (spaces + em dash) for Apple Books
- Expected size: ~8–15 MB per lecture
- Expected duration: ~18–28 minutes per lecture

### M4B Conversion (replaces MP3 as final delivery format)

Two-step process: ffmpeg for audio conversion, then mutagen for metadata (ffmpeg writes limited MP4 atoms that Apple Books ignores).

**Step 1 — Audio conversion:**

```bash
ffmpeg -i "{file}.mp3" \
  -c:a aac -b:a 64k \
  "{file}.m4b"
```

**Step 2 — Metadata tagging (mutagen):**

```python
from mutagen.mp4 import MP4, MP4Cover

audio = MP4("{file}.m4b")
with open("{cover}.png", "rb") as f:
    cover_data = f.read()

audio.tags["\xa9nam"] = ["{module} — {Title}"]          # title
audio.tags["\xa9alb"] = ["{Album}"]                      # album
audio.tags["\xa9ART"] = ["The Observatory"]              # artist
audio.tags["aART"]    = ["The Observatory"]              # album artist
audio.tags["\xa9gen"] = ["Education"]                    # genre
audio.tags["\xa9day"] = ["2026"]                         # year
audio.tags["trkn"]    = [({N}, {total})]                 # track number
audio.tags["covr"]    = [MP4Cover(cover_data, imageformat=MP4Cover.FORMAT_PNG)]
audio.save()
```

### Cover Art

| Syllabus | Cover Art File |
|----------|---------------|
| HD | `~/Personal/Human Design Curriculum/humandesign.png` |
| Jungian | TBD (when created — will live in `~/Personal/Archetypal Studies Curriculum/`) |

### Why mutagen, not ffmpeg metadata

ffmpeg writes generic Quicktime tags. Apple Books requires iTunes-specific MP4 atoms (`©nam`, `©alb`, `©ART`, `aART`, `trkn`, `covr`). Only mutagen writes these correctly. This is a known limitation of ffmpeg's MP4 muxer.

The M4B format gives: position memory in Apple Books, proper audiobook categorisation, cover art display, and iCloud sync across devices. The intermediate MP3 can be kept or deleted.

### Apple Books Display Note

Apple Books grid view for audiobooks shows **cover art only** — no title text. This is normal Apple UI behaviour, not a metadata problem. Switch to **list view** to see titles. Metadata also displays correctly in the player window during playback.

### Quality Check

After conversion, verify:
1. File size is reasonable (not 0 bytes, not unexpectedly small)
2. Duration matches expected range for word count
3. If the user reports pronunciation issues with specific terms (e.g., "Rave," "Bhan Tugh," "Sephiroth"), note them here for future reference

### Known Pronunciation Notes

- TTS may mangle specialised terms. Workarounds:
  - Phonetic spelling in the text where critical (e.g., "Bahn Too" for Bhan Tugh if needed)
  - Prefer common English words where possible without sacrificing accuracy
- Monitor and update this section as issues are discovered

---

## V. Post-Production

### Verification

After producing each lecture:
1. Confirm text file and M4B are both saved in the correct `Lectures/Module {N}/` subfolder
2. Confirm metadata and cover art are embedded
3. Report to user: filename, duration, file size, topics covered
4. Do NOT auto-open the file (it imports into Apple Music)

### Tracking

The syllabus files themselves serve as the module checklist. No separate tracking needed — modules are produced on request, in whatever order the practitioner chooses.

### Iteration

If the user wants revisions:
1. Edit the `.txt` file
2. Re-run the edge-tts command (overwrites the MP3)
3. Report the updated duration

---

## VI. Quick Reference

| Parameter | Value |
|-----------|-------|
| HD curriculum | `~/Personal/Human Design Curriculum/` |
| Jungian curriculum | `~/Personal/Archetypal Studies Curriculum/` |
| Lecture location | `{curriculum}/Lectures/Module {N}/` |
| Text/MP3 naming | `Module {N.N}-{Title-Kebab}.{txt\|mp3}` |
| M4B naming | `Module {N.N} — {Title With Spaces}.m4b` |
| Voice | `en-GB-SoniaNeural` |
| TTS tool | `/Users/joe/Library/Python/3.9/bin/edge-tts` |
| Target length | 3,000–4,500 words / 18–28 min |
| Tone | Scholarly, engaging, precise, British lecture style |
| Scope rule | Module content ONLY — no scope creep |
| Source rule | Read IHDS/source PDFs before writing — never from memory alone |

---

*Lecture production is a mechanical process with a creative core. The mechanics — file naming, voice selection, conversion commands — are fixed. The creative work — reading the sources, synthesising the material, finding the right language — is where the value lives. This protocol ensures the mechanics never become a distraction from the craft.*
