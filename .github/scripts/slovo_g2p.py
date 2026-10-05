#!/usr/bin/env python3
"""Old East Slavic (Слово о пълку Игоревѣ, 1800 spelling) -> carrier text + IPA pins, for build_pinned.py.

This is the hand method used for the proem (claude/slovo-audio.json, July 2026), made automatic:
- the voice (ru-RU-Wavenet-A, rate 0.92) reads a modern-normalized Cyrillic CARRIER, and every carrier
  word is overridden by an IPA pin (Google customPronunciations), so the pins carry the pronunciation and
  the carrier only supplies clean word boundaries;
- convention: reconstructed late-12th-century Old East Slavic, as stated in slovo-audio.json — every
  vowel full in every position (no akanye), ы [ɨ], ѣ a clear [e], я/ю [ʲa]/[ʲu]; weak yers silent (a weak
  ь still softens the consonant before it), vocalized yers о/е; г [g] (also in -его/-ого), ч [tʃ],
  ш [ʃ], ж [ʒ], щ [ʃtʃ], ц [ts], х [x]; consonants other than к г х ж ш ч щ ц soften before ь е и ѣ я ю;
  no final devoicing; titlo numerals read as the number word (ĩ десять, д̃ четыре, г̃ три).
- stress is free in Old East Slavic and is the least certain layer. It comes from the stress lexicon
  .github/pipeline/slovo/audio-lexicon.json: for every word form of the poem, its carrier with the
  stressed vowel marked (U+0301). The lexicon was drafted 2026-10-04 from attested Old Russian / modern
  reflexes and the proem's hand pins; correct a word there and only the clips containing it are remade.
"""
import json, os, re, unicodedata as U

HERE = os.path.dirname(os.path.abspath(__file__))
LEX_PATH = os.path.join(HERE, "..", "pipeline", "slovo", "audio-lexicon.json")
ACUTE = "́"
NUMERALS = {"ĩ": "десять", "д̃": "четыре", "г̃": "три", "і̃": "десять"}
VOWELS = "аеёиоуыэюяѣі"
HARD_ONLY = set("кгхжшчщцй")
PAL_VOWELS = {"е": "e", "и": "i", "я": "a", "ю": "u", "ё": "o"}
PLAIN_V = {"а": "a", "о": "o", "у": "u", "ы": "ɨ", "э": "e"}
CONS = {"б": "b", "в": "v", "г": "ɡ", "д": "d", "ж": "ʒ", "з": "z", "к": "k", "л": "l", "м": "m",
        "н": "n", "п": "p", "р": "r", "с": "s", "т": "t", "ф": "f", "х": "x", "ц": "ts", "ч": "tʃ",
        "ш": "ʃ", "щ": "ʃtʃ", "й": "j", "ѳ": "f"}
PREP = {"къ", "съ", "въ", "отъ", "подъ", "надъ", "предъ", "изъ", "безъ", "объ", "възъ"}

_LEX = None


def lexicon():
    global _LEX
    if _LEX is None:
        try:
            _LEX = json.load(open(LEX_PATH, encoding="utf-8"))
        except FileNotFoundError:
            _LEX = {}
    return _LEX


def draft_carrier(word):
    """Modern-normalized carrier for one word of the 1800 text (no stress). Rules only; the lexicon wins."""
    w = U.normalize("NFC", word.lower())
    for k, v in NUMERALS.items():
        if w == U.normalize("NFC", k):
            return v
    w = w.replace("ѣ", "е").replace("і", "и").replace("ѵ", "и").replace("ѳ", "ф")
    if w in PREP:
        return w[:-1]
    if w.endswith("ъ"):
        w = w[:-1]
    nv = sum(ch in VOWELS for ch in w)
    if nv == 0 and "ъ" in w:                 # нъ, тъ: a word whose only vowel is a yer keeps it
        w = w.replace("ъ", "о")
    # yer in a liquid group between consonants: пълку -> полку, плъкы -> полкы, бръзыя -> борзыя
    C = "бвгджзклмнпрстфхцчшщ"
    w = re.sub("([%s])ъ([рл])(?=[%s])" % (C, C), r"\1о\2", w)
    w = re.sub("([%s])([рл])ъ(?=[%s])" % (C, C), r"\1о\2", w)
    w = re.sub("([%s])ь([рл])(?=[%s])" % (C, C), r"\1е\2", w)
    w = re.sub("([%s])([рл])ь(?=[%s])" % (C, C), r"\1е\2", w)
    w = w.replace("ъ", "о")                  # remaining medial ъ: Святъславъ -> Святослав
    return w


def carrier(word):
    """Stressed carrier (with U+0301) for a word of the text: the lexicon's, else the draft."""
    k = U.normalize("NFC", word.lower())
    return lexicon().get(k) or draft_carrier(word)


def carrier_ipa(c):
    """IPA for a (stressed) carrier word."""
    c = U.normalize("NFD", c.lower())
    c = U.normalize("NFC", c.replace("̆", "̆"))  # keep й composed
    out = []          # list of (kind, ipa)
    stress_at = None
    prev = None
    chars = list(U.normalize("NFC", c.lower()))
    for k, ch in enumerate(chars):
        if ch == ACUTE:
            stress_at = len(out) - 1
            continue
        if ch in PLAIN_V:
            out.append(("V", PLAIN_V[ch]))
        elif ch in PAL_VOWELS:
            v = PAL_VOWELS[ch]
            if out and out[-1][0] == "C" and prev not in HARD_ONLY and prev is not None and not out[-1][1].endswith("ʲ"):
                out[-1] = ("C", out[-1][1] + "ʲ")
                out.append(("V", v))
            elif out and out[-1][0] == "C":
                out.append(("V", v))
            else:                              # initial, after a vowel, after ь/ъ: [j]
                if ch == "и" and not (prev in ("ь", "ъ")):
                    out.append(("V", "i"))
                else:
                    out.append(("C", "j")); out.append(("V", v))
        elif ch == "ь":
            if out and out[-1][0] == "C" and prev not in HARD_ONLY and not out[-1][1].endswith("ʲ"):
                out[-1] = ("C", out[-1][1] + "ʲ")
        elif ch == "ъ":
            pass
        elif ch in CONS:
            out.append(("C", CONS[ch]))
        prev = ch
    nv = sum(1 for t, _ in out if t == "V")
    if stress_at is None or nv < 2:
        return "".join(x for _, x in out)
    # ˈ before the onset: the consonant just before the vowel, or the whole cluster if word-initial
    j = stress_at
    while j - 1 >= 0 and out[j - 1][0] == "C":
        j -= 1
    if j > 0 and j < stress_at - 1:
        a, b = out[stress_at - 2][1], out[stress_at - 1][1]
        two = (a[:1] in "pbtdkɡfv" and b in ("r", "rʲ", "l", "lʲ")) or a in ("s", "sʲ", "z", "zʲ")
        j = stress_at - 2 if two else stress_at - 1
    seq = [x for _, x in out]
    seq.insert(j, "ˈ")
    return "".join(seq)


def ipa(word):
    """IPA for one token of the text (a hyphenated token's parts are joined by a space)."""
    return " ".join(carrier_ipa(c) for p in word.split("-") if p for c in carrier(p).split())


def plain(c):
    return U.normalize("NFC", U.normalize("NFD", c).replace(ACUTE, ""))


def request(text, word_re):
    """(carrier text, [(phrase, ipa)]) for a stretch of the 1800 text: words replaced by carriers."""
    pins, out, pos = {}, [], 0
    for m in word_re.finditer(text):
        out.append(text[pos:m.start()])
        parts = []
        for p in m.group(0).split("-"):
            if not p:
                continue
            sub = []
            for c in carrier(p).split():               # лѣполи -> two carrier words, лепо ли
                pc = plain(c)
                ip = carrier_ipa(c)
                # A vowelless carrier (в, с, к from въ, съ, къ) gets no pin: Google rejects a custom
                # pronunciation with no vowel (run #288, 2026-10-05: "phrases are invalid: в, с").
                # The voice reads it as the ordinary Russian proclitic, joined to the next word.
                if any(ch in "aeiouɨ" for ch in ip):
                    pins[pc.lower()] = ip
                sub.append(pc)
            pc = " ".join(sub)
            parts.append(pc if not p[:1].isupper() else pc[:1].upper() + pc[1:])
        out.append("-".join(parts))
        pos = m.end()
    out.append(text[pos:])
    t = "".join(out).replace("\n", " ")
    return t, sorted(pins.items())


if __name__ == "__main__":
    import sys
    for w in sys.argv[1:]:
        print(w, carrier(w), ipa(w))
