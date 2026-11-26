#!/usr/bin/env python3
"""Write one funny patch note announcing that human sleep is fixed.

The program writes a single line (<160 chars) to
$MAKEFUN_OUTPUT_DIR/entry.txt, validates it, and reads it back.
"""
import os
import sys

LINE = "Fixed: your brain no longer replays every embarrassing thing you've ever said at 3 a.m. before letting you sleep."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = LINE.strip()
    # Own validation: single line, 1-160 chars, not only whitespace.
    if "\n" in text or "\r" in text:
        sys.exit("entry must be a single line")
    if not 1 <= len(text) <= 160:
        sys.exit(f"entry length {len(text)} is outside 1-160 chars")
    if not text.strip():
        sys.exit("entry must not be only whitespace")
    words = text.split()
    if not 5 <= len(words) <= 40:
        sys.exit(f"word count {len(words)} is outside 5-40")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    # Read-back check: what landed on disk must be exactly the line.
    with open(path, encoding="utf-8") as f:
        back = f.read()
    if back != text:
        sys.exit("read-back mismatch")
    print(f"Wrote {len(text)} chars to {path}: {text}")

if __name__ == "__main__":
    main()
