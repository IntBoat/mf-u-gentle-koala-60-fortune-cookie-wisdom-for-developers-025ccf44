#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers (make.fun).

Writes the entry -- one original fortune-cookie line about the
unreproducible bug -- to /output/entry.txt, where the sealed scorer
reads it.
"""

import os

TEXT = "The bug you cannot reproduce is the one your users can reproduce every single day."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
