#!/usr/bin/env python3
"""
PDF to Markdown Converter v2 - With Page Range & Filtering

Improvements over v1:
- Accepts page range to skip front/back matter
- Filters print production codes
- Cleaner output

Usage:
    python3 convert_pdf_to_md_v2.py <pdf_file> --start 8 --end 200 [--output <output_file>]
"""

import sys
import subprocess
import argparse
import re
from pathlib import Path
from datetime import date


def extract_text_from_pdf(pdf_path, start_page=None, end_page=None):
    """Extract text from PDF using pdftotext with optional page range."""
    cmd = ['/opt/homebrew/bin/pdftotext']

    if start_page:
        cmd.extend(['-f', str(start_page)])
    if end_page:
        cmd.extend(['-l', str(end_page)])

    cmd.extend([str(pdf_path), '-'])

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error extracting text from PDF: {e}")
        sys.exit(1)


def get_pdf_info(pdf_path):
    """Get PDF metadata using pdfinfo."""
    try:
        result = subprocess.run(
            ['/opt/homebrew/bin/pdfinfo', str(pdf_path)],
            capture_output=True,
            text=True,
            check=True
        )
        info = {}
        for line in result.stdout.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                info[key.strip()] = value.strip()
        return info
    except subprocess.CalledProcessError as e:
        print(f"Error getting PDF info: {e}")
        return {}


def parse_filename(filename):
    """Extract author and title from filename (format: 'Author - Title.pdf')."""
    stem = Path(filename).stem
    if ' - ' in stem:
        parts = stem.split(' - ', 1)
        return parts[0].strip(), parts[1].strip()
    else:
        return "Unknown", stem


def create_yaml_frontmatter(pdf_path, start_page, end_page):
    """Generate YAML frontmatter for the markdown file."""
    author, title = parse_filename(pdf_path.name)
    pdf_info = get_pdf_info(pdf_path)
    total_pages = pdf_info.get('Pages', 'Unknown')

    # Calculate content pages
    if start_page and end_page:
        content_pages = f"{end_page - start_page + 1} (extracted from pages {start_page}-{end_page} of {total_pages})"
    else:
        content_pages = total_pages

    # Detect pillar from path
    pillar = "Unknown"
    if 'Astrology' in str(pdf_path):
        pillar = "Astrology"
    elif 'Human Design' in str(pdf_path):
        pillar = "Human Design"
    elif 'Personal Mythos' in str(pdf_path):
        pillar = "Personal Mythos"
    elif 'The Tarot' in str(pdf_path):
        pillar = "The Tarot"
    elif 'Interdisciplinary' in str(pdf_path):
        pillar = "Interdisciplinary"

    yaml = f"""---
title: "{title}"
author: "{author}"
date_published: [YYYY - FILL IN]
publisher: "[Publisher - FILL IN]"
isbn: "[ISBN - FILL IN]"
pillar: "{pillar}"
tags: [{pillar.lower().replace(' ', '-')}, foundational-text]
source_type: "foundational_text"
library_status: "[tier_1_critical / tier_2_high_priority / tier_3_depth]"
citation_count: [COUNT - FILL IN]
date_converted: {date.today().isoformat()}
conversion_method: "pdftotext"
conversion_notes: "Pages {start_page}-{end_page} extracted, production codes filtered"
original_file: "{pdf_path.name}"
pages: {content_pages}
---

"""
    return yaml


def filter_production_codes(text):
    """Remove print production codes and artifacts."""
    lines = text.split('\n')
    filtered_lines = []

    # Patterns to skip
    skip_patterns = [
        r'^\d{5}$',  # 45173
        r'^\d{2}-\d{2}-\d{2}$',  # 11-06-03
        r'^TXT\d+$',  # TXT7
        r'^\d{2}:\d{2}:\d{2}$',  # 15:49:46
        r'^Black$',  # Black
        r'^--$',  # --
        r'PM$',  # PM
        r'\.indd',  # .indd files
        r'Saturn Layout',  # Layout markers
        r'Pages_\d+\.indd',  # Page layout files
        r'^\d{1,2}/\d{1,2}/\d{4}\s+\d{1,2}:\d{2}:\d{2}\s+[AP]M$',  # Timestamps
    ]

    for line in lines:
        # Check if line matches any skip pattern
        skip = False
        for pattern in skip_patterns:
            if re.search(pattern, line.strip()):
                skip = True
                break

        if not skip:
            filtered_lines.append(line)

    return '\n'.join(filtered_lines)


def clean_text(text):
    """Clean and format extracted text for markdown."""
    # Filter production codes first
    text = filter_production_codes(text)

    # Remove excessive blank lines (more than 2 consecutive)
    text = re.sub(r'\n{3,}', '\n\n', text)

    # Convert form feed to section breaks
    text = text.replace('\f', '\n\n')

    return text.strip()


def convert_pdf_to_markdown(pdf_path, output_path=None, start_page=None, end_page=None):
    """Main conversion function."""
    pdf_path = Path(pdf_path)

    if not pdf_path.exists():
        print(f"Error: PDF file not found: {pdf_path}")
        sys.exit(1)

    # Determine output path
    if output_path is None:
        output_path = pdf_path.with_suffix('.md')
    else:
        output_path = Path(output_path)

    print(f"Converting: {pdf_path.name}")
    if start_page and end_page:
        print(f"Extracting pages {start_page}-{end_page}")
    print(f"Output: {output_path}")

    # Extract text
    print("Extracting text from PDF...")
    text = extract_text_from_pdf(pdf_path, start_page, end_page)

    # Generate YAML frontmatter
    print("Generating YAML frontmatter...")
    yaml = create_yaml_frontmatter(pdf_path, start_page, end_page)

    # Clean text
    print("Cleaning and formatting text...")
    cleaned_text = clean_text(text)

    # Combine YAML + text
    markdown_content = yaml + cleaned_text

    # Write to file
    print(f"Writing markdown to {output_path}...")
    output_path.write_text(markdown_content, encoding='utf-8')

    print(f"✓ Conversion complete!")
    pdf_info = get_pdf_info(pdf_path)
    if start_page and end_page:
        print(f"  Pages extracted: {start_page}-{end_page} (of {pdf_info.get('Pages', 'Unknown')} total)")
    else:
        print(f"  Pages: {pdf_info.get('Pages', 'Unknown')}")
    print(f"  Output size: {len(markdown_content)} characters")
    print(f"\nNext steps:")
    print(f"  1. Review and fill in YAML fields marked [FILL IN]")
    print(f"  2. Check text formatting and structure")
    print(f"  3. Verify content starts/ends appropriately")


def main():
    parser = argparse.ArgumentParser(
        description='Convert PDF source texts to markdown with YAML frontmatter'
    )
    parser.add_argument('pdf_file', help='Path to PDF file')
    parser.add_argument('--output', '-o', help='Output markdown file path (optional)')
    parser.add_argument('--start', '-s', type=int, help='First page to extract')
    parser.add_argument('--end', '-e', type=int, help='Last page to extract')

    args = parser.parse_args()

    convert_pdf_to_markdown(args.pdf_file, args.output, args.start, args.end)


if __name__ == '__main__':
    main()
