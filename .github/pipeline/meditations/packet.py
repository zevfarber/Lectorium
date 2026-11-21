#!/usr/bin/env python3
"""Make the drafting packet for a part.   usage: python3 packet.py meditations-NNN
Writes drafts/meditations-NNN/packet.md (the text, chapter by chapter and block by block; sentences that already stand in a
published part, with their English), novel-forms.json (forms the glosser must write), known-forms.json (forms that already
have an entry, with the entry — checked against their use here, broadened if it does not cover it) and aesop-forms.json
(forms new here that the Aesop glossary has: a starting point, checked against this use)."""
import sys,os
import med_lib as O
pid=sys.argv[1]; P=O.part(pid); C=O.chapters_of(P)
assert O.sha(C)==P['sha256'],'source does not match parts.json'
d=os.path.join(O.HERE,'drafts',pid); os.makedirs(d,exist_ok=True)
G=O.glossary()['glossary']
fs=sorted({f for ch in C for bl in ch['blocks'] for f in O.forms(bl['t'])})
O.jdump([f for f in fs if f not in G],os.path.join(d,'novel-forms.json'),0)
O.jdump({f:G[f] for f in fs if f in G},os.path.join(d,'known-forms.json'))
AG=O.aesop_glossary()
O.jdump({f:AG[f] for f in fs if f not in G and f in AG},os.path.join(d,'aesop-forms.json'))
out=[f'# {pid} — Meditations {P["cite"]} ({P["chapters"]} chapters, {P["words"]} words)\n',
     'Each chapter begins a paragraph. Blocks are separated by a blank line; a unit never crosses a block. '
     '[verse] marks a quotation Leopold sets as verse (its units are v:true and keep its line breaks in l); '
     '[subscription] marks the line Leopold prints at a book\'s end.\n']
for ch in C:
    out.append(f'## {ch["b"]}.{ch["c"]}\n')
    for bl in ch['blocks']:
        tag=' [verse]' if bl.get('v') else ' [subscription]' if bl.get('sub') else ''
        out.append(f'```{tag}\n{bl["t"]}\n```\n')
# sentences that already stand in a published unit (Marcus repeats himself)
pub={}
for st in O.published_stories():
    for u in st['sentences']:
        k=O.letters_only(u['t'])
        if len(k.split())>=5: pub.setdefault(k,(st['id'],u))
out.append('## Sentences that already stand in a published part\n')
hit=0
for ch in C:
    for bl in ch['blocks']:
        for k,(sid,u) in pub.items():
            if k in O.letters_only(bl['t']):
                hit+=1; out.append(f'- **{ch["b"]}.{ch["c"]}** contains a unit of {sid}:\n  - t: {u["t"]!r}\n  - l: {u["l"]!r}\n  - i: {u["i"]!r}')
if not hit: out.append('none')
out.append('\nWhere a whole unit of yours has the same Greek as a published unit, its `l` and `i` must be identical to the published ones (the validator enforces it).')
open(os.path.join(d,'packet.md'),'w',encoding='utf8').write('\n'.join(out)+'\n')
print(f'packet for {pid}: {P["chapters"]} chapters, {len([f for f in fs if f not in G])} novel forms, {len([f for f in fs if f in G])} known forms, {hit} repeats')
