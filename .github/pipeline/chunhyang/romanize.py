"""Revised Romanization of Korean (2000), as pronounced, for the Chunhyang romanization line (tr).

Input is modern Hangul (each unit's `say`). Sound changes are applied inside each word, as the
Revised Romanization does: linking of a final consonant into a following vowel, nasalization,
ㄴ/ㄹ → ll, aspiration with ㅎ, and palatalization of ㄷ/ㅌ before 이. Tensification is not written.
Punctuation and spaces pass through unchanged.
"""
import re

CHO = ["g", "kk", "n", "d", "tt", "r", "m", "b", "pp", "s", "ss", "", "j", "jj", "ch", "k", "t", "p", "h"]
JUNG = ["a", "ae", "ya", "yae", "eo", "e", "yeo", "ye", "o", "wa", "wae", "oe", "yo", "u", "wo", "we", "wi",
        "yu", "eu", "ui", "i"]
# final consonants by index (0 = none), as jamo letters
JONG = ["", "ㄱ", "ㄲ", "ㄳ", "ㄴ", "ㄵ", "ㄶ", "ㄷ", "ㄹ", "ㄺ", "ㄻ", "ㄼ", "ㄽ", "ㄾ", "ㄿ", "ㅀ", "ㅁ", "ㅂ", "ㅄ",
        "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]
CHO_J = ["ㄱ", "ㄲ", "ㄴ", "ㄷ", "ㄸ", "ㄹ", "ㅁ", "ㅂ", "ㅃ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅉ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]
CHO_R = dict(zip(CHO_J, CHO))
# a final as it is said before a consonant or at the end of a word (the seven representative sounds)
FINAL = {"": "", "ㄱ": "k", "ㄲ": "k", "ㄳ": "k", "ㄺ": "k", "ㅋ": "k",
         "ㄴ": "n", "ㄵ": "n", "ㄶ": "n",
         "ㄷ": "t", "ㅅ": "t", "ㅆ": "t", "ㅈ": "t", "ㅊ": "t", "ㅌ": "t", "ㅎ": "t",
         "ㄹ": "l", "ㄼ": "l", "ㄽ": "l", "ㄾ": "l", "ㅀ": "l",
         "ㅁ": "m", "ㄻ": "m",
         "ㅂ": "p", "ㅍ": "p", "ㅄ": "p", "ㄿ": "p",
         "ㅇ": "ng"}
# compound finals: (stays, moves into a following vowel)
SPLIT = {"ㄳ": ("ㄱ", "ㅅ"), "ㄵ": ("ㄴ", "ㅈ"), "ㄶ": ("ㄴ", "ㅎ"), "ㄺ": ("ㄹ", "ㄱ"), "ㄻ": ("ㄹ", "ㅁ"),
         "ㄼ": ("ㄹ", "ㅂ"), "ㄽ": ("ㄹ", "ㅅ"), "ㄾ": ("ㄹ", "ㅌ"), "ㄿ": ("ㄹ", "ㅍ"), "ㅀ": ("ㄹ", "ㅎ"),
         "ㅄ": ("ㅂ", "ㅅ")}
ASPIRATE = {"ㄱ": "ㅋ", "ㄷ": "ㅌ", "ㅈ": "ㅊ", "ㅂ": "ㅍ"}


def _syllables(word):
    out = []
    for ch in word:
        c = ord(ch) - 0xAC00
        if not 0 <= c < 11172:
            raise ValueError("not a modern Hangul syllable: %r in %r" % (ch, word))
        out.append([CHO_J[c // 588], (c % 588) // 28, JONG[c % 28]])
    return out


def _word(word):
    sy = _syllables(word)
    for k in range(len(sy) - 1):
        a, b = sy[k], sy[k + 1]
        fin, ini = a[2], b[0]
        if not fin:
            continue
        if ini == "ㅇ":                      # linking into a vowel
            if fin == "ㅇ":
                continue
            if fin in ("ㅎ",):
                a[2] = ""
                continue
            if fin in ("ㄶ", "ㅀ"):
                a[2], b[0] = "", SPLIT[fin][0]
                continue
            stay, move = SPLIT.get(fin, ("", fin))
            if move == "ㅆ":
                move = "ㅆ"
            if JUNG[b[1]] == "i" and move in ("ㄷ", "ㅌ"):   # palatalization: 굳이 → 구지
                move = "ㅈ" if move == "ㄷ" else "ㅊ"
            a[2], b[0] = stay, move
            continue
        if ini == "ㅎ":
            # k/t/p + ㅎ: the h is kept, as the Revised Romanization does in nouns and in -하다 verbs
            # (덕화 deokhwa, 생각하고 saenggakhago); ㅈ + ㅎ is aspirated (맞히다 machida)
            if fin == "ㅎ":
                a[2] = ""
            elif fin == "ㅈ":
                a[2], b[0] = "", "ㅊ"
            continue
        if fin in ("ㅎ", "ㄶ", "ㅀ") and ini in ASPIRATE:   # ㅎ + ㄱㄷㅈ → aspirate
            a[2], b[0] = ("" if fin == "ㅎ" else SPLIT[fin][0]), ASPIRATE[ini]
            continue
        f = FINAL[fin]
        if ini in ("ㄴ", "ㅁ") and f in ("k", "t", "p"):   # nasalization
            a[2] = {"k": "ㅇ", "t": "ㄴ", "p": "ㅁ"}[f]
            continue
        if ini == "ㄹ":
            if f in ("n", "l"):
                a[2], b[0] = "ㄹ", "ㄹ"
            elif f in ("m", "ng"):
                b[0] = "ㄴ"
            elif f in ("k", "t", "p"):
                a[2], b[0] = {"k": "ㅇ", "t": "ㄴ", "p": "ㅁ"}[f], "ㄴ"
            continue
        if ini == "ㄴ" and f == "l":
            b[0] = "ㄹ"
    out = []
    for k, (ini, v, fin) in enumerate(sy):
        cho = CHO_R[ini]
        if ini == "ㄹ":
            cho = "l" if k and FINAL[sy[k - 1][2]] == "l" else "r"
        out.append(cho + JUNG[v] + FINAL[fin])
    return "".join(out)


def romanize(text, names=()):
    """names: modern-Hangul stems of proper names; a word beginning with one is capitalized,
    as is the first word of the text."""
    def one(m):
        w = m.group(0)
        r = _word(w)
        if m.start() == 0 or any(w.startswith(n) for n in names):
            r = r[:1].upper() + r[1:]
        return r
    return re.sub("[가-힣]+", one, text)


if __name__ == "__main__":
    import sys
    for w in sys.argv[1:]:
        print(w, romanize(w))
