#!/usr/bin/env python3
"""
PDF to Markdown Converter for Athenaeum Source Texts

Extracts text from PDF, adds YAML frontmatter, preserves structure.
Part of Phase 1: Source Text Conversion (Library Restructure)

Usage:
    python3 convert_pdf_to_md.py <pdf_file> [--output <output_file>]
"""

import sys
import subprocess
import argparse
from pathlib import Path
from datetime import date
import re


def extract_text_from_pdf(pdf_path):
    """Extract text from PDF using pdftotext."""
    try:
        result = subprocess.run(
            ['/opt/homebrew/bin/pdftotext', '-layout', str(pdf_path), '-'],
            capture_output=True,
            text=True,
            check=True
        )
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


def create_yaml_frontmatter(pdf_path, text_content):
    """Generate YAML frontmatter for the markdown file."""
    author, title = parse_filename(pdf_path.name)
    pdf_info = get_pdf_info(pdf_path)
    pages = pdf_info.get('Pages', 'Unknown')

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
conversion_method: "pdftotext -layout"
original_file: "{pdf_path.name}"
pages: {pages}
---

"""
    return yaml


def clean_text(text):
    """Clean and format extracted text for markdown."""
    # Remove excessive blank lines (more than 2 consecutive)
    text = re.sub(r'\n{3,}', '\n\n', text)

    # Remove form feed characters
    text = text.replace('\f', '\n\n---\n\n')  # Convert page breaks to horizontal rules

    return text.strip()


def convert_pdf_to_markdown(pdf_path, output_path=None):
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
    print(f"Output: {output_path}")

    # Extract text
    print("Extracting text from PDF...")
    text = extract_text_from_pdf(pdf_path)

    # Generate YAML frontmatter
    print("Generating YAML frontmatter...")
    yaml = create_yaml_frontmatter(pdf_path, text)

    # Clean text
    print("Cleaning and formatting text...")
    cleaned_text = clean_text(text)

    # Combine YAML + text
    markdown_content = yaml + cleaned_text

    # Write to file
    print(f"Writing markdown to {output_path}...")
    output_path.write_text(markdown_content, encoding='utf-8')

    print(f"✓ Conversion complete!")
    print(f"  Pages: {get_pdf_info(pdf_path).get('Pages', 'Unknown')}")
    print(f"  Output size: {len(markdown_content)} characters")
    print(f"\nNext steps:")
    print(f"  1. Review and fill in YAML fields marked [FILL IN]")
    print(f"  2. Check text formatting and structure")
    print(f"  3. Verify astrological glyphs rendered correctly")


def main():
    parser = argparse.ArgumentParser(
        description='Convert PDF source texts to markdown with YAML frontmatter'
    )
    parser.add_argument('pdf_file', help='Path to PDF file')
    parser.add_argument('--output', '-o', help='Output markdown file path (optional)')

    args = parser.parse_args()

    convert_pdf_to_markdown(args.pdf_file, args.output)


if __name__ == '__main__':
    main()
