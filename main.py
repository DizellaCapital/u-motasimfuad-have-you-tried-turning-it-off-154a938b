"""Have You Tried Turning It Off? — entry program, variant 3.

One funny line a hopeless tech support agent says to a desperate
customer. Mr. Adi's voice is shaking, so the agent turns the fix
into something they do together: unplug the printer, count to ten,
and pretend the blinking red light is applause. The scene is
specific — a shaking voice, a named customer, a printer counting
down with them — and the twist is the applause: the error light
gets a round of it.

The program enforces the bounty limits — a single line of 1 to 199
characters — and writes the line to entry.txt, verifying the write
by reading it back.
"""

import os
import sys

LINE = "Your voice is shaking, Mr. Adi — let's unplug the printer together, count to ten, and I'll pretend the blinking red light is applause."

MAX_CHARS = 199


def defects(line):
    """List every way the line breaks the bounty limits, if any."""
    bad = []
    if not line or line.strip() != line:
        bad.append("empty or padded")
    if len(line) > MAX_CHARS:
        bad.append("over 199 characters")
    if "\n" in line or "\r" in line:
        bad.append("more than one line")
    return bad


def main():
    bad = defects(LINE)
    if bad:
        print("invalid entry: " + "; ".join(bad), file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    with open(path, encoding="utf-8") as f:
        if f.read() != LINE:
            print("read-back mismatch", file=sys.stderr)
            return 1
    print("wrote %d characters to %s" % (len(LINE), path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
