#!/usr/bin/env python3
"""The reader's word splitter, in Python — ONE copy, imported by everything that counts words.

reader.html decides what a tappable word is (WORD_CLASS / HAN_CLASS / WORD_RE, near the top of
its script). Karaoke timings are one [start, end] per such word, so any script that produces or
checks align.json must split a sentence exactly as the reader does.

WHY THIS FILE EXISTS. align_dtw.py used to carry its own, Latin-only copy of the class. When the
reader learned Greek, Cyrillic, Mongolian, Arabic and Devanagari, that copy was never updated, and
on 2026-09-20 the first Arabic texts (the Nights) came back with a clip for every sentence and an
EMPTY timing list for every sentence: no Arabic letter matched, so every sentence had "no words".
Nothing failed, because zero timings for zero tokens is self-consistent. The clips could play but
could not highlight or seek.

When reader.html's WORD_CLASS changes, change it here too — and only here.
"""
import re

WORD_CLASS = (
    'A-Za-zÀ-ÖØ-öø-ÿĀ-ɏ̀-ͯḀ-ỿ'
    # Greek, Cyrillic, Greek Extended, Mongolian + its invisible shaping controls
    'Ά-ϿЀ-ӿἀ-῿ᠠ-ᡷ᠋-᠎'
    # Arabic: letters, tatweel and tashkil (part of the word); not U+0600-061F, not digits/punct.
    'ؠ-ٰٟ-ۓە-ۭ'
    # Devanagari: letters, vowel signs, virama, anusvara/visarga, avagraha; not danda or digits.
    'ऀ-ॣॱ-ॿ'
)
HAN_CLASS = '㐀-䶿一-鿿豈-﫿'
WORD_RE = re.compile('[' + HAN_CLASS + ']|[' + WORD_CLASS + ']+(?:[-\\[\\]()][' + WORD_CLASS + ']+)*')


def sent_tokens(s):
    """One token per unit the reader can highlight and seek to.

    Words-model stories (Han, hieroglyphs, cuneiform, Sanskrit) carry an explicit `words` array,
    and their .word[data-wi] indices are positions in THAT array, not WORD_RE matches — so the
    timings must be built from it or karaoke lands on the wrong unit. Punctuation glyphs are
    dropped: written, but not spoken.
    """
    if s.get("words"):
        return ["".join(g.get("s", "") for g in w.get("glyphs", []) if g.get("role") != "punct")
                for w in s["words"]]
    return WORD_RE.findall(s["t"])
