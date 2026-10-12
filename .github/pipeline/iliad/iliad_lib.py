#!/usr/bin/env python3
import sys,os; sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','odyssey'))  # scan_hexameter, translit_grc are the Odyssey's, shared
"""Shared helpers for the Iliad pipeline. Everything is derived from files in this repository."""
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
    if _SRC is None: _SRC=jload(os.path.join(HERE,'source','iliad-monro-allen1920.json'))
    return _SRC
def lines_of(p):
    """the part's lines, in the order the edition prints them """
    b=source()['books'][str(p['book'])]
    i0=next(i for i,l in enumerate(b) if l['n']==p['from']); i1=next(i for i,l in enumerate(b) if l['n']==p['to'])
    return b[i0:i1+1]
def sha(lines): return hashlib.sha256('\n'.join(l['t'] for l in lines).encode('utf8')).hexdigest()
def forms(text): return [w.lower() for w in WORD.findall(text)]
def glossary_path(): return os.path.join(ROOT,'iliad-glossary.json')
def glossary(): return jload(glossary_path())
def published_stories():
    out=[]
    for f in sorted(glob.glob(os.path.join(ROOT,'iliad-[0-9][0-9][0-9].json'))): out.append(jload(f))
    return out
def letters_only(t): return ' '.join(WORD.findall(t)).lower()
# the Odyssey's published parts: Homer's formulae are shared, so the packet shows where an Iliad line already stands there
ODY=os.path.join(ROOT,'.github','pipeline','odyssey')
def odyssey_stories():
    return [jload(f) for f in sorted(glob.glob(os.path.join(ROOT,'odyssey-[0-9][0-9][0-9].json')))]
def odyssey_glossary(): return jload(os.path.join(ROOT,'odyssey-glossary.json'))['glossary']
# work-level constants (the build takes them from here, not from a published part, so the first part can be built)
WORK='Ἰλιάς'; WORK_EN='The Iliad (Homer)'
SOURCE=("Homer, The Iliad, Greek text of D. B. Monro and T. W. Allen, Homeri Opera, tomi I–II, 3rd ed. "
 "(Oxford Classical Texts; Oxford: Clarendon Press, 1920), public domain; TEI from PerseusDL/canonical-greekLit "
 "tlg0012.tlg001.perseus-grc2, sha256 {teisha}. Text as printed: the edition sets no quotation marks round speeches, and none are added. "
 "Pronunciation: reconstructed Attic, after W. S. Allen, Vox Graeca — an admitted convention; Homer's own pronunciation was older "
 "and is not recoverable in detail. Romanization: standard classical transliteration (ē/ō; th/ph/ch; y for υ, u in diphthongs; "
 "h = rough breathing; ēi/āi/ōi for iota subscript; ï for a separately sounded ι; accents omitted). Scansion: made by program from "
 "the text and checked; it shows one defensible reading of each line, and the notes say where a line is irregular. "
 "All translations were made fresh from the Greek for Lectorium.")
def source_statement(): return SOURCE.format(teisha=source()['teiSha256'][:16])
