#!/usr/bin/env python3
import sys,os; sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','odyssey'))  # translit_grc is the Odyssey's, shared
"""Shared helpers for the Meditations pipeline (set up 2026-11-21 from the Hesiod pipeline, adapted for prose).
Everything is derived from files in this repository."""
import json,re,hashlib,glob
HERE=os.path.dirname(os.path.abspath(__file__))
ROOT=os.path.abspath(os.path.join(HERE,'..','..','..'))
WORD=re.compile(r"[A-Za-zΆΈ-Ͽἀ-῿]+")      # the reader's WORD_RE, restricted to what this Greek text contains
TERMINAL='.;·,'
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
    if _SRC is None: _SRC=jload(os.path.join(HERE,'source','meditations-leopold1908.json'))
    return _SRC
def chapters_of(p):
    return [ch for ch in source()['chapters'] if ch['b']==p['book'] and p['fromCh']<=ch['c']<=p['toCh']]
def sha(chs): return hashlib.sha256(json.dumps([ch['blocks'] for ch in chs],ensure_ascii=False).encode('utf8')).hexdigest()
def forms(text): return [w.lower() for w in WORD.findall(text)]
def glossary_path(): return os.path.join(ROOT,'meditations-glossary.json')
def glossary(): return jload(glossary_path())
def published_stories():
    return [jload(f) for f in sorted(glob.glob(os.path.join(ROOT,'meditations-[0-9][0-9][0-9].json')))]
def letters_only(t): return ' '.join(WORD.findall(t)).lower()
def aesop_glossary(): return jload(os.path.join(ROOT,'aesop-glossary.json'))['glossary']
WORK=('Τὰ εἰς ἑαυτόν','Meditations (Marcus Aurelius)')
GROUP=lambda b: f'Book {b}'
SOURCE=("Marcus Aurelius, Meditations (Τὰ εἰς ἑαυτόν, “To Himself”), book {b}, chapters {cite}. Greek text of J. H. Leopold, "
 "M. Antoninus Imperator Ad se ipsum (1908), public domain; TEI from PerseusDL/canonical-greekLit tlg0562.tlg001.perseus-grc2, "
 "sha256 {teisha}. Chapter numbers are the standard ones (book.chapter). Text as printed: the editor’s supplements in ⟨ ⟩, words he "
 "deletes in [ ], † where he judges the text corrupt beyond repair; verse Marcus quotes is set as verse. "
 "Pronunciation: reconstructed Attic, after W. S. Allen, Vox Graeca — the convention used for all Greek in Lectorium; "
 "Marcus, writing in the second century AD, spoke a later Greek. Romanization: standard classical transliteration (ē/ō; th/ph/ch; "
 "y for υ, u in diphthongs; h = rough breathing; ēi/āi/ōi for iota subscript; ï for a separately sounded ι; accents omitted). "
 "All translations were made fresh from the Greek for Lectorium.")
def source_statement(p):
    return SOURCE.format(b=p['book'],cite=p['cite'],teisha=source()['teiSha256'][:16])
