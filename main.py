#!/usr/bin/env python3
"""Monday Morning Punchlines.

A tiny joke writer: it drops one Monday-morning punchline into a
plain text file so the entry can be graded. No arguments, no
dependencies, no surprises -- just one line, exactly as written.
"""

import os

JOKE = "Monday morning is the only time my bed and my boss both want me, and somehow I'm disappointing both."


def main():
    """Write the punchline to entry.txt, with no trailing newline."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(JOKE)


if __name__ == "__main__":
    main()

