#!/usr/bin/env python3
"""Make the drafting packet for a part.   usage: python3 packet.py iliad-NNN
Writes drafts/iliad-NNN/packet.md (the lines; what repeats from published parts and how it was rendered there;
what the scanner flagged), novel-forms.json (forms the glosser must write) and known-forms.json (forms of this part that
already have an entry, with the entry — to be checked against their use here, and broadened if it does not cover it)."""
import sys,os,json
import iliad_lib as O
from scan_hexameter import scan_line
pid=sys.argv[1]; P=O.part(pid); L=O.lines_of(P)
assert O.sha(L)==P['sha256'],'source does not match parts.json'
d=os.path.join(O.HERE,'drafts',pid); os.makedirs(d,exist_ok=True)
G=O.glossary()['glossary']
fs=sorted({f for l in L for f in O.forms(l['t'])})
O.jdump([f for f in fs if f not in G],os.path.join(d,'novel-forms.json'),0)
O.jdump({f:G[f] for f in fs if f in G},os.path.join(d,'known-forms.json'))
OG=O.odyssey_glossary()
O.jdump({f:OG[f] for f in fs if f not in G and f in OG},os.path.join(d,'odyssey-forms.json'))  # novel here, already glossed in the Odyssey: a starting point, checked against this use
# repeats: whole lines of this part that stand inside a published unit
pub=[]
for st in O.published_stories()+O.odyssey_stories():
    for u in st['sentences']:
        for k,ln in enumerate(u['t'].split('\n')): pub.append((O.letters_only(ln),st['id'],u))
out=[f'# {pid} — Iliad {P["cite"]} ({len(L)} lines)\n','## The lines (¶ = Monro & Allen begin a paragraph)\n','```']
for l in L: out.append(f'{"¶" if l["p"] else " "} {l["n"]:>3}  {l["t"]}')
out.append('```\n\n## Lines that already stand in a published part\n')
hit=0
for l in L:
    key=O.letters_only(l['t'])
    for k,sid,u in pub:
        if k==key and len(key.split())>=4:
            hit+=1; out.append(f'- **{P["book"]}.{l["n"]}** = a line of {sid}, unit at line {u["ln"]}:\n  - t: {u["t"]!r}\n  - l: {u["l"]!r}\n  - i: {u["i"]!r}'); break
if not hit: out.append('none')
out.append('\nLines of the Odyssey count too (Homer shares formulae across the two poems): reuse their English unless the Iliad context forbids it, and say so in new-renderings.md when you depart. Where a whole unit of yours has the same Greek as a published Iliad unit, its `l` and `i` must be identical to the published ones (the validator enforces it). Where only a line inside your unit repeats, reuse the published wording for that line as far as your sentence allows.\n\n## Scansion flags\n')
fl=[(l['n'],s['flags'],s['licences']) for l in L for s in [scan_line(l['t'],l['n'])] if any(('UNRESOLVED' in f) or ('AMBIGUOUS' in f) or ('NO FIT' in f) for f in s['flags'])]
out+= [f'- line {n}: {f}; {lic}' for n,f,lic in fl] or ['none']
out.append('\nA flagged line is scanned by hand by the reviewer; if the irregularity is real, the unit\'s note says in one sentence that the line is metrically irregular as transmitted, and where.')
open(os.path.join(d,'packet.md'),'w',encoding='utf8').write('\n'.join(out)+'\n')
print(f'packet for {pid}: {len(L)} lines, {len([f for f in fs if f not in G])} novel forms, {len([f for f in fs if f in G])} known forms, {hit} repeated lines, {len(fl)} scansion flags')
