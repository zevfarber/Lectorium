# aeneid-027 (IV.305–407): reviewer's record

I made two passes. (1) I checked every grammatical label against its form and its line. (2) I checked the Latin against `l`
word by word, `l` against `i`, the line division of `l` against `t`, `i` for echoes of remembered English versions, and the
speech marks. For scansion I read all 103 lines by hand against the scanner's printout, not only the flagged ones.
`units.json` was edited by script; the script asserted that `t`, `ln`, `p` and `v` are unchanged, and the tiling is the same.
`draft.py` was then regenerated from `units.json`, and `make_units.py` run from it reproduces `units.json` byte for byte. No
modern translation was consulted.

Counts: units/notes **major 1, medium 6, low 12**; scansion **major 2, medium 8, low 1**.
Overall **major 3, medium 14, low 13**.

## Cut at 318 (`et istam—`): kept
`build_aeneid.py` line 35 accepts a unit whose `t` ends in a dash (`… and not t.endswith('—')`), and `aeneid_lib.cut` finds
`istam—` on line 318. The published parts already end units like this (aeneid-001 `Argis—`, aeneid-003, aeneid-004). I tested
by running the build's own tiling and scansion code up to the glossary step (not the full build, so no file was written). It
passes with no errors. The dash marks Dido breaking off before the parenthesis `oro, si quis adhuc precibus locus`, so the cut
stays.

## Speech marks (checked, no change needed)
“ opens unit 0 (305, Dido), unit 16 (333, Aeneas, mid-line after `Tandem pauca refert:`) and unit 32 (365, Dido).
” closes unit 12 (330), unit 30 (361) and unit 50 (387). `l` and `i` carry the same marks on the same units.

## Units: major
- **16 (333–335) `l`, `n`.** `l` read “I you, **who** very many things by speaking to list are able”. That makes `quae` refer
  to Dido. `quae` is neuter plural: the services she can list, which are the object of `promeritam`. `l` now reads “I you,
  things which, very many, by speaking / you are able to list, never, queen, will deny / to have deserved;”. The note now
  says outright that `quae` is neuter plural, not “who”.

## Units: medium
- **1 (307–308) `n`.** “one singular verb, `tenet`, held to the end” was false: `tenet` stands mid-line in 308. Corrected.
  Also removed “this is the first time Dido openly speaks of her death” (it can't be checked, and IV.24–27 already has her
  wishing for death). Cut “as if she were someone else's grief” (embellishment).
- **4 (314–318) `n`.** The note said “the personal pronouns `ego… te` are tucked between `per` and its noun”. Only `ego` is;
  `te` follows `tuam` and is the object of `oro`. Rewritten.
- **12 (327–330) `n`/`l`/`i`.** The note glossed `suscepta fuisset` “had been acknowledged”, `l` has “received” and `i`
  “had a child”. The note now gives “had been received”, with `suscipere` used of having a child (literally, taking up a
  newborn as one's own), which agrees with both layers.
- **32 (365–367) `n`.** `l` and the note attached `duris cautibus` to `genuit` (“on hard crags”). `i` attached it to `horrens`
  (“rough with jagged rocks”). The note now gives both constructions and says which layer follows which. The Iliad citation
  “(16.33–35)” became “(Book 16)”. The content (Patroclus telling Achilles his parents were the sea and the cliffs, not Peleus
  and Thetis) is certain, but the exact line numbers are from memory and so are not printed.
- **2 (309–311) `i`.** The Latin is a question (`crudelis?`) and `i` was an exclamation. Now “What, are you even fitting out
  your fleet under a winter sky, and hurrying to put to sea with the north winds at their height, cruel man?”. This also
  drops “in the teeth of”, and “with the north winds at their height” agrees with the note.
- **3 (311–314) `i`.** Greenough has `sed Troia antiqua maneret`, “but”, which `l` keeps; `i` had “and”. Now “but ancient
  Troy still stood”. (The Latin Library reads `et` here; Greenough is the text.)

## Units: low
- 0 `n`: “`tantum… nefas` frames the end of one line and the start of the next” → “is split across the line-end, with `posse`
  between”.
- 7 `i`: `fama prior` had lost “former” (“that good name of mine”) → “the good name I once had”.
- 9 `i`: started lowercase (“since this…”) although the Latin starts a new sentence (`Hoc`); now “Since that is the only name
  now left of a husband.”
- 12 `i`: “who would still bring back your face to me, I should not feel myself so utterly taken and forsaken” →
  “who in spite of all would bring you back to me in his face, I would not seem so wholly a captive and abandoned”. This
  keeps `tamen`, `te … ore` and `viderer` as “seem”, and drops a rhyming pair that may echo a remembered version.
- 30 `i`: “I do not seek Italy of my own free will” is close to the standard English wording of a famous line. Now “It is not
  by my own choice that I make for Italy.”
- 31 `i`: “glaring”, which is not in `tuetur`, → “watching”.
- 42 `i`: “the Furies have set me on fire” committed to the personified Furies, where the note leaves `furiis` open → “I am on
  fire with frenzy, and swept away!”
- 51 `n`: “`medium… sermonem` frames the line” (it frames `dictis` only) → “is split by `dictis`”.
- 51 `i`: “left him hesitating in his fear over much that he was ready to say” misread the two `multa` → “leaving him
  hesitating long in fear, with much that he was making ready to say”.
- 54 `n`: “`celsas… naves` frames the next line” (`naves` stands mid-398) → “is split across the line-end”.
- 55 `n`: “The line is another half-line” (the unit has two lines) → “Line 400 is another half-line”.
- 4 `n`: “`meum` is a neuter adjective used as a noun” → “`quicquam… meum`, ‘anything of mine’, with `dulce` as predicate”.

## Scansion (hand-scanned; added to `scan-fixes.json`)
All 103 lines were scanned by hand. These lines are correct as the scanner reads them and get no entry: every line not in
the table below. Notable among them:
- 4.338 (COSTLY 2.1): spē-rā | vī nē | fīn-gĕ fŭ | gām nēc | cōn-iŭ-gĭs | ūm-quam, with consonantal i in `coniugis`.
- 4.345 (COSTLY 2.0): Sēd nūnc | Ī-tă-lĭ | ām māg | nām Grȳ | nē-ŭs Ă | pōllo. `Grynēus` has three syllables, the ē for
  Greek ει; this is the only fit.
- 4.373: `Eiectum` = Ē-iec-tum, consonantal i after the prefix, read correctly.
- 4.323: `cui` is one syllable. 4.336: `mei` has two syllables. 4.343 aside, `Priami` and `Troia`/`Troianam` (consonantal i)
  are right.
- 4.376: `Heu` is one syllable. 4.368: `maiora` has long `mai-`. 4.316: `cō-nū-bĭ-a`.

Added (11):

| line | problem | fix |
|---|---|---|
| 4.324 | `coniuge` read co-ni-u-ge, `de` and `co` short (COSTLY 2.0) | con-iŭ-gĕ, consonantal i; S S D S D |
| 4.326 | `Iarbas` consonantal, spondaic fifth foot `tū-lūs` (COSTLY 2.0) | Ĭ-ar-bas, three syllables (as 4.196); `Gaetūlŭs Ĭ` dactyl |
| 4.329 | `Ae-` split (cost 1.8) | Ae-nē-ās |
| 4.343 | synizesis `reliqu-ias` (cost 0.0, unflagged) | rē-lĭ-quĭ-ās, as 1.30, 1.598, 3.87; 16 syllables |
| 4.349 | `Te-u-cros` split (cost 0.0, unflagged) | Teu-crōs |
| 4.354 | `i-ni-u-ri-a` five syllables (cost 0.6) | in-iū-rĭ-a, consonantal i after the prefix |
| 4.361 | half-line, UNRESOLVED | `Half-line`: Ī-tă-lĭ \| am nōn \| spon-tĕ sĕ \| quor× (3½ feet) |
| 4.393 | `Ae-` split (cost 1.2) | Ae-nē-ās |
| 4.397 | `Te-u-cri` split (cost 0.0, unflagged) | Teu-cr(i) elided into `incumbunt`; four spondees |
| 4.399 | correct, but its unit runs into the half-line 400, and the build gives no `sc` to a unit with an unresolved line | carrier entry, scanner's own fit |
| 4.400 | half-line, UNRESOLVED | `Half-line`: in-fă-brĭ \| cā-tă fŭ \| gae stŭ-dĭ \| ō× (3½ feet) |

Severity: 4.361 and 4.400 are major (without them the build refuses: UNRESOLVED). 4.324, 4.326, 4.329, 4.343, 4.349, 4.354,
4.393 and 4.397 are medium (wrong syllabification or quantities). 4.399 is low (a carrier entry).

Checked: every entry matches the words of its line. The two `Half-line` entries pass the validator's half-line test (feet
numbered 1..4, one ×). The nine full lines pass its six-foot pattern test. Running the build's own tiling and scansion code
on the reviewed `units.json` gives “hand scansions applied” for all 11, no UNRESOLVED, and the validator's scansion check
passes on all 103 lines. The only COSTLY lines left in the report are 4.338 and 4.345, both confirmed above.

## Refused / left as drafted
- **379–380 Epicurean remark (unit 44): kept.** The picture of gods untroubled by human affairs is plainly Epicurean
  doctrine, and the old commentators read Dido's `Scilicet … quietos sollicitat` that way. The note says no more than that.
- **Iliad reference (unit 32): kept, without line numbers** (see medium).
- **29 (360) `l`:** “Cease both me with your and yourself to inflame complaints” does not follow the Latin order exactly
  (`incendere` precedes `teque`). A strictly literal order (“with your to inflame and yourself complaints”) is less readable,
  and coherence wins ties. Left.
- **50 (387) `l`:** “this to the Shades … beneath the lowest” splits `sub imos Manis` as the Latin does. Left.
- **11 (326) `n`:** “she fled Tyre with his treasure”. In Book I the treasure is Sychaeus's hidden gold, called Pygmalion's
  wealth (`Pygmalionis opes`). “his” is ambiguous but not false. Left.
- **31 `i`** keeps past tenses for the historic presents (`tuetur`, `profatur`), which is ordinary English narrative. Left.
- **Latin Library variants** (309 `moliri`, 312 `et`): neither changes the sense enough to note. The drafter did not note
  them. Left.
- **No modern-translator names** appear in any `n`, `l` or `i`.

## Outside this part (for the owner)
- **4.36 in `scan-fixes.json`** (published, aeneid-024) still scans `Iarbas` with a consonantal I and a spondaic fifth foot.
  4.196 (aeneid-025) already reads the vowel I and says so, and 4.326 here does the same. Three line-ends all spondaic would
  be implausible in Virgil. 4.36 should probably be re-entered as `pēc-tŭs Ĭ | ar-bas` and aeneid-024 rebuilt. I did not
  touch it: it is outside this part.
