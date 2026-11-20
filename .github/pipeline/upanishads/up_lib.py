"""Shared helpers for the Upanishads pipeline (set up 2026-11-20 on the Bhagavadgītā's machinery).

A part's source is source/<part>.txt: blocks separated by a blank line, one block = one unit. A numbered
unit's last line ends '॥ <n> ॥' (Devanagari numeral); an unnumbered unit (peace invocation, heading,
colophon) has no number. Tokens are the space-separated pieces of each line; a token made only of
daṇḍas (। ॥) is punctuation and belongs to the word before it (or, at the start of a line, the word
after it); every other token is a word the drafter must cover, in order."""
import hashlib, json, os, re, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'source')
PUNCT = re.compile(r'^[।॥]+$')
DIG = '०१२३४५६७८९'


def dev_int(s):
    return int(''.join(str(DIG.index(c)) for c in s))


def parts():
    return json.load(open(os.path.join(HERE, 'parts.json'), encoding='utf-8'))


def part(pid):
    return next(p for p in parts()['parts'] if p['part'] == pid)


def read_part(pid):
    """→ list of units {'n': int or None, 'lines': [line, ...]} with the verse number taken off the last line
    (its closing ॥ stays)."""
    raw = open(os.path.join(SRC, pid + '.txt'), encoding='utf-8').read().strip()
    out = []
    for b in raw.split('\n\n'):
        lines = [l.strip() for l in b.split('\n') if l.strip()]
        m = re.search(r'\s*॥\s*([०-९]+)\s*॥$', lines[-1])
        n = None
        if m:
            n = dev_int(m.group(1))
            lines[-1] = lines[-1][:m.start()] + ' ॥'
        out.append({'n': n, 'lines': lines})
    return out


def line_tokens(line):
    """→ list of (token, is_punct)."""
    return [(t, bool(PUNCT.match(t))) for t in line.split()]


def words_of(unit):
    """The word tokens of a unit, line by line (punctuation dropped): what words.txt must reproduce."""
    return [[t for t, p in line_tokens(l) if not p] for l in unit['lines']]


def text(pid):
    return unicodedata.normalize('NFC', open(os.path.join(SRC, pid + '.txt'), encoding='utf-8').read())


def sha(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()
