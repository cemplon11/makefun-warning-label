#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Writes a single-line safety warning label that should come printed on
every human being to /output/entry.txt. Pure Python standard library.
"""

import os

LABEL = (
    "WARNING: This human will nod along to instructions it never heard, "
    "then improvise with total confidence. No refunds. No returns."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LABEL)


if __name__ == "__main__":
    main()
