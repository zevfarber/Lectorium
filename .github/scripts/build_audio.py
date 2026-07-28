#!/usr/bin/env python3
"""Synthesize per-sentence audio clips for a story and build karaoke timings.

Runs on a GitHub-hosted runner (open internet, unlike the Cowork sandbox):
  * synthesizes any MISSING audio/<id>/<i>.mp3 via Google Cloud TTS (pinned
    Chirp voice), so re-runs are idempotent;
  * then runs the proven model-free aligner (align_dtw.py) to write
    audio/<id>/align.json.

Voice + espeak mapping is keyed by the story's langCode and must match the
Spoken-audio policy (German de-DE-Chirp-HD-F, French fr-FR-Chirp-HD-F).

Rate limiting: Chirp-HD voices have a modest requests-per-minute quota, so long
tales (e.g. 56 sentences) burst past it and get HTTP 429. We throttle between
clips and back off (honouring Retry-After) on 429/5xx.

Usage: python3 build_audio.py <story-id>
Env:   GOOGLE_TTS_KEY  (Google Cloud TTS API key, from Actions secret)
"""
import base64, json, os, subprocess, sys, time, urllib.request, urllib.error

VOICES = {
    "de-DE": {"name": "de-DE-Chirp-HD-F", "lang": "de-DE", "espeak": "de"},
    "fr-FR": {"name": "fr-FR-Chirp-HD-F", "lang": "fr-FR", "espeak": "fr"},
    # Classical Chinese is READ in modern Mandarin (the stated convention), so a real
    # voice exists. Resolved once on 2026-07-27 and now PINNED, like German and French.
    "zh-CN": {"name": "cmn-CN-Chirp3-HD-Achernar", "lang": "cmn-CN", "espeak": "cmn"},
}

VOICES_URL = "https://texttospeech.googleapis.com/v1/voices"


def resolve_voice(cfg, key):
    """Return the pinned voice name, or deterministically choose the best available one.

    Only runs for a language with no pinned name yet. Preference is by quality tier then
    alphabetical, so the same catalogue always yields the same answer. The chosen name is
    written to audio/<id>/voice.txt so it can be read back and pinned here.
    """
    if cfg.get("name"):
        return cfg["name"]
    url = "%s?languageCode=%s&key=%s" % (VOICES_URL, cfg["lang"], key)
    with urllib.request.urlopen(url, timeout=60) as r:
        voices = json.load(r).get("voices", [])
    if not voices:
        raise SystemExit("No TTS voices offered for %s" % cfg["lang"])

    def tier(n):
        for i, mark in enumerate(("Chirp3-HD", "Chirp-HD", "Neural2", "Wavenet", "Standard")):
            if mark in n:
                return i
        return 9

    pool = [v["name"] for v in voices if v.get("ssmlGender") == "FEMALE"] or [v["name"] for v in voices]
    chosen = sorted(pool, key=lambda n: (tier(n), n))[0]
    print("resolved voice for %s: %s (%d offered)" % (cfg["lang"], chosen, len(voices)))
    return chosen

TTS_URL = "https://texttospeech.googleapis.com/v1/text:synthesize"

THROTTLE_S = 0.7   # pause between successful clips to stay under the per-minute quota
MAX_ATTEMPTS = 6


def synth(text, cfg, key):
    body = json.dumps({
        "input": {"text": text},
        "voice": {"languageCode": cfg["lang"], "name": cfg["name"]},
        "audioConfig": {"audioEncoding": "MP3"},
    }).encode("utf-8")
    req = urllib.request.Request(
        TTS_URL + "?key=" + key, data=body,
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=90) as r:
        return base64.b64decode(json.load(r)["audioContent"])


def synth_with_retry(text, cfg, key):
    last_err = None
    for attempt in range(MAX_ATTEMPTS):
        try:
            return synth(text, cfg, key)
        except urllib.error.HTTPError as e:
            last_err = e
            if e.code == 429:
                ra = e.headers.get("Retry-After")
                wait = float(ra) if (ra and str(ra).isdigit()) else min(5 * (2 ** attempt), 60)
            elif 500 <= e.code < 600:
                wait = min(3 * (2 ** attempt), 30)
            else:
                raise  # other 4xx = a real request problem, not transient
            print("  TTS %d, retry %d/%d after %.0fs" % (e.code, attempt + 1, MAX_ATTEMPTS, wait))
            time.sleep(wait)
        except Exception as e:  # noqa: BLE001 - network hiccup, retry
            last_err = e
            time.sleep(2 * (attempt + 1))
    raise last_err


def main():
    sid = sys.argv[1]
    story = json.load(open(sid + ".json", encoding="utf-8"))
    lc = story.get("langCode")
    if lc not in VOICES:
        raise SystemExit("No voice configured for langCode %r (story %s)" % (lc, sid))
    cfg = dict(VOICES[lc])
    key = os.environ["GOOGLE_TTS_KEY"]

    adir = "audio/" + sid
    os.makedirs(adir, exist_ok=True)

    # an already-resolved voice sticks (idempotent re-runs must never drift)
    vf = adir + "/voice.txt"
    if not cfg.get("name") and os.path.exists(vf):
        cfg["name"] = open(vf, encoding="utf-8").read().strip() or None
    cfg["name"] = resolve_voice(cfg, key)
    open(vf, "w", encoding="utf-8").write(cfg["name"] + "\n")

    # Clips are cached by TEXT, not merely by existence. Skipping on existence alone means a
    # corrected sentence keeps its old recording forever — and when the correction does not change
    # the word count (e.g. swapping 愛國治民 -> 愛民治國) the aligner still reports a clean match, so
    # nothing anywhere reveals that the voice is reading the superseded text.
    tf = adir + "/texts.json"
    prev_texts = {}
    if os.path.exists(tf):
        try:
            prev_texts = json.load(open(tf, encoding="utf-8"))
        except Exception:
            prev_texts = {}

    made = restaled = 0
    texts = {}
    for i, s in enumerate(story["sentences"]):
        path = "%s/%d.mp3" % (adir, i)
        text = s["t"].replace("\n", " ").strip()
        texts[str(i)] = text
        fresh = os.path.exists(path) and os.path.getsize(path) > 0
        if fresh and prev_texts.get(str(i)) == text:
            continue
        if fresh:
            restaled += 1
            print("  text changed for sentence %d — resynthesizing" % i)
        open(path, "wb").write(synth_with_retry(text, cfg, key))
        made += 1
        time.sleep(THROTTLE_S)
    json.dump(texts, open(tf, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("synth: %d clip(s) written (%d of them stale text) of %d total for %s"
          % (made, restaled, len(story["sentences"]), sid))

    env = dict(os.environ)
    env["ESPEAK_VOICE"] = cfg["espeak"]
    subprocess.run(
        ["python3", ".github/scripts/align_dtw.py", sid],
        check=True, env=env,
    )


if __name__ == "__main__":
    main()
