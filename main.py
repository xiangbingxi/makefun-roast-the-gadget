"""Write the one-line roast to /output/entry.txt.

Writes the entry exactly as given: UTF-8, no trailing newline,
no external files read, no network. After writing, reads the file
back and verifies it matches the entry byte for byte; any mismatch
or out-of-range length makes the program fail loudly instead of
leaving a bad entry behind.
"""

import os
import sys

ENTRY = "My smartwatch told me to stand up while I was on the toilet, which is a lot of confidence for something with no idea how pants work."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ENTRY:
        print("error: /output/entry.txt does not match ENTRY", file=sys.stderr)
        sys.exit(1)
    if not 1 <= len(written) <= 200:
        print(
            "error: entry length %d is outside the 1-200 character limit"
            % len(written),
            file=sys.stderr,
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
