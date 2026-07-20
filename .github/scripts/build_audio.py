#!/usr/bin/env python3
"""Synthesize per-sentence audio clips for a story and build karaoke timings.

Runs on a GitHub-hosted runner (open internet, unlike the Cowork sandbox):
  * synthesizes any MISSING audio/<id>/<i>.mp3 via Google Cloud TTS (pinned
    Chirp voice), so re-runs are idempotent;
  * then runs the proven model-free aligner (align_dtw.py) to write
    audio/<id>/align.json.

Voice + espeak mapping is keyed by the story's langCode and must match the
Spoken-audio policy (German de-DE-Chirp-HD-F, French fr-FR-Chirp-HD-F).

Usage: python3 build_audio.py <story-id>
Env:   GOOGLE_TTS_KEY  (Google Cloud TTS API key, from Actions secret)
"""
import base64, json, os, subprocess, sys, time, urllib.request

VOICES = {
    "de-DE": {"name": "de-DE-Chirp-HD-F", "lang": "de-DE", "espeak": "de"},
    "fr-FR": {"name": "fr-FR-Chirp-HD-F", "lang": "fr-FR", "espeak": "fr"},
}

TTS_URL = "https://texttospeech.googleapis.com/v1/text:synthesize"


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
        d = json.load(r)
    return base64.b64decode(d["audioContent"])


def main():
    sid = sys.argv[1]
    story = json.load(open(sid + ".json", encoding="utf-8"))
    lc = story.get("langCode")
    if lc not in VOICES:
        raise SystemExit("No voice configured for langCode %r (story %s)" % (lc, sid))
    cfg = VOICES[lc]
    key = os.environ["GOOGLE_TTS_KEY"]

    adir = "audio/" + sid
    os.makedirs(adir, exist_ok=True)

    made = 0
    for i, s in enumerate(story["sentences"]):
        path = "%s/%d.mp3" % (adir, i)
        if os.path.exists(path) and os.path.getsize(path) > 0:
            continue
        text = s["t"].replace("\n", " ").strip()
        last_err = None
        for attempt in range(3):
            try:
                open(path, "wb").write(synth(text, cfg, key))
                made += 1
                last_err = None
                break
            except Exception as e:  # noqa: BLE001 - retry any transient failure
                last_err = e
                time.sleep(2 * (attempt + 1))
        if last_err is not None:
            raise last_err
    print("synth: %d new clip(s) of %d total for %s" % (made, len(story["sentences"]), sid))

    env = dict(os.environ)
    env["ESPEAK_VOICE"] = cfg["espeak"]
    subprocess.run(
        ["python3", ".github/scripts/align_dtw.py", sid],
        check=True, env=env,
    )


if __name__ == "__main__":
    main()
