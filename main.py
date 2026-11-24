#!/usr/bin/env python3
"""Seventeen Syllables of Debugging — one-haiku entry.

Writes one haiku about debugging (three lines, 5-7-5 syllables,
at most 200 characters) to /output/entry.txt: a concrete picture —
a cursor blinking at three in the morning — and a last line that
turns what came before.

Stdlib only, offline, deterministic: every run writes the same bytes.
"""

import os
from pathlib import Path

# The haiku:
#   three a.m. cursor                  (5 syllables)
#   blinks at the code I swore worked  (7 syllables)
#   it never once did                  (5 syllables)
# Counted at 69 characters — inside the 1..200 window.
HAIKU = (
    "three a.m. cursor\n"
    "blinks at the code I swore worked\n"
    "it never once did"
)


def output_dir() -> Path:
    """Where the grader expects the entry file.

    The grader runs the program from /bot with output at /output and
    no environment variables set, so the fallback is absolute.
    """
    return Path(os.environ.get("OUTPUT_DIR", "/output"))


def main() -> None:
    """Write the haiku to entry.txt."""
    out = output_dir()
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(HAIKU, encoding="utf-8")


# Guard: only run when executed directly.
if __name__ == "__main__":
    main()
