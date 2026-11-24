#!/usr/bin/env python3
"""Weirdest Job Title: Blind Judge Showdown.

Writes a single job title — a real-sounding job with one hilariously
specific twist — to /output/entry.txt, exactly 44 characters, no newline.
"""
import os

TITLE = "Professional Mourner for Strangers' Goldfish"


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TITLE)


if __name__ == "__main__":
    main()
