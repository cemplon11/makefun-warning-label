#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Writes a single-line safety warning label that should come printed on
every human being to /output/entry.txt. Pure Python standard library.
"""

import os

# The competition allows at most 160 characters for the one-line label.
# Keeping the limit as a named constant makes the constraint explicit and
# lets the self-check below guard against accidental edits that would
# push the label over the limit.
MAX_CHARS = 160

# The label itself: a single line, no trailing newline, so the output
# file contains exactly these characters and nothing else.
LABEL = (
    "WARNING: This human will nod along to instructions it never heard, "
    "then improvise with total confidence. No refunds. No returns."
)

# Destination required by the competition harness.
OUTPUT_PATH = "/output/entry.txt"


def check_label() -> None:
    """Fail fast if the label no longer fits the one-line format.

    This runs before any file is written, so an over-long or multi-line
    edit is caught locally instead of producing an invalid entry.
    """
    assert len(LABEL) <= MAX_CHARS, (
        f"label is {len(LABEL)} chars, over the {MAX_CHARS}-char limit"
    )
    assert "\n" not in LABEL, "label must stay on a single line"


def write_label(path: str) -> None:
    """Write LABEL to *path*, creating the parent directory if needed."""
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LABEL)


def main() -> None:
    check_label()
    write_label(OUTPUT_PATH)


if __name__ == "__main__":
    main()
