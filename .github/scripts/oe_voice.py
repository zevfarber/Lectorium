#!/usr/bin/env python3
"""Old English (Beowulf, Klaeber 1922) for build_pinned.py: the American English carrier under IPA pins.

Voice chosen by Zev 2026-10-12 from the sample round (audio-pilot/beowulf.html, Voice B):
en-US-Neural2-D, speaking rate 0.85, a 350 ms pause at each verse-line end. The sample measured it
bit-identical on the same input twice (relative RMS 0.000), so one listen approves every fitt.

The pronunciation rules live in ONE place, .github/pipeline/beowulf/oe_g2p.py (reconstructed late West
Saxon, c. 1000, after Campbell); this module only adds the builder interface and the voice's inventory.
A later fix to oe_g2p.py changes the pins, texts.json notices, and only the clips it affects are redone.

ACCEPTED is the intersection of the two probes in audio-pilot/beowulf/report.json for en-US-Neural2-D
(customPronunciations refused: bare o, yː, æː, æːɑ, ɣ and the o-diphthong spellings). What that costs
the reading: ǣ, ȳ and the long diphthong ēa are heard short; [ɣ] is heard as g.
"""
import os, re, sys
from xml.sax.saxutils import escape

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "pipeline", "beowulf"))
import oe_g2p as G  # noqa: E402

ACCEPTED = set("""a aː b d dʒ d͡ʒ e eɔ eː eːɔ f g h hw i ie iɔ iɛ iː iːe iːɔ iːɛ j k l m n oː p r s t ts tʃ t͡ʃ
u uː v w x y z æ æa æɑ ç ð ŋ ɑ ɑː ɔ ɛ ɛa ɛɑ ɛɔ ɪ ɪe ɪɔ ɪɛ ɹ ʃ ʊ ʏ ʒ ː θ""".split())
GEM_OK = True
LINE_BREAK = '<break time="350ms"/>'
_WORD = None


def ipa(word):
    return G.reduce(G.ipa_tokens(word), ACCEPTED, GEM_OK)


def _ph(ip, word):
    return '<phoneme alphabet="ipa" ph="%s">%s</phoneme>' % (escape(ip, {'"': "&quot;"}), escape(G.plain(word)))


def _pause(gap):
    """Klaeber's punctuation between two words -> one pause mark (a row of dots for lost words is one)."""
    for ch, mark in (("?", "?"), ("!", "!"), (".", "."), (";", ","), (":", ","), (",", ","), ("—", ",")):
        if ch in gap:
            return mark
    return ""


def sentence_ssml(s):
    """One unit (several verse lines joined by \\n): a pinned <phoneme> per word, punctuation as pauses,
    and a short break at each line end — verse read as verse, as in the approved sample."""
    global _WORD
    if _WORD is None:
        import align_wordref as AW
        _WORD = AW.WORD_RE
    lines = []
    for line in s["t"].split("\n"):
        body, pos = "", 0
        for m in _WORD.finditer(line):
            body += _pause(line[pos:m.start()])
            ip = ipa(m.group(0))
            if ip:
                body += " " + _ph(ip, m.group(0))
            pos = m.end()
        body += _pause(line[pos:])
        if body.strip():
            lines.append(body.strip())
    return "<speak>" + (" " + LINE_BREAK + " ").join(lines) + "</speak>"


DETERMINISM_FILE = "audio/_oe-determinism.json"


def determinism_check(cfg, synth):
    """Once ever (2026-10-12): the same pinned SSML twice through the build's own request path; the two
    MP3s should be byte-identical, as the sample measured on LINEAR16. Recorded in DETERMINISM_FILE
    (committed with the clips); a mismatch is reported in the log and the build carries on."""
    import json, hashlib, time
    if os.path.exists(DETERMINISM_FILE):
        return
    ssml = "<speak>" + _ph(ipa("Hwæt"), "Hwæt") + " " + _ph(ipa("gēardagum"), "gēardagum") + "</speak>"
    a = synth({"ssml": ssml}); b = synth({"ssml": ssml})
    res = {"date": time.strftime("%Y-%m-%d", time.gmtime()), "voice": cfg["voice"], "rate": cfg["rate"],
           "ssml": ssml, "bytes": [len(a), len(b)],
           "sha256": [hashlib.sha256(a).hexdigest(), hashlib.sha256(b).hexdigest()],
           "identical": a == b}
    json.dump(res, open(DETERMINISM_FILE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("Old English determinism check:", "byte-identical" if a == b else "DIFFERENT", res["bytes"])


if __name__ == "__main__":
    for w in sys.argv[1:]:
        print(w, ipa(w))
