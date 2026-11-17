#!/usr/bin/env python3
"""Machine listening check: does each prepared clip say the text it was given?

Written 2026-11-17 after the Hebrew failure (a Chirp 3 HD voice invented sounds on Pirkei Avot and the
only check, Whisper "small", could not tell). Two independent listeners transcribe every clip:

  * Whisper large-v3 (faster-whisper, runs on the GitHub runner, free);
  * Google Cloud Speech-to-Text (same Google project as the voices; needs GOOGLE_TTS_KEY).

Each transcript is compared with the text the voice was asked to read, after a per-language
normalization that removes everything a correct reading may legitimately differ in:

  * Hebrew: points, punctuation, final letter forms and the vowel letters vav/yod are dropped
    (recognizers write unpointed, usually full spelling);
  * Arabic: vowel marks and tatweel dropped; alef/hamza, ta marbuta and alef maqsura unified;
  * Chinese: both sides turned into toneless pinyin syllables, so a homophone written with another
    character is not an error (the text is Classical, the recognizer writes modern Mandarin).

The score is the character (Chinese: syllable) error rate. A request (request.json) names sets of
clips; a set is either the clips stored at a git ref, or a fresh synthesis with a named voice.
With two sets of the same stories, one labelled bad and one good by a human ear, the report says
how well each listener separates them — the calibration. Nothing is committed; the report is printed
between LISTEN-REPORT-BEGIN / LISTEN-REPORT-END and saved as listen-report.json.

Usage: python3 listen_check.py .github/listen/request.json
"""
import base64, json, os, re, subprocess, sys, tempfile, time, unicodedata, urllib.request, urllib.error

TTS_URL = "https://texttospeech.googleapis.com/v1/text:synthesize"
STT_URL = "https://speech.googleapis.com/v1/speech:recognize"
STT_LANG = {"he": ["he-IL", "iw-IL"], "ar": ["ar-XA", "ar-EG", "ar-SA"], "zh": ["cmn-Hans-CN", "zh"]}


def lang_of(story):
    lc = (story.get("langCode") or "").lower()
    if lc.startswith("he"): return "he"
    if lc.startswith("ar"): return "ar"
    if lc.startswith(("zh", "cmn")): return "zh"
    return lc.split("-")[0]


def spoken_text(s):
    say = s.get("say")
    src = say if isinstance(say, str) and say.strip() else s["t"]
    return src.replace("\n", " ").strip()


_pinyin = None


def units(text, lang):
    """The sequence compared: letters (he, ar, other) or toneless syllables (zh)."""
    if lang == "he":
        text = re.sub("[֑-ׇ]", "", text)
        text = text.translate(str.maketrans("ךםןףץ", "כמנפצ"))
        return list(re.sub("[^א-ת]|[וי]", "", text))
    if lang == "ar":
        text = re.sub("[ً-ٰٟـ]", "", text)
        text = re.sub("[أإآٱ]", "ا", text).replace("ة", "ه").replace("ى", "ي").replace("ؤ", "و").replace("ئ", "ي")
        return list(re.sub("[^ء-ي]", "", text))
    if lang == "zh":
        global _pinyin
        if _pinyin is None:
            from pypinyin import lazy_pinyin
            _pinyin = lazy_pinyin
        han = re.findall("[㐀-䶿一-鿿]", text)
        return _pinyin("".join(han))
    text = unicodedata.normalize("NFKD", text.lower())
    return list(re.sub(r"[^a-z]", "", text))


def error_rate(ref, hyp):
    if not ref:
        return 0.0 if not hyp else 1.0
    prev = list(range(len(hyp) + 1))
    for i in range(1, len(ref) + 1):
        cur = [i] + [0] * len(hyp)
        for j in range(1, len(hyp) + 1):
            cur[j] = min(prev[j - 1] + (ref[i - 1] != hyp[j - 1]), prev[j] + 1, cur[j - 1] + 1)
        prev = cur
    return prev[-1] / float(len(ref))


def git_bytes(ref, path):
    r = subprocess.run(["git", "show", "%s:%s" % (ref, path)], capture_output=True)
    return r.stdout if r.returncode == 0 and r.stdout else None


def ensure_ref(ref):
    if ref in ("HEAD", "main"):
        return "HEAD"
    if subprocess.run(["git", "cat-file", "-e", ref + "^{commit}"], capture_output=True).returncode != 0:
        subprocess.run(["git", "fetch", "--depth", "1", "--filter=blob:none", "origin", ref], check=True)
    return ref


def synth(text, voice, key):
    body = json.dumps({"input": {"text": text}, "voice": {"languageCode": "-".join(voice.split("-")[:2]), "name": voice},
                       "audioConfig": {"audioEncoding": "MP3"}}).encode("utf-8")
    req = urllib.request.Request(TTS_URL + "?key=" + key, data=body, headers={"Content-Type": "application/json"})
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=90) as r:
                return base64.b64decode(json.load(r)["audioContent"])
        except urllib.error.HTTPError as e:
            if e.code not in (429, 500, 502, 503): raise
            time.sleep(5 * (attempt + 1))
    raise RuntimeError("TTS kept failing")


def to_flac_chunks(mp3_path, td, seconds=50):
    """16 kHz mono FLAC pieces of at most `seconds` (the synchronous recognizer takes under a minute)."""
    pat = os.path.join(td, "c%03d.flac")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", mp3_path, "-ac", "1", "-ar", "16000",
                    "-f", "segment", "-segment_time", str(seconds), pat], check=True)
    return sorted(os.path.join(td, f) for f in os.listdir(td) if f.startswith("c") and f.endswith(".flac"))


def google_stt(mp3_path, lang, key, state):
    if state.get("dead"):
        return None
    out = []
    with tempfile.TemporaryDirectory() as td:
        for piece in to_flac_chunks(mp3_path, td):
            audio = base64.b64encode(open(piece, "rb").read()).decode()
            codes = [state["code"]] if state.get("code") else STT_LANG.get(lang, [lang])
            got = None
            for code in codes:
                body = json.dumps({"config": {"languageCode": code, "encoding": "FLAC", "sampleRateHertz": 16000},
                                   "audio": {"content": audio}}).encode()
                req = urllib.request.Request(STT_URL + "?key=" + key, data=body, headers={"Content-Type": "application/json"})
                try:
                    with urllib.request.urlopen(req, timeout=120) as r:
                        d = json.load(r)
                    got = " ".join(a["alternatives"][0].get("transcript", "") for a in d.get("results", []) if a.get("alternatives"))
                    state["code"] = code
                    break
                except urllib.error.HTTPError as e:
                    msg = e.read().decode("utf-8", "replace")[:300]
                    print("  google stt %s: HTTP %s %s" % (code, e.code, msg.replace(key, "…")))
                    if e.code in (401, 403):
                        state["dead"] = "HTTP %s: %s" % (e.code, msg.replace(key, "…")[:200])
                        return None
            if got is None:
                state["dead"] = "no language code accepted"
                return None
            out.append(got)
    return " ".join(out)


def auc(bad, good):
    """Chance that a clip from the bad set scores worse (higher) than a clip from the good set."""
    if not bad or not good: return None
    wins = sum((b > g) + 0.5 * (b == g) for b in bad for g in good)
    return round(wins / (len(bad) * len(good)), 3)


def main():
    req = json.load(open(sys.argv[1], encoding="utf-8"))
    key = os.environ.get("GOOGLE_TTS_KEY", "")
    models = {}
    from faster_whisper import WhisperModel
    for name in req.get("whisper", ["large-v3"]):
        t0 = time.time()
        models[name] = WhisperModel(name, device="cpu", compute_type="int8")
        print("loaded whisper %s in %.0fs" % (name, time.time() - t0), flush=True)
    report = {"generated": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "jobs": []}
    for job in req["jobs"]:
        jr = {"name": job["name"], "sets": []}
        stt_state = {}
        for st in job["sets"]:
            sr = {"label": st["label"], "verdict": st.get("verdict"), "clips": []}
            ref = ensure_ref(st["ref"]) if st.get("ref") else None
            for sid in st["stories"]:
                story = json.load(open(sid + ".json", encoding="utf-8"))
                lang = lang_of(story)
                idxs = range(len(story["sentences"]))
                if st.get("max_units"):
                    idxs = list(idxs)[:st["max_units"]]
                for i in idxs:
                    text = spoken_text(story["sentences"][i])
                    if st.get("synth"):
                        data = synth(text, st["synth"], key); time.sleep(0.3)
                    else:
                        data = git_bytes(ref, "audio/%s/%d.mp3" % (sid, i))
                    if not data:
                        sr["clips"].append({"story": sid, "i": i, "missing": True}); continue
                    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
                        f.write(data); path = f.name
                    refu = units(text, lang)
                    row = {"story": sid, "i": i, "n": len(refu)}
                    for name, m in models.items():
                        segs, _ = m.transcribe(path, language=lang, beam_size=5, vad_filter=False,
                                               condition_on_previous_text=False)
                        heard = " ".join(s.text for s in segs).strip()
                        row["whisper-" + name] = {"err": round(error_rate(refu, units(heard, lang)), 3), "heard": heard}
                    if key and req.get("google_stt", True):
                        heard = google_stt(path, lang, key, stt_state)
                        if heard is not None:
                            row["google-stt"] = {"err": round(error_rate(refu, units(heard, lang)), 3), "heard": heard}
                    os.unlink(path)
                    sr["clips"].append(row)
                    print(job["name"], st["label"], sid, i, {k: v["err"] for k, v in row.items() if isinstance(v, dict)}, flush=True)
            jr["sets"].append(sr)
        if stt_state.get("dead"):
            jr["google_stt_unavailable"] = stt_state["dead"]
        # summary per listener and set; calibration if the sets carry human verdicts
        listeners = sorted({k for s in jr["sets"] for c in s["clips"] for k, v in c.items() if isinstance(v, dict)})
        summ = {}
        for L in listeners:
            per = {}
            for s in jr["sets"]:
                errs = sorted(c[L]["err"] for c in s["clips"] if L in c)
                if errs:
                    per[s["label"]] = {"clips": len(errs), "median": errs[len(errs) // 2], "min": errs[0], "max": errs[-1],
                                       "mean": round(sum(errs) / len(errs), 3)}
            bad = [c[L]["err"] for s in jr["sets"] if s.get("verdict") == "bad" for c in s["clips"] if L in c]
            good = [c[L]["err"] for s in jr["sets"] if s.get("verdict") == "good" for c in s["clips"] if L in c]
            if bad and good:
                per["separation"] = auc(bad, good)
                best = None
                for thr in sorted(set(bad + good)):
                    miss = sum(b <= thr for b in bad); false = sum(g > thr for g in good)
                    if best is None or miss + false < best[1] + best[2]:
                        best = (thr, miss, false)
                per["best_threshold"] = {"flag_above": best[0], "bad_clips_missed": best[1], "of_bad": len(bad),
                                         "good_clips_flagged": best[2], "of_good": len(good)}
            summ[L] = per
        jr["summary"] = summ
        report["jobs"].append(jr)
        print("SUMMARY", job["name"], json.dumps(summ, ensure_ascii=False), flush=True)
    json.dump(report, open("listen-report.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("LISTEN-REPORT-BEGIN")
    print(json.dumps(report, ensure_ascii=False))
    print("LISTEN-REPORT-END")


if __name__ == "__main__":
    main()
