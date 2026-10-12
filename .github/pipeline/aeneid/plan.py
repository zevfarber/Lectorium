#!/usr/bin/env python3
"""Regenerate plan.md from parts.json."""
import aeneid_lib as A, os
P = A.parts()['parts']; done = sum(p['status'] == 'published' for p in P)
out = [f'# Aeneid — plan\n\n{done} of {len(P)} parts published. Parts end only where Greenough begins a paragraph (an indented line).\n',
       '| part | book | cite | lines | status |', '|---|---|---|---|---|']
out += [f'| {p["id"]} | {p["book"]} | {p["cite"]} | {p["lines"]} | {p["status"]} |' for p in P]
open(os.path.join(A.HERE, 'plan.md'), 'w', encoding='utf8').write('\n'.join(out) + '\n'); print(done, 'of', len(P))
