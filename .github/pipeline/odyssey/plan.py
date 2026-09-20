#!/usr/bin/env python3
"""Regenerate plan.md from parts.json."""
import odyssey_lib as O, os
P=O.parts()['parts']; done=sum(p['status']=='published' for p in P)
out=[f'# Odyssey — plan\n\n{done} of {len(P)} parts published. Parts end only where Murray begins a paragraph.\n','| part | cite | lines | status |','|---|---|---|---|']
out+=[f'| {p["id"]} | {p["cite"]} | {p["lines"]} | {p["status"]} |' for p in P]
open(os.path.join(O.HERE,'plan.md'),'w',encoding='utf8').write('\n'.join(out)+'\n'); print(done,'of',len(P))
