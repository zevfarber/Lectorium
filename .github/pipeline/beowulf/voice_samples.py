#!/usr/bin/env python3
"""Beowulf voice samples (2026-10-12): Beowulf lines 1-11 read by candidate carrier voices under IPA pins.

Runs on GitHub Actions (workflow oe-voice-samples.yml; the Google key is the GOOGLE_TTS_KEY secret).
For each candidate voice it:
  1. probes which IPA symbols the voice accepts, two ways: customPronunciations (the API names every
     invalid phrase) and one SSML <phoneme> request per symbol (an error = refused);
  2. checks the voice really honours pins: the same visible word under two different pins, LINEAR16,
     relative RMS of the difference (about 0 = pins ignored);
  3. checks determinism: the same pinned input twice, compared the same way;
  4. renders lines 1-11 as one clip, every word pinned with oe_g2p reduced to that voice's inventory.
Writes audio-pilot/beowulf/<voice>.mp3, audio-pilot/beowulf/report.json, and the characters it sent
to audio-pilot/beowulf/chars.json (the workflow adds them to audio/_tts-usage.json).
Never touches any Beowulf story file.
"""
import base64, io, json, math, os, re, struct, sys, time, urllib.error, urllib.request, wave
from xml.sax.saxutils import escape

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import oe_g2p as G

KEY = os.environ["GOOGLE_TTS_KEY"]
URL = "https://texttospeech.googleapis.com/v1/text:synthesize"
URL_BETA = "https://texttospeech.googleapis.com/v1beta1/text:synthesize"
OUT = "audio-pilot/beowulf"
RATE = 0.85
VOICES = [  # (option label, voice)
    ("A", "de-DE-Wavenet-B"),
    ("B", "en-US-Neural2-D"),
    ("C", "en-GB-Neural2-B"),
]
CHARS = {}


def call(inp, voice, enc="MP3", beta=False):
    lang = "-".join(voice.split("-")[:2])
    body = json.dumps({"input": inp, "voice": {"languageCode": lang, "name": voice},
                       "audioConfig": {"audioEncoding": enc, "speakingRate": RATE}}).encode()
    n = len(inp.get("ssml", "")) + len(inp.get("text", "")) + sum(
        len(p["phrase"]) + len(p["pronunciation"]) for p in inp.get("customPronunciations", {}).get("pronunciations", []))
    for a in range(6):
        req = urllib.request.Request((URL_BETA if beta else URL) + "?key=" + KEY, data=body,
                                     headers={"Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=90) as r:
                data = base64.b64decode(json.load(r)["audioContent"])
            fam = next((f for f in ("Chirp", "Neural2", "Wavenet", "Standard") if f in voice), voice)
            CHARS[fam] = CHARS.get(fam, 0) + n
            time.sleep(0.25)
            return data, None
        except urllib.error.HTTPError as e:
            msg = e.read().decode("utf-8", "replace")
            if e.code == 429 or e.code >= 500:
                time.sleep(5 * (a + 1)); continue
            return None, msg
    return None, "gave up after retries"


def pcm(wav_bytes):
    with wave.open(io.BytesIO(wav_bytes)) as w:
        raw = w.readframes(w.getnframes())
    return struct.unpack("<%dh" % (len(raw) // 2), raw)


def rel_rms(a, b):
    n = max(len(a), len(b))
    a = list(a) + [0] * (n - len(a)); b = list(b) + [0] * (n - len(b))
    num = math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)) / n)
    den = math.sqrt(sum(x * x for x in a) / n) or 1
    return round(num / den, 4)


def ph(ipa, word):
    return '<phoneme alphabet="ipa" ph="%s">%s</phoneme>' % (escape(ipa, {'"': "&quot;"}), escape(G.plain(word)))


def probe_custom(voice, symbols):
    """customPronunciations probe: returns (accepted set, rejected set) or (None, error)."""
    items = []
    for i, s in enumerate(symbols):
        if s == "ː":
            p = "tatːa"
        elif G.is_vowel(s):
            p = "t" + s + "t"
        else:
            p = "a" + s + "a"
        items.append(("zq%dx" % i, p, s))
    text = " ".join(x[0] for x in items)
    inp = {"text": text, "customPronunciations": {"pronunciations": [
        {"phrase": ph_, "phoneticEncoding": "PHONETIC_ENCODING_IPA", "pronunciation": p} for ph_, p, _ in items]}}
    data, err = call(inp, voice, beta=True)
    if data:
        return set(symbols), set()
    bad = set(re.findall(r"zq(\d+)x", err or ""))
    if not bad:
        return None, (err or "")[:400]
    rej = {items[int(i)][2] for i in bad}
    return set(symbols) - rej, rej


def probe_ssml(voice, symbols):
    acc, rej = set(), {}
    for s in symbols:
        if s == "ː":
            p = "ˈtatːa"
        elif G.is_vowel(s):
            p = "ˈt" + s + "t"
        else:
            p = "ˈa" + s + "a"
        data, err = call({"ssml": "<speak>" + ph(p, "ta") + "</speak>"}, voice)
        if data:
            acc.add(s)
        else:
            rej[s] = (err or "")[:160]
    return acc, rej


def units(lines):
    """Klaeber's lines 1-11 as SSML: one pinned <phoneme> per word, his punctuation as pauses,
    and a short break at each line end (verse is read as verse)."""
    return lines


def line_ssml(line, accepted, gem_ok, log):
    parts = []
    for m in re.finditer(r"[^\s,;!.:?—]+|[,;!.:?]", line):
        tok = m.group(0)
        if tok in ",;!.:?":
            parts.append({",": ",", ";": ",", ":": ",", "!": "!", ".": ".", "?": "?"}[tok]); continue
        ipa = G.reduce(G.ipa_tokens(tok), accepted, gem_ok, log)
        parts.append(" " + ph(ipa, tok))
    return "".join(parts).strip()


def main():
    src = json.load(open(os.path.join(HERE, "source/beowulf-klaeber1922.json"), encoding="utf-8"))
    lines = [l["t"] for l in src["lines"][:11]]
    os.makedirs(OUT, exist_ok=True)
    symbols = G.all_candidates() + ["ː", "ˈ"]
    symbols = sorted(set(symbols))
    report = {"date": "2026-10-12", "rate": RATE, "lines": lines, "voices": {}}
    for label, voice in VOICES:
        r = {"label": label}
        acc_c, rej_c = probe_custom(voice, [s for s in symbols if s != "ˈ"])
        r["custom_probe"] = ({"rejected": sorted(rej_c)} if acc_c is not None else {"error": rej_c})
        acc_s, rej_s = probe_ssml(voice, [s for s in symbols if s != "ˈ"])
        r["ssml_probe_rejected"] = sorted(rej_s)
        r["ssml_probe_errors_sample"] = dict(list(rej_s.items())[:3])
        accepted = set(acc_s) if acc_c is None else (set(acc_s) & set(acc_c))
        r["accepted"] = sorted(accepted)
        if not accepted:
            r["skipped"] = "voice refused every pin"; report["voices"][voice] = r; continue
        gem_ok = "ː" in accepted
        # pin-honour test: same visible word, two different pins
        a, _ = call({"ssml": "<speak>" + ph("ˈtata", "Hwaet") + "</speak>"}, voice, "LINEAR16")
        b, _ = call({"ssml": "<speak>" + ph("ˈmɔnɛ", "Hwaet") + "</speak>"}, voice, "LINEAR16")
        c, _ = call({"text": "Hwaet"}, voice, "LINEAR16")
        if a and b and c:
            r["pin_A_vs_pin_B"] = rel_rms(pcm(a), pcm(b))
            r["pin_A_vs_unpinned"] = rel_rms(pcm(a), pcm(c))
        log = []
        ssml = "<speak>" + ' <break time="350ms"/> '.join(line_ssml(l, accepted, gem_ok, log) for l in lines) + "</speak>"
        r["ssml"] = ssml
        fb = {}
        for ideal, used in log:
            fb["%s→%s" % (ideal, used or "single")] = fb.get("%s→%s" % (ideal, used or "single"), 0) + 1
        r["fallbacks"] = fb
        mp3, err = call({"ssml": ssml}, voice)
        if not mp3:
            r["render_error"] = (err or "")[:400]; report["voices"][voice] = r; continue
        open("%s/%s.mp3" % (OUT, voice), "wb").write(mp3)
        w1, _ = call({"ssml": ssml}, voice, "LINEAR16")
        w2, _ = call({"ssml": ssml}, voice, "LINEAR16")
        if w1 and w2:
            p1 = pcm(w1)
            r["determinism_rel_rms"] = rel_rms(p1, pcm(w2))
            r["seconds"] = round(len(p1) / 24000.0, 2)
            with wave.open(io.BytesIO(w1)) as w:
                r["seconds"] = round(w.getnframes() / float(w.getframerate()), 2)
        report["voices"][voice] = r
        print(label, voice, "accepted", len(accepted), "fallbacks", fb, "pins", r.get("pin_A_vs_pin_B"))
    report["chars"] = CHARS
    json.dump(report, open(OUT + "/report.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    json.dump(CHARS, open(OUT + "/chars.json", "w"), indent=1)
    print("characters sent:", CHARS)


if __name__ == "__main__":
    main()
