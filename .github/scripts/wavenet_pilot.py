#!/usr/bin/env python3
"""Pilot only (2026-10-04): re-speak the already-built Greek pins with a Google WaveNet voice.

WaveNet has a 4M-character monthly free allowance (Neural2: 1M). Zev chose the Neural2 voice
(Voice A) by ear; this makes the same clips, from the very same SSML in audio/<id>/texts.json,
in a WaveNet voice, so he can compare. Writes audio-pilot/wavenet/<id>/<n>.mp3.

Usage: python3 wavenet_pilot.py <voice> <id> [<id> ...]     Env: GOOGLE_TTS_KEY
"""
import json, os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_pinned import synth_ssml

voice, ids = sys.argv[1], sys.argv[2:]
cfg = {"lang": "-".join(voice.split("-")[:2]), "voice": voice, "rate": 0.9}
key = os.environ["GOOGLE_TTS_KEY"]
for sid in ids:
    texts = json.load(open("audio/%s/texts.json" % sid, encoding="utf-8"))
    out = "audio-pilot/wavenet/" + sid
    os.makedirs(out, exist_ok=True)
    for n, ssml in sorted(texts.items(), key=lambda kv: int(kv[0])):
        open("%s/%s.mp3" % (out, n), "wb").write(synth_ssml(ssml, cfg, key))
        time.sleep(0.25)
    open(out + "/voice.txt", "w").write(voice + "\n")
    print(sid, len(texts), "clips")
