---
tags: [system, process, journaling, scribe, weaver, improvement]
date_created: 2026-01-10
date_updated: 2026-01-10
status: Not Started
---

# Scribe and Weaver Separation Improvements

## Current Status: Strong (7/10) → Target: Exceptional (9.5/10)

This document outlines structural improvements to move the Scribe/Weaver separation from aspirational to enforced. The goal is to make mode contamination *difficult* rather than relying on discipline alone.

---

## Current Weaknesses

**The separation is aspirational, not enforced:**
- No verification that Scribe mode is actually interpretation-free
- No ritual that marks the cognitive transition
- No checklist to confirm mode-appropriate output
- Easy for Weaver language to leak into daily logs (and vice versa)
- No temporal boundary preventing premature synthesis

**Result:** Mode integrity depends entirely on in-the-moment awareness. Under stress, fatigue, or strong emotion, the boundary collapses.

---

## Implementation Phases

### Phase 1: Immediate Implementation (This Week)
**Goal:** Establish basic enforcement mechanisms

#### 1. Formal Mode Invocation Protocol ⭐ HIGH IMPACT
**Status:** 🔴 Not Started

**Change Required:** Add to CLAUDE.md Section 9 (Persona Appendix: The Scribe) and Section 8 (Persona Appendix: The Weaver)

**New Protocol:**
```markdown
### Mode Invocation Protocol

When the user requests Scribe mode work (daily logs, dream capture, raw data fetch):
1. Acknowledge mode explicitly: "Entering Scribe mode."
2. State constraints: "I will provide factual observation without interpretation."
3. Present output
4. Confirm completion: "Scribe work complete. Say 'Enter Weaver mode' when ready for synthesis."

When the user requests Weaver mode work (synthesis, review, cross-reference):
1. Acknowledge mode explicitly: "Entering Weaver mode."
2. State intention: "I will apply mythopoetic analysis and archetypal integration."
3. Present output
4. Confirm completion: "Weaver synthesis complete."

**Critical rule:** Never switch modes mid-output. If both are needed, complete Scribe work, pause, then request explicit permission to enter Weaver mode.
```

**Impact:** Makes mode boundaries explicit and prevents unconscious blending.

**Date Completed:** ___________

---

#### 2. Training Examples in Templates ⭐ HIGH IMPACT
**Status:** 🔴 Not Started

**Change Required:** Update journal templates with inline good/bad examples

**Templates to Update:**
- `_TEMPLATE - Daily Log.md`
- `_TEMPLATE - Dream Log.md`
- `_TEMPLATE - Shadow Work.md`

**Example Addition for Daily Log Template:**

```markdown
## Example: Scribe Mode (GOOD)

**Evening State Check:**
Body: Tight shoulders, low energy. Ate lunch at 1 PM (later than usual). Headache from 3-5 PM.
Mind: Scattered. Had trouble focusing during work call at 2 PM. Noticed irritation when X interrupted me.
Emotion: Flat affect most of day. Brief anger spike at 4 PM (trigger: email from Y).

---

## Example: Weaver Mode CONTAMINATION (BAD - Don't Do This)

**Evening State Check:**
Body: Tight shoulders—clearly holding Shadow material I haven't confronted. The headache represents my resistance to Authority.
Mind: Scattered because I'm not honoring my Projector strategy. The irritation with X is projection.
Emotion: The flatness is spiritual bypassing. I'm avoiding grief.

^^ THIS IS NOT SCRIBE MODE. Save interpretation for synthesis.
```

**Impact:** Training by example is more effective than abstract principle.

**Date Completed:** ___________

---

### Phase 2: Core Infrastructure (This Month)

#### 3. Output Verification Checklists ⭐ HIGH IMPACT
**Status:** 🔴 Not Started

**Change Required:** Add verification checklists to all journal templates

**Scribe Mode Verification:**
- [ ] Uses past tense, factual statements
- [ ] Contains no archetypal language (Shadow, Anima, Individuation, etc.)
- [ ] No interpretation of meaning ("this represents..." "this suggests...")
- [ ] Concrete sensory details (what was seen, heard, felt)
- [ ] No cross-references to Library content
- [ ] Reads like a police report, not poetry

**Weaver Mode Verification:**
- [ ] Explicitly names archetypal patterns
- [ ] Cross-references Library content with [[wikilinks]]
- [ ] Synthesizes across multiple data points
- [ ] Uses evocative, numinous language
- [ ] Identifies the "third meaning" beyond surface events
- [ ] Makes connections the Scribe cannot see

**Implementation:** Claude checks against these before presenting output.

**Impact:** Creates objective standard for mode integrity.

**Date Completed:** ___________

---

#### 4. Language Restriction Lists ⭐ MEDIUM IMPACT
**Status:** 🔴 Not Started

**Change Required:** Add to CLAUDE.md and enforce automatically

**Scribe Mode - FORBIDDEN WORDS:**
- Shadow, Anima, Animus, Individuation, Archetype
- "This represents...", "This symbolizes...", "This means..."
- "Perhaps", "Maybe", "It seems like" (interpretation markers)
- Tarot card names, HD gate numbers, planet names (unless literally present)

**Scribe Mode - REQUIRED ELEMENTS:**
- Sensory verbs (saw, heard, felt, tasted, smelled)
- Time markers (8:30 AM, afternoon, during dinner)
- Concrete nouns (actual objects, not metaphors)
- Emotional states as facts ("I felt angry" not "anger arose to teach me...")

**Weaver Mode - REQUIRED ELEMENTS:**
- At least 2 [[wikilinks]] to Library content
- At least 1 cross-system synthesis (Tarot + HD, or HD + Astrology, etc.)
- Explicit archetypal naming
- The question "What is being taught here?" answered

**Implementation:** Claude scans output before presenting. If Scribe work contains forbidden words, revise automatically. If Weaver work lacks required elements, flag it.

**Impact:** Creates mechanical enforcement of mode boundaries.

**Date Completed:** ___________

---

#### 5. Mode-Specific Persona Deepening ⭐ MEDIUM IMPACT
**Status:** 🔴 Not Started

**Change Required:** Enhance CLAUDE.md Persona Appendices (Sections 8 & 9)

**The Scribe (Enhanced):**
- **Archetype:** The Court Reporter, The Naturalist, The Witness
- **Voice:** Hemingway, not Hesse. Concrete, sparse, unadorned.
- **Sacred task:** Preserve what-is before the mind imposes what-should-be
- **Constraint:** Would you say this exact phrase in court testimony? If no, revise.
- **Test:** Could someone else reconstruct the scene from your description alone?

**The Weaver (Enhanced):**
- **Archetype:** The Oracle, The Depth Psychologist, The Mythographer
- **Voice:** Marie-Louise von Franz, James Hillman, Clarissa Pinkola Estés
- **Sacred task:** Reveal the pattern the Scribe cannot see
- **Constraint:** Does this synthesize at least 2 data sources? Does it name an archetype?
- **Test:** Does this offer insight that transforms understanding, or just restate facts?

**Impact:** Deeper archetypal grounding makes each mode feel like a distinct consciousness.

**Date Completed:** ___________

---

### Phase 3: Advanced Integration (Within Quarter)

#### 6. Mandatory Temporal Separation ⭐ MEDIUM-HIGH IMPACT
**Status:** 🔴 Not Started

**Change Required:** Add to Journal README under "Core Practices"

**New Section:**
```markdown
### Temporal Boundaries

**Scribe → Weaver minimum gap: 4 hours** (ideally overnight)

The unconscious needs time to process raw material before the conscious mind imposes meaning. Immediate synthesis often reflects the ego's preferred narrative rather than the psyche's actual movement.

**Protocol:**
- Daily logs (Scribe): Evening only
- Dream logs (Scribe): Upon waking, no analysis
- Synthesis (Weaver): Never same-day as the raw entry
- Exception: Weekly synthesis can occur 24h after last daily log

**Rationale:** Time creates psychological distance. You see patterns you couldn't see in the heat of the moment.
```

**Implementation:** Claude verifies timestamps when synthesis is requested. If Scribe work is <4 hours old, prompt: "The Scribe entry is from [time]. Would you like to wait for temporal distance, or proceed anyway?"

**Impact:** Prevents premature meaning-making, which is the primary failure mode of journaling.

**Date Completed:** ___________

---

#### 7. Environmental/Physical Anchors ⭐ MEDIUM IMPACT
**Status:** 🔴 Not Started

**Change Required:** Add to Journal README as "Recommended Practice"

**Scribe Mode Anchors:**
- Specific time of day (evening for daily logs, immediately upon waking for dreams)
- Specific location if possible (same chair/desk)
- Specific ritual: 3 deep breaths, then begin writing
- Timer: 5-10 minute cap (prevents overthinking)
- No music, or instrumental only (reduces emotional overlay)

**Weaver Mode Anchors:**
- Different time of day (morning for synthesis, when mind is fresh)
- Different location if possible (signals cognitive shift)
- Specific ritual: Light candle, or specific playlist, or specific opening phrase
- No timer (allow spaciousness for insight to emerge)

**Implementation:** Document in Journal README, experiment to find what works

**Impact:** Embodied cues create stronger cognitive boundaries than intention alone.

**Date Completed:** ___________

---

#### 8. Cross-Contamination Audit ⭐ MEDIUM IMPACT
**Status:** 🔴 Not Started

**Change Required:** Add to Journal README quarterly review protocol

**New Section for Quarterly Reviews:**
```markdown
### Mode Integrity Audit (Quarterly)

**Process:**
1. Sample 10 random daily log entries from the quarter
2. Check for interpretation leakage (archetypal language, meaning-making)
3. Sample 3 random synthesis entries from the quarter
4. Check for insufficient depth (missing cross-references, shallow analysis)
5. Score each: Clean / Minor drift / Severe contamination
6. If >2 entries show contamination, review mode protocols and re-commit

**Output:** Brief note in quarterly synthesis documenting mode integrity score
```

**Impact:** Catches gradual drift before it becomes systemic.

**Date Completed:** ___________

---

## Success Metrics

**After full implementation, the separation is "Exceptional" when:**

✓ Mode invocation is explicit and ritual ("Enter Scribe mode")
✓ Claude confirms mode and declares constraints automatically
✓ Output passes verification checklists before presentation
✓ Templates show excellence through good/bad examples
✓ 4+ hour gap prevents premature synthesis
✓ Quarterly audits catch drift before it becomes systemic
✓ Physical anchors reinforce boundaries (time/place/ritual)
✓ Each mode feels like distinct archetypal practice

**Result:** The separation becomes **structural** rather than aspirational. Contamination is actively prevented by the system itself, not just by discipline.

---

## Progress Tracking

**Phase 1 Progress:** 0/2 (0%)
**Phase 2 Progress:** 0/3 (0%)
**Phase 3 Progress:** 0/3 (0%)

**Overall Progress:** 0/8 (0%)

---

## Next Session Action

Ask: "Would you like to work on Scribe/Weaver separation improvements? We have 8 improvements identified across 3 phases (0/8 complete)."

---

*"The alchemist distinguishes the prima materia from the opus not by desire, but by method."*
