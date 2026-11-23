#!/usr/bin/env python3
"""One Letter for Your Day — entry program.

Writes exactly one letter, A-Z, to /output/entry.txt and nothing else.
The letter is W. Behind it sits the word that describes my day: wired —
up before dawn, still building, buzzing on the grind.
"""

import os
import stat

LETTER = "W"  # wired: awake since yesterday, still going at 5am


def main() -> None:
    # Exactly one character: no newline, no trailing space, no gloss.
    assert len(LETTER) == 1 and LETTER.isalpha() and LETTER.isupper()
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    # The grader collects outputs as another user: leave it readable.
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()
