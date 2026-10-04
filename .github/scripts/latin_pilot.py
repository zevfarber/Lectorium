#!/usr/bin/env python3
"""Pilot only (2026-10-04): Latin voices for Zev to compare by ear.

Ovid, Metamorphoses I.1-4 and Virgil, Aeneid I.1-4, one clip per line, read in restored Classical
pronunciation with normal word stress (Zev's choice), long vowels held, elision as in verse. The long
vowels were marked by hand for these eight lines; production will take them from a scansion pass.
Each voice reads the same IPA pins (latin_g2p.py). A voice that refuses the request is skipped.

Writes audio-pilot/latin/<voice>/<id>-<n>.mp3 and audio-pilot/latin/pins.json.
Usage: python3 latin_pilot.py <voice> [<voice> ...]     Env: GOOGLE_TTS_KEY
"""
import json, os, re, sys, time
from xml.sax.saxutils import escape
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import latin_g2p as L
from build_pinned import synth_ssml

LINES = {
    "ovid": ["In nova fert animus mūtātās dīcere fōrmās",
             "corpora; dī, coeptīs (nam vōs mūtāstis et illās)",
             "adspīrāte meīs prīmaque ab orīgine mundī",
             "ad mea perpetuum dēdūcite tempora carmen."],
    "virgil": ["Arma virumque canō, Trōiae quī prīmus ab ōrīs",
               "Ītaliam fātō profugus Lāvīniaque vēnit",
               "lītora, multum ille et terrīs iactātus et altō",
               "vī superum, saevae memorem Iūnōnis ob īram;"],
}
PUNCT = {",": ",", ";": ",", ".": ".", ":": ",", "(": ",", ")": ",", "?": "?", "!": "!"}
WORD = re.compile(r"[A-Za-zĀĒĪŌŪȲāēīōūȳ]+")
ELIDE = re.compile(r"(?:aɪ|ɔʏ|aʊ|ɛʊ|[aɛɪɔʊʏ]ː?|[aeiouy]ː)m?$")


def line_ssml(t):
    toks = list(WORD.finditer(t)); parts = []; pos = 0; pend = ""
    for k, m in enumerate(toks):
        for ch in t[pos:m.start()]:
            if ch in PUNCT: parts.append(PUNCT[ch])
        pos = m.end()
        p = L.ipa(m.group(0))
        nxt = toks[k + 1].group(0).lower() if k + 1 < len(toks) else ""
        gap = t[m.end():toks[k + 1].start()] if k + 1 < len(toks) else ""
        # elision: a final vowel or vowel+m before a word beginning with a vowel or h, no pause between
        if nxt and not any(c in PUNCT for c in gap) and re.match(r"[aeiouyāēīōūȳh]", nxt) \
                and not re.match(r"i[aeiouāēīōū]", nxt) and ELIDE.search(p):
            pend += ELIDE.sub("", p).replace("ˈ", ""); continue
        word = pend + p; pend = ""
        rom = re.sub("[ˈː]", "", word)
        parts.append('<phoneme alphabet="ipa" ph="%s">%s</phoneme>' % (escape(word, {'"': "&quot;"}), escape(rom)))
    for ch in t[pos:]:
        if ch in PUNCT: parts.append(PUNCT[ch])
    body = ""
    for x in parts:
        body += x if x in PUNCT.values() else " " + x
    return "<speak>" + body.strip() + "</speak>"


def main():
    key = os.environ["GOOGLE_TTS_KEY"]
    os.makedirs("audio-pilot/latin", exist_ok=True)
    pins = {f"{w}-{n}": line_ssml(t) for w, ls in LINES.items() for n, t in enumerate(ls)}
    json.dump({"lines": LINES, "ssml": pins}, open("audio-pilot/latin/pins.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    done = []
    for voice in sys.argv[1:]:
        cfg = {"lang": "-".join(voice.split("-")[:2]), "voice": voice, "rate": 0.85}
        out = "audio-pilot/latin/" + voice
        try:
            synth_ssml(pins["ovid-0"], cfg, key)
        except Exception as e:  # noqa: BLE001
            print("SKIP", voice, str(e)[:200]); continue
        os.makedirs(out, exist_ok=True)
        for k, ssml in pins.items():
            open(f"{out}/{k}.mp3", "wb").write(synth_ssml(ssml, cfg, key)); time.sleep(0.25)
        done.append(voice); print("done", voice)
    json.dump(done, open("audio-pilot/latin/voices.json", "w"), indent=1)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--show":
        for w, ls in LINES.items():
            for t in ls: print(line_ssml(t))
    else:
        main()
