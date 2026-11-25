"""Have You Tried Turning It Off? — entry program, variant 5.

One funny line a hopeless tech support agent says to a desperate
customer. Mrs. Hartono's password expired in 2019, the system has
forgiven her — and the agent has already forgotten the new one for
her. The scene is specific — a password dead since 2019, a system
that forgives, a new password already forgotten — and the twist is
the agent doing the forgetting for her, helpfully, in advance.

The program enforces the bounty limits — a single line of 1 to 199
characters — and writes the line to entry.txt, verifying the write
by reading it back.
"""

import os
import sys

LINE = "Please hold, Mrs. Hartono — your password expired in 2019, the system has forgiven you, and I have already forgotten the new one for you."

MAX_CHARS = 199


def issues(line):
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
    bad = issues(LINE)
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
