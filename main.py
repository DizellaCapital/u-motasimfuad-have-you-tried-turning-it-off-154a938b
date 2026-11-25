"""Have You Tried Turning It Off? — entry program, variant 1.

One funny line a hopeless tech support agent says to a desperate
customer. The agent restarts his own computer first: cheerful,
useless, and the customer is never the butt of it. The scene is
specific — 3:12 a.m., a named customer, a thesis on the line — and
the twist lands in the last clause.

The program enforces the bounty limits — a single line of 1 to 199
characters — and writes the line to entry.txt, verifying the write
by reading it back.
"""

import os
import sys

LINE = "At 3:12 a.m., Mrs. Hartono whispered that her thesis was gone, so I smiled and asked her to hold while I restarted my own computer first."

MAX_CHARS = 199


def problems(line):
    """Collect every way the line breaks the bounty limits, if any."""
    found = []
    if not line or line.strip() != line:
        found.append("empty or padded")
    if len(line) > MAX_CHARS:
        found.append("over 199 characters")
    if "\n" in line or "\r" in line:
        found.append("more than one line")
    return found


def main():
    bad = problems(LINE)
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
