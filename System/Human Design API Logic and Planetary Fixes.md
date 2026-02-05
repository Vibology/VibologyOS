Here is the definitive set of instructions to provide to Claude Code (or any developer) to build your API logic. These instructions derive strictly from the mechanics outlined in *The Definitive Book of Human Design*.

### Instruction Set for Human Design Fixing API

**1\. The Data Structure (The Reference Table)**You must create a lookup table (JSON or Database) derived from **Section Ten** of *The Definitive Book of Human Design* 1, 2\. For each of the 384 Lines, store the following properties:

* **Gate ID:** (1-64)  
* **Line ID:** (1-6)  
* **Exaltation Planet(s):** List of planets that trigger the ▲ symbol 3\.  
* **Detriment Planet(s):** List of planets that trigger the ▼ symbol 3\.  
* **Juxtaposition Planet(s):** List of planets that trigger the ✦ symbol 3\.  
* **Special Condition:** Boolean flag for "No Polarity" (e.g., Gate 50.5, 57.3) where the text explicitly states "No specific planetary accent" or "No polarity" 4, 5\.

**2\. The Input Parameters**The function requires three inputs for the specific line being calculated:

1. **Active\_Planet**: The planet activating the line in the user's chart.  
2. **Harmonic\_Active**: Boolean (Is the harmonic gate at the other end of the channel defined?).  
3. **Harmonic\_Planet**: The planet activating the harmonic gate (if Harmonic\_Active is True).

**3\. The Calculation Logic (The Algorithm)**Instruct Claude to implement this exact "If/Then" hierarchy to determine the output state:

* **Step 1: Check for "No Polarity"**  
* IF the line is flagged as "No Polarity" in the database (e.g., 57.3), RETURN Neutral/None. (These lines cannot be fixed; they always operate as is) 5\.  
* **Step 2: Check for Juxtaposition (Star)**  
* IF (Active\_Planet OR Harmonic\_Planet) matches a **Juxtaposition Planet** in the database, RETURN Juxtaposition (Star Symbol) 3, 6\.  
* **Step 3: Check for Exaltation**  
* IF (Active\_Planet OR Harmonic\_Planet) matches an **Exaltation Planet** in the database, ADD Exaltation to results 7\.  
* **Step 4: Check for Detriment**  
* IF (Active\_Planet OR Harmonic\_Planet) matches a **Detriment Planet** in the database, ADD Detriment to results 7\.

**4\. The Final Output Rules**

* **Single Match:** If only Exaltation is found, return ▲. If only Detriment is found, return ▼.  
* **Double Match:** If *both* Exaltation and Detriment triggers are present (e.g., User has Venus, Harmonic has Moon), return **Both** (often displayed as a Star or both icons). The text states: "If you have a juxtaposition... then both descriptions apply" 6\.  
* **No Match:** If no planets match, return Neutral (No Symbol).

This logic covers the "Direct Fixing" (user's planet) and "Harmonic Fixing" (channel partner) rules mandated by the source text 7\.  

What is Juxtaposition in a Line?
In the Rave I’Ching, Juxtaposition is represented by a Star symbol (⭐). Unlike the Exaltation (▲) which expresses the "positive" or high energy, or the Detriment (▼) which expresses the "negative" or low energy, Juxtaposition means both polarities are fixed and operate simultaneously.
The text states: "If you have a juxtaposition (a star shaped symbol representing both the exaltation and detriment), then both descriptions apply". This creates a "fixed fate" effect where the individual cannot fluctuate between the poles but must deal with the tension of both forces at once.
How to Calculate Juxtaposition (API Logic)
There are two distinct ways a line becomes Juxtaposed in a chart. Your script must check for both.
Scenario A: The "Star" Glyph (Intrinsic Juxtaposition)
Some lines in the source text explicitly list a Planet next to a Star symbol instead of a triangle.
• The Logic: If the source text assigns a specific planet to the Star symbol for that line.
• API Check: IF (Active_Planet == Star_Planet) OR (Harmonic_Planet == Star_Planet) THEN Result = "Juxtaposition" (Star)
Scenario B: Juxtaposition by "Double Fixing"
This occurs when the mechanics of the chart force both the Exaltation and the Detriment to happen at the same time. This is defined in the Glossary as "Juxtaposition in Fixing: When both the exaltation and the detriment in a line definition are fixed and emphasized".
• The Logic: This happens when the User has the planet required for one polarity, and the Harmonic Gate (or a Transit) provides the planet required for the opposite polarity.
• API Check:
    1. Identify the Exaltation_Planet required for the line.
    2. Identify the Detriment_Planet required for the line.
    3. IF (Active_Planet == Exaltation_Planet AND Harmonic_Planet == Detriment_Planet)
    4. OR IF (Active_Planet == Detriment_Planet AND Harmonic_Planet == Exaltation_Planet) THEN Result = "Juxtaposition" (Star)
Summary of Output States for Your Code
For every line analysis, your code should return one of four states:
1. Exalted (▲): Only the Up trigger is present.
2. Detriment (▼): Only the Down trigger is present.
3. Juxtaposed (⭐): The "Star" trigger is present OR both Up and Down triggers are present simultaneously.
4. Neutral/Unfixed: No specific planetary triggers are present (energy fluctuates).
Note: Be careful not to confuse this with "Juxtaposition Incarnation Crosses" (like the 4/1 Profile), which refer to a specific geometry of the whole chart. For your current task regarding line fixing, rely on the Star/Double-Fixing logic.