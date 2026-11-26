#!/usr/bin/env python3
"""One-Liner Laughs entry: writes a single joke line to entry.txt.

Deterministic, stdlib only, no network. The output path is
$MAKEFUN_OUTPUT_DIR/entry.txt, falling back to /output/entry.txt.
"""

import os

JOKE = "My fitness tracker hit 10,000 steps and immediately requested a transfer to someone who actually walks."


def main() -> None:
    # Kit gate: entry.txt must be UTF-8 text of 1 to 200 characters,
    # not only white space. Fail loudly here rather than at the gate.
    if not 1 <= len(JOKE) <= 200 or not JOKE.strip():
        raise ValueError("JOKE must be 1-200 non-blank characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
