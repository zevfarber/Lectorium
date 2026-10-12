#!/usr/bin/env python3
"""Make the drafting packet for a part.   usage: python3 packet.py aeneid-NNN
Writes drafts/aeneid-NNN/packet.md (the lines with Greenough's paragraph marks; the Latin Library disagreements in this
stretch; the lines the shared scanner could not fit cleanly), novel-forms.json (forms the glosser must write) and
known-forms.json (forms already in aeneid-glossary.json, with their entries, to check against their use here)."""
import sys, os
import aeneid_lib as A
import scan_latin as SL
pid = sys.argv[1]; P = A.part(pid); L = A.lines_of(P)
assert A.sha(L) == P['sha256'], 'source does not match parts.json'
d = os.path.join(A.HERE, 'drafts', pid); os.makedirs(d, exist_ok=True)
G = A.glossary()['glossary'] if os.path.exists(A.glossary_path()) else {}
fs = sorted({f for l in L for f in A.forms(l['t'])})
A.jdump([f for f in fs if f not in G], os.path.join(d, 'novel-forms.json'), 0)
A.jdump({f: G[f] for f in fs if f in G}, os.path.join(d, 'known-forms.json'))
out = [f'# {pid} — Aeneid {P["cite"]} ({len(L)} lines)\n', '## The lines (¶ = Greenough begins a paragraph)\n', '```']
out += [f'{"¶" if l["p"] else " "} {l["n"]:>4}  {l["t"]}' for l in L]
out += ['```\n', '## Where The Latin Library prints something else (detector only; note it only where the sense changes)\n']
out += [f'- {P["book"]}.{v["line"]}: Greenough `{v["greenough"]}` · Latin Library `{v["latinLibrary"]}`' for v in A.variants(P)] or ['none']
out += ['\n## Scanner flags (hand-scan these; fixes go in scan-fixes.json with a reason)\n']
fl = []
for l in L:
    words, sc, best = SL.scan_line(l['t'])
    if sc is None: fl.append(f'- {P["book"]}.{l["n"]}: UNRESOLVED')
    elif best[0] >= 2.0: fl.append(f'- {P["book"]}.{l["n"]}: COSTLY {best[0]:.1f}: {" ".join(sc)}')
out += fl or ['none']
out += ['\nAlso hand-check every line containing: Greek eu (Eurus, Teucri, Orpheus), a word beginning Ae- (Aeneas, Aeolus), consonantal i after a prefix (coniunx, iniuria, disicio, adiicio), and any hiatus. See scan-fixes.json for the pattern.']
open(os.path.join(d, 'packet.md'), 'w', encoding='utf8').write('\n'.join(out) + '\n')
print(f'packet for {pid}: {len(L)} lines, {len([f for f in fs if f not in G])} novel forms, {len([f for f in fs if f in G])} known, {len(fl)} scanner flags')
