# Beowulf audio — notes for the full build (2026-10-12)

Status: **samples only, waiting for Zev's choice.** No Beowulf story file has audio and none was changed.
Listening page: https://zevfarber.github.io/Lectorium/audio-pilot/beowulf.html (lines 1–11).

## Pronunciation
Reconstructed late West Saxon, c. 1000, after Campbell, *Old English Grammar* — already in every part's `source`.
`oe_g2p.py` (this folder) turns Klaeber's printed spelling into IPA; its docstring lists every rule and its known
limits. Klaeber does not dot ċ/ġ, so palatal c and g come from rules plus a short word list (`PALATAL_C`); a compound
whose second element begins with f/s/þ after a vowel needs an entry in `SPLITS` or it is wrongly voiced.

## Carriers probed (voice_samples.py, run by .github/workflows/oe-voice-samples.yml)
Probe method: `customPronunciations` with one placeholder phrase per symbol (the API names every invalid phrase).
SSML `<phoneme>` never errors on a bad symbol, so the SSML probe is useless; trust the customPronunciations list.

| option | voice | pins honoured (pin A vs pin B, rel. RMS) | same input twice | refused (fallback used) |
|---|---|---|---|---|
| A | de-DE-Wavenet-B | yes, 1.46 | 0.195 (near, not bit-identical) | æ æː ɑ ɑː eː oː uː yː ɣ, every diphthong except ɛa/eɔ-type, consonant length → ɛ, a, aː, e, o, u, y, g, single consonants |
| B | en-US-Neural2-D | yes, 1.54 | 0.000 (bit-identical) | bare o, yː, æː, ɣ, o-diphthongs → ɔ, y, æ, g; keeps æ, ɑ, ɑː, eː, oː, uː, and the reconstructed diphthongs |
| C | en-GB-Neural2-B | **no: 0.000** (pins ignored) | — | refuses every symbol; dropped, not on the page |

The German inventory matches the Norse findings exactly. American English keeps far more of the reconstruction
(true æ, back ɑ, long eː/oː/uː, æɑ and eɔ diphthongs, geminates); it cannot do [ɣ] or long [yː].

## Wiring once Zev picks
1. Copy `oe_g2p.py` to `.github/scripts/` and give it the builder interface (`ipa(word)` returning the reduced IPA for
   the chosen voice, with the accepted set from `audio-pilot/beowulf/report.json` baked in).
2. Add `"Old English"` to `PINNED` in `build_pinned.py` (voice as chosen, rate 0.85, espeak `en` for the aligner
   fallback), add it to `PINNED_AUTO` and `beowulf-` to `BUILD_ON_PUSH` in `pick_targets.py`.
3. The next push of each `beowulf-*.json` (or a dispatch with its id) builds sentence clips, word clips (mandatory:
   `langCode: null`, so the popup's Say it has no other source) and `align.json` via `align_wordref.py`.
4. Add an "Audio:" sentence to each part's `source` naming the voice and its limits (for German: vowel length shown by
   quality; no geminates; æ read as e). That is a build.py change in this folder so later parts get it too.

## Size and cost
Whole poem (3,182 lines, 5,743 unique word forms, counted with this g2p): about 0.95M characters of sentence SSML +
0.40M of word clips = **~1.36M characters**, either voice. Per fitt about 31k.
- Inside a month's free pool (WaveNet 4M, Neural2 1M) most of it is free, but both pools are shared with Greek,
  Latin, Akkadian and the rest; in October 2026 both are already spent.
- All paid: 1.36M × $16/M ≈ **$22** — over the $10/month budget if done at once. Spread at the routine's pace (one fitt
  every three hours, 44 fitts) it is about $0.50 per fitt paid, so roughly 20 fitts fit in a $10 month alongside nothing
  else. `build_pinned.py` already stops at the budget and the daily check warns Zev.
- The sample run itself: 14,106 WaveNet + 28,224 Neural2 characters (≈ $0.45), recorded in `audio/_tts-usage.json`.
