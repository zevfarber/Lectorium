#!/usr/bin/env python3
"""Pilot only (2026-11-22): voices for Prakrit (the Kalpasūtra), for Zev to compare by ear on audio-pilot/prakrit.html.

Google has no Prakrit voice. Zev's first guess is the Sanskrit solution, so that is option C, exactly as the Gita
is voiced (build_audio.py: Kannada voice kn-IN-Wavenet-B reading the text in Kannada letters, rate 0.8). Two
options he heard for Sanskrit are kept for comparison, since Prakrit's sounds are simpler than Sanskrit's and
the reasons he rejected them may not apply:
  A  Hindi voice reading the Devanagari as printed.
  B  Marathi voice reading the Devanagari as printed.
  C  Kannada voice reading the same text in Kannada letters (the Sanskrit voice).
Four passages from kalpasutra-001: the Namokkāra, its closing verse, the opening of §1, the verse of the dreams.
Writes audio-pilot/prakrit/<option>/<k>.mp3, lines.json, voices.json.   Env: GOOGLE_TTS_KEY
"""
import json, os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_pinned import synth_input
from sanskrit_pilot import kannada

S = json.load(open("kalpasutra-001.json", encoding="utf-8"))["sentences"]
PICK = [("namokkara", 0), ("verse", 1), ("s1", 2), ("dreams", len(S) - 1)]
LINES = [(k, S[i]["t"].replace("\n", " "), S[i]["tr"].replace("\n", " "), S[i].get("i", "")) for k, i in PICK]
OPTIONS = [
    ("A", "Hindi voice, Devanagari as printed", ["hi-IN-Wavenet-C", "hi-IN-Neural2-B", "hi-IN-Wavenet-B"], "deva"),
    ("B", "Marathi voice, Devanagari as printed", ["mr-IN-Wavenet-B", "mr-IN-Wavenet-C", "mr-IN-Wavenet-A"], "deva"),
    ("C", "Kannada voice, Kannada letters (the Sanskrit voice)", ["kn-IN-Wavenet-B"], "knda"),
]

def main():
    key = os.environ["GOOGLE_TTS_KEY"]; base = "audio-pilot/prakrit"; os.makedirs(base, exist_ok=True)
    json.dump({"lines": [{"cite": c, "deva": t, "iast": r, "en": e} for c, t, r, e in LINES]},
              open(base + "/lines.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    done = []
    for opt, label, cands, how in OPTIONS:
        for voice in cands:
            cfg = {"lang": "-".join(voice.split("-")[:2]), "voice": voice, "rate": 0.8}
            try:
                clips = [synth_input({"text": kannada(t) if how == "knda" else t}, cfg, key) for _, t, _, _ in LINES]
            except Exception as e:  # noqa: BLE001
                print("SKIP", opt, voice, str(e)[:300]); continue
            os.makedirs(f"{base}/{opt}", exist_ok=True)
            for (c, _, _, _), a in zip(LINES, clips): open(f"{base}/{opt}/{c}.mp3", "wb").write(a)
            done.append({"option": opt, "label": label, "voice": voice}); print("done", opt, voice); time.sleep(0.5); break
    json.dump(done, open(base + "/voices.json", "w"), indent=1)

if __name__ == "__main__":
    if sys.argv[1:] == ["--show"]:
        for c, t, r, e in LINES: print(c, t, "\n  ", kannada(t))
    else: main()
