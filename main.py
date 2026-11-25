"""Monday Morning Punchlines — writes one joke about Monday mornings.

The program writes exactly one line of text (no trailing newline) to
``entry.txt`` inside the output directory: ``$MAKEFUN_OUTPUT_DIR`` when set,
otherwise ``/output``. It never deletes the output directory itself.
"""

import os

JOKE = (
    "Monday morning is the only time my bed and my boss both want me, "
    "and somehow I'm disappointing both."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
