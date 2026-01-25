#!/bin/bash

# Prima Materia Citation & Sources Audit
# Verifies all Cohort A-D files have inline citations AND Sources sections

OUTPUT_FILE="System/Audit Logs/Citation_Sources_Audit_$(date +%Y%m%d).md"

# Initialize report
cat > "$OUTPUT_FILE" << 'EOF'
# Prima Materia: Citation & Sources Audit

**Audit Date:** $(date +%Y-%m-%d)
**Purpose:** Verify all Cohorts A-D files have inline citations AND Sources sections

---

## Audit Results Summary

EOF

echo "# Prima Materia Citation & Sources Audit" >&2
echo "Checking all Cohorts A-D files..." >&2
echo "" >&2

# Initialize counters
total_files=0
files_with_citations=0
files_with_sources=0
files_complete=0
missing_citations=0
missing_sources=0
missing_both=0

# Arrays to store problematic files
declare -a files_no_citations
declare -a files_no_sources
declare -a files_no_both

# Function to check a single file
check_file() {
    local file="$1"
    local cohort="$2"

    total_files=$((total_files + 1))

    has_citations=false
    has_sources=false

    # Check for inline citations (footnote references like [^1])
    if grep -qE '\[\^[0-9]+\]' "$file"; then
        has_citations=true
        files_with_citations=$((files_with_citations + 1))
    fi

    # Check for Sources section (case insensitive, allowing ## or ###)
    if grep -qiE '^#{2,3} (Sources|References)' "$file"; then
        has_sources=true
        files_with_sources=$((files_with_sources + 1))
    fi

    # Categorize
    if $has_citations && $has_sources; then
        files_complete=$((files_complete + 1))
    elif ! $has_citations && ! $has_sources; then
        missing_both=$((missing_both + 1))
        files_no_both+=("$cohort|$file")
    elif ! $has_citations; then
        missing_citations=$((missing_citations + 1))
        files_no_citations+=("$cohort|$file")
    elif ! $has_sources; then
        missing_sources=$((missing_sources + 1))
        files_no_sources+=("$cohort|$file")
    fi
}

# Cohort A: Incarnation Crosses (193 files)
echo "Checking Cohort A: Incarnation Crosses..." >&2
while IFS= read -r file; do
    check_file "$file" "A-Crosses"
done < <(find "Library/The Seven Pillars of Understanding/Human Design/Incarnation Crosses" -type f -name "*.md")

# Cohort B: P1-CRITICAL (95 files)
echo "Checking Cohort B: Astrology (37 files)..." >&2
while IFS= read -r file; do
    check_file "$file" "B-Astrology"
done < <(find "Library/The Seven Pillars of Understanding/Astrology" -type f -name "*.md")

echo "Checking Cohort B: Human Design subset (33 files)..." >&2
for subdir in "Centers" "Profiles" "Authority" "Types"; do
    if [ -d "Library/The Seven Pillars of Understanding/Human Design/$subdir" ]; then
        while IFS= read -r file; do
            check_file "$file" "B-HD"
        done < <(find "Library/The Seven Pillars of Understanding/Human Design/$subdir" -type f -name "*.md")
    fi
done

echo "Checking Cohort B: Tarot Major Arcana (23 files)..." >&2
while IFS= read -r file; do
    check_file "$file" "B-Tarot"
done < <(find "Library/The Seven Pillars of Understanding/The Tarot/Major Arcana" -type f -name "*.md")

echo "Checking Cohort B: Overview files (2 files)..." >&2
for file in "Library/The Seven Pillars of Understanding/Angelology/Angelology.md" \
            "Library/The Seven Pillars of Understanding/The Window/The Window.md"; do
    if [ -f "$file" ]; then
        check_file "$file" "B-Overview"
    fi
done

# Cohort C: Synthesis-Heavy (76 files)
echo "Checking Cohort C: Personal Mythos (74 files)..." >&2
while IFS= read -r file; do
    check_file "$file" "C-PersonalMythos"
done < <(find "Library/The Seven Pillars of Understanding/Personal Mythos" -type f -name "*.md")

echo "Checking Cohort C: Angelology remaining (2 files)..." >&2
for file in "Library/The Seven Pillars of Understanding/Angelology/The Three Triads.md" \
            "Library/The Seven Pillars of Understanding/Angelology/Angelology and Human Design Integration.md"; do
    if [ -f "$file" ]; then
        check_file "$file" "C-Angelology"
    fi
done

# Cohort D: The Window (71 files)
echo "Checking Cohort D: The Window (71 files)..." >&2
while IFS= read -r file; do
    check_file "$file" "D-Window"
done < <(find "Library/The Seven Pillars of Understanding/The Window" -type f -name "*.md" ! -name "The Window.md")

# Cohort D: Human Design Gates (64 files)
echo "Checking Cohort D: Human Design Gates (64 files)..." >&2
while IFS= read -r file; do
    check_file "$file" "D-Gates"
done < <(find "Library/The Seven Pillars of Understanding/Human Design/Gates" -type f -name "*.md")

# Cohort D: Tarot Minor Arcana (56 files)
echo "Checking Cohort D: Tarot Minor Arcana (56 files)..." >&2
while IFS= read -r file; do
    check_file "$file" "D-MinorArcana"
done < <(find "Library/The Seven Pillars of Understanding/The Tarot/Minor Arcana" -type f -name "*.md")

# Generate summary
{
    echo "| Metric | Count | Percentage |"
    echo "|--------|-------|------------|"
    echo "| **Total Files Checked** | $total_files | 100% |"
    echo "| Files with Citations | $files_with_citations | $(( files_with_citations * 100 / total_files ))% |"
    echo "| Files with Sources Section | $files_with_sources | $(( files_with_sources * 100 / total_files ))% |"
    echo "| **Files Complete (Both)** | $files_complete | $(( files_complete * 100 / total_files ))% |"
    echo "| Missing Citations Only | $missing_citations | $(( missing_citations * 100 / total_files ))% |"
    echo "| Missing Sources Only | $missing_sources | $(( missing_sources * 100 / total_files ))% |"
    echo "| **Missing Both** | $missing_both | $(( missing_both * 100 / total_files ))% |"
    echo ""
    echo "---"
    echo ""

    # Files missing both
    if [ ${#files_no_both[@]} -gt 0 ]; then
        echo "## CRITICAL: Files Missing Both Citations AND Sources"
        echo ""
        echo "| Cohort | File |"
        echo "|--------|------|"
        for item in "${files_no_both[@]}"; do
            cohort="${item%%|*}"
            filepath="${item#*|}"
            filename=$(basename "$filepath")
            echo "| $cohort | $filename |"
        done
        echo ""
    fi

    # Files missing citations only
    if [ ${#files_no_citations[@]} -gt 0 ]; then
        echo "## Files Missing Inline Citations (but have Sources)"
        echo ""
        echo "| Cohort | File |"
        echo "|--------|------|"
        for item in "${files_no_citations[@]}"; do
            cohort="${item%%|*}"
            filepath="${item#*|}"
            filename=$(basename "$filepath")
            echo "| $cohort | $filename |"
        done
        echo ""
    fi

    # Files missing sources only
    if [ ${#files_no_sources[@]} -gt 0 ]; then
        echo "## Files Missing Sources Section (but have citations)"
        echo ""
        echo "| Cohort | File |"
        echo "|--------|------|"
        for item in "${files_no_sources[@]}"; do
            cohort="${item%%|*}"
            filepath="${item#*|}"
            filename=$(basename "$filepath")
            echo "| $cohort | $filename |"
        done
        echo ""
    fi

    # Success message
    if [ $files_complete -eq $total_files ]; then
        echo "## ✅ AUDIT PASSED"
        echo ""
        echo "All $total_files files have both inline citations and Sources sections."
    else
        echo "## ⚠️ AUDIT FAILED"
        echo ""
        echo "$(( total_files - files_complete )) files require remediation."
    fi

} >> "$OUTPUT_FILE"

echo "" >&2
echo "Audit complete. Report saved to: $OUTPUT_FILE" >&2
echo "" >&2
echo "Summary:" >&2
echo "  Total files: $total_files" >&2
echo "  Complete (both): $files_complete" >&2
echo "  Missing citations only: $missing_citations" >&2
echo "  Missing sources only: $missing_sources" >&2
echo "  Missing both: $missing_both" >&2
