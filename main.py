#!/usr/bin/env python3
"""Deadpan Forecasts for Cities That Do Not Exist.

Writes the tournament-champion forecast line to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Champion (136 chars, chosen by a 16-candidate internal pairwise
tournament judged against the published judge brief, in weight order:
on-subject forecast, funnier joke, more vivid detail, believable
broadcast tone, use of characters):
"""

import os
import sys

ENTRY = (
    "Hailstones the size of golf balls are forecast for Pebbleford "
    "this evening; the golf club has asked that none be returned "
    "to the course."
)


def output_path():
    """Return the entry output path from the environment."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def validate(text):
    """Check the entry against the gate: UTF-8, 1-160 chars, not blank."""
    if not text or not text.strip():
        raise ValueError("entry is empty or only whitespace")
    if len(text) > 160:
        raise ValueError(f"entry is {len(text)} characters, over the 160 limit")
    text.encode("utf-8")
    return text


def main():
    """Validate the entry and write it to the output path."""
    text = validate(ENTRY)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
