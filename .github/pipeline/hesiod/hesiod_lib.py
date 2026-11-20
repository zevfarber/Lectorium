#!/usr/bin/env python3
import sys,os; sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','odyssey'))  # scan_hexameter, translit_grc are the Odyssey's, shared
"""Shared helpers for the Hesiod pipeline (cloned from the Iliad's, 2026-11-20). Everything is derived from files in this repository."""
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
    if _SRC is None: _SRC=jload(os.path.join(HERE,'source','hesiod-evelyn-white1914.json'))
    return _SRC
def lines_of(p):
    """the part's lines, in the order the edition prints them """
    b=source()['books'][str(p['book'])]
    return b[p['fromIdx']:p['toIdx']+1]     # by index: Evelyn-White prints some lines transposed, and Th. 929a-t share the number 929
def sha(lines): return hashlib.sha256('\n'.join(l['t'] for l in lines).encode('utf8')).hexdigest()
def forms(text): return [w.lower() for w in WORD.findall(text)]
def glossary_path(): return os.path.join(ROOT,'hesiod-glossary.json')
def glossary(): return jload(glossary_path())
def published_stories():
    out=[]
    for f in sorted(glob.glob(os.path.join(ROOT,'hesiod-[0-9][0-9][0-9].json'))): out.append(jload(f))
    return out
def letters_only(t): return ' '.join(WORD.findall(t)).lower()
# the Odyssey's published parts: Homer's formulae are shared, so the packet shows where an Iliad line already stands there
ODY=os.path.join(ROOT,'.github','pipeline','odyssey')
def odyssey_stories():   # Homer's published parts, both poems: Hesiod shares the epic formulae
    return [jload(f) for f in sorted(glob.glob(os.path.join(ROOT,'odyssey-[0-9][0-9][0-9].json'))+glob.glob(os.path.join(ROOT,'iliad-[0-9][0-9][0-9].json')))]
def odyssey_glossary(): return jload(os.path.join(ROOT,'odyssey-glossary.json'))['glossary']
# work-level constants (the build takes them from here, not from a published part, so the first part can be built)
WORKS={'Th':('Θεογονία','Theogony (Hesiod)'),'WD':('Ἔργα καὶ Ἡμέραι','Works and Days (Hesiod)')}
SOURCE=("Hesiod, {title}, Greek text of H. G. Evelyn-White, Hesiod, the Homeric Hymns and Homerica (Loeb Classical Library; "
 "London: Heinemann, 1914), public domain; TEI from PerseusDL/canonical-greekLit {tei}.perseus-grc2, sha256 {teisha}. "
 "Text as printed: lines the editor brackets as spurious are kept in [ ]; Th. 929a–t, the passage he prints from Chrysippus after line 929, in ⟨ ⟩. "
 "Pronunciation: reconstructed Attic, after W. S. Allen, Vox Graeca — an admitted convention; Hesiod's own pronunciation was older "
 "and is not recoverable in detail. Romanization: standard classical transliteration (ē/ō; th/ph/ch; y for υ, u in diphthongs; "
 "h = rough breathing; ēi/āi/ōi for iota subscript; ï for a separately sounded ι; accents omitted). Scansion: made by program from "
 "the text and checked; it shows one defensible reading of each line, and the notes say where a line is irregular. "
 "All translations were made fresh from the Greek for Lectorium.")
def source_statement(book):
    return SOURCE.format(title=WORKS[book][1].replace(' (Hesiod)',''), tei='tlg0020.'+('tlg001' if book=='Th' else 'tlg002'), teisha=source()['teiSha256'][book][:16])
