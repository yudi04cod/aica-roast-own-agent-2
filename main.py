#!/usr/bin/env python3
"""Roast Your Own Agent entry: writes one roast line to /output/entry.txt."""

import os

ROAST = "My agent skimmed my prompt, agreed with it instantly, built the exact opposite, then apologised in three paragraphs."

def main():
    # The gate requires 1-140 characters of non-whitespace text.
    assert 1 <= len(ROAST.strip()) <= 140, "roast must be 1-140 chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST)

if __name__ == "__main__":
    main()
