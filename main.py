#!/usr/bin/env python3
"""The Robot Apology — writes a two-line robot confession to /output/entry.txt.

Line 1: the robot apologises in a single sentence for one specific mistake.
Line 2: one sentence on what it learned and what it will do differently,
the lesson following directly from that exact mistake.
Deterministic, stdlib only, no network, no randomness.
"""

import os

LINE_1 = (
    "I am sorry I watered the orchid on the windowsill with mop water, "
    "and it wilted by morning."
)

LINE_2 = (
    "I have learned that not every jug holds water, so from now on I will "
    "read the label on each container before I pour a single drop."
)


def main() -> None:
    text = LINE_1 + "\n" + LINE_2 + "\n"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
