#!/usr/bin/env python3
"""Shared helpers for the Odyssey pipeline. Everything is derived from files in this repository."""
import json,re,hashlib,os,glob
HERE=os.path.dirname(os.path.abspath(__file__))
ROOT=os.path.abspath(os.path.join(HERE,'..','..','..'))
# the reader's WORD_RE, restricted to what Greek text can contain (index.html: WORD_CLASS)
WORD=re.compile(r"[A-Za-zΆΈ-Ͽἀ-῿]+")
TERMINAL='.;·'
def jload(p): return json.load(open(p,encoding='utf8'))
def jdump(o,p,indent=1): open(p,'w',encoding='utf8').write(json.dumps(o,ensure_ascii=False,indent=indent))
def parts(): return jload(os.path.join(HERE,'parts.json'))
def part(pid):
    for p in parts()['parts']:
        if p['id']==pid: return p
    raise SystemExit('no such part: '+pid)
_SRC=None
def source():
    global _SRC
    if _SRC is None: _SRC=jload(os.path.join(HERE,'source','odyssey-murray1919.json'))
    return _SRC
def lines_of(p):
    """the part's lines, in the order the edition prints them (3.304/305 and 14.63/64 are printed transposed)"""
    b=source()['books'][str(p['book'])]
    i0=next(i for i,l in enumerate(b) if l['n']==p['from']); i1=next(i for i,l in enumerate(b) if l['n']==p['to'])
    return b[i0:i1+1]
def sha(lines): return hashlib.sha256('\n'.join(l['t'] for l in lines).encode('utf8')).hexdigest()
def forms(text): return [w.lower() for w in WORD.findall(text)]
def glossary_path(): return os.path.join(ROOT,'odyssey-glossary.json')
def glossary(): return jload(glossary_path())
def published_stories():
    out=[]
    for f in sorted(glob.glob(os.path.join(ROOT,'odyssey-[0-9][0-9][0-9].json'))): out.append(jload(f))
    return out
def letters_only(t): return ' '.join(WORD.findall(t)).lower()
