#!/usr/bin/env python3
"""Pilot only (2026-09-29): read Greek texts with a FREE Piper voice from the same IPA pins that
build_pinned.py sends to Google, so Zev can compare the two by ear on audio-pilot/greek.html.

Usage: python3 piper_pilot.py <voice.onnx> <story-id> [<story-id> ...]
Writes audio-pilot/piper/<id>/<n>.mp3. Touches nothing the reader uses.
"""
import json, os, subprocess, sys, wave
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import greek_g2p as G
import align_wordref as AW
from piper import PiperVoice
from piper.config import SynthesisConfig

PUNCT = {".": ".", ",": ",", ";": "?", ";": "?", "·": ",", "·": ",", "!": "!", ":": ","}
ELISION = "’᾽'ʼ᾿"


def phonemes(t):
    out, pos, pend = [], 0, ""
    toks = list(AW.WORD_RE.finditer(t))
    for k, m in enumerate(toks):
        for ch in t[pos:m.start()]:
            if ch in PUNCT:
                out.append(PUNCT[ch])
        pos = m.end()
        p = G.ipa(m.group(0))
        if t[m.end():m.end() + 1] in ELISION and t[m.end():m.end() + 1] and k + 1 < len(toks):
            pend += p.replace("ˈ", ""); continue
        out.append(" " + pend + p); pend = ""
    for ch in t[pos:]:
        if ch in PUNCT:
            out.append(PUNCT[ch])
    return "".join(out).strip()


def main():
    voice = PiperVoice.load(sys.argv[1])
    known = set(voice.config.phoneme_id_map)
    cfg = SynthesisConfig(length_scale=1.1)
    missing = set()
    for sid in sys.argv[2:]:
        story = json.load(open(sid + ".json", encoding="utf-8"))
        odir = "audio-pilot/piper/" + sid
        os.makedirs(odir, exist_ok=True)
        for i, s in enumerate(story["sentences"]):
            ph = phonemes(s["t"])
            seq = [c for c in ph if c in known]
            missing |= {c for c in ph if c not in known}
            audio = voice.phoneme_ids_to_audio(voice.phonemes_to_ids(seq), cfg)
            if isinstance(audio, tuple):
                audio = audio[0]
            pcm = (np.clip(np.asarray(audio, dtype=np.float32), -1, 1) * 32767).astype("<i2")
            wav = "%s/%d.wav" % (odir, i)
            with wave.open(wav, "wb") as w:
                w.setnchannels(1); w.setsampwidth(2); w.setframerate(voice.config.sample_rate)
                w.writeframes(pcm.tobytes())
            subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", wav, "-b:a", "64k",
                            "%s/%d.mp3" % (odir, i)], check=True)
            os.remove(wav)
        print("piper: %d clips for %s" % (len(story["sentences"]), sid))
    print("phonemes the voice does not know (dropped):", "".join(sorted(missing)) or "none")


if __name__ == "__main__":
    main()
