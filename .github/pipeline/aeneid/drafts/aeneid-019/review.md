# aeneid-019 review (III.209–305) — adversarial reviewer

Two passes. Pass 1: every unit read against the Latin word by word (grammar labels, `l`, `i`, notes, speech marks),
every line scanned by hand against the scanner's output. Pass 2: re-read of the edited units for new
inconsistencies, `l` ↔ `i` agreement, and remembered English in `i`. `t` was not touched (checked: the 47 `t`
strings, `ln`, `p`, `v` are identical before and after). `units.json` was edited by script only.

## Counts

| | major | medium | low | total |
|---|---|---|---|---|
| text (`l`, `i`, `n`, `about`) | 4 | 21 | 45 | 70 |
| scansion (`scan-fixes.json`) | 4 | 10 | 3 | 17 |
| **all changes** | **8** | **31** | **48** | **87** |

Pass 1 made 62 text changes and the 17 scansion entries; pass 2 made 8 text changes (7 `i` rewrites, 1 `about`).
No change to `t`. Refused findings: 14 (below).

Severity: major = a false grammatical label, a wrong or missing `l`, or a line the build cannot scan; medium = a
mislabel, an omitted or invented word that moves the sense, an echo of a known version, a wrong scanner
quantity; low = wording, unverifiable asides, pipeline mechanics, typos.

## Major (8)

1. Unit 4 (3.221) note: `caprigenum` called "the genitive plural of `caprigenus` used instead of `caprigenorum`".
   False: it is an adjective (acc. neut. sing.) agreeing with `pecus`. Note rewritten.
2. Unit 4 `l`: "a flock of goat-born ones" took `caprigenum` as a noun. Now "a goat-born flock".
3. Unit 39 (3.288) `l` was the Latin inscription copied in capitals. Now a word-for-word English line.
4. Unit 43 `l`: "Pyrrhus, grandson of Aeacus" — wrong (Pyrrhus is Aeacus's great-grandson; `Aeacidae` is "descendant"),
   and disagreed with `i`. Now "descendant of Aeacus" in both.
5. 3.218 `ora fame` (half-line) — scanner UNRESOLVED; hand entry added.
6. 3.270 `Iam medio adparet…` — scanner UNRESOLVED (appareo has long a, medio elides, Zacynthos Za-cyn-thos);
   hand entry added.
7. 3.271 `Dulichiumque Sameque…` — scanned by hand because the unit of 270–271 got no sc.
8. 3.288 `AENEAS HAEC DE DANAIS VICTORIBVS ARMA` — scanner read V as a consonant (VICTORIBVS as three
   syllables) and split AE-; hand entry added (14 syllables).

## Medium (31) — text (21)

- Unit 1: `metu` ("through fear") omitted in `l` and `i`, and unexplained in the note; `l` syntax repaired ("the
  Strophades, stand named"); `i` "the Greeks gave them their name" went beyond `Graio nomine dictae`; note called
  `Graio nomine` an "ablative of description" (it is the ablative of the name by which they are called) and gave
  an unverifiable etymology (removed). [4]
- Unit 2 note: "The sentence is not finished" — false, the print stops at `undis.`; unit 3 note: "The sentence
  begun at 214 is completed here" — same error. Both rewritten. [2]
- Unit 3 `l`: "Maidens' faces the birds' have" was garbled. [1]
- Unit 6 note: the double `-que… -que` is on `exstruimus` and `dapibus`, not "across the two verbs"; "seats of
  turf" unverifiable. [1]
- Unit 8 note: called the position of `inter` anastrophe (a preposition after its own noun). The order is
  interlaced (`taetrum` of `odorem`, `dira` of `vox`). [1]
- Unit 9 `i`: "we go to a deep recess" added a verb of motion (`in secessu` is location) and doubled "Next/once
  more/again". [1]
- Unit 11 note: "puts `bellum` after `gente`" — false; `bellum` stands before `gente`. [1]
- Unit 23 `l` and `i` added "me" as the object of `iubent` (the Latin leaves it open); the note said "(us)". [2]
- Unit 38 note: garbled ("a comma;is kept") and did not open with the print's reading (rule 5b); also asserted
  that the doorposts are Apollo's temple's and that Abas was a Greek whose arms Aeneas took — neither is in
  the Latin. [2]
- Unit 42 note: `Phaeacum` called "-um for -orum again". False; Phaeaces is third declension, `Phaeacum` is
  its regular genitive plural. [1]
- Unit 45 note: "Andromache has named a little stream" — not stated in these lines. [1]
- Echoes of a known version rephrased in `i`: unit 2 ("rose from the waters of the Styx"), unit 18 (the "what the
  Father told Phoebus, Phoebus told me, and I, the greatest of the Furies, tell you" shape), unit 36 ("a joy
  to have escaped so many Greek cities"), unit 44 ("my heart burned with a strange longing to speak to the
  man and find out"). [4]

## Medium (31) — scansion (10)

All entries are in `scan-fixes.json` with a reason. The scanner treats every open interior syllable as free, so
it returned valid hexameters with wrong quantities; each of these was re-fitted on the lexical quantities.

- 3.212, 3.226, 3.249: `Harpyiae/Harpyias` is four syllables Har-pў-ĭ-ae/as (Greek υ short, ι a vowel), not
  Har-py-iae with a long py-. Same fix for the same name three times.
- 3.248: `Laomedontiadae` is Lā-ŏ-mĕ-don-tĭ-ă-dae (scanner contracted La-o and made me long).
- 3.256: `iniuria` is in-iū-ri-a, i consonantal after the prefix (as 1.27); the scanner read i-ni-u-ri-a.
- 3.272: Ithaca has three short syllables in Greek and the only fit with them needs `Laertia` as
  Lā-ĕr-tĭ-a (diaeresis). The scanner made I- and tha- long.
- 3.277: `ancora` kept short-short; the only fit lengthens the `ra` of `prora` before the consonantal i of
  `iacitur`. The scanner made both the o and the final a of ancora long.
- 3.295: `Helenum` has two short syllables; `Priamiden` can open a hexameter only with Pri- lengthened.
  Scanner had Pria- synizesis, Helenum long-long, -den short.
- 3.302: `Simoentis` is Si-mo-en-tis (four syllables, short Si- and mo-); scanner had a diphthong moen and long Si-.
- 3.303: `Andromache` is An-drŏ-mă-chē and `Manis` has long Mā-; scanner had the reverse.

## Low (48)

45 text changes: `l`/`i` wording (units 0, 2, 8, 11, 22, 26, 29, 30, 32, 37, 38, 42, 43), unverifiable aside removed
(units 0, 1, 4, 9, 12, 15, 19, 31, 38 `about`), pipeline remarks removed (units 27, 29, 35, 39, 41, 42: "needs a
hand scansion", "A short unit, cut at the semicolon" and the like), a typo ("inthe", unit 16), a case slip (unit 30:
`regna` is not in apposition to the genitive `Ithacae`), an unnoted -is accusative (`classis`, unit 45), the half-line
at 218 added to the unit 3 note (precedent aeneid-006/011/013), the closing speech mark no longer repeated in the
`l` of unit 26 (precedent aeneid-004/007/013: it heads the next unit's `t` and is carried in the previous
unit's `l` and `i` only), `about` ("Odysseus's" → "Ulysses'", "Greek city" → "Greek cities", "on a temple door" →
"to the doorposts"). 3 scansion entries: 3.216, 3.217 (scanner's parse right, entered because 218's failure left the
unit without sc), 3.293 (COSTLY flag cleared; scanner right).

## Misprint (rule 5b) — 3.286

Greenough prints `Aere cavo clipeum. magni gestamen Abantis,`: a full stop where a comma is plainly meant (the next
word is lower-case and in apposition). The build and validator require `t` to reproduce the source, so the Latin
stays as printed; the unit keeps lines 286–287 together; the translation reads the comma; the note now opens with
the print's reading. **For `QUESTIONS.md`** (rule 5b: where there is no emend list): Aeneid III.286, the print has a
full stop after `clipeum`, a misprint for a comma; corrected in the translation, `t` left as printed because the
checks require it.

## Speech marks

Celaeno 247–257: `“` opens `t` at 247 (unit 17), `”` closes `t` at 257 (unit 20); `l` and `i` of units 17 and 20 carry them.
Anchises 265–266: `“` opens `t` of unit 25; the print glues the closing mark to the next word (`pios! ”Tum`), so
unit 25 ends at `pios!`, its `l` and `i` carry `”`, and `t` of unit 26 begins `”Tum`; unit 26 `l` and `i` no longer repeat it (done).

## Doubtful quantities (for the owner's QUESTIONS.md; kept on the scanner's fit or on the only fit found)

- 3.209 `Strophadum`: the only fit needs the final -dum long (lengthening at the caesura); scanner's reading kept.
- 3.211 `insulae Ionio in magno`: the scanner's fit has su- long and `Io` as one short syllable; the other fits
  need either `-ae` shortened in hiatus with a long I-, or elided -ae with other changes. Kept on the scanner's fit; not confirmed.
- 3.213 `liquere`: the fit needs li- long (liqui read as līquī).
- 3.257 `absumere` (long su-, sūmo), 3.229 `sub rupe` (short sub- lengthened before br/r-), 3.241/3.262
  `volucres` (long lu-), 3.258 `ablata` (a- long before bl-): standard lengthenings before muta cum liquida; scanner's fits kept.
- 3.272 (Laërtia with diaeresis), 3.277 (`prora iacitur`, ra long), 3.295 (`Priamiden` with Pri- long) rest on
  the only fit found; 3.212 and 3.226/3.249 assume Phī-nē- and Har-pў-ĭ- (Greek quantities).
- 3.244 `semesam`: sē-mē- (the second e from `edo`, ēsus) is needed.
- 3.253/3.254 `Italiam`: Ī- long (Virgil's usage).

## Refused findings (14) — considered and not changed

1. 3.296 `coniugio Aeacidae`: scanner parse is right (con-iu-gi(o) | Ae-ă-cĭ-dae …); no entry.
2. 3.291 `aërias`: scanner's a-ë-ri-as is right (āĕr-); no entry.
3. 3.294 `incredibilis`: scanner right (Hic long, -cre- long, -bi- short); no entry.
4. 3.273 `Ulixi` (short U-, long -lix-, as 2.164): scanner right.
5. 3.274 `Leucatae` (eu diphthong): scanner right.
6. 3.213 `domus`, 3.238 `delapsae`, 3.264 `indicit`, 3.278 `insperata`: no consonantal i or hiatus in these
   words; scanner right (3.213 stands on the doubtful li- below).
7. 3.286 `Aere`, 3.240 `aere`: ae is the diphthong of `aes`; scanner right.
8. 3.230 Latin Library `clausam` vs `clausi`: not noted (the sense is unaffected, `clausam` is its own error).
9. Unit 13 note (Misenus buried at Cumae in Book 6): true; kept.
10. Unit 17 note (Laomedon's broken faith): supported by Aen. 4.542 (`Laomedonteae periuria Troiae`); kept.
11. Unit 34 note (Actium, the Augustan Actian games): known from Conington; kept.
12. Unit 45 `cum… libabat` (inverted `cum` with the indicative) and unit 10 `ore` (singular for plural): labels true; kept.
13. Unit 14 `foedare` ("wound" in `i`, "defile" in `l`): both are in L&S for `foedo ferro`; kept.
14. `i` of units 10, 33, 41, 46: wording shared with Latin-forced phrases only; no distinctive echo found.

## Notes for the build

`python3 build_aeneid.py aeneid-019` was not run (no `gloss.json` yet). The scanner plus `scan-fixes.json` was
simulated for the 97 lines: no line without sc, no bad foot pattern (the units of 216–218 and 270–271, which the
scanner leaves without sc, are covered by the entries for 216, 217, 218, 270, 271).
