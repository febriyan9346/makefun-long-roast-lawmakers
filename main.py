#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one satirical sentence (at most 320 characters) to
/output/entry.txt. Deterministic, standard library only, no network.
"""

import os

LINE = (
    "The senator who wrote the AI Safety Act held up his own bill "
    "\u2014 a photograph of a printout \u2014 and asked the witness, "
    "on the record, to show him how to save it as a PDF."
)


def main() -> None:
    text = LINE.strip()
    if not 1 <= len(text) <= 320:
        raise SystemExit(f"entry must be 1-320 characters, got {len(text)}")
    if text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("entry must be exactly one sentence")
    if any(ord(ch) < 0x20 for ch in text):
        raise SystemExit("entry must not contain control characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
