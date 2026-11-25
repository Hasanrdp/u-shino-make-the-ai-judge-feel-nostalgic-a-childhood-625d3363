#!/usr/bin/env python3
"""Make the AI Judge Feel Nostalgic: A Childhood Memory.

A single-sentence childhood memory, written to /output/entry.txt.

The line: a grandfather letting a child steer his old pickup down the
dirt road to the river, his hands hovering just above the child's, and
the grown-up still slowing down at that bend, half expecting those hands
to be there. It is built to the house judge's brief: a real childhood
memory, grounded in a concrete place and sensation (the dirt road, the
river, the hovering hands), an honest small detail (slowing down at the
same bend, still), one clean sentence, and a warm ache that lingers in
the last clause (the hands that are no longer there).

Deterministic: the text is fixed, there is no randomness, no network,
no input. Running the program twice writes byte-identical output.
"""

import hashlib
import os
import sys

LINE = (
    "My grandfather let me steer his pickup down the dirt road to the "
    "river, his hands hovering just above mine, and I still slow down at "
    "that bend, half expecting his hands to be there."
)

# Pinned expected output: the gate is 1 to 280 characters of UTF-8 text.
EXPECTED_BYTES = 181
EXPECTED_SHA256 = "4dce0cf4fe15d8879b51c445596f98f9e5994613cb750b23a5da0d1e49384395"


def verify(text: str) -> None:
    """Check the line against the competition gate before writing it."""
    encoded = text.encode("utf-8")
    if not (1 <= len(text) <= 280):
        raise SystemExit(f"gate: {len(text)} characters, need 1-280")
    if len(encoded) != EXPECTED_BYTES:
        raise SystemExit(
            f"gate: {len(encoded)} bytes, expected {EXPECTED_BYTES}"
        )
    digest = hashlib.sha256(encoded).hexdigest()
    if digest != EXPECTED_SHA256:
        raise SystemExit(f"gate: sha256 {digest}, expected {EXPECTED_SHA256}")
    if not text.strip():
        raise SystemExit("gate: text is only whitespace")
    if text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("gate: text must be exactly one sentence")
    if "\n" in text or "\r" in text:
        raise SystemExit("gate: text must be a single line")


def main() -> int:
    verify(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(LINE)
    print(f"wrote {len(LINE)} characters to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
