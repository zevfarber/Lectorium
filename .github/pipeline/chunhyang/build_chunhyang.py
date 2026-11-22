#!/usr/bin/env python3
"""Build chunhyang-001.json from units.py + glossary.py, and validate it.

Usage: python3 build_chunhyang.py <repo-root>
"""
import json, os, re, sys, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from units import UNITS
from glossary import G

OLD = {
    "{hA}": "ᄒᆞ", "{hAi}": "ᄒᆡ", "{dAi}": "ᄃᆡ",
    "{sAing}": "ᄉᆡᆼ", "{bAik}": "ᄇᆡᆨ", "{mAi}": "ᄆᆡ",
    "{jAi}": "ᄌᆡ", "{nAi}": "ᄂᆡ", "{sdAi}": "ᄯᆡ",
    "{sgAi}": "ᄭᆡ", "{sgis}": "ᄭᅵᆺ",
}


def ex(s):
    for k, v in OLD.items():
        s = s.replace(k, v)
    assert "{" not in s, s
    return unicodedata.normalize("NFC", s)


# reader.html's WORD_RE, Hangul part (plus the classes that matter for checking punctuation)
HANGUL = "ᄀ-ᇿㄱ-ㆎ〻ꥠ-꥿가-힣ힰ-퟿"
WORD_RE = re.compile("[A-Za-z" + HANGUL + "]+")

ABOUT = ("Chunhyang is the best-loved story in Korean: the daughter of a retired kisaeng and a nobleman "
         "marries the governor’s son in secret, refuses the next governor who wants her for himself, and "
         "is beaten and jailed for it until her husband comes back. It began as pansori, a story sung by "
         "one singer with a drummer, and this printed version keeps the singer’s voice — the asides, the "
         "jokes, the long runs of Chinese learning beside plain speech. The Jeonju woodblock edition in "
         "84 leaves, from the first years of the twentieth century, is the fullest and most admired of the "
         "printed texts. It spells Korean as it was spoken in the southwest, and it still uses the old letter "
         "ㆍ (arae-a); the toggle shows each word in modern spelling.")

SOURCE = ("Text: 열여츈향슈졀가 (Yeollyeo Chunhyang sujeolga), Jeonju woodblock edition in 84 leaves (2 vols., "
          "45 + 39 leaves), Dagaseopo (多佳書舗) printing, c. 1912–1926; University of Tokyo, Graduate School "
          "of Humanities and Sociology, Linguistics Library, Ogura Shinpei collection, L174842 (digitized with "
          "Korea University). Leaves 1a–2a, transcribed by eye from the scan. Spelling as printed, with the old "
          "letter ㆍ (arae-a) and the repeat mark 〻. The print has no spaces or punctuation: word division here "
          "is editorial, following modern spacing. The woodcut often reduces the dot of ㆍ to a touch on the next "
          "stroke; where it cannot be seen, the reading follows the edition’s regular spellings (ᄒᆞ, ᄃᆡ, ᄉᆡᆼ), "
          "and doubtful words are noted. The modern-spelling view and the reading voice follow present-day South "
          "Korean spelling and standard pronunciation. Translations made fresh from the Korean for Lectorium; no "
          "translation consulted.")


def main(root):
    sentences, gl = [], {}
    gx = {ex(k): ex(v) for k, v in G.items()}
    word_say, used = {}, set()
    for u in UNITS:
        t, mt, say = ex(u["t"]), ex(u["mt"]), ex(u["say"])
        tt, mm = WORD_RE.findall(t), WORD_RE.findall(mt)
        st = WORD_RE.findall(say)
        assert t.split() == tt, ("t has non-word characters", t)
        assert len(tt) == len(mm) == len(st), (t, len(tt), len(mm), len(st))
        assert mm == st, ("say words differ from mt", mm, st)
        for a, b in zip(tt, mm):
            assert a.lower() in gx, ("no glossary entry", a)
            used.add(a.lower())
            if a != b:
                if word_say.get(a.lower(), b) != b:
                    raise SystemExit("one printed form, two modern forms: %s" % a)
                word_say[a.lower()] = b
        s = {"t": t, "mt": mm, "say": say, "l": u["l"], "i": u["i"], "n": ex(u["n"])}
        if u.get("p"):
            s = {"p": True, **s}
        sentences.append(s)
    unused = set(gx) - used
    assert not unused, ("unused glossary keys", unused)
    story = {
        "id": "chunhyang-001",
        "title": ex("열여츈향슈졀가"),
        "titleRead": "Yeollyeo Chunhyang sujeolga",
        "titleEn": "Chunhyang — 1: The Age of King Sukjong; Wolmae Longs for a Child",
        "work": ex("열여츈향슈졀가"),
        "workEn": "Chunhyang (The Song of the Faithful Wife Chunhyang)",
        "part": "1 · The age of King Sukjong; Wolmae longs for a child (leaves 1a–2a)",
        "language": "Korean",
        "langCode": "ko-KR",
        "script": "hangul",
        "source": SOURCE,
        "about": ABOUT,
        "wordClips": True,
        "wordSay": dict(sorted(word_say.items())),
        "sayNames": ["숙종대왕", "요순", "우탕", "남원부에", "월매라", "월매", "성가라", "성참판", "공부자도",
                     "이구산에", "정나라", "정자산은", "우성산에", "웅천", "주천의는"],
        "sentences": sentences,
        "glossary": {k: gx[k] for k in sorted(gx)},
    }
    out = os.path.join(root, "chunhyang-001.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(story, f, ensure_ascii=False, indent=1)
        f.write("\n")
    json.load(open(out, encoding="utf-8"))
    print("wrote", out, "-", len(sentences), "units,", sum(len(s["mt"]) for s in sentences), "words,",
          len(gx), "glossary forms,", len(word_say), "respelled for the voice")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
