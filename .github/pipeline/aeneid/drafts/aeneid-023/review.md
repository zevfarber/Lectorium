# aeneid-023 review (III.613–718) — adversarial reviewer

Two passes. Pass 1: all 56 units read against the Latin word by word (grammar labels, cross-references, `l`, `i`, `n`, `about`, speech
marks, `p` flags, Latin Library notes); all 106 lines scanned by hand against the scanner's output, first for the packet's flags
(637, 640, 661, 680, 694), then for Greek `eu`, initial `Ae-`, consonantal `i` and hiatus, and then, syllable by syllable, every
open syllable the scanner made long (the scanner leaves open vowels free at cost 0.0, so a cost-0.0 line can still carry wrong
lengths). Pass 2: the edited units were re-read for `l` <-> `i` agreement, remembered English and note length (which led to
the U1 phrase, a second rewrite of U19 `i`, and the U13 `i`).
`t` was not touched: after every run it was checked by script against the original `units.json` (the 56 `t` strings, `ln`, `p`, `v`
identical). `draft.py` was edited by script (only `l`, `i`, `n` and the part `about`) and `units.json` regenerated with `make_units.py`.
Nothing built, validated against a built file, committed or pushed (`gloss.json` does not exist yet). Reference works only (Lewis &
Short, Allen & Greenough, Conington); no modern translation consulted.

## Counts

| | major | medium | low | total |
|---|---|---|---|---|
| text (`l`, `i`, `n`, `about`) | 13 | 19 | 47 | 79 |
| scansion (`scan-fixes.json`, 6 entries) | 3 | 3 | 0 | 6 |
| **all changes** | **16** | **22** | **47** | **85** |

Severity as in 022: major = a false grammatical label or false statement of the construction, or a line the build cannot scan or
scans with a wrong syllable count; medium = a mislabel that does not mislead the reading, an invented or unverifiable claim that
moves the sense, a wrong reading in `l`, a possible echo of a known version, wrong vowel lengths; low = wording, unverifiable asides,
Latin Library notes on orthography/morphology, meta remarks. Refused findings: 21 (below).

## `p` flags and speech marks (the drafter's worry)

- `p: true` is present on exactly the six units starting at a paragraph line: 613 (U0), 655 (U20), 675 (U29), 692 (U39), 707 (U48),
  716 (U54). Checked against the source (`lines_of`: paragraph lines 613, 655, 675, 692, 707, 716) and against `units.json`. Nothing
  was missing or mislabelled; no change. No other unit has `p`.
- Speech: the source carries “ at 613 and ” at 654 only. “ opens U0 (its first character), ” closes U19 (after `leto.`, no punctuation
  printed outside it). `t`, `l` and `i` each have 1 opening and 1 closing mark (validator warning not expected). Nothing odd in the
  print: no inner quotation marks, nothing at the Aeneas narration from 655 on. Anchises is addressed at 710–711 without marks in
  Greenough, and stays so.

## Major (16)

Text (13):
1. U3 (619–621) `terris` "a dative of separation, or 'from the lands'" (the second half is not a case label at all). A dative of
   reference/disadvantage with `avertite`, "away from the lands". Rewritten; also `Di` called "vocative" only (nominative or vocative).
2. U5 `duo` "the old nominative/accusative form". False: `duo` is the ordinary accusative here (object of `frangeret`). Rewritten.
3. U20 `Polyphemum` "a Greek accusative". False: ordinary Latin accusative. Removed. (Also `cum` placed after `summo` explained;
   `cui lumen ademptum` correctly a relative clause; the vague "exclamatory description in apposition" removed.)
4. U22 `solamen` "the second subject". False: `ea… voluptas solamenque` has one subject (`ea`); `voluptas` and `solamen` are predicate
   nouns. Rewritten.
5. U23 `Postquam` takes "the perfect indicative (`tetigit`, `venit`, `lavit`)". `lavit` cannot be perfect: the metre needs short
   a (dum la vit), so it is the present of `lavo`; `l` "he washed" -> "he washes" (`i` already present).
6. U28 `quo` "a connecting relative". False: an ordinary relative pronoun inside the sentence (ablative of cause). Corrected; the garbled
   `immugiit` sentence ("the verb of a bull, an animal for a giant's roar") rewritten.
7. U29 `Cyclopum` "the old genitive plural (compare `superum`)". False: the ordinary third-declension genitive plural of `Cyclops`.
   Added that `e` governs `montibus altis` too.
8. U30 `concilium horrendum` "an apposition to the whole sight". False: in apposition to `fratres`. Corrected.
9. U31 `cyparissi` "the Greek nominative plural". False: a second-declension feminine, ordinary nominative plural. Corrected.
10. U36 `Megaros` "a Greek accusative plural". False: `-os` is the ordinary Latin accusative plural of the adjective, agreeing with
    `sinus` (accusative plural). Corrected; `l`/`i` "bay/gulf" -> "bays" (low, below).
11. U39 `contra` "follows its noun". False: `contra` precedes `Plemyrium` ("preposition with the accusative"). Corrected.
12. U41 `Alpheum` "a Greek accusative". False: ordinary Latin accusative. Removed; `Siculis undis` "a dative" hedged ("dative (or
    ablative)"); `qui` as a "connecting relative" replaced by "a relative pronoun referring to `Alpheum`".
13. U45 `Geloi` "a Greek genitive of the river-name Gelous". False reading: `Geloi` is the adjective "Geloan", nominative plural with
    `campi`. Corrected; `l` "the fields of Gelous" -> "the Geloan fields" and `i` likewise.

Scansion (3, `scan-fixes.json`):
14. 3.640 `rumpite.` (packet: UNRESOLVED) is one of Virgil's half-lines. Hand entry added (reason begins "Half-line"; feet 1 only, one ×).
15. 3.661 `solamenque mali.` (packet: UNRESOLVED) likewise a half-line; entry added (feet 1–3, one ×). U22's note now says so.
16. 3.716 `Aeneas`: scanner split Ae- (A-e-ne-as, cost 1.2). Right: Ae-nē-ās, three syllables (as 1.92, 1.170, 3.97 and the published
    parts). Entry added (Sic pă-tĕr | Aē-nē | ās in | ten-tīs | om-nĭ-bŭs | ū-nus).

## Medium (22)

Text (19):
1. U0 `patria` "an ablative of origin, 'I am from Ithaca as my country'": not a standard use; now "ablative of respect, 'Ithacan by country'".
   Also the claim "Poverty… now seems a happier lot" hedged; "Odyssey 9 where no Greek is left behind" made exact ("Ulysses' surviving
   men all get away").
2. U6 `l` "and the warm quivered under his teeth the joints" took `tepidi` as a noun; now "and quivered, warm, beneath his teeth, the joints".
3. U8 `-ve` "loosely used for 'and… not'": it continues the negative of `nec` ("nor… or"). Corrected.
4. U9 `n` `cruento` "which is itself bloody, from the men he had drunk with": invented. Replaced by the plain construction (the line break
   separates `cruento` from `mero`).
5. U9 `l` broke the line between `scraps` and `with bloody`; `cruento` belongs to Latin line 3. Now "scraps with bloody / in sleep mingled wine".
6. U13 `i` ("For such as Polyphemus is, great as he is, shutting… a hundred other abominable Cyclopes live…") garbled the comparison; rewritten
   ("A hundred others, as huge and as terrible as the Polyphemus who pens his woolly flocks… and milks them, live in crowds…"). Note rebuilt.
7. U14 `n` "the present tense with `iam` means 'have been dragging', and `cum` simply joins the two facts": `iam` belongs to the first clause;
   rewritten ("`cum` with the present indicative, 'while I drag out'"); "almost three months" -> "the better part of three months".
8. U15 `n` "a mild zeugma in which the boughs and plants stand as givers": no zeugma. Replaced by the plain objects/subject.
9. U16 `i` "Searching the whole coast": `coast` is invented for `omnia`; now "Scanning everything around me".
10. U17 `n` `addixi` "so that he gives himself as one gives over a prisoner" and the claim that the pluperfect "stands for the future
    perfect of his thought": rewritten and hedged.
11. U19 `i` "by whatever death you please" was a close echo of familiar versions; now "You, rather, take this life of mine, by whatever death you will."
12. U20 `l` "when from the mountain-top we see": `summo… monte` is "on" the top (Polyphemus appears there; `i` already says "on"). Corrected.
13. U21 `n` `manu` "an ablative of place, 'in his hand'" stated flatly; hedged ("goes with the pine or with `regit`"); Latin Library `manum` kept as a sense-changing
    variant ("changes the construction").
14. U22 `i` "the only pleasure he has left, and the comfort of his misery" (an echo of a familiar rendering); now "the one pleasure left to him, and the relief of his suffering."
15. U26 `n` "the Cyclops feels the ship moving off": invented; now "perceives the Trojans".
16. U27 `n` "the Ionian Sea, which the Trojans crossed after Epirus" and "because the ship moves faster than he can wade": unverifiable. Replaced
    by "the Ionian waters off the east coast of Sicily" and a plain gloss of `aequare sequendo`.
17. U37 `n` `errata` "used with its object like a transitive verb": it is a passive participle of an intransitive verb, used of the ground covered. Corrected.
18. U50 `i` "you, alas, who were rescued in vain from such perils" a close echo of familiar versions; now "delivered from such great perils for no purpose".
19. `about`: "driving his sheep, his only comfort, down to the sea": the Latin says the sheep accompany him (`comitantur`); now "his sheep, his only
    comfort, following him down to the sea".

Scansion (3, `scan-fixes.json`; the scanner returned a valid hexameter with wrong vowel lengths):
20. 3.644 `Cyclopes`: scanner `Cy⏑ clo⏑ pes– et–` (omega short). Right: Cyclōpes, ō long; Cy long by position; the Greek nominative plural -ĕs short
    (the only natural fit): īn-fān | dī Cȳ | clō-pĕs ĕt | āl-tīs | mōn-tĭ-bŭs | ēr-rānt. Entry notes the one doubtful quantity (pes).
21. 3.656 `pecudes`: scanner `pe– cu– des–` (both short vowels made long). Right: pĕ-cŭ; `vasta` is the ablative with `mole` (vastā), `se` long; ip(sum)in | ter pĕ-cŭ | dēs vās | tā sē | mō-lĕ mŏ | ven-tem.
22. 3.710 `Anchisen… pater`: scanner `An chi⏑ sen⏑` / `pa– ter–`. Right: chi long (as 015, 016, 017, 018) and pa short (as 001, 009, 015): āmit(to) | Ān-chī | sēn hīc | mē pă-tĕr | ŏp-tŭ-mĕ | fēs-sum.

## Low (47) — text only

Latin Library notes on orthography/morphology cut (convention: note a variant only where it changes the sense): U1 (617 `inmemores`/`immemores`),
U13 (643 `uulgo`), U15 (650 `uulsis`), U28 (673 `intremuere`), U30 (677 `astantis`), U32 (682 `praecipitis`), U45 (701 `apparet`, now only the
familiar form given), U46 (703 `maxima`), U50 (710 `optime`), U53 (715 `appulit`, now only the familiar form) (10).
Meta remarks cut ("the dashes have no space after them, so the unit is kept whole"): U0, U3, U11, U22; U7 "a unit of its own because it stands at a semicolon" (5).
Other: U0 `l` "would that that fortune" (1); U0 `i` "that lot" -> "my fortune" (1); U1 `l` "the cruel threshold they leave" misordered the Latin and made `limina` singular (1); U1 `Cyclopis` "Greek genitive" (1); U1 "see
the pilot" (1); U2 `cruentis` hedged "respect or cause" (1); U9 "bent to one side" invented (1); U11 note trimmed from 159 to 137 words and the
Phoebus/moon aside kept short (1); U12 "anaphora" -> "repeated" and the half-line status of 640 stated (2); U16 last sentence of the note (1); U20 "`informe`… as the
giant is shown to the eye" (1); U24 "can also be taken as an adverb" (1); U25 `l` "turn up" (invented) and "with one another in a race" (2); U26 "Notice that" (1);
U30 `lumine` hedged (1); U31 "a sacred wood is made to look more awesome" (1); U32 `quocumque` "fear cares not where" (1); U33 `Contra` "on the other side" -> "on the other hand" (1); U36 `l`
"gulf" -> "bays" and `i` "bay" -> "bays" (2); U37 `retrorsus` "the ships are going back the way he came" (1); U43 "a river that floods and makes marshes" (1); U44 "the oars
almost touch it" (1); U45 oracle reference given as ancient commentators' (1); U47 vocative phrase (1); U53 "since Aeneas does not know which god" (1); U22 note now says 661 is a half-line (1); U19 note last sentence (1); U23 `l` tense (1); `about` "three months" -> "nearly three months" (1). (Where one finding spans `l` and `i`, each layer is counted.)

## Cross-references checked

- Odyssey 9: no Greek is left behind (true); the Cyclops dashes men to the ground (9.289–290), eats them raw leaving nothing, is made drunk and vomits wine and flesh
  (9.371–374), the stake twisted like a shipwright's drill (9.384–386), lots drawn for the four who help (9.331–335), the blinded Cyclops gropes with his hands, hurls rocks
  after the ship, the other Cyclopes come at his cry, they live scattered with no council (9.112–115); the wooded peak simile (9.190–192). All true; kept.
- Odyssey 12 Circe on Scylla and Charybdis: true; kept.
- 1.92/1.170/3.97 and the published Aeneas scansions; 013, 019, 022 `adparet`; 019 `Ionio` (Io short); 021 `Pachyni`, `Pelori`: checked and used as precedent.
- Celaeno as the Harpy of earlier in the book (3.245 ff.): true. Helenus's warnings: true. 714 `haec meta` / 660 `ea` attraction: kept (consistent).
- Servius on Camarina (oracle against draining the marsh): the ancient claim is true; now stated as "as ancient commentators say".

## Hand scansions (6 entries added to `scan-fixes.json`)

3.640 (half-line), 3.644, 3.656, 3.661 (half-line), 3.710, 3.716. Tested without building: the scanner plus all entries leaves no UNRESOLVED line, every entry's
words match its line, every hexameter has six numbered feet, 12–17 syllables, one × and only –⏑⏑ / –– feet (sixth –×), and the two half-lines carry feet 1..k, one ×.
The two half-lines are on lines 640 and 661 of Greenough's print (Virgil's incomplete lines).

## Doubtful quantities (scanner's only fit; no entry, or entered with the doubt stated)

3.642 `claudit` (dit lengthened in thesis before pe-; no natural alternative); 3.617 `socii` (final i long, so-ci-i); 3.644 `Cyclopes` (pes short forced; entered);
3.671 `potis… fluctus` (po long and tus long, the only fit; Io short as in 019 `Ionio`); 3.675 `e silvis` (e long in thesis; the only fit) and 3.676 `portus` (tus long;
the only fit); 3.692 `Sicanio` (Si long in thesis, as published 006 `Sicaniae`); 3.693 `Plemyrium` (Ple long, the only fit); 3.701 `adparet… procul… Geloi` (pa long as
published 013/019/022; pro long and Ge long, the only fit, cost 1.5; `Geloi` two syllables); 3.629 `oblitusve` (tus long by position before -ve); 3.614 `Troiam` (Tro-iam).

## Scanner flags and other checks

- 637 (COSTLY 2.0) Argolici clipei aut Phoebeae lampadis instar: hand-scanned, scanner right (Ar-gŏ-lĭ | cī clĭ-pĕ(i) aut Phoe | bē-ae lam | pă-dĭs ins | tar).
- 680 (COSTLY 2.0) aeriae quercus, aut coniferae cyparissi: hand-scanned, scanner right (ā-ĕ-rĭ | ae quer | cus aut | cō-nĭ-fĕ | rae cў-pă | ris-si).
- 694 (COSTLY 2.3) Ortygiam. Alpheum fama est huc Elidis amnem: hand-scanned, scanner right (Ōr-tў-gĭ(am) | Al-phē | um fā | (ma)est huc | Ē-lĭ-dĭs | am-nem; Alphe-um three syllables).
- Greek `eu`: none in the part (`Alpheum` is Alphē-um, correctly two syllables; `Phoebeae` Phoe-bē-ae). Initial/medial `Ae-`: Achaemenides (614, 691), Aetna (674, 678),
  Aetnaeos, Celaeno (713), aeriae (680), Phoebeae, aequora, Aeneas (716, fixed). Consonantal `i`: Troiam, Iovis (681), iussa/iussi, iacuit/iacet/iacentem, proiecta (699),
  Ionios, Italiae, Dianae, Lilybeia: all right. No hiatus line needing a fix.

## Refused findings (21) — considered and not changed

1. `p` flags on 613, 707: present and correct; no change (see above).
2. Speech marks: complete and correctly placed; no change.
3. Scanner flags 637, 680, 694: scanner right; no entry.
4. 701 `adparet` / `procul` / `Geloi`: kept; published precedent for `adparet`; no natural alternative.
5. 671 `potis` / `fluctus aequare`: kept; no natural alternative; Io short as in 019.
6. 675 `e silvis`, 676 `portus`, 642 `claudit`, 617 `socii`, 693 `Plemyrium`, 692 `Sicanio`: kept (see doubtful list).
7. 629 `oblitusve`: right (tus long before -ve); 624 `magna` (ablative, long a): right; 656 only wrongly lengthened `pe`/`cu`.
8. 658 `lumen ademptum` (no elision of -n): right. 662 `lavit` short a, `venit` long e: right.
9. 673 `contremuere` `-ere` = `-erunt`: flagged in the pilot; note kept (already said "for `contremuerunt`").
10. Latin Library variants kept: 659 `manum`, 685 `utrimque`, 686 `teneam`, 708 `actus` (each changes the sense).
11. U33 (684–686) the indirect-speech subjunctive `teneant`: right; kept.
12. U35 `Ecce autem`, `missus adest`: right; kept.
13. U46 `generator equorum` "famed for its horses": Virgil's own epithet; kept.
14. U40 `nomen… Ortygiam` "in apposition": acceptable; kept.
15. U42 `Iussi` "Aeneas does not say by whom": true; kept.
16. U47 `saxis caecis` "cause or description": defensible; kept.
17. U48, U49, U51, U52, U54, U55 notes: read word by word and true; kept.
18. U4, U10, U18, U34, U38: true; kept.
19. U12 `miseri` + `O`: right; U12 `l`/`i` kept.
20. `l` forms such as "He felt" (`Sensit`), "sent is here" (`missus adest`), "having been driven through" (`actis`): word by word right; kept.
21. Notes over 140 words: none left (U11 trimmed; longest now 137).

## Notes for the build

`gloss.json` does not exist yet, so `python3 build_aeneid.py aeneid-023` cannot finish in the real tree. With the six entries the scansion gate should pass: no UNRESOLVED
line; 640 and 661 are half-lines entered as such. Expected validator WARNs: none for note length (max 137); none for quotation counts (1 and 1 in `t`, `l`, `i`).
The new-renderings file is unchanged (none). Nothing in the part needs a source correction under Rule 5 or 5b.
