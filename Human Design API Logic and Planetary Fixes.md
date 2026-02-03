Here is the definitive set of instructions to provide to Claude Code (or any developer) to build your API logic. These instructions derive strictly from the mechanics outlined in *The Definitive Book of Human Design*.

### Instruction Set for Human Design Fixing API

**1\. The Data Structure (The Reference Table)**You must create a lookup table (JSON or Database) derived from **Section Ten** of *The Definitive Book of Human Design* 1, 2\. For each of the 384 Lines, store the following properties:

* **Gate ID:** (1-64)  
* **Line ID:** (1-6)  
* **Exaltation Planet(s):** List of planets that trigger the ▲ symbol 3\.  
* **Detriment Planet(s):** List of planets that trigger the ▼ symbol 3\.  
* **Juxtaposition Planet(s):** List of planets that trigger the ⭐ symbol 3\.  
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
