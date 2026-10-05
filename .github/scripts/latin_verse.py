#!/usr/bin/env python3
"""Latin verse -> SSML for build_pinned.py (restored Classical pronunciation, Zev's choices of 2026-10-04:
normal WORD stress, long vowels held long, elision as in verse; voice de-DE-Wavenet-B).

The edition (Magnus's Ovid) prints no macrons, so vowel length comes from the Scansion overlay that
scan_latin.py writes into each unit (`sc`, one string per reader word). Reading a vowel's length off the
scansion:
  - an OPEN syllable marked long (–) has a long vowel: mū-tā-tās -> mū, tā;
  - an open syllable marked short (⏑) has a short vowel;
  - a CLOSED syllable is long by position and says nothing about its vowel, so the vowel is read short,
    except where a fixed rule of the language makes it long: a vowel before ns or nf; the endings
    -ās -ōs -ēs (closed final syllables that are long by nature in almost every case in verse);
  - the last syllable of a line (×) is read short unless it ends in a vowel the rules make long (-ō, -ī,
    -ū, -ā of the 1st-declension ablative cannot be told from the nominative, so final -a stays short);
  - an elided syllable is the unmarked tail of a word: it is dropped and the rest of the word is spoken
    joined to the next one.
A unit with no `sc` (a line the scanner could not fit) is read without length marks, with elision decided
by the plain rule (final vowel or vowel+m before a vowel or h).
Stress follows from the lengths (latin_g2p.py: penult if heavy, else antepenult).
"""
import re, sys, os
from xml.sax.saxutils import escape

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import latin_g2p as L
from wordre import WORD_RE

SYL = re.compile(r'(\d?)([^–⏑×‖\d]+?)([–⏑×])')
MAC = {'a': 'ā', 'e': 'ē', 'i': 'ī', 'o': 'ō', 'u': 'ū', 'y': 'ȳ',
       'A': 'Ā', 'E': 'Ē', 'I': 'Ī', 'O': 'Ō', 'U': 'Ū', 'Y': 'Ȳ'}
VOW = set('aeiouyAEIOUY')
DIPH = {'ae', 'oe', 'au', 'eu'}
PUNCT = {",": ",", ";": ",", ".": ".", ":": ",", "(": ",", ")": ",", "?": "?", "!": "!", "\n": ""}
ELIDE = re.compile(r"(?:aɪ|ɔʏ|aʊ|ɛʊ|[aɛɪɔʊʏ]ː?|[aeiouy]ː)m?$")


def _nucleus(syl):
    """Index in `syl` of the vowel that takes a macron, or None (diphthong / no vowel)."""
    s = syl.lower()
    idx = [k for k, ch in enumerate(s) if ch in VOW and not (ch == 'u' and k > 0 and s[k - 1] in 'qg'
                                                               and k + 1 < len(s) and s[k + 1] in VOW)]
    if not idx:
        return None
    # a run of two vowels: a diphthong takes no macron; i/u before a vowel is a consonant
    if len(idx) >= 2 and idx[-1] == idx[-2] + 1:
        if s[idx[-2]] + s[idx[-1]] in DIPH:
            return None
        return idx[-1]
    return idx[-1]


def macronize(tok, sc):
    """(macronized word, elided) from a token and its scansion string."""
    body = sc.replace('‖', '')
    syls = SYL.findall(body)
    tail = SYL.sub('', body)
    out = []
    for n, (_, letters, mark) in enumerate(syls):
        last_letter = letters[-1].lower()
        nxt = syls[n + 1][1].lower() if n + 1 < len(syls) else tail.lower()
        closed = last_letter not in VOW or (last_letter == 'u' and len(letters) > 1 and letters[-2].lower() in 'qg')
        k = _nucleus(letters)
        long_ = False
        if k is not None:
            if mark == '–' and not closed:
                long_ = True
            elif closed:
                after = letters[k + 1:].lower() + nxt[:1]
                is_final = n == len(syls) - 1 and not tail
                if after[:2] in ('ns', 'nf'):
                    long_ = True
                elif is_final and letters[k:].lower() in ('as', 'os', 'es') and len(syls) > 1:
                    long_ = True
            elif mark == '×' and letters[k].lower() in 'oiu' and k == len(letters) - 1:
                long_ = True
        if long_:
            letters = letters[:k] + MAC[letters[k]] + letters[k + 1:]
        out.append(letters)
    return ''.join(out) + tail, bool(tail)


def _plain_elides(p, nxt, gap):
    return (nxt and not any(c in ",;.:()?!" for c in gap) and re.match(r"[aeiouyh]", nxt.lower())
            and not re.match(r"i[aeiou]", nxt.lower()) and ELIDE.search(p))


def unit_words(s):
    """[(token, macronized, elided)] for one unit."""
    toks = WORD_RE.findall(s["t"])
    sc = s.get("sc")
    if sc and len(sc) == len(toks):
        return [(t,) + macronize(t, x) for t, x in zip(toks, sc)]
    out = []
    ms = list(WORD_RE.finditer(s["t"]))
    for k, m in enumerate(ms):
        nxt = ms[k + 1].group(0) if k + 1 < len(ms) else ""
        gap = s["t"][m.end():ms[k + 1].start()] if nxt else ""
        out.append((m.group(0), m.group(0), bool(_plain_elides(L.ipa(m.group(0)), nxt, gap))))
    return out


def _ph(ipa):
    rom = re.sub("[ˈː]", "", ipa)
    return '<phoneme alphabet="ipa" ph="%s">%s</phoneme>' % (escape(ipa, {'"': "&quot;"}), escape(rom))


def sentence_ssml(s):
    t = s["t"]
    words = unit_words(s)
    ms = list(WORD_RE.finditer(t))
    parts, pend, pos = [], "", 0
    for k, m in enumerate(ms):
        for ch in t[pos:m.start()]:
            if PUNCT.get(ch):
                parts.append(PUNCT[ch])
        pos = m.end()
        _, mac, elided = words[k]
        p = L.ipa(mac)
        if elided and k + 1 < len(ms):
            # the elided word keeps its own stress; it is spoken run into the next word
            pend += ELIDE.sub("", p) or p
            continue
        parts.append(_ph(pend + p)); pend = ""
    for ch in t[pos:]:
        if PUNCT.get(ch):
            parts.append(PUNCT[ch])
    body = ""
    for x in parts:
        body += x if x in PUNCT.values() else " " + x
    return "<speak>" + body.strip() + "</speak>"


def word_ipa_map(story, word_key):
    """Glossary key -> IPA for the word clips: each word as it is first met, with its lengths."""
    out = {}
    for s in story["sentences"]:
        for tok, mac, _ in unit_words(s):
            out.setdefault(word_key(tok), L.ipa(mac))
    return out


if __name__ == "__main__":
    import json
    st = json.load(open(sys.argv[1], encoding="utf-8"))
    for s in st["sentences"][: int(sys.argv[2]) if len(sys.argv) > 2 else 2]:
        print(" ".join(m for _, m, e in unit_words(s)))
        print(sentence_ssml(s))
