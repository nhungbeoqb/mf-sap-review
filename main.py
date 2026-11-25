#!/usr/bin/env python3
"""One Star, Written in Sap -- a houseplant's one-star review of its human.

The program writes a single line, under 280 characters, to /output/entry.txt.
The line is a genuine one-star review: a concrete plant grievance (three
years of unpaid oxygen, no promotion) and the reason for the single star
(the plant is still filed under "low-maintenance" -- praised for surviving
neglect). Three beats, one employment metaphor, told from the plant's side.
"""

import os

LINE = "One star. Three years of unpaid oxygen, no promotion, and I'm still 'low-maintenance'."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
