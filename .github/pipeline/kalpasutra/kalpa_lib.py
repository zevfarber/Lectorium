#!/usr/bin/env python3
"""Kalpasūtra (Jacobi 1879) helpers: IAST (Jacobi's romanization) -> Devanagari, and tokenising. Set up 2026-11-21.

Devanagari is made letter for letter: hyphens between compound members are closed up, an elision mark ’ inside a
word or before a following word (ih’ eva, rayaṇ’-uccaya) closes the gap, a consonant ending a word before a vowel
(jogam uvāgaeṇaṃ) joins it. Jaina Prakrit has no diphthongs (Jacobi, introduction): a vowel after a vowel is always
written with its own letter (caittā चइत्ता, havai हवइ)."""
import re, json, os
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
V = {'a': ('अ', ''), 'ā': ('आ', 'ा'), 'i': ('इ', 'ि'), 'ī': ('ई', 'ी'), 'u': ('उ', 'ु'), 'ū': ('ऊ', 'ू'), 'e': ('ए', 'े'), 'o': ('ओ', 'ो')}
C = {'kh': 'ख', 'gh': 'घ', 'ch': 'छ', 'jh': 'झ', 'ṭh': 'ठ', 'ḍh': 'ढ', 'th': 'थ', 'dh': 'ध', 'ph': 'फ', 'bh': 'भ',
     'k': 'क', 'g': 'ग', 'ṅ': 'ङ', 'c': 'च', 'j': 'ज', 'ñ': 'ञ', 'ṭ': 'ट', 'ḍ': 'ड', 'ṇ': 'ण', 't': 'त', 'd': 'द', 'n': 'न',
     'p': 'प', 'b': 'ब', 'm': 'म', 'y': 'य', 'r': 'र', 'l': 'ल', 'v': 'व', 'ś': 'श', 'ṣ': 'ष', 's': 'स', 'h': 'ह'}
VIRAMA = '्'
PUNCT = '‘’()[],.;:|'
LETTERS = re.compile(r"[a-zāīūṃṇṭḍṅñśṣ]")
WORD_DEV = re.compile(r'[ऀ-ॣॱ-ॿ]+')          # the reader's Devanagari word characters

def to_dev(word):
    """One word or joined group of Jacobi's IAST (no outer punctuation) -> Devanagari."""
    s = word.lower().replace('-', '').replace('’ ', '').replace('’', '').replace(' ', '')
    out, i, pend = [], 0, None           # pend: a consonant waiting for its vowel
    while i < len(s):
        ch = s[i]
        if ch == 'ṃ':
            if pend: out.append(pend + VIRAMA); pend = None
            out.append('ं'); i += 1; continue
        two = s[i:i + 2]
        cons = C.get(two) if two in C else C.get(ch)
        if cons:
            if pend: out.append(pend + VIRAMA)
            pend = cons; i += len(two) if two in C else 1; continue
        if ch in V:
            if pend: out.append(pend + V[ch][1]); pend = None
            else: out.append(V[ch][0])
            i += 1; continue
        raise ValueError(f'cannot convert {ch!r} in {word!r}')
    if pend: out.append(pend + VIRAMA)
    return ''.join(out)

def dev_punct(p):
    """Jacobi's punctuation as it stands in the Devanagari line."""
    return p.replace('||', '॥').replace('|', '।').replace('.', '।').replace(';', '।').replace(':', '।')

def split_punct(tok):
    m = re.match(r'^([‘’(\[]*)(.*?)([’)\],.;:|]*)$', tok)
    lead, core, trail = m.groups()
    if core.startswith('’'):            # an elision mark at the head of a word belongs to the word (’mi)
        pass
    return lead, core, trail

def source():
    return json.load(open(os.path.join(HERE, 'source', 'jinacaritra-jacobi1879.json'), encoding='utf8'))
