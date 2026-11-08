# aeneid-024 review (IV.1–104) — adversarial reviewer

Two passes. Pass 1: all 58 units read against the Latin word by word (every grammatical label in `n`, `l` against the Latin order,
`i` against `l`, speech marks, `p` flags, Latin Library notes, every line cite in a note checked against the packet). All 104 lines
scanned by hand against the scanner, first for the packet's flags (4.36, 4.44), then for Greek `eu`, initial `Ae-`, consonantal `i`
after a prefix or at a word start (Iarbas, Iunone, Iovis, iugalia), hiatus and half-lines, and then, syllable by syllable, every open
syllable the scanner made long and every open syllable it made short (the scanner leaves open vowels free at cost 0.0, so a cost-0.0
line can still carry wrong lengths; six such lines were found: 4.1, 4.8, 4.66, 4.69, 4.81, 4.91). Pass 2: the edited units re-read for `l` <-> `i` agreement,
remembered English (the IV.23 set piece first) and note length.
`t` was not touched: after the edit it was checked by script against the original `units.json` (all 58 `t` strings, `ln`, `p`, `v`
identical; `l` has the same number of lines as `t` in every unit; `i` has no line breaks). `units.json` was edited by script only.
`draft.py` was NOT edited, so `make_units.py` would now overwrite these edits: regenerate nothing from `draft.py` without porting them.
Reference works only (Lewis & Short, Allen & Greenough, Conington); no modern translation consulted.

**The build was run once, and it wrote outputs** (it was not refusing: `gloss.json` had appeared in the draft folder, so it ran to the
end). It wrote `/home/user/Lectorium/aeneid-024.json`, `/home/user/Lectorium/aeneid-glossary.json` (218 forms added, 14 broadened) and
`/home/user/Lectorium/stories.json` (one manifest entry). That was before the `l`/`i`/`n` edits below, so the built file is stale
and must be rebuilt (`python3 build_aeneid.py aeneid-024` is idempotent). I tried to revert the three files and the revert was blocked,
so they are left as written. With the 13 new scansion entries the build printed `scanner report: none` and
`python3 validate_aeneid.py aeneid-024` printed PASS (58 units, 104 lines).

## Counts

| | major | medium | low | total |
|---|---|---|---|---|
| text (`l`, `i`, `n`, `about`) | 2 | 15 | 22 | 39 |
| scansion (`scan-fixes.json`, 13 entries) | 9 | 3 | 1 | 13 |
| **all changes** | **11** | **18** | **23** | **52** |

Severity as in 023: major = a false grammatical label or false statement of the construction, or a line the build cannot scan or
scans with a wrong syllable count; medium = a mislabel that does not mislead the reading, an invented or unverifiable claim that moves
the sense, a wrong reading in `l`, a possible echo of a known version, wrong vowel lengths; low = wording, unverifiable asides,
Latin Library notes, meta remarks. Refused findings: 17 (below).

## `p` flags and speech marks

- `p: true` is on exactly the six units that start at a paragraph line: 1 (U0), 6 (U3), 31 (U18), 54 (U32), 65 (U36), 90 (U49).
  Paragraph lines per the packet: 1, 6, 31, 54, 65, 90. U19 starts mid-line 31 and rightly has none. No change.
- Speech: Dido 9–29: “ opens U4 (9), ” closes U16 (29). Anna 31–53: “ opens U19, ” closes U31. Juno 93–104: “ opens U50, ” closes U57.
  `t`, `l` and `i` each carry 3 opening and 3 closing marks, in the same units. Nothing printed inside the speeches, nothing at the
  narration (U17, U18, U32–U49). No change.

## Scansion (13 entries added to `scan-fixes.json`, keys 4.1 … 4.91)

Major (9; wrong syllable count or no scan):
1. **4.6** `Phoebea`: scanner split oe (Pho-e-be-a), 15 syllables. Right: Phoe-bē-ā, 14. Entry added.
2. **4.44** `germanique minas?` (packet: UNRESOLVED): a half-line. Entry added (feet 1–3, one ×); reason begins "Half-line".
3. **4.43** `Quid bella Tyro surgentia dicam,`: carrier. 44 is in the same unit, so without a hand entry for 43 the unit gets no `sc` and the
   tokens of 43 stay empty. The scanner's own fit for the whole line (cost 0.0), checked by hand.
4. **4.48** `coniugio tali! Teucrum`: scanner read co-ni-u-gio and Te-u-crum (cost 1.5), 16 syllables. Right: con-iu-gi-o and Teu-crum, 15.
5. **4.52** `hiemps et aquosus Orion`: scanner (cost 1.8) made `et` long, `a-` long, `quo` short and `-rion` one syllable.
   Right: hĭ-emps ĕt ă-quō-sus Ŏ-rī-on. Entry added.
6. **4.69** `coniecta`: scanner read co-ni-ec-ta (vowel i), 15 syllables. Right: con-iec-ta, 14. The line scans only with the final `-ta`
   of `coniecta` in a long place (foot 4); said so in the reason.
7. **4.74** `Aenean`: scanner split Ae- (A-e-ne-an, cost 1.2). Right: Ae-nē-an. Entry added.
8. **4.81** `suadentque`: scanner read su-a as two shorts, 17 syllables. Right: suā- one long syllable (as 2.9, 3.363), 16.
9. **4.91** `coniunx`: scanner read co-ni-unx. Right: con-iunx (as 2.711, 2.783); `Iovis` has consonantal I. Entry added.

Medium (3; right count, wrong vowel lengths):
10. **4.1** `regina`: scanner re⏑ gi⏑ and gra long. Right: rēgīna, grăvī: At rē | gī-nă-gră | vī iām | dū-dum | sau-ci-ă | cū-ră.
11. **4.8** `unanimam adloquitur`: scanner u short, na long, a-dlo-qui-tur with lo and qui long, `sic` short. Right: cum sīc | ū-nă-nĭ(mam) | ad-lŏ-quĭ |
    tur mă-lĕ | sā-nă-sŏ | rō-rem.
12. **4.66** `quid delubra iuvant? Est mollis`: scanner de, lu short and bra, iu long. Right: dēlūbra, iŭvant: quid dē | lū-bră-iŭ | vant Est | ...

Low (1):
13. **4.36** (packet: COSTLY 2.3): scanner's fit is right, confirmed syllable by syllable (Libyae three syllables; Iarbas Iar-bas with
    consonantal I; `-tus` long by position before it). Entered so the reading is on record, as 2.201 was.

Checked and found right as the scanner has them (no entry): 4.18 `pertaesum` (per-tae-sum), 4.20 `Anna fatebor` (fatēbor, Sychaei Sy-chae-i),
4.21 `coniugis` (con-iu-gis, already consonantal), 4.45 `Iunone` (Iu- with consonantal I; `et` long before it), 4.46 `Iliacas` (vowel Ī, and
`cursum` elides into it; this is the right reading of Ilium), 4.59 `Iunoni … iugalia`, 4.83 `illum absens`, 4.96 `veritam te`, 4.99 `aeternam`
(ae one diphthong), 4.13 and 4.65 `heu`. Hiatus: none in the part (`duorum est` 4.95 is prodelision, rightly handled).

## Major (2, text)

1. U2 (4.4–5) `infixi`: "agrees with them" (`voltus` and `verba`). `infixi` is masculine, so it agrees with `voltus` only and serves `verba`
   by sense. Corrected; `pectore` (ablative of place) added.
2. U19 (4.32) `carpere`: "the infinitive in a question of protest". The metre will not take an infinitive: the fifth foot `pe-re-iu`
   needs a long `pe`, and the infinitive has a short one. It is the second person singular passive (= `carperis`), "will you be worn away",
   as `carpitur` at line 2. Note rewritten; `l` and `i` made passive.

## Medium (15, text)

1. U3 (4.8) `unanimam`: "the first word of the book to show how close the sisters are" (unverifiable). Removed; `polo` (ablative of separation) added.
2. U5 (4.10) `hospes`: "the word that is always used of Aeneas in this book" (unverifiable). Removed.
3. U10 (4.17) `l` "by death has deceived, cheated me" garbled the order of `deceptam … fefellit`. Now "me deceived, by death has cheated".
4. U10 `i` dropped `vellem` ("that I would join myself") and "left me cheated" did not match `deceptam fefellit`. Rewritten.
5. U13 (4.23) the set piece. `l` "I acknowledge the spoor of an old flame" (spoor is not the plain word) and `i` "I know the marks that an old fire left on me"
   (kept "marks" and "old fire" from the best-known versions, as the drafter feared). New `l` "I recognise the footprints of an old flame";
   new `i` "I know again the tracks of a fire that once burned in me". `new-renderings.md` updated. The final decision is the owner's.
6. U19 `i` "dearer to me than the light of day" and "the gifts of Venus" sit close to known versions; rephrased as part of the passive rewrite.
7. U25 (4.41) `i` "harbourless Syrtis" for `inhospita` (and `l` "inhospitable"). Now "inhospitable".
8. U35 (4.61) `media inter cornua`: "`inter` placed after its noun". It stands between the adjective and the noun. Corrected.
9. U35 (4.63) `instaurat diem` (flagged): "she begins the day again with fresh gifts" stated one reading as fact. Now "renews the day with gifts,
   most likely that she keeps the day's worship going with fresh offerings".
10. U36 (4.65) `vatum ignarae mentes`: "`ignarae` takes the genitive" as the only construction, and `i` "blind to what the seers know". Both
    readings are possible ("the ignorant minds of seers" / "minds ignorant of seers"); `n` now says so and uses the first; `l` made neutral
    ("Alas, of seers the ignorant minds!"); `i` "Alas, how blind are the minds of seers!".
11. U45 (4.82–83) `l` gave both "absent"s to the wrong words (`absens` = she, `absentem` = him). Now "she lies, absent herself, him absent both hears and sees".
12. U45 (`stratis relictis`, flagged) `i`/`n` "the couch he left": an unverifiable reading. Now "the deserted couch", `relictis` = left empty, and
    `incubat` + dative stated; `i` ends "each of them absent from the other".
13. U47 (4.86–87) `parant`: "plural, with 'they' (the Carthaginians) as its subject". The subject is `iuventus` read as a plural (singular `exercet`,
    plural `parant`). Corrected, with `tuta bello` "in war or for war"; `i` "no one prepares" now "nor do they make ready".
14. U49 (4.91) "`cara` is ironic" (unverifiable). Removed.
15. U53 (4.99) `i` "the marriage already agreed" invented an agreement; `pactos` = pledged. Now "a pledged marriage".

## Low (22, text)

`about`: "sworn" (the text says only that the resolve is fixed) and the garbled sentence about Anna's argument (2). U13 `n` wording
(2: "recognise", "the footprints look ahead to the hunted doe"). U14 `n`: the Latin Library `Erebo` given a case and a sense it cannot be shown
to carry; the garbled "which are present in Greenough's text" (2). U20: `cinerem` is singular (`l` "ash"), the accusative-and-infinitive
construction not stated, "sarcasm" asserted (2). U22 `Libyae`/`Tyro` case labels (1). U27 `i` "the war" vs plural `bella` (1). U31: Orion "setting"
(unverifiable), and `i` "weave pretexts for delay" (possible echo) (2). U38 `Est` (flagged): the reading as `edo` is the usual one and was kept; wording
made exact ("contracted present of `edo`, the same as `edit`") (1). U40 `Dictaeos` "agrees with both" (`silvas` is feminine) (1). U41 `i` "the deadly shaft sticks fast in her
side" (possible echo) (1). U42 "a form Virgil likes for Greek names" (unverifiable) (1). U45 `l` "presses out" (premit) and the garbled
"paradox" sentence (2). U46 imprecise "the subjunctive expresses her hope" (1). U50 `i` close to known versions (1). U53 `n`
unverifiable gloss on Juno's motive (1). U55 `i` "run through her very bones" (possible echo) (1).

## Refused findings (17)

1. 4.67 `Est mollis flamma medullas` (flagged edit): the reading `est` = `edit` is the usual one, kept; only the wording was tightened (low, above).
2. U0 "whom the reader last saw at the end of Book I falling in love": true (I.749), kept.
3. U7 "since he shows no fear, he cannot be of base stock": an inference, but the drafter says so and it follows the argument; kept.
4. U8 "the word echoes the poem's own opening … `iactatus`": true (I.3), kept.
5. All line cites in the notes (95, 2, 69–73, 56, 27, 68–69, 44, and the speech ranges 29/53/104): checked against the packet, all correct. Kept.
6. U31 `desaevit` "present indicative with `dum`": an alternative (perfect, "until it has raged itself out") exists, but the short `-vit`
   that the metre needs makes it a present. Kept.
7. U32 Latin Library `impenso … flammauit` note: matches the packet's two disagreements; the sense comparison is fair. Kept.
8. U12 "murdered … at the altar (Book I)" and "spattered with blood because the murder was done at the altar": Book I tells it; kept.
9. U13 `agnosco` "compound of `ad` and `gnosco`": true. Kept.
10. 4.64 `pectoribus inhians`: the scanner's fit needs `bus` long before `in-` (a short syllable in the long place of foot 2). It is the only
    fit; left as the scanner has it (doubtful, below), no entry.
11. 4.75 `Sidoniasque`: the scanner's Sīdŏniās (do short) is a valid fit and Sidonius has both quantities in Virgil; left.
12. 4.22 `hic` short before `in-` and 4.50 `sacris` with `sa-` long by position before `cr`: both valid fits; left.
13. U34 `bidentis` "a sheep of two years": standard; kept.
14. U49 "`Saturnia` … Saturn was her father": true; kept.
15. U50 "Cupid, who disguised himself as Ascanius in Book I": true; kept.
16. U27 "line 44 … one of the unfinished half-lines": true, and the sense is complete at the break; kept (the scansion entry says the same).
17. Latin Library notes for 4.2, 4.4, 4.67 (`volnus`/`uulnus`, `voltus`), 4.29 `sepulchro`: orthography only; the notes mention them only briefly.

## Doubtful (not changed)

- 4.64 `bus` long in the arsis; 4.69 `-ta` of `coniecta` long in the arsis (entered, with reason); 4.75 `do` of `Sidonias`; 4.22 `hic`.
- 4.8 `sīc` long in the first foot: forced by the metre (`cum sic | ūnanimam`), but I could not check it against a reference work here.
- `draft.py` is stale (see above).
