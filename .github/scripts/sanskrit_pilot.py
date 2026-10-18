#!/usr/bin/env python3
"""Pilot only (2026-10-18): voices for Sanskrit (the Bhagavad Gita), for Zev to compare by ear.

Google has no Sanskrit voice, so every option borrows one. Three verses (1.1, 2.22, 2.47), one clip
per half-verse, read five ways:

  A  Hindi voice reading the Devanagari as printed. Native script, Indian sound; Hindi habits creep in
     (a final short a dropped: "dharm" for dharma).
  B  Marathi voice reading the Devanagari as printed. Same idea; Marathi keeps more of the Sanskrit
     sounds than Hindi.
  C  Kannada voice reading the same text in Kannada letters (a letter-for-letter change of script).
     South Indian reciters keep every final vowel, so this is the traditional pandit sound.
  D  Hindi voice told the exact sounds (IPA), word by word: every vowel kept, retroflexes and
     aspirates as written.
  E  German voice told the exact sounds (IPA), as for Greek, Latin, Old Norse and Akkadian.

A voice Google refuses is skipped, and the next one listed for that option is tried.
Writes audio-pilot/sanskrit/<option>/<k>.mp3, audio-pilot/sanskrit/lines.json, voices.json.
Usage: python3 sanskrit_pilot.py            Env: GOOGLE_TTS_KEY
"""
import json, os, re, sys, time
from xml.sax.saxutils import escape
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_pinned import synth_input, synth_ssml

LINES = [  # (citation, Devanagari half-verse)
    ("1.1a", "धर्मक्षेत्रे कुरुक्षेत्रे समवेता युयुत्सवः ।"),
    ("1.1b", "मामकाः पाण्डवाश्चैव किमकुर्वत संजय ॥"),
    ("2.22a", "वासांसि जीर्णानि यथा विहाय नवानि गृह्णाति नरोऽपराणि ।"),
    ("2.22b", "तथा शरीराणि विहाय जीर्णान्यन्यानि संयाति नवानि देही ॥"),
    ("2.47a", "कर्मण्येवाधिकारस्ते मा फलेषु कदाचन ।"),
    ("2.47b", "मा कर्मफलहेतुर्भूर्मा ते सङ्गोऽस्त्वकर्मणि ॥"),
]

# ---- Devanagari -> IAST ------------------------------------------------------------------------
V = {"अ": "a", "आ": "ā", "इ": "i", "ई": "ī", "उ": "u", "ऊ": "ū", "ऋ": "ṛ", "ॠ": "ṝ", "ऌ": "ḷ",
     "ए": "e", "ऐ": "ai", "ओ": "o", "औ": "au"}
M = {"ा": "ā", "ि": "i", "ी": "ī", "ु": "u", "ू": "ū", "ृ": "ṛ", "ॄ": "ṝ", "ॢ": "ḷ",
     "े": "e", "ै": "ai", "ो": "o", "ौ": "au"}
C = {"क": "k", "ख": "kh", "ग": "g", "घ": "gh", "ङ": "ṅ", "च": "c", "छ": "ch", "ज": "j", "झ": "jh",
     "ञ": "ñ", "ट": "ṭ", "ठ": "ṭh", "ड": "ḍ", "ढ": "ḍh", "ण": "ṇ", "त": "t", "थ": "th", "द": "d",
     "ध": "dh", "न": "n", "प": "p", "फ": "ph", "ब": "b", "भ": "bh", "म": "m", "य": "y", "र": "r",
     "ल": "l", "व": "v", "श": "ś", "ष": "ṣ", "स": "s", "ह": "h"}


def iast(word):
    out, i = "", 0
    while i < len(word):
        ch = word[i]
        if ch in C:
            out += C[ch]; nxt = word[i + 1] if i + 1 < len(word) else ""
            if nxt == "्": i += 2; continue
            if nxt in M: out += M[nxt]; i += 2; continue
            out += "a"
        elif ch in V: out += V[ch]
        elif ch == "ं": out += "ṃ"
        elif ch == "ः": out += "ḥ"
        elif ch == "ऽ": out += ""          # avagraha: the elided a is silent
        i += 1
    return out


# ---- IAST -> IPA ---------------------------------------------------------------------------------
FULL = [("kh", "kʰ"), ("gh", "ɡʱ"), ("ch", "t͡ɕʰ"), ("jh", "d͡ʑʱ"), ("ṭh", "ʈʰ"), ("ḍh", "ɖʱ"),
        ("th", "t̪ʰ"), ("dh", "d̪ʱ"), ("ph", "pʰ"), ("bh", "bʱ"), ("ai", "ai̯"), ("au", "au̯"),
        ("ā", "aː"), ("ī", "iː"), ("ū", "uː"), ("ṝ", "r̩ː"), ("ṛ", "r̩"), ("ḷ", "l̩"), ("e", "eː"),
        ("o", "oː"), ("a", "ɐ"), ("i", "i"), ("u", "u"), ("k", "k"), ("g", "ɡ"), ("ṅ", "ŋ"),
        ("c", "t͡ɕ"), ("j", "d͡ʑ"), ("ñ", "ɲ"), ("ṭ", "ʈ"), ("ḍ", "ɖ"), ("ṇ", "ɳ"), ("t", "t̪"),
        ("d", "d̪"), ("n", "n"), ("p", "p"), ("b", "b"), ("m", "m"), ("y", "j"), ("r", "ɾ"),
        ("l", "l"), ("v", "ʋ"), ("ś", "ɕ"), ("ṣ", "ʂ"), ("s", "s"), ("h", "ɦ"), ("ṃ", "m"), ("ḥ", "h")]
# The German voice has no retroflex, palatal-sibilant or breathy sounds: nearest German sounds.
CARRIER = dict(FULL)
CARRIER.update({"kh": "kh", "gh": "ɡh", "ch": "tʃh", "jh": "dʒh", "ṭh": "th", "ḍh": "dh", "th": "th",
                "dh": "dh", "ph": "ph", "bh": "bh", "ai": "aɪ", "au": "aʊ", "ṝ": "riː", "ṛ": "ri",
                "ḷ": "li", "a": "a", "c": "tʃ", "j": "dʒ", "ñ": "n", "ṭ": "t", "ḍ": "d", "ṇ": "n",
                "t": "t", "d": "d", "r": "r", "v": "v", "ś": "ʃ", "ṣ": "ʃ", "h": "h"})
VOWELS = ("ai", "au", "ā", "ī", "ū", "ṝ", "ṛ", "ḷ", "e", "o", "a", "i", "u")
LONG = ("ai", "au", "ā", "ī", "ū", "ṝ", "e", "o")


def _tokens(w):
    toks, i = [], 0
    keys = sorted(CARRIER, key=len, reverse=True)
    while i < len(w):
        for k in keys:
            if w.startswith(k, i): toks.append(k); i += len(k); break
        else: i += 1
    return toks


def ipa(word, table):
    """IPA for one IAST word; stress by the classical rule (penult if heavy, else antepenult)."""
    toks = _tokens(word)
    vi = [n for n, t in enumerate(toks) if t in VOWELS]
    heavy = []
    for k, n in enumerate(vi):
        end = vi[k + 1] if k + 1 < len(vi) else len(toks)
        cons = [t for t in toks[n + 1:end] if t not in VOWELS]
        heavy.append(toks[n] in LONG or len(cons) >= 2 or (k == len(vi) - 1 and cons))
    if len(vi) <= 1: s = 0
    elif heavy[-2]: s = len(vi) - 2
    elif len(vi) >= 3: s = len(vi) - 3
    else: s = len(vi) - 2
    # syllable onset of the stressed vowel: the consonant right before it (if any)
    start = vi[s] if s < len(vi) else 0
    if start > 0 and toks[start - 1] not in VOWELS: start -= 1
    out = "".join(("ˈ" if n == start and len(vi) > 1 else "") + table[t] for n, t in enumerate(toks))
    return out


def ssml(line, table, inner_deva=False):
    words = re.findall(r"[ऀ-ॿ]+|[।॥]", line)
    parts = []
    for w in words:
        if w in "।॥": parts.append("." if w == "॥" else ","); continue
        p = ipa(iast(w), table)
        parts.append('<phoneme alphabet="ipa" ph="%s">%s</phoneme>' % (escape(p, {'"': "&quot;"}), escape(w if inner_deva else iast(w))))
    body = ""
    for x in parts: body += x if x in ",." else " " + x
    return "<speak>" + body.strip() + "</speak>"


def kannada(text):
    out = ""
    for ch in text:
        o = ord(ch)
        out += chr(o + 0x380) if 0x0901 <= o <= 0x094D or 0x0966 <= o <= 0x096F else ch
    return out


OPTIONS = [  # option key, label, candidate voices, how the text is sent
    ("A", "Hindi voice, Devanagari as printed", ["hi-IN-Wavenet-C", "hi-IN-Neural2-B", "hi-IN-Wavenet-B"], "deva"),
    ("B", "Marathi voice, Devanagari as printed", ["mr-IN-Wavenet-B", "mr-IN-Wavenet-C", "mr-IN-Wavenet-A"], "deva"),
    ("C", "Kannada voice, Kannada letters", ["kn-IN-Wavenet-B", "kn-IN-Wavenet-D", "kn-IN-Wavenet-A"], "knda"),
    ("D", "Hindi voice, exact sounds", ["hi-IN-Wavenet-C", "hi-IN-Neural2-B", "hi-IN-Wavenet-B"], "ipa-full"),
    ("E", "German voice, exact sounds (as Greek and Latin)", ["de-DE-Wavenet-B"], "ipa-carrier"),
]


def make_input(line, how):
    if how == "deva": return {"text": line}
    if how == "knda": return {"text": kannada(line)}
    if how == "ipa-full": return {"ssml": ssml(line, dict(FULL), inner_deva=True)}
    return {"ssml": ssml(line, CARRIER)}


def main():
    key = os.environ["GOOGLE_TTS_KEY"]
    base = "audio-pilot/sanskrit"
    os.makedirs(base, exist_ok=True)
    json.dump({"lines": [{"cite": c, "deva": t, "iast": " ".join(iast(w) for w in re.findall(r"[ऀ-ॿ]+", t))}
                         for c, t in LINES]},
              open(base + "/lines.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    done = []
    for opt, label, cands, how in OPTIONS:
        for voice in cands:
            cfg = {"lang": "-".join(voice.split("-")[:2]), "voice": voice, "rate": 0.8}
            try:
                clips = [synth_input(make_input(t, how), cfg, key) for _, t in LINES]
            except Exception as e:  # noqa: BLE001
                print("SKIP", opt, voice, str(e)[:300]); continue
            os.makedirs(f"{base}/{opt}", exist_ok=True)
            for (c, _), a in zip(LINES, clips):
                open(f"{base}/{opt}/{c}.mp3", "wb").write(a)
            done.append({"option": opt, "label": label, "voice": voice}); print("done", opt, voice)
            time.sleep(0.5); break
    json.dump(done, open(base + "/voices.json", "w"), indent=1)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--show":
        for c, t in LINES:
            print(c, kannada(t)); print("  ", ssml(t, dict(FULL))); print("  ", ssml(t, CARRIER))
    else:
        main()
