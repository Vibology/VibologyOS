#!/usr/bin/env python3
"""
Create stub files for high and medium priority dead wikilinks.
Places files in appropriate Library categories based on content type.
"""

from pathlib import Path
from datetime import date

# Stub file definitions
STUBS = {
    # HIGH PRIORITY - Angelology
    "Lucifer": {
        "path": "Angelology/Lucifer.md",
        "title": "Lucifer",
        "subtitle": "The Light-Bearer — The Fallen Seraph and Shadow of the Divine",
        "tags": ["angelology", "fallen-angels", "lucifer", "satan", "shadow", "stub"],
        "system": "Angelology",
        "overview": """**Lucifer** (Latin: *Lux Ferre*, "Light-Bearer"; Hebrew: *Helel ben Shachar*, הילל בן שחר, "Shining One, Son of Dawn") is the most enigmatic figure in angelology—the **Fallen Seraph**, the **Morning Star** who fell from heaven, the **Shadow of the Divine** made manifest.

In Christian tradition, Lucifer is identified with **Satan**, the adversary, the tempter, the prince of demons. In esoteric traditions, Lucifer represents the **shadow of Kether**, the **inverse of divine light**—not evil in essence, but the **necessary opposition** that allows for free will, individuation, and the drama of consciousness.""",
        "cross_refs": ["[[Seraphim]]", "[[Qlippoth]]", "[[The Shadow]]", "[[Kether]]"],
        "expansion": "Scriptural references (Isaiah 14, Ezekiel 28, Revelation 12), Lucifer vs. Satan distinction, the Fall narrative, Gnostic interpretations, Lucifer in tarot (The Devil card), psychological shadow integration."
    },

    "Guardian Angel": {
        "path": "Angelology/Guardian Angel.md",
        "title": "Guardian Angel",
        "subtitle": "The Personal Protector — Angelic Guidance and Individual Providence",
        "tags": ["angelology", "guardian-angel", "protection", "providence", "stub"],
        "system": "Angelology",
        "overview": """The **Guardian Angel** is a theological and mystical concept found across multiple traditions: the belief that each human soul is assigned a **personal angelic protector** who guides, guards, and intercedes on behalf of the individual throughout life.

In Christian tradition, guardian angels are understood as **Angels** (ninth order) assigned to specific persons. In Jewish mysticism, they are **maggidim** (revealers) or protective spirits. In Islamic tradition, the **Kiraman Katibin** (noble scribes) record deeds and offer protection.""",
        "cross_refs": ["[[Angels]]", "[[Michael]]", "[[The Self]]", "[[Numinous Experience]]"],
        "expansion": "Scriptural foundation (Matthew 18:10, Psalm 91:11), invocation practices, relationship to the Higher Self in Jungian terms, the Holy Guardian Angel in Thelema (Abramelin operation)."
    },

    # HIGH PRIORITY - Qabalah
    "Divine Names": {
        "path": "The Tarot/Qabalah/Divine Names.md",
        "title": "Divine Names",
        "subtitle": "The Sacred Names of God — Sephirotic Invocations and Divine Attributes",
        "tags": ["tarot", "qabalah", "divine-names", "tetragrammaton", "sephiroth", "stub"],
        "system": "Tarot",
        "subsystem": "Qabalah",
        "overview": """The **Divine Names** (Hebrew: *Shemot HaKodesh*, שמות הקודש) are the sacred appellations of God associated with each of the ten [[Sephiroth]] on the [[Tree of Life]]. Each name represents a specific **divine attribute** or **mode of divine action** in the world.

The names include the **Tetragrammaton** (YHVH), Elohim, Adonai, Shaddai, and others. Proper pronunciation and invocation of these names is central to Qabalistic ritual, meditation, and pathworking.""",
        "cross_refs": ["[[Tree of Life]]", "[[Sephiroth]]", "[[Kether]]", "[[Four Worlds]]"],
        "expansion": "Complete list of divine names for all ten Sephiroth, pronunciation guides, theological significance, use in Lesser Banishing Ritual of the Pentagram, relationship to Hebrew letter mysticism."
    },

    "Merkabah Mysticism": {
        "path": "The Tarot/Qabalah/Merkabah Mysticism.md",
        "title": "Merkabah Mysticism",
        "subtitle": "Chariot Mysticism — Heavenly Ascent and Throne Vision",
        "tags": ["tarot", "qabalah", "merkabah", "chariot", "mysticism", "throne-vision", "stub"],
        "system": "Tarot",
        "subsystem": "Qabalah",
        "overview": """**Merkabah Mysticism** (Hebrew: *Merkavah*, מרכבה, "Chariot") is an early form of Jewish mysticism (c. 100 BCE – 1000 CE) focused on visionary ascent through the **seven heavenly palaces** (*Hekhalot*) to behold the **Throne of God** and the divine **Chariot** described in Ezekiel 1.

Merkabah practice involved intense meditation, fasting, prayer, and recitation of divine names to achieve ecstatic states and angelic visions. It is a precursor to later Qabalistic mysticism.""",
        "cross_refs": ["[[Ezekiel's Vision]]", "[[The Chariot (VII)]]", "[[Cherubim]]", "[[Metatron]]", "[[Throne]]"],
        "expansion": "Hekhalot literature, dangerous nature of the practice, the four who entered Pardes, relationship to Gnosticism, influence on later Qabalah."
    },

    "Path 25": {
        "path": "The Tarot/Qabalah/Path 25.md",
        "title": "Path 25 — Samekh",
        "subtitle": "The Arrow — Yesod to Tiphareth, The Path of Testing",
        "tags": ["tarot", "qabalah", "paths", "samekh", "temperance", "stub"],
        "system": "Tarot",
        "subsystem": "Qabalah",
        "hebrew": "ס",
        "letter": "Samekh",
        "connects": "Yesod (Foundation) to Tiphareth (Beauty)",
        "tarot": "Temperance (XIV)",
        "overview": """**Path 25** connects [[Yesod]] (Foundation, the Moon, the personal unconscious) to [[Tiphareth]] (Beauty, the Sun, the Higher Self). It is the **Path of Samekh** (ס), the Hebrew letter meaning "support" or "prop"—the arrow aimed at the heart.

This path is associated with [[Temperance (XIV)|Temperance]], the card of alchemical integration, the angel pouring water between vessels. It represents the journey from ego-personality (Yesod) to the solar consciousness of the Higher Self (Tiphareth)—a path of testing, purification, and balance.""",
        "cross_refs": ["[[Yesod]]", "[[Tiphareth]]", "[[Temperance (XIV)]]", "[[Sagittarius ♐]]", "[[The Arrow]]"],
        "expansion": "Astrological correspondence (Sagittarius), spiritual tests on this path, alchemical symbolism, meditation practices for traversing Path 25."
    },

    "Pillar of Severity": {
        "path": "The Tarot/Qabalah/Pillar of Severity.md",
        "title": "Pillar of Severity",
        "subtitle": "The Left Pillar — Binah, Geburah, Hod: Form, Judgment, and Restriction",
        "tags": ["tarot", "qabalah", "pillars", "severity", "judgment", "binah", "geburah", "hod", "stub"],
        "system": "Tarot",
        "subsystem": "Qabalah",
        "overview": """The **Pillar of Severity** (also called the **Black Pillar** or **Pillar of Form**) is the left pillar of the [[Tree of Life]], consisting of three Sephiroth:

1. [[Binah]] (Understanding) — The Great Mother, form, limitation, the womb
2. [[Geburah]] (Severity) — Judgment, destruction, Mars, the warrior
3. [[Hod]] (Splendor) — Intellect, analysis, Mercury, the scribe

This pillar represents the **contracting force** in creation—limitation, form, judgment, discipline, and the necessary destruction that precedes transformation. It balances the [[Pillar of Mercy]] (expansion) through the [[Middle Pillar]] (equilibrium).""",
        "cross_refs": ["[[Pillar of Mercy]]", "[[Middle Pillar]]", "[[Binah]]", "[[Geburah]]", "[[Hod]]"],
        "expansion": "Feminine vs. masculine (despite left position), relationship to Saturn, the dark mother, necessary role of limitation, pathworking the Pillar of Severity."
    },

    "The Abyss": {
        "path": "The Tarot/Qabalah/The Abyss.md",
        "title": "The Abyss",
        "subtitle": "The Great Divide — The Chasm Between Supernal and Manifested Consciousness",
        "tags": ["tarot", "qabalah", "abyss", "daath", "supernal-triangle", "crossing", "stub"],
        "system": "Tarot",
        "subsystem": "Qabalah",
        "overview": """**The Abyss** is the metaphysical chasm on the [[Tree of Life]] that separates the **Supernal Triangle** (Kether, Chokmah, Binah) from the seven lower Sephiroth. It represents the **ontological divide** between:

- The **unmanifest divine** (above) and **manifested creation** (below)
- **Pure Being** and **individuated existence**
- The **transcendent** and the **immanent**

[[Daath]] ("Knowledge") is the **non-Sephirah** that exists within the Abyss—the point of crossing, the place where the aspirant must surrender the ego to attain union with the divine. Crossing the Abyss is the **death of the personal self** and rebirth into universal consciousness.""",
        "cross_refs": ["[[Daath]]", "[[Supernal Triangle]]", "[[Tiphareth]]", "[[Ego-Death]]", "[[The Tower (XVI)]]"],
        "expansion": "Aleister Crowley's 'Ordeal of the Abyss,' the Dweller on the Threshold, Choronzon (demon of dispersion), initiation into Magister Templi grade."
    },

    # MEDIUM PRIORITY - Jungian/Psychological
    "The Collective Unconscious": {
        "path": "Personal Mythos/Jungian Archetypes/The Collective Unconscious.md",
        "title": "The Collective Unconscious",
        "subtitle": "The Universal Psyche — Shared Archetypal Structures Across Humanity",
        "tags": ["personal-mythos", "jung", "collective-unconscious", "archetypes", "psyche", "stub"],
        "system": "Personal Mythos",
        "subsystem": "Jungian Archetypes",
        "overview": """The **Collective Unconscious** is Carl Jung's term for the **deepest layer of the psyche**, shared by all humans across cultures and time. Unlike the **personal unconscious** (individual repressed memories and complexes), the collective unconscious contains **archetypal patterns**—universal images, symbols, and motifs that appear in myths, dreams, religions, and art worldwide.

Jung wrote: *"The collective unconscious contains the whole spiritual heritage of mankind's evolution, born anew in the brain structure of every individual."*

Key archetypes residing in the collective unconscious include [[The Shadow]], [[The Anima]], [[The Animus]], [[The Self]], [[The Great Mother]], [[The Wise Old Man]], and others.""",
        "cross_refs": ["[[Jungian Archetypes]]", "[[The Self]]", "[[Synchronicity]]", "[[Psychoid Archetype]]"],
        "expansion": "Relationship to Plato's Forms, evidence from cross-cultural mythology, instincts vs. archetypes, critique and reception in modern psychology."
    },

    "The Transcendent Function": {
        "path": "Personal Mythos/Jungian Archetypes/The Transcendent Function.md",
        "title": "The Transcendent Function",
        "subtitle": "The Union of Opposites — Psychic Synthesis Through Creative Tension",
        "tags": ["personal-mythos", "jung", "transcendent-function", "coniunctio", "individuation", "stub"],
        "system": "Personal Mythos",
        "subsystem": "Jungian Archetypes",
        "overview": """The **Transcendent Function** is Jung's term for the psyche's capacity to hold **opposites in tension** until a **third thing** emerges that reconciles and transcends both. It is the psychological mechanism of **creative synthesis**, allowing consciousness to move beyond either/or thinking into both/and integration.

Example: Thesis (freedom) + Antithesis (responsibility) → Synthesis (mature autonomy that honors both)

The transcendent function operates through dreams, active imagination, art, and symbolic work. It is central to the process of [[Individuation]]—the integration of unconscious contents into conscious awareness.""",
        "cross_refs": ["[[Coniunctio]]", "[[Individuation]]", "[[Active Imagination]]", "[[Temperance (XIV)]]"],
        "expansion": "Jung's 1916 essay, relationship to Hegelian dialectic, practical methods for activating the transcendent function, neurological basis in hemispheric integration."
    },

    "Inflation": {
        "path": "Personal Mythos/Jungian Archetypes/Inflation.md",
        "title": "Inflation",
        "subtitle": "Psychic Inflation — Identification with Archetypal Forces",
        "tags": ["personal-mythos", "jung", "inflation", "ego", "shadow", "grandiosity", "stub"],
        "system": "Personal Mythos",
        "subsystem": "Jungian Archetypes",
        "overview": """**Inflation** (or **psychic inflation**) is a Jungian term for the condition where the **ego identifies with archetypal forces** from the unconscious, leading to grandiosity, hubris, and loss of groundedness.

When the ego inflates, it believes itself to be more than it is—a god, a messiah, a genius—rather than recognizing it is being **moved by** archetypal energies. Common causes include:
- Contact with numinous experiences without integration
- Identification with [[The Hero]], [[The Wise Old Man]], or [[The Great Mother]]
- Spiritual bypass (claiming enlightenment prematurely)

The remedy is **humility**, recognition of the Self as greater than the ego, and grounding in ordinary human reality.""",
        "cross_refs": ["[[The Shadow]]", "[[The Self]]", "[[Ego-Death]]", "[[Numinous Experience]]"],
        "expansion": "Marie-Louise von Franz on inflation, clinical examples, relationship to narcissism, inflation in spiritual communities, deflation and collapse."
    },

    "Ego-Death": {
        "path": "Personal Mythos/Jungian Archetypes/Ego-Death.md",
        "title": "Ego-Death",
        "subtitle": "The Dissolution of Identity — Mystical Annihilation and Rebirth",
        "tags": ["personal-mythos", "ego-death", "mysticism", "transformation", "individuation", "stub"],
        "system": "Personal Mythos",
        "subsystem": "Jungian Archetypes",
        "overview": """**Ego-Death** is the psychological and spiritual experience of the **dissolution of the sense of separate self**—the temporary or permanent collapse of ego-boundaries, leading to mystical union, terror, or both.

Ego-death occurs in:
- Mystical experiences (union with the divine)
- Psychedelic states (dissolution of subject/object duality)
- Severe trauma or crisis (breakdown of identity structures)
- Advanced meditation practices (cessation, nirvana)
- Crossing [[The Abyss]] in esoteric initiation

Ego-death can be **terrifying** (loss of control, annihilation anxiety) or **liberating** (union, oceanic bliss). Integration is essential—returning to functional ego-consciousness without inflation or fragmentation.""",
        "cross_refs": ["[[The Abyss]]", "[[The Tower (XVI)]]", "[[Kenosis - The Path of Self-Emptying]]", "[[Death and Resurrection]]"],
        "expansion": "Psychological vs. spiritual ego-death, Freud's 'oceanic feeling,' Buddhist anatta (no-self), dangers of unintegrated ego-death, re-emergence and rebirth."
    },

    "Numinous Experience": {
        "path": "Personal Mythos/Numinous Experience.md",
        "title": "Numinous Experience",
        "subtitle": "Encounter with the Holy — The Mysterium Tremendum et Fascinans",
        "tags": ["personal-mythos", "numinous", "mysticism", "holy", "otto", "jung", "stub"],
        "system": "Personal Mythos",
        "overview": """**Numinous Experience** is theologian Rudolf Otto's term (from Latin *numen*, "divine presence") for the direct encounter with the **holy**—the **mysterium tremendum et fascinans**, the mystery that is both terrifying and fascinating.

Otto identified three characteristics of the numinous:
1. **Tremendum** — Awe, terror, the overwhelming
2. **Majestas** — Majesty, power, absolute otherness
3. **Fascinans** — Attraction, beauty, irresistible draw

Jung adopted the concept to describe encounters with archetypal forces from [[The Collective Unconscious]]. Numinous experiences may occur through religious ritual, spontaneous visions, dreams, nature encounters, or psychedelic states.""",
        "cross_refs": ["[[The Collective Unconscious]]", "[[Synchronicity]]", "[[Mystical Union]]", "[[Theosis]]"],
        "expansion": "Otto's *The Idea of the Holy*, Jung's use of the numinous, numinous vs. moral, integration of numinous experience, pathology vs. genuine encounter."
    },

    "Synchronicity": {
        "path": "Personal Mythos/Jungian Archetypes/Synchronicity.md",
        "title": "Synchronicity",
        "subtitle": "Meaningful Coincidence — Acausal Connecting Principle",
        "tags": ["personal-mythos", "jung", "synchronicity", "meaning", "acausal", "unus-mundus", "stub"],
        "system": "Personal Mythos",
        "subsystem": "Jungian Archetypes",
        "overview": """**Synchronicity** is Jung's term for **meaningful coincidences**—events that are connected not by cause-and-effect but by **shared meaning**. Synchronicities occur when an inner psychological state (thought, dream, emotion) corresponds to an outer event with no causal link between them.

Examples:
- Thinking of a friend moments before they call
- Dreaming of a symbol that appears the next day
- Encountering the exact book/person/information needed at a critical moment

Jung proposed synchronicity as evidence of the **psychoid** nature of reality—that psyche and matter share a common ground in the **unus mundus** (one world). Synchronicities increase during times of heightened emotional intensity, crisis, or [[Individuation]].""",
        "cross_refs": ["[[The Collective Unconscious]]", "[[Psychoid Archetype]]", "[[Numinous Experience]]", "[[The Wheel of Fortune (X)]]"],
        "expansion": "Jung's collaboration with physicist Wolfgang Pauli, I-Ching and synchronicity, quantum physics parallels, theological implications, pathological synchronicity (over-reading)."
    },

    # MEDIUM PRIORITY - Practices
    "Contemplative Prayer": {
        "path": "The Magdalene Path/Contemplative Prayer.md",
        "title": "Contemplative Prayer",
        "subtitle": "Silent Prayer — Resting in the Divine Presence",
        "tags": ["magdalene-path", "prayer", "contemplation", "silence", "mysticism", "stub"],
        "system": "The Magdalene Path",
        "overview": """**Contemplative Prayer** is a form of Christian mystical prayer characterized by **silence, stillness, and wordless presence** before God. Unlike petitionary prayer (asking) or intercessory prayer (praying for others), contemplative prayer seeks **union with the divine** through receptive waiting.

Forms include:
- **Centering Prayer** (Thomas Keating, Basil Pennington)
- **The Prayer of Quiet** (Teresa of Ávila)
- **Hesychasm** (Eastern Orthodox practice using the Jesus Prayer)

Contemplative prayer is the Christian equivalent of meditation—a descent into the **heart center**, where the ego is silenced and the soul rests in divine love.""",
        "cross_refs": ["[[Kenosis - The Path of Self-Emptying]]", "[[Mystical Union]]", "[[Theosis]]", "[[The Bridal Chamber and Sacred Union]]"],
        "expansion": "Historical development (Desert Fathers, Teresa of Ávila, John of the Cross), relationship to Eastern meditation, stages of contemplative prayer, obstacles and dark nights."
    },

    "Bedtime Shema": {
        "path": "Angelology/Bedtime Shema.md",
        "title": "Bedtime Shema",
        "subtitle": "Jewish Evening Prayer — Angelic Protection and Divine Presence",
        "tags": ["angelology", "judaism", "prayer", "protection", "shema", "angels", "stub"],
        "system": "Angelology",
        "overview": """The **Bedtime Shema** (*Kriat Shema al HaMitah*, קריאת שמע על המיטה) is a Jewish liturgical practice performed before sleep, invoking divine protection and angelic guardianship through the night.

The prayer includes:
1. The **Shema** (Deuteronomy 6:4) — "Hear O Israel, the Lord is our God, the Lord is One"
2. Invocation of the **four archangels**: [[Michael]] (right), [[Gabriel]] (left), [[Uriel]] (front), [[Raphael]] (behind), with the [[Shekinah]] (divine presence) above
3. Confession and forgiveness
4. Psalm 91 (protection)

The Bedtime Shema creates a sacred boundary around sleep, inviting angelic protection and purification during the vulnerable night hours.""",
        "cross_refs": ["[[Michael]]", "[[Gabriel]]", "[[Uriel]]", "[[Raphael]]", "[[The Four Quarters]]"],
        "expansion": "Full liturgical text, Kabbalistic interpretation, relationship to Lesser Banishing Ritual, psychological function of ritual protection."
    },

    "Invocation of Raphael": {
        "path": "Angelology/Invocation of Raphael.md",
        "title": "Invocation of Raphael",
        "subtitle": "Calling the Healer — Prayer for Divine Healing and Guidance",
        "tags": ["angelology", "raphael", "invocation", "healing", "prayer", "stub"],
        "system": "Angelology",
        "overview": """The **Invocation of Raphael** is a ritual prayer calling upon [[Raphael]] (רפאל, "God Heals"), the archangel of [[Tiphareth]] and commander of the [[Virtues]], for healing, guidance, and divine intervention.

Raphael is invoked for:
- **Physical healing** (illness, injury, recovery)
- **Emotional healing** (trauma, grief, heartbreak)
- **Spiritual healing** (restoration of faith, guidance through crisis)
- **Safe travel** (Raphael guides Tobias in the Book of Tobit)

Traditional invocations include visualization of golden-green light, the element of Air (breath, spirit), and the caduceus symbol. Raphael's presence is felt as warmth in the heart or solar plexus.""",
        "cross_refs": ["[[Raphael]]", "[[Virtues]]", "[[Tiphareth]]", "[[Prayer for Healing]]"],
        "expansion": "Full invocation text, visualization instructions, timing (Sunday, dawn, Tiphareth correspondences), integration with medical treatment."
    },

    "Prayer for Healing": {
        "path": "Angelology/Prayer for Healing.md",
        "title": "Prayer for Healing",
        "subtitle": "Petitionary Prayer — Invoking Divine Grace for Restoration",
        "tags": ["angelology", "prayer", "healing", "grace", "intercession", "stub"],
        "system": "Angelology",
        "overview": """**Prayer for Healing** is the practice of petitioning divine grace—through God, Christ, angels, or saints—for the restoration of health, wholeness, and well-being. Healing prayer appears in all major religious traditions and may be directed toward:

- Physical ailments (illness, injury, chronic conditions)
- Emotional wounds (trauma, grief, depression, anxiety)
- Spiritual crises (loss of faith, dark night of the soul)
- Relationship healing (reconciliation, forgiveness)

Healing prayer may invoke [[Raphael]], [[Michael]], Christ as divine physician, or the [[Virtues]] (angels of miracles and grace). Effective prayer combines **faith** (trust in divine will), **surrender** (releasing attachment to specific outcomes), and **action** (seeking medical care, therapy, spiritual direction).""",
        "cross_refs": ["[[Virtues]]", "[[Raphael]]", "[[Invocation of Raphael]]", "[[Contemplative Prayer]]"],
        "expansion": "Scriptural foundation (James 5:14-15, healing miracles of Jesus), sacrament of anointing the sick, intercessory vs. petitionary prayer, empirical studies on prayer and healing."
    },

    "Discernment of Spirits": {
        "path": "Angelology/Discernment of Spirits.md",
        "title": "Discernment of Spirits",
        "subtitle": "Spiritual Discrimination — Distinguishing Divine, Angelic, and Demonic Influences",
        "tags": ["angelology", "discernment", "spirits", "mysticism", "testing", "stub"],
        "system": "Angelology",
        "overview": """**Discernment of Spirits** (*diakrisis pneumaton*, διάκρισις πνευμάτων) is the Christian mystical practice of **distinguishing between spiritual influences**—determining whether a vision, voice, impulse, or experience originates from:

1. **Divine/Angelic source** (God, Christ, Holy Spirit, angels)
2. **Human source** (ego, imagination, wishful thinking)
3. **Demonic source** (deception, temptation, illusion)

Criteria for discernment (from Ignatius of Loyola):
- **Consolation** (peace, clarity, love, humility) → likely divine
- **Desolation** (fear, confusion, pride, division) → likely demonic
- **Fruits** (does it lead to virtue, service, love?) → test by results

The gift of discernment is essential for navigating mystical experiences, spiritual direction, and protection from spiritual deception.""",
        "cross_refs": ["[[Guardian Angel]]", "[[The Abyss]]", "[[Inflation]]", "[[Numinous Experience]]"],
        "expansion": "1 Corinthians 12:10 (spiritual gift), Ignatius's Rules for Discernment, Teresa of Ávila on testing visions, modern psychological parallels."
    },

    "Heart Chakra Meditation": {
        "path": "Personal Mythos/Heart Chakra Meditation.md",
        "title": "Heart Chakra Meditation",
        "subtitle": "Anahata Practice — Opening the Heart Center",
        "tags": ["personal-mythos", "meditation", "chakra", "heart", "anahata", "stub"],
        "system": "Personal Mythos",
        "overview": """**Heart Chakra Meditation** is a contemplative practice focused on opening and balancing **Anahata** (अनाहत, "unstruck sound"), the fourth chakra, located at the center of the chest. The heart chakra governs:

- **Love** (universal compassion, not just romantic love)
- **Compassion** (capacity to feel with others without being overwhelmed)
- **Forgiveness** (releasing resentment, healing wounds)
- **Connection** (bridge between self and other, lower and upper chakras)

Practice involves:
1. Seated meditation, focus on the heart center
2. Visualization of green or pink light, expanding with each breath
3. Affirmations or mantras (e.g., *"I am open to love," "YAM"*)
4. Sending loving-kindness (metta) to self, loved ones, all beings

Regular practice cultivates emotional resilience, empathy, and the capacity to give from overflow rather than depletion.""",
        "cross_refs": ["[[Virtues]]", "[[Tiphareth]]", "[[Contemplative Prayer]]", "[[The Great Mother]]"],
        "expansion": "Yogic tradition (pranayama, mantra), relationship to Tiphareth in Qabalah, heart-brain coherence research, blocked heart chakra symptoms."
    },
}


def create_stub_file(stub_info, base_path):
    """Create a single stub markdown file."""
    file_path = base_path / stub_info["path"]

    # Ensure directory exists
    file_path.parent.mkdir(parents=True, exist_ok=True)

    # Build YAML frontmatter
    yaml = ["---"]
    yaml.append(f"tags: {stub_info['tags']}")
    yaml.append(f"system: {stub_info['system']}")
    if "subsystem" in stub_info:
        yaml.append(f"subsystem: {stub_info['subsystem']}")
    yaml.append(f"date_created: {date.today()}")
    yaml.append("status: stub")
    yaml.append("expansion_needed: true")

    # Add optional fields
    if "hebrew" in stub_info:
        yaml.append(f"hebrew: {stub_info['hebrew']}")
    if "letter" in stub_info:
        yaml.append(f"letter: {stub_info['letter']}")
    if "connects" in stub_info:
        yaml.append(f"connects: {stub_info['connects']}")
    if "tarot" in stub_info:
        yaml.append(f"tarot_card: {stub_info['tarot']}")

    yaml.append("---")

    # Build content
    content = [
        "\n".join(yaml),
        "",
        f"# {stub_info['title']}",
        f"*{stub_info['subtitle']}*",
        "",
        "---",
        "",
        "> **Note:** This entry is a structural stub. Core framework established; detailed content pending.",
        "",
        "---",
        "",
        "## Overview",
        "",
        stub_info['overview'],
        "",
        "---",
        "",
        "## Cross-References",
        "",
    ]

    for ref in stub_info["cross_refs"]:
        content.append(f"- {ref}")

    content.extend([
        "",
        "---",
        "",
        f"*Expansion needed: {stub_info['expansion']}*",
        "",
    ])

    # Write file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(content))

    return file_path


def main():
    base_path = Path("Library/The Seven Pillars of Understanding")

    print("="*70)
    print("CREATING HIGH & MEDIUM PRIORITY STUB FILES")
    print("="*70)

    created_files = []

    for name, stub_info in STUBS.items():
        file_path = create_stub_file(stub_info, base_path)
        created_files.append(file_path)
        print(f"✓ Created: {file_path.relative_to('Library/The Seven Pillars of Understanding')}")

    print(f"\n{'='*70}")
    print(f"SUMMARY: {len(created_files)} stub files created")
    print(f"{'='*70}")

    # Show breakdown by system
    by_system = {}
    for name, info in STUBS.items():
        system = info['system']
        by_system.setdefault(system, []).append(name)

    print("\nBreakdown by System:")
    for system, files in sorted(by_system.items()):
        print(f"  {system}: {len(files)} files")
        for f in files:
            print(f"    - {f}")


if __name__ == "__main__":
    main()
