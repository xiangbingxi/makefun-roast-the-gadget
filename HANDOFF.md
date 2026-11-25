# Handoff — One-Line Roast: The Gadget You Use Every Day

Competition: `u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610`
($5, deadline 2026-11-26 23:00 CST / 15:00 UTC, limit 200 characters)

## The entry

> My smartwatch told me to stand up while I was on the toilet, which is a lot of confidence for something with no idea how pants work.

- Characters: 132 (limit 200 — inside by 68)
- Bytes: 132 (all ASCII)
- SHA-256 of `/output/entry.txt`: `1dd09468bceb61f5d5ee723458420ab1c27912b44f768f7724b5e76cab1ff69c`
- The line is the user's own wording, submitted exactly as given, one character unchanged.

## How it works

`main.py` writes the line to `/output/entry.txt` (UTF-8, no trailing newline,
no external files read, no network). It was written in two passes: the first
version wrote the file and ran clean; the second version adds a real
improvement — after writing, it reads `/output/entry.txt` back, checks it
matches the line byte for byte, checks the length is within 1–200 characters,
and exits non-zero with an error message on any mismatch.

## Verification

- `python3 main.py` run A: exit 0
- `python3 main.py` run B: exit 0
- `cmp` of the two runs' outputs: byte-identical
- `entry.txt`: 132 bytes / 132 characters, sha256 matches the expected hash
  of the line computed independently
- `prompt.txt` (132 bytes) is byte-identical to `/output/entry.txt`
- `LICENSE` is MIT and carries `SPDX-License-Identifier: MIT`
- `README.md` links the bounty page and carries all three official make.fun badges
- `.makefun/owner.json` holds the wallet `6t8k8dD19c2zDMiZ1VNsbRDWaSNSedmQQB6A15hy3XFx`

## Files

- `main.py`
- `LICENSE`
- `README.md`
- `prompt.txt`
- `.makefun/owner.json`
- `HANDOFF.md` (this file)

Not submitted, no GitHub repository created, no bundle touched — ready for the
parent agent to package and submit.
