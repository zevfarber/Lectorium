#!/usr/bin/env python3
"""Make the drafting packet for a part.   usage: python3 packet.py beowulf-fitt-NN
Writes drafts/<id>/packet.md (the lines with Klaeber's numbers; his emendation italics; low-confidence readings; the
apparatus for the part's pages; any boundary note), novel-forms.json (forms the glosser must write) and known-forms.json
(forms of this part that already have an entry, with the entry — to be checked against their use here)."""
import sys, os
import beowulf_lib as B
pid = sys.argv[1]; P = B.part(pid); L = B.lines_of(P)
if B.sha(L) != P['sha256']: sys.exit('source does not match parts.json sha256 — stop and write it to QUESTIONS.md')
d = os.path.join(B.HERE, 'drafts', pid); os.makedirs(d, exist_ok=True)
G = B.glossary()['glossary']
fs = sorted({f for l in L for f in B.forms(l['t'])})
B.jdump([f for f in fs if f not in G], os.path.join(d, 'novel-forms.json'), 0)
B.jdump({f: G[f] for f in fs if f in G}, os.path.join(d, 'known-forms.json'))
S = B.source()
out = [f"# {pid} — {P['part']}\n", f"{P['lines']} lines, Klaeber printed pages {', '.join(map(str, P['pages']))}.\n"]
if P.get('boundary'): out.append(f"**Boundary:** {P['boundary']}\n")
out += ['## The lines\n', '```']
for l in L: out.append(f"{l['n']:>4}  {l['t']}")
out.append('```\n')
it = [(l['n'], i) for l in L for i in l.get('italics', [])]
out.append("## Letters Klaeber prints in italic (his sign that a word is altered by emendation)\n")
out += [f"- line {n}: {i.get('word')} — italic: {i.get('italic_part')}" for n, i in it] or ['none']
out.append("\nAn italic letter means Klaeber changed the manuscript there. The apparatus below usually gives the manuscript "
           "reading; where it matters for the sense, the unit's note says what the manuscript has.\n")
var = [(l['n'], l['variant_note']) for l in L if l.get('variant')]
out.append("## Readings settled with low confidence at transcription\n")
out += [f"- line {n}: {v}" for n, v in var] or ['none']
out.append("\n## Klaeber's apparatus for these pages (transcribed once, best effort — check before quoting)\n")
for p in P['pages']:
    out.append(f"### page {p}\n\n{S['apparatus'].get(str(p), '(none)')}\n")
open(os.path.join(d, 'packet.md'), 'w', encoding='utf8').write('\n'.join(out) + '\n')
print(f"packet for {pid}: {len(L)} lines, {len([f for f in fs if f not in G])} novel forms, "
      f"{len([f for f in fs if f in G])} known forms, {len(it)} italic spots, {len(var)} low-confidence lines")
