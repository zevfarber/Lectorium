#!/usr/bin/env python3
# Forced-ish alignment via Vosk for one or more stories. Recognizes each per-sentence
# mp3, then maps recognized word times onto the exact tokens the reader displays
# (same WORD_RE), interpolating any tokens Vosk missed.
# Output per story: audio/<id>/align.json
#   { "<sentenceIndex>": [[startSec, endSec], ... one per WORD_RE token ], ... }
import json, re, subprocess, os, sys, difflib, wave
from vosk import Model, KaldiRecognizer

# (story_id, vosk_model_dir)
JOBS = [
    ("hansel-und-grethel",  os.path.expanduser("~/vosk-model-de")),
    ("petit-chaperon-rouge", os.path.expanduser("~/vosk-model-fr")),
]

# must match reader.html WORD_RE (Latin incl. accents + Latin Extended-A)
WORD_RE = re.compile(r"[A-Za-zÀ-ÖØ-öø-ÿĀ-ɏ]+(?:[-\[\]()][A-Za-zÀ-ÖØ-öø-ÿĀ-ɏ]+)*")
def norm(w):
    return "".join(c for c in w.lower() if c.isalpha())

def vosk_words(mp3, model):
    wav = "/tmp/a.wav"
    subprocess.run(["ffmpeg", "-y", "-i", mp3, "-ar", "16000", "-ac", "1", wav],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    wf = wave.open(wav, "rb")
    rec = KaldiRecognizer(model, 16000)
    rec.SetWords(True)
    res = []
    while True:
        d = wf.readframes(4000)
        if not d:
            break
        if rec.AcceptWaveform(d):
            res += json.loads(rec.Result()).get("result", [])
    res += json.loads(rec.FinalResult()).get("result", [])
    return res

def audio_dur(mp3):
    o = subprocess.run(["ffprobe", "-v", "quiet", "-show_entries", "format=duration",
                        "-of", "csv=p=0", mp3], capture_output=True, text=True).stdout.strip()
    try:
        return float(o)
    except Exception:
        return 0.0

def fill(times, D):
    n = len(times)
    for k in range(n):
        if times[k] is None:
            p = None
            for j in range(k - 1, -1, -1):
                if times[j]:
                    p = times[j][1]; break
            q = None
            for j in range(k + 1, n):
                if times[j]:
                    q = times[j][0]; break
            if p is None: p = 0.0
            if q is None: q = D
            if q < p: q = p
            times[k] = [round(p, 3), round(q, 3)]
    return times

def align_story(sid, model):
    story = json.load(open(sid + ".json", encoding="utf-8"))
    out = {}
    total_tok = total_match = 0
    for i, s in enumerate(story["sentences"]):
        mp3 = "audio/%s/%d.mp3" % (sid, i)
        toks = WORD_RE.findall(s.get("t", ""))
        D = audio_dur(mp3)
        vw = vosk_words(mp3, model)
        a = [norm(t) for t in toks]
        b = [norm(w["word"]) for w in vw]
        times = [None] * len(toks)
        for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
            if op == "equal":
                for k in range(i2 - i1):
                    w = vw[j1 + k]
                    times[i1 + k] = [round(w["start"], 3), round(w["end"], 3)]
        total_tok += len(toks); total_match += sum(1 for t in times if t)
        times = fill(times, D)
        out[str(i)] = times
        if i % 20 == 0:
            print("%s %d/%d" % (sid, i, len(story["sentences"]))); sys.stdout.flush()
    with open("audio/%s/align.json" % sid, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False)
    print("%s DONE  %d/%d words matched (%.0f%%)" %
          (sid, total_match, total_tok, 100.0 * total_match / max(1, total_tok)))

def main():
    for sid, model_dir in JOBS:
        model = Model(model_dir)
        align_story(sid, model)
    print("ALL DONE")

if __name__ == "__main__":
    main()
