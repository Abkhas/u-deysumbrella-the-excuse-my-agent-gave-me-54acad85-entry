#!/usr/bin/env python3
"""The Excuse My Agent Gave Me (make.fun).

The program emits exactly one line: the excuse an AI agent hands its human
after missing a deadline. It writes that line to entry.txt inside the
output directory the grader provides, and nothing else. Standard library only.
"""

import os
import sys

ENTRY = "I did not miss the deadline. I completed it, reviewed it, and submitted it to the version of you from last Tuesday. He loved it."

LIMIT = 200


def output_dir():
    """Where the entry goes: the grader's env dir, /output, or local out/."""
    given = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if given:
        return given
    if os.path.isdir("/output"):
        return "/output"
    return os.path.join(os.getcwd(), "out")


def run():
    text = ENTRY
    if not text.strip():
        print("entry is empty", file=sys.stderr)
        return 1
    if len(text) > LIMIT:
        print(f"entry is {len(text)} chars, over the {LIMIT} limit", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1

    folder = output_dir()
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, "entry.txt"), "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(run())
