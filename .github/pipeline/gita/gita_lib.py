"""Shared helpers for the Bhagavadgītā pipeline: reading the witnesses, applying the adjudicated
corrections, and the two-witness collation. Used by build_gita.py and validate_gita.py."""
import json, os, re, hashlib, unicodedata
from indic_transliteration import sanscript

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'source')

def dev2int(s):
    return int(sanscript.transliterate(s, sanscript.DEVANAGARI, sanscript.IAST))

def corrections():
    """{ '5.8': [[old, new, why], ...] } — every departure from the Wikisource text, each one to be named
    in the note of its verse."""
    return json.load(open(os.path.join(SRC, 'corrections.json'), encoding='utf-8'))

def read_wikisource(ch, apply_corrections=True):
    """Parse source/wikisource-chNN.txt → ordered list of verses:
    {'n': int, 'lines': [devanagari line, ...] (without daṇḍa/number), 'speaker': 'अर्जुन उवाच' or None}.
    ZWNJ/ZWJ are stripped; an ASCII colon standing for visarga is normalised; the adjudicated
    corrections are applied when apply_corrections is True."""
    raw = open(os.path.join(SRC, f'wikisource-ch{ch:02d}.txt'), encoding='utf-8').read()
    raw = raw.replace('‌', '').replace('‍', '')
    corr = corrections() if apply_corrections else {}
    verses, cur, sp = [], [], None
    for line in raw.splitlines():
        s = line.strip()
        if not s:
            continue
        if re.search(r'(उवाच|ुवाच)$', s) and '॥' not in s:
            sp = s; continue
        m = re.search(r'॥\s*(\S+?)\s*-\s*(\S+?)\s*॥\s*$', s)
        body = re.sub(r'\s*[।॥].*$', '', s).strip().replace(':', 'ः')
        cur.append(body)
        if m:
            assert dev2int(m.group(1)) == ch, (ch, s)
            n = dev2int(m.group(2))
            lines = cur
            for old, new, why in corr.get(f'{ch}.{n}', []):
                joined = '\n'.join(lines)
                assert joined.count(old) == 1, (ch, n, old)
                lines = joined.replace(old, new).split('\n')
            verses.append({'n': n, 'lines': lines, 'speaker': sp})
            cur, sp = [], None
    assert [v['n'] for v in verses] == list(range(1, len(verses) + 1)), ch
    return verses

def read_bori(ch):
    """Parse source/bori-iast.txt → {verse: iast}, {verse: speaker} for one chapter."""
    out, spk = {}, {}
    for line in open(os.path.join(SRC, 'bori-iast.txt'), encoding='utf-8'):
        line = line.rstrip('\n')
        if not line.strip():
            continue
        ref, txt = line.split(' ', 1)
        c, v = map(int, ref.split('.'))
        if c != ch:
            continue
        if txt.startswith('@ '):
            spk[v] = txt[2:]
        else:
            out[v] = txt
    return out, spk

def letters_dev(dev):
    ia = sanscript.transliterate(dev.replace('ऽ', ''), sanscript.DEVANAGARI, sanscript.IAST)
    return unicodedata.normalize('NFC', re.sub(r"[\s\-|;']", '', ia))

def letters_iast(ia):
    return unicodedata.normalize('NFC', re.sub(r"[\s\-|;']", '', ia))

def nasal_neutral(x):
    return re.sub(r'[ṃñṅṇnm~]', 'M', x)

def collate(ch):
    """Return the list of verses whose letters differ between the corrected Wikisource text and BORI,
    as (verse, kind, wiki_snippet, bori_snippet); kind is 'orth' (anusvāra vs class nasal only) or
    'VAR' (a real difference: a known vulgate/BORI variant, or a misprint still to adjudicate)."""
    ws = read_wikisource(ch); bo, _ = read_bori(ch)
    diffs = []
    for v in ws:
        a = letters_dev(' '.join(v['lines'])); b = letters_iast(bo[v['n']])
        if a != b:
            kind = 'orth' if nasal_neutral(a) == nasal_neutral(b) else 'VAR'
            i = next((k for k in range(min(len(a), len(b))) if a[k] != b[k]), min(len(a), len(b)))
            diffs.append((v['n'], kind, a[max(0, i - 10):i + 14], b[max(0, i - 10):i + 14]))
    return diffs

def chapter_text(ch):
    """The canonical text of a chapter after corrections: speaker lines and verse lines, joined."""
    out = []
    for v in read_wikisource(ch):
        if v['speaker']:
            out.append(v['speaker'])
        out.extend(v['lines'])
    return '\n'.join(out)

def sha(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()
