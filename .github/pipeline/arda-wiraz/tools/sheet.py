#!/usr/bin/env python3
"""python3 tools/sheet.py <leaf> [<leaf> ...]   -> drafts/_sheets/n<leaf>-a.png, -b.png …
Each printed line of the page as a strip, word shapes boxed and numbered from the right. Read the sheets to
write a part's cut file (see runbook.md, "The cut file")."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pagelib
out = os.path.join(pagelib.HERE, 'drafts', '_sheets')
for leaf in sys.argv[1:]:
    files, counts = pagelib.sheets(int(leaf), out)
    print(f'n{leaf}: {len(counts)} lines, shapes per line {counts}')
    for f in files:
        print('  ', os.path.relpath(f, pagelib.HERE))
