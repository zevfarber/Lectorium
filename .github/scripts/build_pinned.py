#!/usr/bin/env python3
"""Prepared audio for languages with no voice of their own: a carrier voice reads per-word IPA pins.

Written 2026-09-28 for Ancient Greek (reconstructed Attic, after Allen, Vox Graeca). The recipe is
the one proven on the Hávamál (claude/norse-audio-carrier-findings.md): de-DE-Neural2-D, SSML
<phoneme alphabet="ipa">, deterministic, so one listen approves a whole language.

Called by build_audio.py for a story whose `language` is in PINNED. Writes, like every other audio
story: audio/<id>/<n>.mp3 (one per sentence), texts.json (the SSML each clip speaks, so a changed
line or a changed pin re-synthesizes and nothing else does), w/<n>.mp3 + words.json (word clips
for the popup and as the aligner's reference), voice.txt, then runs align_wordref.py.

Usage: python3 build_pinned.py <story-id>     Env: GOOGLE_TTS_KEY
"""
import json, os, re, subprocess, sys, time, base64, urllib.request, urllib.error
from xml.sax.saxutils import escape

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import align_wordref as AW

PINNED = {
    "Ancient Greek": {"module": "greek_g2p", "voice": "de-DE-Neural2-D", "lang": "de-DE",
                      "rate": 0.9, "espeak": "grc"},
}
TTS_URL = "https://texttospeech.googleapis.com/v1/text:synthesize"
THROTTLE_S = 0.25
ELISION = "’᾽'ʼ᾿"
# printed punctuation -> what the carrier voice sees (pauses only)
PUNCT = {".": ".", ",": ",", ";": "?", ";": "?", "·": ",", "·": ",", "!": "!", ":": ","}


def synth_ssml(ssml, cfg, key, attempts=6):
    body = json.dumps({"input": {"ssml": ssml},
                       "voice": {"languageCode": cfg["lang"], "name": cfg["voice"]},
                       "audioConfig": {"audioEncoding": "MP3", "speakingRate": cfg["rate"]}}).encode()
    last = None
    for a in range(attempts):
        req = urllib.request.Request(TTS_URL + "?key=" + key, data=body,
                                     headers={"Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=90) as r:
                return base64.b64decode(json.load(r)["audioContent"])
        except urllib.error.HTTPError as e:
            last = e
            if e.code == 429 or 500 <= e.code < 600:
                time.sleep(min(5 * 2 ** a, 60)); continue
            raise RuntimeError("TTS %d: %s" % (e.code, e.read().decode("utf-8", "replace")[:500]))
        except Exception as e:  # noqa: BLE001
            last = e; time.sleep(2 * (a + 1))
    raise last


def ph(ipa):
    return '<phoneme alphabet="ipa" ph="%s">x</phoneme>' % escape(ipa, {'"': "&quot;"})


def sentence_ssml(t, G):
    """One <phoneme> per word; an elided word is spoken glued to the next one."""
    parts, pend = [], ""
    pos = 0
    toks = list(AW.WORD_RE.finditer(t))
    for k, m in enumerate(toks):
        gap = t[pos:m.start()]
        for ch in gap:
            if ch in PUNCT:
                parts.append(PUNCT[ch])
        pos = m.end()
        p = G.ipa(m.group(0))
        after = t[m.end():m.end() + 1]
        if after and after in ELISION and k + 1 < len(toks):
            pend += p.replace("ˈ", "")
            continue
        parts.append(ph(pend + p) if (pend + p) else "")
        pend = ""
    for ch in t[pos:]:
        if ch in PUNCT:
            parts.append(PUNCT[ch])
    body = ""
    for x in parts:
        body += (x if x in PUNCT.values() else (" " + x))
    return "<speak>" + body.strip() + "</speak>"


def main():
    sid = sys.argv[1]
    story = json.load(open(sid + ".json", encoding="utf-8"))
    cfg = PINNED[story["language"]]
    G = __import__(cfg["module"])
    key = os.environ["GOOGLE_TTS_KEY"]
    adir = "audio/" + sid
    os.makedirs(adir + "/w", exist_ok=True)

    # Aspirates: keep [pʰ tʰ kʰ] only if the voice accepts ʰ; otherwise fall back to p t k.
    if hasattr(G, "ASP") and G.ASP:
        try:
            synth_ssml("<speak>" + ph("ˈpʰos") + "</speak>", cfg, key)
        except RuntimeError as e:
            print("voice refuses ʰ, aspirates fall back to plain stops:", e); G.ASP = ""
    open(adir + "/voice.txt", "w").write(cfg["voice"] + "\n")

    tf = adir + "/texts.json"
    prev = json.load(open(tf, encoding="utf-8")) if os.path.exists(tf) else {}
    texts, made = {}, 0
    for i, s in enumerate(story["sentences"]):
        ssml = sentence_ssml(s["t"], G)
        texts[str(i)] = ssml
        p = "%s/%d.mp3" % (adir, i)
        if os.path.exists(p) and os.path.getsize(p) > 0 and prev.get(str(i)) == ssml:
            continue
        open(p, "wb").write(synth_ssml(ssml, cfg, key)); made += 1; time.sleep(THROTTLE_S)
    json.dump(texts, open(tf, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("sentence clips: %d written of %d for %s" % (made, len(story["sentences"]), sid))

    wf, wtf = adir + "/words.json", adir + "/w/texts.json"
    words = json.load(open(wf, encoding="utf-8")) if os.path.exists(wf) else {}
    wtexts = json.load(open(wtf, encoding="utf-8")) if os.path.exists(wtf) else {}
    nxt = max([int(n) for n in words.values()] + [-1]) + 1
    keys = {}
    for s in story["sentences"]:
        for tok in AW.WORD_RE.findall(s["t"]):
            keys.setdefault(AW.word_key(tok), tok)
    wmade, skipped = 0, []
    for k in sorted(keys):
        ipa = G.ipa(keys[k])
        if not re.search("[aeiouyɛɔɪʏʊœ]", ipa):
            skipped.append(k); continue          # a bare elided consonant has nothing to say alone
        if k not in words:
            words[k] = nxt; nxt += 1
        n = str(words[k]); p = "%s/w/%s.mp3" % (adir, n)
        ssml = "<speak>" + ph(ipa) + "</speak>"
        if os.path.exists(p) and os.path.getsize(p) > 0 and wtexts.get(n) == ssml:
            continue
        open(p, "wb").write(synth_ssml(ssml, cfg, key)); wtexts[n] = ssml; wmade += 1
        time.sleep(THROTTLE_S)
    json.dump(words, open(wf, "w", encoding="utf-8"), ensure_ascii=False, indent=1, sort_keys=True)
    json.dump(wtexts, open(wtf, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("word clips: %d written of %d keys; no clip for %s" % (wmade, len(keys), skipped or "none"))

    env = dict(os.environ); env["ESPEAK_VOICE"] = cfg["espeak"]
    subprocess.run(["python3", os.path.join(HERE, "align_wordref.py"), sid], check=True, env=env)


if __name__ == "__main__":
    main()
