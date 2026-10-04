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
    # Voice switched 2026-10-04 from de-DE-Neural2-D to de-DE-Wavenet-B: Zev compared them by ear and
    # could not tell them apart, and WaveNet's free allowance is 4M characters a month against 1M.
    # The pilot clips already built with Neural2 (aesop-001, odyssey-001) are kept.
    "Ancient Greek": {"module": "greek_g2p", "voice": "de-DE-Wavenet-B", "lang": "de-DE",
                      "rate": 0.9, "espeak": "grc"},
}
TTS_URL = "https://texttospeech.googleapis.com/v1/text:synthesize"

# MONTHLY FREE ALLOWANCE GUARD (2026-10-04). Zev's rule: audio stays inside Google's free monthly
# characters; nothing may run up a bill. Every character this module sends is counted in
# audio/_tts-usage.json (committed with the clips; the build-audio job runs one at a time, so the
# count is exact), and a story that would cross the cap is skipped, not half-built. A skipped story
# has no align.json, so the daily "missing" sweep picks it up again next month.
USAGE_FILE = "audio/_tts-usage.json"
MONTHLY_CAP = {"Wavenet": 3600000, "Neural2": 900000}   # Google free tiers: 4M and 1M, with margin


def _family(voice):
    return next((f for f in MONTHLY_CAP if f in voice), voice)


def _usage():
    try:
        return json.load(open(USAGE_FILE, encoding="utf-8"))
    except Exception:  # noqa: BLE001
        return {}


def _charge(voice, n):
    u = _usage(); m = time.strftime("%Y-%m", time.gmtime())
    fam = u.setdefault(_family(voice), {}); fam[m] = fam.get(m, 0) + n
    os.makedirs(os.path.dirname(USAGE_FILE), exist_ok=True)
    json.dump(u, open(USAGE_FILE, "w", encoding="utf-8"), indent=1, sort_keys=True)


def used_this_month(voice):
    return _usage().get(_family(voice), {}).get(time.strftime("%Y-%m", time.gmtime()), 0)
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
                audio = base64.b64decode(json.load(r)["audioContent"])
            _charge(cfg["voice"], len(ssml))
            return audio
        except urllib.error.HTTPError as e:
            last = e
            if e.code == 429 or 500 <= e.code < 600:
                time.sleep(min(5 * 2 ** a, 60)); continue
            raise RuntimeError("TTS %d: %s" % (e.code, e.read().decode("utf-8", "replace")[:500]))
        except Exception as e:  # noqa: BLE001
            last = e; time.sleep(2 * (a + 1))
    raise last


_ROMAN = str.maketrans({"ˈ": "", "ʰ": "h", "ŋ": "ng", "ɛ": "e", "ɔ": "o", "ʏ": "y", "ɪ": "i",
                        "ʊ": "u", "ː": "", "j": "i"})


def ph(ipa):
    # The inner text is what the voice reads if it rejects the IPA (it did so for every string with ʰ,
    # and read the old placeholder "x" as the letter — "ex"). A rough romanization is the safer fallback.
    return '<phoneme alphabet="ipa" ph="%s">%s</phoneme>' % (escape(ipa, {'"': "&quot;"}),
                                                            escape(ipa.translate(_ROMAN)))


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

    # Free-allowance guard: estimate this story (sentence clips, plus word clips at about the same
    # again, measured on the pilots) and skip it whole if it would cross the month's cap.
    need = sum(len(sentence_ssml(s["t"], G)) for i, s in enumerate(story["sentences"])
               if prev.get(str(i)) != sentence_ssml(s["t"], G))
    cap = MONTHLY_CAP.get(_family(cfg["voice"]))
    if cap and need and used_this_month(cfg["voice"]) + int(need * 2.2) > cap:
        print("FREE ALLOWANCE: %s needs ~%d characters; %d of %d already used this month. Skipped "
              "until next month." % (sid, int(need * 2.2), used_this_month(cfg["voice"]), cap))
        return
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
