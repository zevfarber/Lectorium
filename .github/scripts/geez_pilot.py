#!/usr/bin/env python3
"""Pilot only (2026-11-01): voices for Ge'ez (the Kebra Nagast), for Zev to compare by ear.

Two choices ride on this round: the pronunciation convention (traditional Ethiopian church reading vs
reconstructed Ge'ez) and the voice. Google has no Ge'ez voice; every option borrows one.

  A  Amharic voice reading the Ge'ez letters as printed. Amharic is written in the same letters and
     the Ethiopian church reads Ge'ez with Amharic sounds, so this is the traditional liturgical sound:
     the throat letters (ሀ ሐ ኀ, አ ዐ) and ሰ/ሠ, ጸ/ፀ merge, as in church today.
  B  Arabic voice reading the text changed into vocalized Arabic letters (from the romanization).
     Reconstructed Ge'ez: keeps ḥ, ʿ, ḫ, q, the emphatics and doubled consonants, the sounds Ge'ez
     shares with Arabic. Limits: Arabic has no g (ج is read j), no e/o (read ī/ū).
  C  German voice given the exact sounds (IPA), as for Akkadian, Greek and Latin. Reconstructed, but
     the throat sounds and emphatics are lost (ḥ = h, q = k, ʿ silent); doubled consonants read single.
  D  American English voice given the exact sounds (IPA), as for Beowulf. Same losses as C, keeps the
     doubled consonants.

Stress in C and D: on the next-to-last syllable (the usual simplified rule for Ge'ez).
A voice Google refuses is skipped, and the next one listed for that option is tried.
Writes audio-pilot/geez/<option>/<k>.mp3, audio-pilot/geez/lines.json, voices.json.
Usage: python3 geez_pilot.py            Env: GOOGLE_TTS_KEY
       python3 geez_pilot.py --show     (prints what each option is sent; no network)
"""
import json, os, re, sys, time, unicodedata as U
from xml.sax.saxutils import escape

LINES = [  # (key, citation, fidel, romanization as published, English)
    ("1", "ch. 21",
     "ንግሥተ ፡ አዜብ ፡ ትትነሣእ ፡ አመ ፡ ዕለተ ፡ ኰነኔ ፡ ወትትዋቀሦሙ ፡ ወትትፋትሖሙ ፡ ወትመውኦሙ ፡ ለዛቲ ፡ ትውልድ ፡ እለ ፡ ኢሰምዑ ፡ ስብከተ ፡ ቃልየ ፤",
     "nəgśətä ʾäzeb tətnäśaʾ ʾämä ʿəlätä kʷänäne wättəwaqäśomu wättəfatḥomu wätmäwʾomu läzati təwləd ʾəlä ʾisämʿu səbkätä qalyä",
     "The Queen of the South will rise up on the day of judgment, and reproach them and contend with them and overcome them, this generation, who did not hear the preaching of my word."),
    ("2", "ch. 24",
     "ወትቤሎሙ ፡ ስምዑ ፡ ቃልየ ፡ እሊአየ ፡ ወአፅምኡኒ ፡ ነገርየ ፤",
     "wätbelomu səmʿu qalyä ʾəliʾäyä wäʾäṣ́məʾuni nägäryä",
     "And she said to them: Hear my word, my own people, and give ear to my speech."),
    ("3", "ch. 24",
     "እስመ ፡ ተነደፍኩ ፡ በፍቅረ ፡ ጥበብ ፡ ወተስሕብኩ ፡ በአሕባለ ፡ አእምሮ ፤",
     "ʾəsmä tänädäfku bäfqərä ṭəbäb wätäsḥəbku bäʾäḥbalä ʾäʾməro",
     "For I was pierced by love of wisdom and drawn by the cords of knowledge."),
    ("4", "ch. 24",
     "እስመ ፡ ትኄይስ ፡ ጥበብ ፡ እመዝገበ ፡ ወርቅ ፡ ወብሩር ፤",
     "ʾəsmä təḫeys ṭəbäb ʾəmäzgäbä wärq wäbrur",
     "For wisdom is better than a treasury of gold and silver."),
    ("5", "ch. 24",
     "ጥበብሰ ፡ ትኄይስ ፡ እምነ ፡ ኴሉ ፡ ዘተፈጥረ ፡ ዲበ ፡ ምድር ።",
     "ṭəbäbsä təḫeys ʾəmnä kʷelu zätäfäṭrä dibä mədr",
     "Wisdom is better than all that was created on the earth."),
]

VOWELS = {"ä", "a", "ə", "i", "u", "e", "o"}


def segments(word):
    """Romanized word -> [('C', letter) | ('V', vowel)], labialization as its own ('W',) segment."""
    w = U.normalize("NFD", word)
    out, i = [], 0
    while i < len(w):
        ch = w[i]; j = i + 1
        while j < len(w) and U.combining(w[j]): j += 1
        tok = U.normalize("NFC", w[i:j]); i = j
        if tok == "ʷ": out.append(("W", "w"))
        elif tok in VOWELS: out.append(("V", tok))
        elif tok.strip(): out.append(("C", tok))
    return out


# ---- B: vocalized Arabic letters ---------------------------------------------------------------
AR_C = {"b": "ب", "g": "ج", "d": "د", "h": "ه", "w": "و", "z": "ز", "ž": "ج", "ḥ": "ح", "ṭ": "ط",
        "y": "ي", "k": "ك", "l": "ل", "m": "م", "n": "ن", "ñ": "ن", "s": "س", "ʿ": "ع", "f": "ف",
        "ṣ": "ص", "ṣ́": "ض", "q": "ق", "r": "ر", "ś": "ش", "t": "ت", "č": "تش", "ḫ": "خ",
        "p": "ب", "p̣": "ب", "ʾ": "ء"}
FATHA, KASRA, DAMMA, SUKUN, SHADDA = "َ", "ِ", "ُ", "ْ", "ّ"
AR_V = {"ä": FATHA, "a": FATHA + "ا", "ə": KASRA, "i": KASRA + "ي", "e": KASRA + "ي",
        "u": DAMMA + "و", "o": DAMMA + "و"}


def arabic(word):
    segs = segments(word)
    out, k = "", 0
    while k < len(segs):
        t, x = segs[k]
        if t == "V":  # a vowel with no consonant before it: seat it on an alif
            out += "ا" + AR_V[x]; k += 1; continue
        letter = AR_C.get(x, "")
        if t == "W": letter = "و"
        gem = k + 1 < len(segs) and segs[k + 1] == (t, x) and t == "C"
        nxt = segs[k + 2] if gem and k + 2 < len(segs) else (segs[k + 1] if not gem and k + 1 < len(segs) else None)
        if x == "ʾ":  # hamza: seat by the vowels around it
            prev = segs[k - 1][1] if k > 0 and segs[k - 1][0] == "V" else None
            nv = nxt[1] if nxt and nxt[0] == "V" else None
            if k == 0:
                letter = "إ" if nv in ("ə", "i", "e") else ("آ" if nv == "a" else "أ")
            elif prev in ("ə", "i", "e") or nv in ("i", "e"): letter = "ئ"
            elif prev in ("u", "o") or nv in ("u", "o"): letter = "ؤ"
            elif nv in ("ä", "a") or prev in ("ä", "a"): letter = "أ"
        out += letter + (SHADDA if gem else "")
        k += 2 if gem else 1
        if nxt and nxt[0] == "V":
            out += ("" if letter == "آ" else AR_V[nxt[1]]); k += 1
        else:
            out += SUKUN
    return out


# ---- C, D: IPA for a carrier voice ----------------------------------------------------------------
IPA_C = {"b": "b", "g": "g", "d": "d", "h": "h", "w": "w", "z": "z", "ž": "ʒ", "ḥ": "h", "ṭ": "t",
         "y": "j", "k": "k", "l": "l", "m": "m", "n": "n", "ñ": "n", "s": "s", "ʿ": "", "f": "f",
         "ṣ": "ts", "ṣ́": "ts", "q": "k", "r": "r", "ś": "s", "t": "t", "č": "tʃ", "ḫ": "x",
         "p": "p", "p̣": "p", "ʾ": ""}
IPA_V = {"de": {"ä": "a", "a": "aː", "ə": "ɪ", "i": "iː", "u": "u", "e": "e", "o": "o"},
         "en": {"ä": "a", "a": "aː", "ə": "ɪ", "i": "iː", "u": "uː", "e": "eː", "o": "oː"}}


def ipa(word, inv):
    segs = segments(word)
    vi = [n for n, s in enumerate(segs) if s[0] == "V"]
    stress = None
    if len(vi) >= 2:  # next-to-last vowel; the mark goes before that syllable's consonant
        n = vi[-2]
        stress = n - 1 if n > 0 and segs[n - 1][0] != "V" else n
    out, prev = "", None
    for n, (t, x) in enumerate(segs):
        sym = IPA_V[inv][x] if t == "V" else ("w" if t == "W" else IPA_C.get(x, ""))
        if n == stress: out += "ˈ"
        if inv == "de" and t == "C" and sym and sym == prev: continue  # German voice: no doubled consonants
        out += sym
        prev = sym if t == "C" else None
    return out


def ssml(roman, inv):
    parts = []
    for w in roman.split():
        p = ipa(w, inv)
        if p: parts.append('<phoneme alphabet="ipa" ph="%s">%s</phoneme>' % (escape(p, {'"': "&quot;"}), escape(w)))
    return "<speak>" + " ".join(parts) + ".</speak>"


def fidel_text(t):
    t = t.replace("፡", " ").replace("፤", ",").replace("።", ".").replace("፨", ".")
    return re.sub(r"\s+([,.])", r"\1", re.sub(r"\s+", " ", t)).strip()


OPTIONS = [  # option key, label, candidate voices, how the text is sent
    ("A", "Amharic voice, Ge'ez letters as printed (traditional church sound)",
     ["am-ET-Wavenet-B", "am-ET-Wavenet-A", "am-ET-Standard-B", "am-ET-Standard-A"], "fidel"),
    ("B", "Arabic voice, text in Arabic letters (reconstructed sound)",
     ["ar-XA-Wavenet-B", "ar-XA-Wavenet-C", "ar-XA-Wavenet-A"], "arabic"),
    ("C", "German voice, exact sounds (as Akkadian, Greek and Latin)",
     ["de-DE-Neural2-D", "de-DE-Wavenet-B"], "de"),
    ("D", "American English voice, exact sounds (as Beowulf)", ["en-US-Neural2-D"], "en"),
]


def make_input(line, how):
    _, _, fidel, roman, _ = line
    if how == "fidel": return {"text": fidel_text(fidel)}
    if how == "arabic": return {"text": " ".join(arabic(w) for w in roman.split()) + "."}
    return {"ssml": ssml(roman, how)}


def main():
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from build_pinned import synth_input
    key = os.environ["GOOGLE_TTS_KEY"]
    base = "audio-pilot/geez"
    os.makedirs(base, exist_ok=True)
    json.dump({"lines": [{"key": k, "cite": c, "fidel": f, "roman": r, "en": e} for k, c, f, r, e in LINES]},
              open(base + "/lines.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    done = []
    for opt, label, cands, how in OPTIONS:
        for voice in cands:
            cfg = {"lang": "-".join(voice.split("-")[:2]), "voice": voice, "rate": 0.85}
            try:
                clips = [synth_input(make_input(ln, how), cfg, key) for ln in LINES]
            except Exception as e:  # noqa: BLE001
                print("SKIP", opt, voice, str(e)[:300]); continue
            os.makedirs(f"{base}/{opt}", exist_ok=True)
            for ln, a in zip(LINES, clips):
                open(f"{base}/{opt}/{ln[0]}.mp3", "wb").write(a)
            done.append({"option": opt, "label": label, "voice": voice}); print("done", opt, voice)
            time.sleep(0.5); break
    json.dump(done, open(base + "/voices.json", "w"), indent=1)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--show":
        for ln in LINES:
            for _, _, _, how in OPTIONS:
                print(how, make_input(ln, how))
            print()
    else:
        main()
