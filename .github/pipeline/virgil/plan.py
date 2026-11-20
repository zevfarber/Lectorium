#!/usr/bin/env python3
"""Regenerate plan.md from parts.json."""
import virgil_lib as A, os
P = A.parts()['parts']; done = sum(p['status'] == 'published' for p in P)
out = [f'# Eclogues and Georgics — plan\n\n{done} of {len(P)} parts published. Each Eclogue is one part; the Georgics are cut at the Perseus sense sections.\n',
       '| part | work | cite | lines | status |', '|---|---|---|---|---|']
out += [f'| {p["id"]} | {p["work"]} | {p["cite"]} | {p["lines"]} | {p["status"]} |' for p in P]
open(os.path.join(A.HERE, 'plan.md'), 'w', encoding='utf8').write('\n'.join(out) + '\n'); print(done, 'of', len(P))
