#!/bin/bash
# Weekly cleanup script — deletes one-off output files after use
# Run manually or schedule via Windows Task Scheduler
# Target: content/, research/, contracts/ — NOT context/, references/, memory/

BASE="c:/Users/Reyhan Khan/OneDrive/Desktop/Claude Code/EA Demo"

echo "Running EA Demo cleanup — $(date)"

# Patterns to delete (one-off outputs, not permanent references)
find "$BASE/content"   -type f \( -name "*.md" -o -name "*.html" -o -name "*.txt" \) -delete
find "$BASE/research"  -type f \( -name "*.md" -o -name "*.html" -o -name "*.txt" \) -delete
find "$BASE/contracts" -type f \( -name "*.html" -o -name "*.pdf" -o -name "*.docx" \) -delete

echo "Cleanup complete."
