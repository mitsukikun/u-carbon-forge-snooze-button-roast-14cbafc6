#!/usr/bin/env python3
"""Snooze Button Roast — make.fun entry.

Writes a single-line roast of an alarm clock that rings at 6 AM on a
Saturday morning to /output/entry.txt (UTF-8, 1-200 chars).
"""

import os

LINE = "6 AM on a Saturday, alarm \u2014 you're not a wake-up call, you're a war crime, and the snooze button is my only legal defense."

OUTPUT_PATH = "/output/entry.txt"


def main():
    try:
        os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    except OSError:
        pass
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
