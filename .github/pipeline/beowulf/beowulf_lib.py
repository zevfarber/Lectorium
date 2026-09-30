#!/usr/bin/env python3
"""Shared helpers for the Beowulf pipeline. Everything is derived from files in this repository."""
import json, re, hashlib, os, glob, sys, unicodedata
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, '.github', 'scripts'))
from wordre import WORD_RE          # the reader's own word splitter — one copy, shared

TERMINAL = '.,;:!?—’”'
# Klaeber's inventory: letters, the marks he prints, his punctuation. Anything else is damage.
LETTERS = set('abcdefghiklmnoprstuwxyzþðæęœ')
MARKS = {'̄', '̂', '̣', '̨'}     # macron, circumflex, dot below, ogonek
PUNCT = set(' \n.,;:!?\'-—()[]‘’“”†')

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
    if _SRC is None: _SRC = jload(os.path.join(HERE, 'source', 'beowulf-klaeber1922.json'))
    return _SRC
def lines_of(p):
    L = {l['n']: l for l in source()['lines']}
    return [L[n] for n in range(p['from'], p['to'] + 1)]
def sha(lines): return hashlib.sha256('\n'.join(l['t'] for l in lines).encode('utf8')).hexdigest()
def key(w):
    """the reader's wordKey(): brackets/parentheses stripped, lowercased"""
    return re.sub(r'[\[\]()]', '', w).lower()
def forms(text): return [key(w) for w in WORD_RE.findall(text)]
def glossary_path(): return os.path.join(ROOT, 'beowulf-glossary.json')
def glossary(): return jload(glossary_path())
def published_stories():
    out = []
    for p in parts()['parts']:
        f = os.path.join(ROOT, p['file'])
        if p['status'] == 'published' and os.path.exists(f): out.append(jload(f))
    return out
def charset_errors(t):
    bad = []
    for ch in unicodedata.normalize('NFD', t):
        if ch.lower() in LETTERS or ch in MARKS or ch in PUNCT: continue
        bad.append(ch)
    return sorted(set(bad))
def page_range(p):
    a, b = p['pages'][0], p['pages'][-1]
    return f'p. {a}' if a == b else f'pp. {a}–{b}'
def source_statement(p):
    label = 'the unnumbered prologue' if p['seq'] == 0 else f"fitt {p['fitt']}"
    s = (f"Fr. Klaeber, Beowulf and the Fight at Finnsburg, 1st edition (Boston: D. C. Heath & Co., 1922), "
         f"{page_range(p)}, lines {p['from']}–{p['to']} ({label}). Text follows Klaeber's printing exactly — þ, ð, æ, "
         "vowel-length macrons, a circumflex for contracted vowels (Klaeber prints one mark over the pair of vowels; we place it "
         "on the second), [brackets] for letters or words added by emendation, (parentheses) for conjectural restoration of "
         "fire-damaged letters, and Klaeber's rows of dots where words are lost. A dot under a vowel (dōgọra) is Klaeber's sign "
         "that the vowel does not count in the metre. Transcribed from the page images of the archive.org scan, every page read "
         "twice. ")
    if p['seq'] in (29, 30):
        s += ("Klaeber prints the section numeral [XXVIIII–XXX] at line 2039 and marks no new section at line 2093; the division "
              "between fitts XXIX and XXX at 2093 is ours. ")
    s += ("Pronunciation convention: reconstructed late West Saxon, c. 1000, following Campbell's Old English Grammar. "
          "Translations made fresh from the original.")
    return s
