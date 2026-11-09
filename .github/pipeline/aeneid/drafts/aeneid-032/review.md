# aeneid-032 (Aeneid V.104–200) — reviewer's record

Two passes (pass 1: every note's grammar, Latin to `l` word by word, `l`/`i` agreement, echoes, speech marks, misprint notes; pass 2: all 97 lines scanned by hand against the scanner's fits, then every unit re-read as edited). `t` untouched (asserted identical before and after every edit script); `units.json` edited by script in `l`, `i`, `n` only; `draft.py` kept in sync (the same replacements, checked field for field against `units.json`). `scan-fixes.json` extended by script: 6 new keys appended after 5.103, existing entries and order untouched. Nothing built or published: `build_aeneid.py` has no dry run, so its scansion stage was reproduced with `scan_latin.scan_story` plus `scan-fixes.json` (the same code path), and the validator's foot, syllable-count and `×` checks were run on the result: 0 UNRESOLVED, 0 MISMATCH, 0 COSTLY, `sc` on all 47 units, all 97 lines are six feet. Every note is 15–140 words (144 and 162 trimmed to get there); `l` has the same line count as `t` in every unit.

Severity counts: **major 8, medium 7, low 16.** (Major = a false grammatical label, an `l` that gets the sense wrong, or a scansion with wrong quantities or syllable count. Of the 8, 2 are text and 6 are scansion.)

## Major

1. **5.124 `spumantia contra / litora`**: the note said `contra` is "placed after its noun (anastrophe)". It stands between the adjective and its noun, before `litora`. Note now: "with the preposition 'contra' set between the adjective and its noun."
2. **5.156 `l`** "now the beaten one passes the huge / Centaur" made the Pristis the subject. The Centaur passes her (`victam` is the object). `l` now "now her, beaten, passes the huge / Centaur". (`i` and note were already right.)
3–8. **Scansion: wrong syllable count or quantities in the scanner's fit.** All six are now in `scan-fixes.json`, each with its reason:
   - **5.105** `Phaethontis` read with `ae` as a diphthong (14 syllables, cost 0.0). Phaethon is Phă-ĕ-thōn (Φαέθων): Au-rō | ram Phă-ĕ | thon-tĭs ĕ | quī iam | lū-cĕ vĕ | hē-bant. The metre allows both readings; the word allows only the second.
   - **5.129** `Aeneas` split A-e-ne-as with short ne (cost 1.2). Hīc vĭ-rĭ(dem) | Ae-nē | ās fron | den(ti) ex | ī-lĭ-cĕ | mē-tam.
   - **5.144** `biiugo`: the scanner ran bi-iu into one long syllable (cost 1.5). It is bĭ-jŭ-gō (bi + iugum, consonantal i, short prefix; as `biiugique` 10.253): Non tam | prae-cĭ-pĭ | tēs bĭ-jŭ | gō cer | tā-mĭ-nĕ | cam-pum.
   - **5.181** `Teucri` split Te-u-cri, and the printed `Ilium` read by synizesis (cost 1.5). The line scans only as `Illum`: Il-l(um) et | lā-ben | tem Teu | cr(i) et rī | sē-rĕ-nă | tan-tem. The first word is marked `1Il–ium` (the print's letters, `-ium` unmarked as elided), since the fix must match the printed words.
   - **5.186** `praeeunte` with long prae and eun one syllable by synizesis (cost 1.5). Prae is shortened before the vowel (as `praeustis`, 7.524) and e-un stays two syllables: nec tō | tā tă-men | il-lĕ prĭ | ŏr praĕ-ĕ | un-tĕ că | rī-na. Unconfirmed: see open questions.
   - **5.193** `Ionio` read with consonantal I (cost 0.6), which forced `-que` (before m) and `ma-` long. Vowel I, five dactyls: Ī-ŏ-nĭ | ō-quĕ mă | rī Mă-lĕ | ae-quĕ sĕ | quā-cĭ-bŭs | un-dis.

## Medium

1. **5.116 `Pristim`** was called "a Greek accusative in -im". The Greek accusative would be -in; -im is the Latin i-stem accusative. Note: "an accusative in -im (as 'puppim', 'turrim')".
2. **5.188 `socios… per ipsos`**: the note said "the noun framed with the preposition after it". Now: "with 'per' set between the noun and 'ipsos'".
3. **5.137–138 `i`** "while throbbing fear and an eager longing for glory drain their leaping hearts" ran close to a known version in both shape and wording. Rephrased: "their leaping hearts emptied by the hammering of fear and a quickened hunger for praise."
4. **5.115 `l`** "four from the whole chosen fleet keels" attached `delectae` to the fleet. Now "four, chosen from the whole fleet, keels."
5. **5.116 `l`** "The swift Mnestheus drives" made Mnestheus swift (`velocem` goes with `Pristim`). With the pilot's commas for hyperbaton, it now reads "The swift, Mnestheus drives with keen crew, Pristis,".
6. **5.118 `l`** "and the huge Gyas" had the same problem (`ingentem` goes with `Chimaeram`). Now "and the huge, Gyas, of huge bulk, Chimaera,".
7. **5.129 `l`** "Here a green Aeneas" had the same problem (`viridem` goes with `metam`). Now "Here a green, Aeneas, from a leafy holm-oak, turning-post".

## Low

1. **5.113** `l` "from the middle of the mound" and the note's "from the middle of a mound" did not match `i` "from a mound in the middle". `l` is now "from the mound in the middle", and the note says "'on (from) the mound in the middle' of the ring".
2. **5.128** `l` "gulls" became "divers", to match the note (`mergus`, a diving bird).
3. **5.135** `l` "they gleam" had a singular subject (`iuventus… nitescit`). Now "and, its bared shoulders with oil steeped, it gleams."
4. **5.151** `l` "on the front glides out of the waves" became "over the foremost waves glides away".
5. **5.164** speech marks: the last `l` of Gyas's speech had no ”. Added (house practice: the ” goes on the last unit's `l` and `i`, while `t`'s ” stays at the head of the next unit).
6. **5.197** speech marks: the same fix on the last `l` of Mnestheus's speech.
7. **5.190** `i` "comrades of Hector's breed" implied kinship, against the note ("men who fought beside him"). Now "Hector's comrades".
8. **5.198** `i` "under their mighty strokes" (a stock phrase of a known version) became "at their huge strokes", and "bronze-clad" became "bronze-plated".
9–15. **Scansion remarks added to notes**, so that the reader's `sc` is explained: 104 `Phaethontis` four syllables; 144 `biiugo` scanned bĭ-jŭ-gō; 181 the line scans only with `Illum`; 184 `Mnesthei` two syllables; 186 short `prae` in `praeeunte`; 193 `Ionio` four syllables, vowel I; 195 `quamquam` elides into `O`.
16. **Note lengths**: 144 (147 words) and 162 (`Huc dirige`, over 140) trimmed below the validator's 140-word WARN, with no content lost beyond redundancy (the dropped bits were the gloss of `Huc`, already in `l`; "concussere is another -ere perfect"; and a restatement of the variant's sense).

## Misprints (checked for consistency, no change needed)

5.135 `perfilsa`, 5.166 `Pete`, 5.181 `Ilium`: `t` stays as printed in all three, and each note opens with "The print has '…', a misprint for '…'", gives the intended reading, and (135, 181) cites The Latin Library. This matches the precedent of QUESTIONS #19/#23. 135 scans the same with either reading (fil and fū are both long). 166 has no metrical effect. 181 needed the hand scansion above.

## Refused or checked without change

- **Caesura marks**: at 116, 117, 127, 145 and 189 the scanner leaves out `‖` or puts it after a minor word (it does not see the end of `Mnestheus` as a word end). The quantities are right, and a fix for the mark alone is outside what `scan-fixes.json` is for. Not entered.
- **5.116, 117, 189, 194 `Mnestheus`** (cost 1.5): Mnes-theus with `eu` as one long syllable is correct. 184 `Mnestheique` with `-thei` as one syllable is correct.
- **5.123** long `tibī` before the caesura (cost 0.6) is the only fit. Kept.
- **5.195** `quamquam O`: the scanner elides `-am` into the interjection. A hiatus reading gives no hexameter, so the scanner's fit is kept and the note now says so.
- **5.108** `visur(i) Aeneadas`: here the scanner gets `Ae-` right. 5.121, 122, 133, 139 and 150 (named in the brief) have no consonantal-i or hiatus problem, and the scanner's fits are right. 5.117 `Italus` is short Ĭ, which the metre requires and the scanner has.
- **5.117 `genus a quo nomine Memmi`**: I considered reading `quo` with `nomine` ("from which name"). The note's "from whose name" gives the same sense, so it is kept.
- **5.104 `l`**: `serena` (line 1) is rendered with `luce` on line 2. Coherence wins; kept.
- **5.178 `i`** leaves out `vix` ("scarcely"). The sense is carried by "at last"; kept.
- **5.162–164, 196–197, 199–200 `i`**: checked for echoes of known versions. These are plain renderings of the Latin, with nothing distinctive to rephrase. Kept.
- **`about`**: accurate, no echoes. Kept.

## Open questions (for QUESTIONS.md)

1. **Phaethon**: the published Ovid parts (`ovid-met-010`, `011`, `012`, `028`, `095`) scan `Phae-` as one syllable. This part enters the trisyllabic Phă-ĕ-thōn (Greek, Lewis & Short). The metre cannot tell the two apart. The owner may want one reading across both works.
2. **Ionius**: published `aeneid-019` (3.211 `insulae Ionio`) and `aeneid-023` (3.671 `Ionios`) carry the scanner's one-syllable `Io`. 3.211 needs vowel I for its famous hiatus, so both are probably worth re-entering.
3. **5.186 `praeeunte`**: short prae before the vowel (my reading, on the analogy of 7.524 `praeustis`), against the scanner's long prae plus synizesis. Both give six feet. Unconfirmed.
4. **`biiugus`**: `ovid-met-026` has `biiu–3gum–`, which looks like the same bi-iu fusion corrected here at 5.144.
