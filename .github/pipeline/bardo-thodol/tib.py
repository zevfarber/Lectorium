# Tibetan helpers for the Bardo Thodol pilot: letters (Wylie) and pronunciation (THL Simplified
# Phonetic Transcription, Germano & Tournadre 2003) for a word given in Tibetan script.
import re
import pyewts
_C = pyewts.pyewts()
TSHEG = '་'
PUNCT = '༔།༈༄༅'   # ༔ ། ༈ ༄ ༅

def wylie_syl(syl):
    """EWTS for one syllable, in the form shown to the reader (long vowels with macrons, no '+')."""
    w = _C.toWylie(syl).strip()
    w = w.replace('+', '')
    w = w.replace('A', 'ā').replace('I', 'ī').replace('U', 'ū').replace('M', 'ṃ')
    return w

ROOT = {'k': 'k', 'kh': 'kh', 'g': 'g', 'ng': 'ng', 'c': 'ch', 'ch': 'ch', 'j': 'j', 'ny': 'ny',
        't': 't', 'th': 't', 'd': 'd', 'n': 'n', 'p': 'p', 'ph': 'p', 'b': 'b', 'm': 'm',
        'ts': 'ts', 'tsh': 'ts', 'dz': 'dz', 'w': 'w', 'zh': 'zh', 'z': 'z', "'": '', 'y': 'y',
        'r': 'r', 'l': 'l', 'sh': 'sh', 's': 's', 'h': 'h', '': '',
        'ky': 'ky', 'khy': 'khy', 'gy': 'gy', 'py': 'ch', 'phy': 'ch', 'by': 'j', 'my': 'ny',
        'kr': 'tr', 'khr': 'tr', 'gr': 'dr', 'tr': 'tr', 'thr': 'tr', 'dr': 'dr', 'pr': 'tr',
        'phr': 'tr', 'br': 'dr', 'sr': 's', 'hr': 'hr', 'mr': 'm', 'nr': 'n', 'shr': 'sh',
        'kl': 'l', 'gl': 'l', 'bl': 'l', 'rl': 'l', 'sl': 'l', 'zl': 'd', 'lh': 'lh',
        'g.y': 'y', 'db': 'w', 'dby': 'y', 'dbr': 'r'}
STRIP = "gdbm'rls"
SUF = {'g': 'k', 'ng': 'ng', 'd': '', 'n': 'n', 'b': 'p', 'm': 'm', "'": '', 'r': 'r', 'l': 'l', 's': '', '': ''}
FRONT = {'a': 'e', 'o': 'ö', 'u': 'ü', 'i': 'i', 'e': 'e'}
SYL = re.compile(r"^(.*?)([aeiou])(ng|[gdnbm'rls])?(s|d)?('i|'o|'u|'am|'ang)?$")

def onset_sound(on):
    o = on
    while True:
        if o in ROOT: return ROOT[o]
        if o.endswith('w') and o[:-1] in ROOT: return ROOT[o[:-1]]      # wa-zur is silent
        if o and o[0] in STRIP: o = o[1:]
        else: raise ValueError('onset ' + on)

def thl_syl(w, pos, prev=''):
    """w: plain EWTS syllable (ASCII); pos: index of the syllable in its word; prev: the syllable before it."""
    m = SYL.match(w)
    if not m: raise ValueError('syllable ' + w)
    on, v, s1, s2, tail = m.group(1), m.group(2), m.group(3) or '', m.group(4) or '', m.group(5) or ''
    c = onset_sound(on)
    if on == 'db' and v == 'u': c = ''                                    # dbu, dbus, dbugs
    if pos > 0 and on == 'b' and v in 'ao' and s1 in ('', 'r', 's') and not s2 \
       and re.search(r"([aeiou]|ng|r|l|'|d|s)$", prev) and not re.search(r"[gbm]s$", prev): c = 'w'   # ba, bo after an open or soft ending
    if s1 in ('d', 'n', 'l', 's') and not s2: v2 = FRONT[v]
    else: v2 = v
    out = c + v2 + SUF[s1]
    if tail == "'i": out = c + {'a': 'e', 'e': 'e', 'i': 'i', 'o': 'ö', 'u': 'ü'}[v]
    elif tail in ("'am", "'ang"): out += tail
    elif tail: out += tail[1:]
    return out

OVERRIDE = {'pad+ma': 'pema', 'd+hU': 'dhu', 'tIr': 'tir', 'kyai': 'kyé',
            'd+hu': 'dhu', 'A': 'a', "seng+ge'i": 'sengge'}   # 2026-11-20: bardo-thodol-002

def word(tok):
    """tok: one word in Tibetan script, syllables joined by tsheg, optional trailing tsheg / punctuation.
    Returns (key, glyphs, reading, say)."""
    lead = ''
    while tok and tok[0] in PUNCT + ' ': lead += tok[0]; tok = tok[1:]
    trail = ''
    while tok and tok[-1] in PUNCT: trail = tok[-1] + trail; tok = tok[:-1]
    has_tsheg = tok.endswith(TSHEG)
    syls = [s for s in tok.split(TSHEG) if s]
    glyphs = []
    if lead: glyphs.append({'s': lead, 'tr': ' ', 'role': 'punct'})
    wy, say = [], []
    prev = ''
    for i, s in enumerate(syls):
        raw = _C.toWylie(s).strip()
        wy.append(wylie_syl(s))
        say.append(OVERRIDE[raw] if raw in OVERRIDE else thl_syl(raw, i, prev))
        prev = raw
        last = (i == len(syls) - 1)
        glyphs.append({'s': s + (TSHEG if (not last or has_tsheg) else ''), 'tr': wy[-1]})
    if trail: glyphs.append({'s': trail, 'tr': ' ', 'role': 'punct'})
    sayw = ''.join(say)
    if sayw.endswith('e'): sayw = sayw[:-1] + 'é'
    return TSHEG.join(syls), glyphs, ' '.join(wy), sayw

if __name__ == '__main__':
    for t in ['ཐོས་གྲོལ་', 'འོད་དཔག་མེད༔', 'སྣང་བ་མཐའ་ཡས་', 'ལོངས་སྤྱོད་རྫོགས་སྐུ་', 'པདྨ་འབྱུང་གནས་', 'འགྲོ་བའི་', 'དབང་པོ་',
              'ཕྱག་འཚལ་ལོ༔', 'རྣལ་འབྱོར་', 'གཡས་', 'དབྱངས་', 'བླ་མའམ་', 'བྱའོ༔', 'ཀྱཻ༔', 'དྷཱུ་ཏཱིར་', 'སངས་རྒྱས་', 'ཡེ་ཤེས་', 'སྨྲེ་སྔགས་']:
        print(t, word(t)[2:], sep='  ')
