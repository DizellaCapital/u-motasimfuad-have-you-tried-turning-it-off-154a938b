"""Have You Tried Turning It Off? — entry program, variant 2.

One funny line a hopeless tech support agent says to a desperate
customer. The router has been unplugged since Tuesday and the agent
can see that from his desk — so he asks the customer to unplug it
again, slowly, like it means something. The scene is specific —
a router dead since Tuesday, an agent who can already see it —
and the twist is the ritual: do the useless thing again, but
with feeling.

The program enforces the bounty limits — a single line of 1 to 199
characters — and writes the line to entry.txt, verifying the write
by reading it back.
"""

import os
import sys

LINE = "Your router has been unplugged since Tuesday, sir — I can see that from here, which is why I'll ask you to unplug it again, slowly, like it means something."

MAX_CHARS = 199


def violations(line):
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
    bad = violations(LINE)
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
