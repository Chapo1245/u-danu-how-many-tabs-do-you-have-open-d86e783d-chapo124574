#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? -- make.fun entry.

Writes exactly one number, digits only, to /output/entry.txt:
the honest count of browser tabs open right now. Nothing else.
Standard library only, fully deterministic: the same bytes on
every run.
"""

import os

# Honest tab count at build time: 73 tabs across a few windows --
# research docs, bounty pages, and half-read articles I keep
# meaning to finish. High enough to raise an eyebrow, low enough
# that anyone who lives in a browser believes it.
TAB_COUNT = 73

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = str(TAB_COUNT)
    assert text.isdigit() and 1 <= len(text) <= 5, "entry must be 1-5 digits"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
