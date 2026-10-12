#!/usr/bin/env python3
"""Shared helpers for the Aeneid pipeline. Everything is derived from files in this repository."""
import json, os, re, hashlib, glob, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, '.github', 'scripts'))
from wordre import WORD_RE            # the reader's own word splitter (one copy, mirrors reader.html)
TERMINAL = '.;:?!'
def jload(p): return json.load(open(p, encoding='utf8'))
def jdump(o, p, indent=1): open(p, 'w', encoding='utf8').write(json.dumps(o, ensure_ascii=False, indent=indent))
def parts(): return jload(os.path.join(HERE, 'parts.json'))
def part(pid):
    for p in parts()['parts']:
        if p['id'] == pid: return p
    raise SystemExit('no such part: ' + pid)
_SRC = None
def source():
    global _SRC
    if _SRC is None: _SRC = jload(os.path.join(HERE, 'source', 'aeneid-greenough.json'))
    return _SRC
def lines_of(p):
    b = source()['books'][str(p['book'])]
    i0 = next(i for i, l in enumerate(b) if l['n'] == p['from']); i1 = next(i for i, l in enumerate(b) if l['n'] == p['to'])
    return b[i0:i1 + 1]
def sha(lines): return hashlib.sha256('\n'.join(l['t'] for l in lines).encode('utf8')).hexdigest()
def forms(text): return [w.lower() for w in WORD_RE.findall(text)]
def glossary_path(): return os.path.join(ROOT, 'aeneid-glossary.json')
def glossary(): return jload(glossary_path())
def published_stories(): return [jload(f) for f in sorted(glob.glob(os.path.join(ROOT, 'aeneid-[0-9][0-9][0-9].json')))]
def variants(p):
    v = jload(os.path.join(HERE, 'source', 'variants-latinlibrary.json')).get(str(p['book']), [])
    return [x for x in v if p['from'] <= x['line'] <= p['to']]
def cut(p, ends):
    """ends: [(line, closing text)] -> list of (t, ln). t is sliced from the edition, never typed."""
    L = lines_of(p); S = '\n'.join(l['t'] for l in L); nums = [l['n'] for l in L]
    starts = []; acc = 0
    for l in L: starts.append(acc); acc += len(l['t']) + 1
    out, pos = [], 0
    for ln, tail in ends:
        li = nums.index(ln); lend = starts[li] + len(L[li]['t'])
        k = S.rfind(tail, pos, lend)
        if k < 0 or S[pos:lend].count(tail) == 0: raise SystemExit(f'cannot find {tail!r} on line {ln}')
        end = k + len(tail); t = S[pos:end]
        startline = nums[max(i for i, s in enumerate(starts) if s <= pos)]
        out.append((t, startline)); pos = end
        while pos < len(S) and S[pos] in ' \n': pos += 1
    if pos != len(S): raise SystemExit(f'units stop before the end of the part (at char {pos})')
    return out
