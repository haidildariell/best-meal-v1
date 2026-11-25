#!/usr/bin/env python3
"""Entry for "The Best Meal You Ever Had" (make.fun).

Writes one sentence about the best meal to /output/entry.txt.
"""

import os

SENTENCE = "The 2019 rendang at a roadside stall in Bukittinggi arrived still bubbling in its clay pot, and I ate it standing up because every plastic chair was taken."

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")

MIN_LEN = 1
MAX_LEN = 200


def validate_sentence(sentence):
    """One clean sentence, 1-200 chars, no title or explanation."""
    text = sentence.strip()
    if not MIN_LEN <= len(text) <= MAX_LEN:
        raise ValueError(f"sentence must be {MIN_LEN}-{MAX_LEN} chars, got {len(text)}")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    return text


def write_entry(sentence):
    text = validate_sentence(sentence)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    return text


def main():
    text = write_entry(SENTENCE)
    print(f"Wrote {len(text)} characters to {OUTPUT_FILE}")
    print(text)


if __name__ == "__main__":
    main()
