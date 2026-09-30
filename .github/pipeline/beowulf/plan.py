#!/usr/bin/env python3
"""Regenerate plan.md from parts.json."""
import beowulf_lib as B, os
P = B.parts()['parts']; done = sum(p['status'] == 'published' for p in P)
out = [f'# Beowulf — plan\n\n{done} of {len(P)} parts published. One part per fitt, as Klaeber numbers them.\n',
       '| part | fitt | lines | status |', '|---|---|---|---|']
out += [f'| {p["id"]} | {p["fitt"]} · {p["name"]} | {p["from"]}–{p["to"]} | {p["status"]} |' for p in P]
open(os.path.join(B.HERE, 'plan.md'), 'w', encoding='utf8').write('\n'.join(out) + '\n'); print(done, 'of', len(P))
