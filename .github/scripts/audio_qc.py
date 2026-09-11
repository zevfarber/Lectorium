#!/usr/bin/env python3
"""Automatic listening check for prepared sentence clips (audio/<id>/qc.json).

Written 2026-09-10 for Perrault's 1697 text. It stands in for a human ear on the
GitHub runner, which has open internet and can download a French speech-recognition
model. Each clip is transcribed with faster-whisper and compared with the text the
voice was asked to read (`say` when present, otherwise `t`).

  * word error rate against the spoken text, with substitutions and deletions of
    declared proper nouns forgiven (Riquet, Darmancour ... are not dictionary words);
  * seconds per character, which catches a clip cut short or padded with silence;
  * a clip over the threshold is re-synthesized, up to three times. Chirp renders a
    different take every time, so a re-roll usually fixes a truncated or garbled clip.
    A re-roll replaces the clip only when it scores better. The recorded text in
    texts.json does not change, because the spoken text did not.

Clips still failing are listed in qc.json, which the next production firing reads.
The usual cause is a wrong speech-map entry: the firing fixes the map, rebuilds `say`
and re-lands the story.

This script never fails the job. Only stories with a string `say` or `wordClips: true`
are checked; every other story is skipped before anything is imported.

Usage:
  python3 audio_qc.py --needs <id>   exit 0 if the story is checked (the workflow installs
                                     faster-whisper only then), 1 otherwise
  python3 audio_qc.py <id>           run the check, write audio/<id>/qc.json
"""
import glob, json, os, re, sys, time, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
MODEL = "small"
THRESHOLD = 0.34          # word error rate above which a clip fails
CPC_RANGE = (0.03, 0.14)  # seconds per non-space character; checked only on >= 20 characters
MAX_REROLLS = 3


def eligible(story):
    return bool(story.get("wordClips") is True
                or any(isinstance(s.get("say"), str) for s in story.get("sentences", [])))


def spoken_text(s):
    say = s.get("say")
    src = say if isinstance(say, str) and say.strip() else s["t"]
    return src.replace("\n", " ").strip()


def words(text):
    text = unicodedata.normalize("NFC", text.lower())
    text = re.sub(r"[\u2019'`\-\u2013\u2014]", " ", text)
    return re.findall(r"[a-z\u00e0-\u00f6\u00f8-\u00ff\u0153\u00e6]+", text)


def proper_nouns():
    out = set()
    for f in glob.glob(os.path.join(HERE, "..", "tools", "*-speech-map.json")):
        d = json.load(open(f, encoding="utf-8"))
        out.update(w.lower() for w in (d.get("properNouns") or []))
    return out


def wer(ref, hyp, forgive):
    """Levenshtein over words; substituting or dropping a forgiven reference word costs 0."""
    if not ref:
        return 0.0 if not hyp else 1.0
    n, m = len(ref), len(hyp)
    prev = list(range(m + 1))
    for i in range(1, n + 1):
        cur = [prev[0] + (0 if ref[i - 1] in forgive else 1)] + [0] * m
        for j in range(1, m + 1):
            sub = 0 if (ref[i - 1] == hyp[j - 1] or ref[i - 1] in forgive) else 1
            dele = 0 if ref[i - 1] in forgive else 1
            cur[j] = min(prev[j - 1] + sub, prev[j] + dele, cur[j - 1] + 1)
        prev = cur
    return prev[m] / float(n)


def main():
    if len(sys.argv) >= 3 and sys.argv[1] == "--needs":
        try:
            story = json.load(open(sys.argv[2] + ".json", encoding="utf-8"))
        except Exception:
            sys.exit(1)
        sys.exit(0 if eligible(story) else 1)

    sid = sys.argv[1]
    story = json.load(open(sid + ".json", encoding="utf-8"))
    adir = "audio/" + sid
    if not eligible(story):
        print("qc: %s has no spoken layer or word clips; skipped" % sid)
        return
    result = {"story": sid, "model": "faster-whisper " + MODEL + " int8 (cpu)",
              "threshold": THRESHOLD, "cpcRange": list(CPC_RANGE),
              "units": len(story["sentences"]),
              "generated": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    try:
        from faster_whisper import WhisperModel
        import librosa
    except Exception as e:  # noqa: BLE001
        result.update(status="unavailable", error=str(e))
        json.dump(result, open(adir + "/qc.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print("qc: speech recognition unavailable (%s); qc.json records that" % e)
        return

    sys.path.insert(0, HERE)
    import build_audio as BA
    cfg = dict(BA.VOICES.get(story.get("langCode"), {}))
    vf = adir + "/voice.txt"
    if os.path.exists(vf):
        cfg["name"] = open(vf, encoding="utf-8").read().strip() or cfg.get("name")
    key = os.environ.get("GOOGLE_TTS_KEY", "")
    lang = (story.get("langCode") or "fr-FR").split("-")[0]
    model = WhisperModel(MODEL, device="cpu", compute_type="int8")
    forgive = proper_nouns()

    def score(path, text):
        segs, _ = model.transcribe(path, language=lang, beam_size=1, vad_filter=False)
        heard = " ".join(s.text for s in segs).strip()
        dur = librosa.get_duration(path=path)
        chars = len(re.sub(r"\s", "", text))
        cpc = dur / chars if chars else 0.0
        e = wer(words(text), words(heard), forgive)
        bad_cpc = chars >= 20 and not (CPC_RANGE[0] <= cpc <= CPC_RANGE[1])
        return {"wer": round(e, 3), "cpc": round(cpc, 4), "heard": heard,
                "fail": e > THRESHOLD or bad_cpc}

    failed, rerolled = [], []
    for i, s in enumerate(story["sentences"]):
        path = "%s/%d.mp3" % (adir, i)
        if not os.path.exists(path):
            failed.append({"i": i, "reason": "clip missing"})
            continue
        text = spoken_text(s)
        best = score(path, text)
        tries = 0
        while best["fail"] and tries < MAX_REROLLS and key and cfg.get("name"):
            tries += 1
            tmp = path + ".reroll.mp3"
            try:
                open(tmp, "wb").write(BA.synth_with_retry(text, cfg, key))
                cand = score(tmp, text)
            except Exception as e:  # noqa: BLE001
                print("  reroll %d failed for sentence %d: %s" % (tries, i, e))
                break
            finally:
                time.sleep(BA.THROTTLE_S)
            if cand["wer"] < best["wer"] or (best["fail"] and not cand["fail"]):
                os.replace(tmp, path)
                best = cand
                rerolled.append(i)
            elif os.path.exists(tmp):
                os.remove(tmp)
        if best["fail"]:
            failed.append(dict(best, i=i, rerolls=tries, said=text))
    result.update(status="clean" if not failed else "residue",
                  rerolled=sorted(set(rerolled)), failed=failed,
                  residuePct=round(100.0 * len(failed) / max(1, len(story["sentences"])), 2))
    json.dump(result, open(adir + "/qc.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("qc: %s %s; %d re-rolled, %d still failing of %d"
          % (sid, result["status"], len(result["rerolled"]), len(failed), len(story["sentences"])))


if __name__ == "__main__":
    main()
