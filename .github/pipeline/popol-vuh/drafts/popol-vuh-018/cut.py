#!/usr/bin/env python3
"""Cut packet.md's pinned paragraphs into pieces (cut.json); t is never retyped.

A piece ends at ; always, and at . ? ! (with any closing ”) unless the next word starts lower case
(a speech tag such as xꜭha follows the closing quote and stays with its speech)."""
import json, re, sys
sys.path.insert(0, '/home/user/Lectorium/.github/scripts')
from wordre import WORD_RE

def paragraphs(path='packet.md'):
    txt = open(path, encoding='utf-8').read()
    body = txt.split('## Establishment log')[0]
    paras = re.findall(r'^¶\d+\n(.+?)(?=\n\n|\Z)', body, re.S | re.M)
    return [re.sub(r'\s+', ' ', p).strip() for p in paras]

def cut(p):
    pieces, start = [], 0
    for m in re.finditer(r'(;|[.?!]”?)\s+', p):
        nxt = p[m.end():m.end() + 1]
        if m.group(1) != ';' and nxt.islower():
            continue
        pieces.append(p[start:m.start(1) + len(m.group(1))])
        start = m.end()
    pieces.append(p[start:])
    assert ' '.join(pieces) == p
    return pieces

if __name__ == '__main__':
    out = []
    for i, p in enumerate(paragraphs(), 1):
        for j, t in enumerate(cut(p)):
            w = WORD_RE.findall(t)
            out.append({'para': i, 'first_in_para': j == 0, 't': t, 'n_words': len(w), 'words': w})
    json.dump(out, open('cut.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    for k, x in enumerate(out):
        print(k, x['para'], x['t'])
