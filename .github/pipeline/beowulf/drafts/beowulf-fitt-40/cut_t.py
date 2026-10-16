#!/usr/bin/env python3
"""Cut t for beowulf-fitt-40 from packet.md's lines, then merge l/i/n from unit-text.json -> units.json.
Each unit ends right after the given end-string (searched in order); t is never typed by hand."""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
packet = open(os.path.join(HERE, 'packet.md'), encoding='utf8').read()
block = re.search(r'## The lines\s+```\n(.*?)\n```', packet, re.S).group(1)
rows = [re.match(r'(\d+)  (.*)$', r).groups() for r in block.split('\n')]
nums = [int(n) for n, _ in rows]; S = '\n'.join(t for _, t in rows)
ENDS = ['lēofes monnes.', 'sægde ofer ealle:', 'wyrmes dǣdum;', 'sēoc;', 'wunde gewyrcean.', 'lēofes ond lāðes.',
        'weorðeð.', 'Frēsna land,', 'on fēðan;', 'ealdor dugoðe.', 'ungyfeðe. —', 'wæs wīde cūð,', 'Gūð-Scilfingas.',
        'ondslyht āgeaf,', 'Onelan mōdor ond Ōhtheres;', 'hlāfordlēase.', 'wērge;', 'ondlonge niht,', 'tō gamene.',
        'ǣrdæge,', 'on lāst faran.']
text = json.load(open(os.path.join(HERE, 'unit-text.json'), encoding='utf8'))
assert len(text) == len(ENDS), (len(text), len(ENDS))
pos = 0; out = []
for k, e in enumerate(ENDS):
    j = S.index(e, pos) + len(e)
    t = S[pos:j]; ln = nums[S.count('\n', 0, pos)]
    out.append({'v': True, 'ln': ln, 't': t, **text[k]})
    pos = j + 1 if j < len(S) else j
assert pos >= len(S), 'edition not fully covered'
json.dump({'sentences': out}, open(os.path.join(HERE, 'units.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print(len(out), 'units')
