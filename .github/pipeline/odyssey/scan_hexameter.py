#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Homeric hexameter scanner (standard library only).

usage:
  python3 scan_hexameter.py src-001.json scan-001.json [--report scan-001-report.txt] [--notes notes.txt]
  python3 scan_hexameter.py --tei ../od.xml --books 1,9 [--report robustness.txt]

Method: every line is fitted to the hexameter by a cost-minimising dynamic programme.
Each syllable gets a set of (weight, cost, licence) options from its vowel (nature), what
follows it (position, computed across word boundaries) and the Homeric licences; the DP
picks the cheapest way to fill  L(L|SS) x5 + L X.  Licences are never free, so a line that
needs one says so, and a line that needs an *unexplained* one is flagged UNRESOLVED.
"""
import sys, re, json, unicodedata, argparse

LONG, SHORT, ANC, CAES = '\u2013', '\u23d1', '\u00d7', '\u2016'

# ----------------------------------------------------------------------------- letters
WORD_RE = re.compile(r'[A-Za-z\u0370-\u03ff\u1f00-\u1fff]+')
NONLETTER = {'\u0387', '\u00b7', '\u037e'}
ELISION = {'\u2019', '\u02bc', "'", '\u1fbd', '\u1fbf'}
PUNCT = set(',.;:\u00b7\u0387\u037e\u2014!?')

VOWELS = set('αεηιουω')
CONS = set('βγδζθκλμνξπρστφχψ')
DOUBLE = set('ζξψ')
MUTES = set('πβφτδθκγχ')
VOICED = set('βγδ')
LIQ = set('λρμν')
DIPH = {'αι', 'ει', 'οι', 'υι', 'αυ', 'ευ', 'ηυ', 'ου', 'ωυ'}

M_ACUTE, M_GRAVE, M_CIRC = '\u0301', '\u0300', '\u0342'
M_SMOOTH, M_ROUGH, M_DIAER, M_SUB = '\u0313', '\u0314', '\u0308', '\u0345'
M_MACRON, M_BREVE = '\u0304', '\u0306'
ACCENTS = {M_ACUTE, M_GRAVE, M_CIRC}


def tokenize(line):
    """-> list of dicts {text,start,end,elided,punct_after}; exact reader-app token class."""
    toks = []
    for m in WORD_RE.finditer(line):
        s = m.group(0)
        # split on the punctuation code points that live inside the Greek block
        pos = m.start()
        for piece in re.split('([\u0387\u037e])', s):
            if piece and piece not in NONLETTER:
                toks.append({'text': piece, 'start': pos, 'end': pos + len(piece)})
            pos += len(piece)
    for k, t in enumerate(toks):
        nxt = toks[k + 1]['start'] if k + 1 < len(toks) else len(line)
        gap = line[t['end']:nxt]
        t['elided'] = bool(gap) and gap[0] in ELISION
        t['punct_after'] = any(c in PUNCT for c in gap)
    return toks


def letters_of(word):
    """one entry per letter: (orig_substring, base, marks)"""
    out = []
    for ch in word:
        d = unicodedata.normalize('NFD', ch)
        if unicodedata.category(d[0]) == 'Mn' and out:          # stray combining mark
            o = out[-1]
            out[-1] = (o[0] + ch, o[1], o[2] | set(d))
            continue
        base = d[0].lower()
        if base == 'ς':
            base = 'σ'
        out.append((ch, base, set(d[1:])))
    return out


def plain(word):
    return ''.join(b for _, b, _ in letters_of(word))


# ----------------------------------------------------------------------------- lexical knowledge
def _sig(words):
    """lists are written with final ς for legibility; the scanner's plain form has σ throughout"""
    return [w.replace('ς', 'σ') for w in words]


# Words before which a lost digamma (or σϝ-) still makes position / allows hiatus.
DIGAMMA_PREFIX = tuple(_sig((
    'ανακτ', 'αναξ', 'ανασσ', 'αστυ', 'αστε', 'ειπ', 'εειπ', 'εργ', 'εοργ', 'ερδ', 'ερξ',
    'οικ', 'οιν', 'ιδ', 'οιδ', 'οισθ', 'ειδ', 'εκαστ', 'εκαεργ', 'εκηβολ', 'εκατηβολ', 'εκητι',
    'εκηλ', 'εοικ', 'εικελ', 'εικυι', 'εικτ', 'ικελ', 'εσπερ', 'εσθητ', 'εσθης', 'ειματ', 'ειμα',
    'ιαχ', 'ιοειδ', 'ιφι', 'ιλι', 'ηδυ', 'ανδαν', 'εαδ', 'εθνε', 'εθνος', 'ηθε', 'ελικ',
    'ελισσ', 'ειλιποδ', 'ελπ', 'εελπ', 'εολπ', 'ερυσ', 'ερυοντ', 'ερυω', 'ερρυσ', 'ερε', 'εικοσ', 'εεικοσ',
    'εαγ', 'ιεμεν', 'ελωρ', 'ετης', 'εται', 'ετησ', 'ισος', 'ισον', 'ιση', 'ισα',
    'εισης', 'ιτε', 'ιον', 'ηρα', 'ειαρ', 'εαρ', 'ιριν', 'ιρις', 'ιρος', 'ιρον', 'ιρω',
    'αλωναι', 'αλοντ', 'αλω', 'ειλ', 'αρν',
)))
DIGAMMA_EXACT = set(_sig((
    'επος', 'επεα', 'επε', 'επεσσι', 'επεσσιν', 'επεσι', 'επεσιν', 'επεων', 'επεεσσι', 'επεεσσιν', 'επες',
    'ετος', 'ετεα', 'ετει', 'ετεων', 'εκας', 'εκων', 'αλις', 'οπα', 'οπι', 'ις', 'ινες', 'εσσε', 'εστο',
    'εννυτο', 'εσσατο', 'εεδνα', 'εδνα', 'αδε', 'ευαδε', 'ηχη', 'ηχηεντα', 'ηχηεσσα', 'αγη', 'εαξε',
    'εαξαν', 'ηκα')))
# 3rd-person pronoun / possessive (σϝ-) and other ϝ-words that need the rough breathing to be told apart
DIGAMMA_ROUGH = set(_sig((
    'ε', 'εο', 'ευ', 'εθεν', 'ειο', 'οι', 'ος', 'ον', 'ην', 'ης', 'ω', 'η', 'ου', 'οιο',
    'οισι', 'οισιν', 'ησι', 'ησιν', 'ους', 'ας', 'α', 'εος', 'εον', 'εου', 'εοιο', 'εω',
    'εη', 'εην', 'εης', 'εοι', 'εοισι', 'εοισιν', 'εους', 'εα', 'εας', 'εων', 'ως', 'ονδε',
    'εκαθεν', 'εξ', 'εκτος', 'ηδυς', 'ηδυ', 'ηδεος', 'ηδεα', 'ηδειαν', 'ηδεια',
    'ηδιστος', 'ιετο', 'ιεσθην', 'ιεμαι', 'ιεται', 'εννυσθαι', 'εσθην', 'εσασθαι', 'ειμενος',
    'ειμενοι', 'ειμενα', 'ανδανε', 'ανδανει')))
# δϝ-: δέος, δείδω, δεινός, δήν, δηρόν lengthen a preceding short open vowel
DW_PREFIX = tuple(_sig(('δεος', 'δειδ', 'δεισ', 'δεινο', 'δεινη', 'δεινα', 'δεινω', 'δεινου', 'δην', 'δηρον', 'δηθα')))
# σκ-/ζ- words before which a short vowel may stay short (they could not otherwise stand in the verse)
NOPOSITION_PREFIX = ('ζακυνθ', 'ζελει', 'σκαμανδρ', 'σκεπαρν')
# words that fuse with a following vowel (synecphonesis)
SYNECPH_FIRST = {'δη', 'η', 'μη', 'επει', 'ω', 'εγω'}

POSTPOSITIVE = set(_sig(('δε', 'δ', 'τε', 'τ', 'θ', 'γαρ', 'μεν', 'γε', 'γ', 'περ', 'κε', 'κεν', 'κ', 'αν', 'ρα', 'ρ',
                'αρα', 'αρ', 'νυ', 'μιν', 'οι', 'μοι', 'τοι', 'σφι', 'σφιν', 'τις', 'τι', 'ποτε', 'ποτ',
                'ποθ', 'που', 'με', 'μ', 'σε', 'σ', 'μευ', 'σφεας', 'σφισι', 'σφισιν', 'πως', 'πω', 'ε')))

# Firm quantities of α ι υ in very common stems (macron = long, breve = short).  Written as
# (kind, plain-pattern, {offset: 'L'|'S'}); kind: 'pre' prefix, 'exact', 'suf' suffix.
def _h(s):
    s = unicodedata.normalize('NFD', s)
    pat, q = '', {}
    for ch in s:
        if ch == M_MACRON:
            q[len(pat) - 1] = 'L'
        elif ch == M_BREVE:
            q[len(pat) - 1] = 'S'
        else:
            pat += ch
    return pat.replace('ς', 'σ'), q

HINTS = [('pre',) + _h(s) for s in (
    'θῡμ', 'ψῡχ', 'νῑκ', 'τῑμ', 'ἀτῑμ', 'μῡθ', 'μῡρι', 'κῡματ', 'κῡμα', 'ᾱθᾰνᾰτ', 'οδῠσ', 'πολῠ',
    'λᾱο', 'λᾱω', 'ῑφι', 'ῑρ', 'ῡμετερ', 'ῡμε', 'ῡμι', 'ῡμα', 'ῐθᾰκ', 'κῐκον', 'κῠκλωπ', 'κῠκλωψ',
    'τηλεμᾰχ', 'ᾰγᾰμεμν', 'ᾰχῐλ', 'κᾰλῠψ', 'θῠγᾰτηρ', 'θῠγᾰτερ', 'ᾰγορ', 'ᾰλοχ', 'θᾰλᾰσσ',
    'δᾰκρυ', 'φᾰρμᾰκ', 'μεγᾰρ', 'μεγᾰλ', 'ποσῐδᾱ', 'ποσειδᾱ',
)] + [('exact',) + _h(s) for s in (
    'κᾰτᾰ', 'ᾰνᾰ', 'πᾰρᾰ', 'μετᾰ', 'ᾰμᾰ', 'ᾰρᾰ', 'μᾰλᾰ', 'ῐνᾰ', 'αλλᾰ', 'δῐος', 'δῐι', 'δῐᾰ',
    'δῑου', 'δῑω', 'δῑης', 'δῑη', 'δῑοιο', 'κᾱλος', 'κᾱλον', 'κᾱλου', 'κᾱλη', 'κᾱλην', 'κᾱλης',
    'κᾱλοι', 'κᾱλᾰ', 'κᾱλᾱς', 'κᾱλοιο', 'κᾱλω', 'ενῐ', 'επῐ', 'περῐ', 'ᾰπο', 'ῠπο', 'ᾰτᾰρ',
    'αυτᾰρ', 'τᾰχᾰ', 'σῠ', 'μᾰκᾰρες', 'μᾰκᾰρων', 'πᾰτηρ', 'πᾰτερ', 'πᾰτερᾰ', 'μῐν', 'νῠ', 'γᾰρ', 'ᾰν',
    'νῠν', 'τῐς', 'τῐ',
)]
HINTS = [h for h in HINTS if h[1]]


def is_digamma_word(tok):
    p = tok['plain']
    if tok.get('rough'):
        if p in DIGAMMA_ROUGH:
            return True
    if p in DIGAMMA_EXACT:
        return True
    if p == 'ιδε':                       # ἰδέ 'and' is not a ϝ-word
        return False
    return p.startswith(DIGAMMA_PREFIX)


# ----------------------------------------------------------------------------- analysis of a line
class Nucleus:
    __slots__ = ('tok', 'a', 'b', 'nat', 'why', 'final', 'base', 'idx')


def analyse(line):
    toks = tokenize(line)
    nuclei = []
    for ti, t in enumerate(toks):
        L = letters_of(t['text'])
        t['letters'] = L
        t['plain'] = ''.join(b for _, b, _ in L)
        t['rough'] = bool(L) and any(M_ROUGH in m for _, _, m in L[:2])
        t['nuclei'] = []
        i = 0
        while i < len(L):
            ch, b, m = L[i]
            if b in VOWELS:
                j = i + 1
                if j < len(L):
                    ch2, b2, m2 = L[j]
                    if (b + b2) in DIPH and M_DIAER not in m2 and not (m & (ACCENTS | {M_SMOOTH, M_ROUGH, M_DIAER} - set())) \
                            and M_SUB not in m and M_MACRON not in m2:
                        # a diaeresis on the FIRST vowel (ϋι) still allows a diphthong only if no other mark
                        j = i + 2
                        # με-μα-υῖ-α, ἐκ-γε-γα-υῖ-α: before an accented ι the υ belongs to υι, not to αυ
                        if b2 == 'υ' and not m2 and j < len(L) and L[j][1] == 'ι' and (L[j][2] & ACCENTS) \
                                and M_DIAER not in L[j][2]:
                            j = i + 1
                n = Nucleus()
                n.tok, n.a, n.b = ti, i, j
                marks = set().union(*[L[k][2] for k in range(i, j)])
                n.base = ''.join(L[k][1] for k in range(i, j))
                if j - i == 2:
                    n.nat, n.why = 'L', 'diphthong'
                elif M_CIRC in marks:
                    n.nat, n.why = 'L', 'circumflex'
                elif M_SUB in marks:
                    n.nat, n.why = 'L', 'iota subscript'
                elif M_MACRON in marks:
                    n.nat, n.why = 'L', 'macron'
                elif M_BREVE in marks:
                    n.nat, n.why = 'S', 'breve'
                elif b in 'ηω':
                    n.nat, n.why = 'L', 'η/ω'
                elif b in 'εο':
                    n.nat, n.why = 'S', 'ε/ο'
                else:
                    n.nat, n.why = 'U', ''
                n.final = False
                t['nuclei'].append(n)
                i = j
            else:
                i += 1
        if t['nuclei']:
            t['nuclei'][-1].final = True
        apply_accent_rules(t)
        apply_ending_rules(t)
        apply_hints(t)
        nuclei.extend(t['nuclei'])
    for k, n in enumerate(nuclei):
        n.idx = k
    return toks, nuclei


def accent_of(t, n):
    m = set().union(*[t['letters'][k][2] for k in range(n.a, n.b)])
    if M_CIRC in m:
        return 'c'
    if M_ACUTE in m:
        return 'a'
    if M_GRAVE in m:
        return 'g'
    return ''


def apply_accent_rules(t):
    """Quantities of α ι υ that the accent itself guarantees (σωτῆρα law and the law of limitation)."""
    N = t['nuclei']
    if t['elided'] or len(N) < 2:
        return
    acc = [(k, accent_of(t, n)) for k, n in enumerate(N) if accent_of(t, n)]
    if not acc:
        return
    k, kind = acc[0]
    from_end = len(N) - k            # 1 ultima, 2 penult, 3 antepenult
    ult, pen = N[-1], N[-2]
    if kind == 'c' and from_end == 2 and ult.nat == 'U':
        ult.nat, ult.why = 'S', 'accent: circumflex on penult'
    elif kind == 'a' and from_end == 3 and ult.nat == 'U':
        ult.nat, ult.why = 'S', 'accent: acute on antepenult'
    elif kind == 'a' and from_end == 2:
        if pen.nat == 'U' and ult.nat == 'S' and ult.b - ult.a == 1 and ult.why == 'ε/ο':
            pen.nat, pen.why = 'S', 'accent: acute penult before short ultima'
        elif pen.nat == 'L' and ult.nat == 'U':
            p = t['plain']
            if not (p.endswith(('τις', 'τι', 'τιν')) or p.endswith(('περ', 'δε', 'τε', 'γε'))):
                ult.nat, ult.why = 'L', 'accent: acute on long penult'


# Final -ι -ιν -ις -υ -υν -υς are short unless the word is one of these (long by nature; most are
# printed with a circumflex anyway, which is caught before this rule is reached).
LONG_FINAL_IU = set(_sig((
    'ορνις', 'ορνιν', 'κνημις', 'κληις', 'κληιν', 'ηνις', 'ηνιν', 'βλοσυρωπις', 'ιχθυς', 'ιχθυν', 'ιθυς', 'ιθυν',
    'νηδυς', 'νηδυν', 'πληθυς', 'πληθυν', 'ισχυς', 'ισχυν', 'οφρυς', 'οφρυν', 'ερινυς', 'ερινυν', 'αχλυς', 'αχλυν',
    'οιζυς', 'οιζυν', 'ιλυς', 'ιλυν', 'δρυς', 'μυς', 'συς', 'υς', 'πριν', 'ημιν', 'υμιν', 'κονι',
    'μητι', 'θετι', 'παρακοιτι', 'μαστι', 'κνηστι', 'αγυρι', 'βρωτυν', 'γραπτυς', 'εδητυς', 'εδητυν', 'ορχηστυς', 'ορχηστυν',
    'κλιτυς', 'κλιτυν', 'κιθαριστυς', 'κιθαριστυν', 'αγορητυς', 'αγορητυν', 'ακοντιστυν', 'οτρυντυς', 'ταρφυς',
    'λιγνυς', 'λιγνυν', 'δυ', 'φυ', 'ις', 'ιν', 'λις', 'λιν', 'αντικρυ', 'ιφι')))


def apply_ending_rules(t):
    N = t['nuclei']
    if t['elided'] or not N:
        return
    p = t['plain']
    ult = N[-1]
    if ult.nat == 'U' and ult.base in 'ιυ':
        tail = ''.join(b for _, b, _ in t['letters'][ult.b:])
        if tail in ('', 'ν', 'σ') and p not in LONG_FINAL_IU and not p.endswith(('εδυ', 'εφυ')):
            ult.nat, ult.why = 'S', 'ending -%s%s' % (ult.base, tail)
    # 1st-declension genitive -ᾱο (Ἀτρεΐδαο, Ὀρέσταο); 2 sg. middle -σᾰο / -νᾰο (ὠδύσαο, ἐγείναο) is short
    if len(N) >= 3 and p.endswith('αο') and N[-2].nat == 'U' and N[-2].base == 'α':
        if p.endswith(('σαο', 'ναο')) and not p.endswith(('ιδαο', 'αδαο')):
            N[-2].nat, N[-2].why = 'S', 'ending -σᾰο (2 sg. middle)'
        else:
            N[-2].nat, N[-2].why = 'L', 'ending -ᾱο (genitive)'


def apply_hints(t):
    p = t['plain']
    for kind, pat, q in HINTS:
        if kind == 'pre' and p.startswith(pat):
            off = 0
        elif kind == 'exact' and p == pat:
            off = 0
        elif kind == 'suf' and p.endswith(pat) and len(p) > len(pat):
            off = len(p) - len(pat)
        else:
            continue
        for n in t['nuclei']:
            if kind == 'suf' and not accent_of(t, n):
                continue                      # -άων (θεάων, ναιετάων) but not Δαναῶν
            if n.b - n.a == 1 and (n.a - off) in q and n.nat == 'U':
                if t['elided'] and n.final and kind == 'exact':
                    continue
                n.nat, n.why = q[n.a - off], 'lexicon'


NOT_DATIVE_I = set(_sig(('επι', 'ενι', 'περι', 'αμφι', 'ετι', 'οτι', 'τι', 'ποτι', 'προτι', 'αντι', 'ουκετι', 'μηκετι',
                          'αρτι', 'αυθι', 'ηχι', 'νοσφι', 'ιφι', 'υψι', 'αγχι', 'ουχι', 'οθι', 'τοθι', 'ποθι', 'εστι', 'εισι',
                          'φησι', 'φασι', 'αυτοθι', 'κειθι')))


def is_dative_i(t, n):
    """3rd-declension dative singular -ι, originally long (Monro, Homeric Grammar § 373)"""
    p = t['plain']
    if not n.final or n.base != 'ι' or not p.endswith('ι') or len(t['nuclei']) < 2 or p in NOT_DATIVE_I:
        return False
    return not p.endswith(('σι', 'φι', 'θι', 'στι', 'κι', 'ξι', 'ψι'))


def cluster_after(toks, nuclei, k):
    """consonants between nucleus k and the next nucleus: (list of cons, n_in_own_word, next_tok or None, punct)"""
    n = nuclei[k]
    t = toks[n.tok]
    own = [b for _, b, _ in t['letters'][n.b:] if b in CONS] if n.final else None
    if not n.final:
        nxt = nuclei[k + 1]
        return [b for _, b, _ in t['letters'][n.b:nxt.a]], None, None, False
    cons = list(own)
    punct = t['punct_after']
    ti = n.tok + 1
    nexttok = None
    while ti < len(toks):
        t2 = toks[ti]
        if t2['nuclei']:
            cons += [b for _, b, _ in t2['letters'][:t2['nuclei'][0].a]]
            nexttok = t2
            break
        cons += [b for _, b, _ in t2['letters'] if b in CONS]
        punct = punct or t2['punct_after']
        ti += 1
    return cons, len(own), nexttok, punct


class Opt:
    __slots__ = ('w', 'cost', 'prior', 'lic', 'flag', 'lengthen')

    def __init__(self, w, cost=0.0, prior=0.0, lic=None, flag=None, lengthen=False):
        self.w, self.cost, self.prior, self.lic, self.flag, self.lengthen = w, cost, prior, lic, flag, lengthen


def options(toks, nuclei, k, nat=None, merged_label=None):
    """weight options of the syllable whose (last) nucleus is k."""
    n = nuclei[k]
    t = toks[n.tok]
    word = t['text']
    nat = nat or n.nat
    last = (k == len(nuclei) - 1)
    cons, own, nexttok, punct = cluster_after(toks, nuclei, k)
    if last:
        return [Opt('L'), Opt('S')]
    ncons = len(cons)
    heavy = ncons >= 2 or any(c in DOUBLE for c in cons)
    UNR = 'UNRESOLVED'
    out = []
    if heavy:
        out.append(Opt('L'))
        ml = (ncons == 2 and cons[0] in MUTES and cons[1] in LIQ)
        same_word = (own is None) or own == 0          # both internal, or both open the next word
        if ml and same_word and own != 1:
            weak = cons[0] in VOICED and cons[1] in 'λμν'
            if nat != 'L':
                c = (0.5 if own == 0 else 1.0) + (1.0 if weak else 0.0)
                out.append(Opt('S', c, lic='mute+liquid no position: %s (%s%s)' % (word, cons[0], cons[1])))
            else:
                out.append(Opt('S', 9, lic='long scanned short: ' + word, flag=UNR))
        elif own == 0 and nexttok is not None and nexttok['plain'].startswith(NOPOSITION_PREFIX) and nat != 'L':
            out.append(Opt('S', 1.0, lic='no position before %s' % nexttok['text']))
        else:
            out.append(Opt('S', 9, lic='closed syllable scanned short: ' + word, flag=UNR))
        return out
    # ---- open syllable (or closed by a single final consonant before a vowel)
    hiatus_final = n.final and ncons == 0 and nexttok is not None and not t['elided']
    dig = nexttok is not None and n.final and is_digamma_word(nexttok)
    if nat == 'L':
        if hiatus_final:
            out.append(Opt('S', 0.3, lic='correption: ' + word))
            out.append(Opt('L', 0.3 if dig else 0.6,
                           lic='hiatus, long kept%s: %s' % (' (digamma follows)' if dig else (' at punctuation' if punct else ''), word)))
        else:
            out.append(Opt('L'))
            if ncons == 0 and not n.final:
                out.append(Opt('S', 3.0, lic='internal correption: ' + word))
            else:
                out.append(Opt('S', 9, lic='long scanned short: ' + word, flag=UNR))
        return out
    if nat == 'U':
        out.append(Opt('S'))
        if hiatus_final:
            out.append(Opt('L', 0.3 if dig else 0.6, prior=0.1, lic='hiatus, long kept: ' + word))
        else:
            out.append(Opt('L', prior=0.1))
        return out
    # nat == 'S'
    out.append(Opt('S'))
    if n.final and own == 1 and ncons == 1 and nexttok is not None:
        if dig:
            out.append(Opt('L', 1.0, lic='position by digamma: %s + %s' % (word, nexttok['text']), lengthen=True))
        else:
            out.append(Opt('L', 3.0, lic='short closed final lengthened before vowel: %s + %s' % (word, nexttok['text']), lengthen=True))
    elif n.final and own == 0 and ncons == 1 and nexttok is not None and not t['elided']:
        c = cons[0]
        if c == 'ρ':
            out.append(Opt('L', 1.0, lic='initial ρ doubled: %s + %s' % (word, nexttok['text']), lengthen=True))
        elif c in 'λμνσ':
            out.append(Opt('L', 2.0, lic='lengthening before initial %s: %s + %s' % (c, word, nexttok['text']), lengthen=True))
        elif nexttok['plain'].startswith(DW_PREFIX):
            out.append(Opt('L', 2.0, lic='lengthening before δ(ϝ): %s + %s' % (word, nexttok['text']), lengthen=True))
        elif is_dative_i(t, n):
            out.append(Opt('L', 3.0, lic='dative -ι scanned long: ' + word, lengthen=True))
        else:
            out.append(Opt('L', 6.0, lic='metrical lengthening: ' + word, flag=UNR, lengthen=True))
    elif not n.final and ncons == 1 and cons[0] == 'δ' and t['plain'][nuclei[k + 1].a - 1:].startswith(DW_PREFIX[:3]):
        out.append(Opt('L', 2.0, lic='lengthening before δ(ϝ) inside the word: ' + word, lengthen=True))
    elif hiatus_final and dig:
        out.append(Opt('L', 2.0, lic='lengthening before digamma: %s + %s' % (word, nexttok['text']), lengthen=True))
    elif hiatus_final and is_dative_i(t, n):
        out.append(Opt('L', 3.0, lic='dative -ι scanned long: ' + word, lengthen=True))
    else:
        out.append(Opt('L', 6.0, lic='metrical lengthening: ' + word, flag=UNR, lengthen=True))
    return out


def syllable_candidates(toks, nuclei, force=None):
    """cands[i] = list of (advance, [Opt], merge_label).  force = {nucleus idx: 'L'|'S'} for the freedom test."""
    m = len(nuclei)
    cands = []
    for i, n in enumerate(nuclei):
        c = []
        o = options(toks, nuclei, i)
        if force and i in force:
            o = [x for x in o if x.w == force[i]] if i < m - 1 else o
        c.append((1, o, None))
        if i + 1 < m:
            n2 = nuclei[i + 1]
            t = toks[n.tok]
            if n2.tok == n.tok and n2.a == n.b and n.base in ('ε', 'ι', 'υ', 'ο'):   # first vowel simple, never a diphthong
                first = n.base
                cost = 1.5 if first == 'ε' else 3.5
                lab = 'synizesis: %s (%s%s)' % (t['text'], n.base, n2.base)
                o2 = [Opt(x.w, x.cost + cost, x.prior, lab + ('; ' + x.lic if x.lic else ''), x.flag) for x in
                      options(toks, nuclei, i + 1, nat='L')]
                c.append((2, o2, lab))
            elif n.final and n2.tok != n.tok and n.nat == 'L' and not t['elided']:
                cons, own, nexttok, punct = cluster_after(toks, nuclei, i)
                if not cons and nexttok is not None:
                    lab = 'synecphonesis: %s %s' % (t['text'], nexttok['text'])
                    sc = 2.0 if t['plain'] in SYNECPH_FIRST else 4.0
                    o2 = [Opt(x.w, x.cost + sc, x.prior, lab + ('; ' + x.lic if x.lic else ''), x.flag) for x in
                          options(toks, nuclei, i + 1, nat='L')]
                    c.append((2, o2, lab))
        cands.append(c)
    return cands


BICEPS_LENGTHEN_EXTRA = 1.5   # licence-lengthened syllables belong in the longum, not the biceps
EPS = 1e-9


def solve(toks, nuclei, force=None, max_paths=400):
    """-> (mincost, [paths]); path = list of (first_nucleus, advance, Opt, foot, slot)"""
    m = len(nuclei)
    cands = syllable_candidates(toks, nuclei, force)
    memo = {}

    def best(i, f, p):
        key = (i, f, p)
        if key in memo:
            return memo[key]
        if f == 6:
            r = 0.0 if i == m else float('inf')
            memo[key] = r
            return r
        if i >= m:
            memo[key] = float('inf')
            return memo[key]
        r = float('inf')
        for step in moves(i, f, p):
            adv, o, extra, nf, np_ = step
            v = o.cost + extra + best(i + adv, nf, np_)
            if v < r:
                r = v
        memo[key] = r
        return r

    def moves(i, f, p):
        for adv, opts, lab in cands[i]:
            if f == 5 and p == 1:
                if i + adv == m:
                    # final anceps: take the cheapest reading, record its natural weight
                    o = min(opts, key=lambda x: (x.cost if x.lic and x.lic.startswith('syn') else 0, x.prior))
                    base = o.cost if (adv == 2) else 0.0
                    oo = Opt(o.w, base, 0.0, o.lic if adv == 2 else None, None)
                    yield adv, oo, 0.0, 6, 0
                continue
            for o in opts:
                if p == 0:
                    if o.w == 'L':
                        yield adv, o, 0.0, f, 1
                elif p == 1:
                    if o.w == 'L':
                        yield adv, o, (BICEPS_LENGTHEN_EXTRA if o.lengthen else 0.0), f + 1, 0
                    else:
                        yield adv, o, 0.0, f, 2
                else:
                    if o.w == 'S':
                        yield adv, o, 0.0, f + 1, 0

    total = best(0, 0, 0)
    if total == float('inf'):
        return total, []
    paths = []

    def walk(i, f, p, acc):
        if len(paths) >= max_paths:
            return
        if f == 6:
            paths.append(list(acc))
            return
        target = best(i, f, p)
        for adv, o, extra, nf, np_ in moves(i, f, p):
            if abs(o.cost + extra + best(i + adv, nf, np_) - target) < EPS:
                acc.append((i, adv, o, f, p, extra))
                walk(i + adv, nf, np_, acc)
                acc.pop()

    walk(0, 0, 0, [])
    return total, paths


def path_key(path):
    fifth = [s for s in path if s[3] == 4]
    dact5 = 0 if len(fifth) == 3 else 1
    nlic = sum(1 for s in path if s[2].lic)
    prior = sum(s[2].prior for s in path)
    return (dact5, nlic, prior)


def signature(path):
    return tuple((s[0], s[1], s[2].w, s[3], s[4]) for s in path[:-1]) + ((path[-1][0], path[-1][1]),)


# ----------------------------------------------------------------------------- caesura + rendering
def choose_caesura(toks, nuclei, path):
    """returns (kind, syllable index after which it falls, token index after which ‖ is printed)"""
    def word_end(si):
        s = path[si]
        k = s[0] + s[1] - 1
        return nuclei[k].final and (si + 1 < len(path)) and nuclei[path[si + 1][0]].tok != nuclei[k].tok

    def after_tok(si):
        k = path[si][0] + path[si][1] - 1
        ti = nuclei[k].tok
        while ti + 1 < len(toks) and not toks[ti + 1]['nuclei']:
            ti += 1                                   # δ’ γ’ τ’ lean back on the word before them
        return ti

    def next_word_postpositive(ti):
        return ti + 1 < len(toks) and toks[ti + 1]['plain'] in POSTPOSITIVE and not _accented_orthotone(toks[ti + 1])

    def punct_at(si):
        k = path[si][0] + path[si][1] - 1
        a, b = nuclei[k].tok, after_tok(si)
        return any(toks[x]['punct_after'] for x in range(a, b + 1))

    pos = {}
    for si, s in enumerate(path):
        pos[(s[3], s[4])] = si
    cand = {}
    if (2, 0) in pos and word_end(pos[(2, 0)]):
        cand['masculine'] = pos[(2, 0)]
    if (2, 1) in pos and path[pos[(2, 1)]][2].w == 'S' and word_end(pos[(2, 1)]):
        cand['feminine'] = pos[(2, 1)]
    real = {k: v for k, v in cand.items() if not next_word_postpositive(after_tok(v)) or punct_at(v)}
    # a vowelless elided postpositive (δ’) is already carried across by after_tok
    pick = None
    if len(real) == 2:
        pm, pf = punct_at(real['masculine']), punct_at(real['feminine'])
        if pm and not pf:
            pick = 'masculine'
        elif pf and not pm:
            pick = 'feminine'
        else:
            # the short monosyllable between the two breaks: postpositive -> leans back (feminine);
            # otherwise it is a prepositive (ὁ, τό, ἐν, σύ …) and leans forward (masculine)
            mid = toks[nuclei[path[real['feminine']][0]].tok]
            pick = 'feminine' if mid['plain'] in POSTPOSITIVE else 'masculine'
    elif len(real) == 1:
        pick = next(iter(real))
    if pick:
        return pick, real[pick], after_tok(real[pick])
    if (3, 0) in pos and word_end(pos[(3, 0)]):
        si = pos[(3, 0)]
        if not next_word_postpositive(after_tok(si)) or punct_at(si):
            return 'hephthemimeral', si, after_tok(si)
    if cand:
        k = 'feminine' if 'feminine' in cand else 'masculine'
        return k, cand[k], after_tok(cand[k])
    if (3, 0) in pos and word_end(pos[(3, 0)]):
        si = pos[(3, 0)]
        return 'hephthemimeral', si, after_tok(si)
    return 'none', None, None


def _accented_orthotone(t):
    # οἵ / τίς / ἄν- etc. carry an accent when they are not the enclitic; δέ μέν γάρ keep theirs always
    return False


def pieces_for_token(t, groups):
    """groups: list of (a,b) letter ranges of the syllable nuclei in this token -> list of text pieces"""
    L = t['letters']
    if not groups:
        return []
    cuts = []
    for g in range(len(groups) - 1):
        b, a2 = groups[g][1], groups[g + 1][0]
        n = a2 - b
        if n <= 1:
            cuts.append(b)
        elif n == 2 and L[b][1] in MUTES and L[b + 1][1] in LIQ:
            cuts.append(b)
        else:
            cuts.append(b + 1)
    bounds = [0] + cuts + [len(L)]
    return [''.join(x[0] for x in L[bounds[i]:bounds[i + 1]]) for i in range(len(bounds) - 1)]


def render(toks, nuclei, path, caes):
    kind, csi, ctok = caes
    # pattern
    feet = [[] for _ in range(6)]
    for si, s in enumerate(path):
        mark = ANC if si == len(path) - 1 else (LONG if s[2].w == 'L' else SHORT)
        feet[s[3]].append(mark + (CAES if si == csi else ''))
    pattern = '|'.join(''.join(f) for f in feet)
    # tokens
    per_tok = {}
    for si, s in enumerate(path):
        ks = list(range(s[0], s[0] + s[1]))
        mark = ANC if si == len(path) - 1 else (LONG if s[2].w == 'L' else SHORT)
        digit = str(s[3] + 1) if s[4] == 0 else ''
        tks = sorted({nuclei[k].tok for k in ks})
        if len(tks) == 1:
            per_tok.setdefault(tks[0], []).append(((nuclei[ks[0]].a, nuclei[ks[-1]].b), digit, mark))
        else:                                   # synecphonesis: the first word's piece carries no mark
            per_tok.setdefault(tks[0], []).append(((nuclei[ks[0]].a, nuclei[ks[0]].b), digit, ''))
            per_tok.setdefault(tks[1], []).append(((nuclei[ks[1]].a, nuclei[ks[1]].b), '', mark))
    out = []
    for ti, t in enumerate(toks):
        syl = per_tok.get(ti, [])
        if not syl:
            s = t['text']
        else:
            pcs = pieces_for_token(t, [g for g, _, _ in syl])
            s = ''.join(d + p + mk for p, (_, d, mk) in zip(pcs, syl))
        if ctok == ti:
            s += CAES
        out.append(s)
    return pattern, out


def strip_marks(s):
    return re.sub('[1-6%s%s%s%s]' % (LONG, SHORT, ANC, CAES), '', s)


# ----------------------------------------------------------------------------- one line
def scan_line(text, n=None):
    toks, nuclei = analyse(text)
    res = {'n': n, 'text': text}
    total, paths = solve(toks, nuclei)
    if not paths:
        res.update(pattern='', caesura='none', cost=None, licences=[], flags=['NO FIT (%d syllables)' % len(nuclei)],
                   tokens=[t['text'] for t in toks], free=[])
        return res
    sigs = {}
    for p in paths:
        sigs.setdefault(signature(p), p)
    uniq = sorted(sigs.values(), key=path_key)
    path = uniq[0]
    flags = []
    if len(uniq) > 1:
        flags.append('AMBIGUOUS (%d scansions at cost %.1f)' % (len(uniq), total))
    lic = []
    for s in path:
        if s[2].lic:
            where = ''
            if s[2].lengthen:
                where = ' [in the biceps of foot %d]' % (s[3] + 1) if s[4] else ' [longum of foot %d]' % (s[3] + 1)
            lic.append(s[2].lic + where)
        if s[2].flag and s[2].flag not in flags:
            flags.append(s[2].flag)
    fifth = [s for s in path if s[3] == 4]
    if len(fifth) == 2:
        flags.append('spondaic fifth')
    caes = choose_caesura(toks, nuclei, path)
    pattern, tokstrs = render(toks, nuclei, path, caes)
    for t, s in zip(toks, tokstrs):
        assert strip_marks(s) == t['text'], (t['text'], s)
    nsyl = len(path)
    assert 12 <= nsyl <= 17
    # which open α ι υ were really free?  (force the opposite weight and re-solve)
    free = []
    for si, s in enumerate(path[:-1]):
        if s[1] != 1:
            continue
        nu = nuclei[s[0]]
        if nu.nat != 'U':
            continue
        cons = cluster_after(toks, nuclei, s[0])[0]
        if len(cons) >= 2 or any(c in DOUBLE for c in cons):
            continue
        alt, altpaths = solve(toks, nuclei, force={s[0]: 'S' if s[2].w == 'L' else 'L'}, max_paths=1)
        if altpaths and alt <= total + 1.0 + EPS:
            free.append('%s: %s scanned %s (alternative costs %.1f)' % (
                toks[nu.tok]['text'], nu.base, 'long' if s[2].w == 'L' else 'short', alt))
    res.update(pattern=pattern, caesura=caes[0], cost=round(total, 2), licences=lic, flags=flags, tokens=tokstrs,
               free=free, nsyl=nsyl,
               unknowns=['%s:%s%s' % (toks[nuclei[s[0]].tok]['text'], nuclei[s[0]].base, LONG if s[2].w == 'L' else SHORT)
                         for s in path[:-1] if s[1] == 1 and nuclei[s[0]].nat == 'U' and
                         not (len(cluster_after(toks, nuclei, s[0])[0]) >= 2 or
                              any(c in DOUBLE for c in cluster_after(toks, nuclei, s[0])[0]))])
    return res


# ----------------------------------------------------------------------------- I/O
def read_tei(path, books):
    x = open(path, encoding='utf8').read()
    out = []
    for m in re.finditer(r'<div n="(\d+)"[^>]*subtype="book"[^>]*>(.*?)</div>', x, re.S):
        b = int(m.group(1))
        if books and b not in books:
            continue
        for lm in re.finditer(r'<l\b[^>]*\bn="([^"]+)"[^>]*>(.*?)</l>', m.group(2), re.S):
            t = re.sub(r'<[^>]+>', '', lm.group(2))
            t = unicodedata.normalize('NFC', t.replace('ʼ', '’'))
            t = re.sub(r'\s+', ' ', t).strip()
            out.append({'n': '%d.%s' % (b, lm.group(1)), 't': t})
    return out


def table(results):
    rows = []
    for r in results:
        rows.append('%-7s %-32s %5s  %-15s %s%s' % (
            r['n'], r['pattern'], '-' if r['cost'] is None else ('%.1f' % r['cost']), r['caesura'],
            '; '.join(r['licences']) or '-', ('   !! ' + ', '.join(r['flags'])) if r['flags'] else ''))
    return rows


def summary(results):
    fit = [r for r in results if r['cost'] is not None]
    nofit = [r for r in results if r['cost'] is None]
    unres = [r for r in fit if 'UNRESOLVED' in r['flags']]
    amb = [r for r in fit if any(f.startswith('AMBIGUOUS') for f in r['flags'])]
    lines = ['lines: %d' % len(results),
             'fit at cost 0            : %d' % sum(1 for r in fit if r['cost'] == 0),
             'fit at cost < 2          : %d' % sum(1 for r in fit if r['cost'] < 2),
             'fit at cost >= 2, explained licences only : %d' % sum(1 for r in fit if r['cost'] >= 2 and r not in unres),
             'needed an UNRESOLVED licence : %d' % len(unres),
             'AMBIGUOUS                : %d' % len(amb),
             'no fit                   : %d' % len(nofit)]
    cnt = {}
    for r in fit:
        for l in r['licences']:
            k = l.split(':')[0].split(',')[0]
            cnt[k] = cnt.get(k, 0) + 1
    lines.append('licence counts: ' + ', '.join('%s %d' % kv for kv in sorted(cnt.items(), key=lambda kv: -kv[1])))
    caes = {}
    for r in fit:
        caes[r['caesura']] = caes.get(r['caesura'], 0) + 1
    lines.append('caesurae: ' + ', '.join('%s %d' % kv for kv in sorted(caes.items(), key=lambda kv: -kv[1])))
    return lines


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('src', nargs='?')
    ap.add_argument('out', nargs='?')
    ap.add_argument('--report')
    ap.add_argument('--notes', help='text file of by-eye review notes appended to the report')
    ap.add_argument('--tei')
    ap.add_argument('--books', default='')
    ap.add_argument('--worst', type=int, default=25)
    a = ap.parse_args()
    if a.tei:
        books = [int(b) for b in a.books.split(',') if b]
        src = read_tei(a.tei, books)
    else:
        src = json.load(open(a.src, encoding='utf8'))
    results = [scan_line(unicodedata.normalize('NFC', o['t'].replace('ʼ', '’')), o['n']) for o in src]
    rep = []
    if a.tei:
        rep.append('ROBUSTNESS RUN  %s  books %s' % (a.tei, a.books or 'all'))
        for b in (books or [None]):
            sub = [r for r in results if b is None or str(r['n']).startswith('%d.' % b)]
            rep.append('')
            rep.append('== Book %s ==' % b)
            rep += summary(sub)
        rep.append('')
        rep.append('== worst lines ==')
        worst = sorted(results, key=lambda r: -(999 if r['cost'] is None else r['cost']))[:a.worst]
        for r in worst:
            rep.append('%s  %s' % (r['n'], r['text']))
            rep.append('        ' + ' '.join(r['tokens']))
            rep += ['        ' + x for x in table([r])]
    else:
        rep.append('SCAN REPORT  %s' % a.src)
        rep += summary(results)
        rep.append('')
        rep.append('%-7s %-32s %5s  %-15s %s' % ('line', 'pattern', 'cost', 'caesura', 'licences   !! flags'))
        rep += table(results)
        rep.append('')
        rep.append('== syllabified lines, with every open α ι υ the solver had to decide ==')
        for r in results:
            rep.append('%-4s %s' % (r['n'], ' '.join(r['tokens'])))
            if r.get('unknowns'):
                rep.append('       α ι υ: ' + '  '.join(r['unknowns']))
            for f in r.get('free', []):
                rep.append('       FREE (not forced by the metre): ' + f)
        out = {'lines': [{'n': r['n'], 'pattern': r['pattern'], 'caesura': r['caesura'], 'cost': r['cost'],
                          'licences': r['licences'], 'flags': r['flags'], 'tokens': r['tokens']} for r in results]}
        json.dump(out, open(a.out, 'w', encoding='utf8'), ensure_ascii=False, indent=1)
    if a.notes:
        rep.append('')
        rep.append(open(a.notes, encoding='utf8').read().rstrip())
    text = '\n'.join(rep) + '\n'
    if a.report:
        open(a.report, 'w', encoding='utf8').write(text)
    else:
        sys.stdout.write(text)
    bad = [r for r in results if r['cost'] is None]
    return 1 if bad and not a.tei else 0


if __name__ == '__main__':
    sys.exit(main())
