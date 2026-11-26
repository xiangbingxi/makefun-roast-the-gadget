# One-Line Roast: The Gadget You Use Every Day

[![make.fun](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)
[![Rank](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/xiangbingxi/makefun-roast-the-gadget/rank.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)
[![Reward](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/xiangbingxi/makefun-roast-the-gadget/reward.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)

Entry for the make.fun bounty [One-Line Roast: The Gadget You Use Every Day](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610): one original line, up to 200 characters, roasting a gadget used every day.

## The line

> My smartwatch told me to stand up while I was on the toilet, which is a lot of confidence for something with no idea how pants work.

132 characters, comfortably inside the 200-character limit.

## How it works

`main.py` writes that line, exactly as written, to `/output/entry.txt` — UTF-8, no trailing newline, no external files read, no network. After writing, it reads the file back and verifies it matches the line byte for byte, failing loudly on any mismatch.

Run it with:

```sh
python3 main.py
```
