# aeneid-031 (Aeneid V.1–103) — reviewer's record

Two passes (pass 1: grammar of every note, Latin to `l` word by word, `l` and `i` agreement, echoes, speech marks; pass 2: all 103 lines scanned by hand against the scanner's fits). `t` untouched (checked identical to the pre-review file); `units.json` edited by script in `l`, `i`, `n` only; `scan-fixes.json` extended by script, additions only (13 new keys, existing format). Nothing built or published. `build_aeneid.py` was not run (no dry-run mode): its scansion stage was reproduced line for line with `scan_latin.scan_story` plus `scan-fixes.json` (the same code path as the build), and the validator's foot, syllable-count and `×` checks were reproduced on the result. Outcome: 0 UNRESOLVED, 0 MISMATCH, 0 COSTLY left, every unit gets `sc`, all 103 lines pass as six feet and 12–17 syllables. Unit-level scan equals line-level scan on every unfixed line. Note lengths all within 15–140 words; `l` has the same line count as `t` in every unit; no `i` has a line break.

Severity counts: **major 18, medium 14, low 17.** (Major = a false grammatical label, a mistranslation in `l`, or a scansion with wrong quantities or syllable count. Of the 18, 6 are text and 12 are scansion.)

## Major

1. **5.4 `tantum`** was labelled "an adverb, 'so greatly'". It agrees with `ignem` (`tantum ignem`, "so great a fire"). Note rewritten; `i` now "The cause that kindled so great a fire is hidden from them;".
2. **5.26–27 `sic poscere ventos`**: note and `l` made `te` the subject of both `poscere` and `tendere` and `ventos` its object. `ventos` is the subject of `poscere` ("that the winds demand it so"); `te` is the subject of `tendere` only. Note rewritten (two accusative-and-infinitive clauses); `l` now "Indeed so to demand, the winds, / long ago and in vain I see, you strain against them:" (`i` was already right).
3. **5.32 `portus`** was called "the -is accusative plural (a recurring Greenough spelling)". `portus` is the fourth-declension accusative plural (as the note on 5.57 says). Note fixed.
4. **5.80–81 `recepti nequiquam cineres`**: note said Aeneas "carried Anchises's body out of Troy and as far as Sicily". He carried his father out of Troy alive; Anchises died in Sicily. Note rewritten (and says the plurals `animae`, `umbrae`, `cineres` are poetic).
5. **5.1 `l`** "Meanwhile the middle Aeneas" made `medium` agree with `Aeneas`; it agrees with `iter` (line 2). `l` now "Meanwhile the middle, Aeneas now with his fleet, was holding / sure, the way, and…"; note corrected (it also said `medium… iter` "frames the first line"; `iter` is in line 2); `i` now "…holding a sure course".
6. **5.70 `l`** "the earned await the prizes of the palm" made `meritae` the subject of `exspectent`. It agrees with `palmae`. `l` now "…and of the earned palm await the prizes."; note says `meritae` agrees with `palmae`, `-que` joins `exspectent` to `adsint`.
7–18. **Scansion, wrong syllable count or quantities in the scanner's fit** (all now in `scan-fixes.json`, each with its reason):
   - **5.1** `Aeneas` split A-e-ne-as (cost 1.2). Ae-nē-ās: Īn-tĕ-rĕ | ā mĕ-dĭ(um) | Ae-nē | ās iam | clās-sĕ tĕ | nē-bat.
   - **5.7** `Teucrorum` split Te-u (16 syllables). Teu one long syllable: trīs-tĕ pĕr | au-gŭ-rĭ | um Teu | crō-rum | pec-tŏ-ră | du-cunt.
   - **5.13** `quianam` read as one long syllable (five spondees, cost 0.0). Quĭ-ă-nam: Heu quĭ-ă | nam tan | ti cin | xē-runt | ae-thĕ-ră | nim-bi (as 4.538 `Quiane`).
   - **5.17** `Aenea` split. Mag-nă-nĭ(me) | Ae-nē | ā non | sī mĭ-hĭ | Iup-pĭ-tĕr | auc-tor. The final vocative -ā is long here: the only fit with natural quantities for the rest (the short-a reading used at published 017 would force `mihi` long-long). Doubtful, listed below.
   - **5.26** `Aeneas` split and `Equidem` read E-qui long. Tum pĭ-ŭs | Ae-nē | ās Ĕ-quĭ | dem sic | pos-cĕ-rĕ | ven-tos (as 1.576).
   - **5.44** `Aeneas` split. ad-vŏ-căt | Ae-nē | ās tŭ-mŭ | lī-(que) ex | ag-gĕ-rĕ | fā-tur.
   - **5.47** `reliquias` read by synizesis (re-liqu-ias, three syllables). rē-lĭ-quĭ-ās four syllables (as published 001, 007, 017, 027).
   - **5.51** (cost 0.0, a valid line with wrong quantities) `Gaetulis` fitted with short tu, and `agerem` with long a and ge. Gaetūlis has long tū; ăgĕrem is short-short: Hunc ĕ-gŏ | Gae-tū | lis ă-gĕ | rem sī | Syr-tĭ-bŭs | ex-sul.
   - **5.55** (cost 1.5) `cineres` fitted with long ci and ne, `ipsius` by synizesis. Nunc ul | (tro) ad-ci-ne | res ip | sī-ŭs et | os-sa pa | ren-tis: ultro elides into ad, cĭnĕres short-short, ipsīus long sī.
   - **5.66** `Teucris` split Te-u (15 syllables). Teu one syllable: prī-mă cĭ | tae Teu | cris pō | nam cer | tā-mĭ-nă | clas-sis.
   - **5.90** `Aeneas` split. Obs-tĭ-pŭ | it vī(su) | Ae-nē | ās Il(le) | ag-mĭ-nĕ | lon-go.
   - **5.102** `aena` as a diphthong plus `ordine` read or-di-ne with both long. Trisyllabic a-ē-na with `ne` elided, exactly as 1.213 and published 003: or-dĭ(ne) ă | ē-nă-lŏ | cant ă-lĭ | ī fū | si-que pĕr | her-bam.

## Medium

1. 5.10 note: `aër` called "the Greek form of 'aer'". It is the Greek loanword `aer` in the nominative; the diaeresis marks two syllables. Rewritten.
2. 5.21 note: `nec… nec` called "the double negative". It is the correlative "neither… nor". Fixed.
3. 5.23 note: `longe` "modifies the sentence". `nec… longe` goes with `reor` ("I do not think them far off"); `fida` adds "safe". Fixed.
4. 5.32 note: `boum` called "the old genitive plural" (it is the ordinary one); "`Penates / et patrios` framing the line break" (no framing; `patrios` goes with `Penates`, `epulis` is a dative); the `naves`/`nauis` parenthetical was muddled (Greenough prints `naves`, the Latin Library `nauis`); `numero` was not labelled (ablative, "by count"). Rewritten.
5. 5.59–60 note: `urbe posita` and `templis dicatis` were lumped as "ablative absolutes / ablatives"; the subject of `velit` hedged ("Anchises or the divine power"); `velit` called "jussive or optative". Now: `urbe posita` is an ablative absolute, `templis dicatis` an ablative of place with a participle, `velit` a wish, and the subject is Anchises (required by `sibi`). `i` made "may my father be willing…" so the reader is not left with an unnamed "he".
6. 5.64 `l` and note: `nona` was placed beside `diem` in `l` ("if the ninth day to mortals kindly / Aurora…"); it agrees with `Aurora`. `l` now "if the ninth, the day to mortals kindly, / Aurora…"; note says so. Note's "I will set (as prizes)" cut (`ponam certamina` = set up contests).
7. 5.72 `l` "he veils his maternal brows with myrtle" took `materna` with `tempora`; it frames `tempora` with `myrto` ("maternal myrtle"). Fixed (`i` was right).
8. 5.32–33 `l` put `secundi` (end of line 32) at the start of the next line ("favourable Zephyrs"). `l` now "…and the sails the favouring / Zephyrs stretch tight;".
9. 5.38 `l` put `mater` in the third line ("whom his mother bore") though it stands in line 38. `l` now "Trojan, from the river Crinisus conceived, the mother / whom bore:"; note says `Troïa` is an adjective agreeing with `mater`.
10. 5.85 note: "`septem ingens gyros` frames the line: 'huge, in seven coils'". There is no frame; `ingens` agrees with `anguis`, `septem` with `gyros`. Rewritten.
11. 5.87 note: `caeruleae cui terga notae` "to which the back's marks were blue" left the subject unclear. Now: `cui` dative of possession, `notae` the nominative subject, `terga` the poetic plural for the back.
12. 5.93 `i` "went back, harmless, to the foot of the tomb" for `imo… tumulo` ("into the depths of the tomb"). Fixed.
13. 5.96 `i` "two sheep of two years each" fused `binas` (two each) with `bidentes` (full-grown). Now "two sheep apiece".
14. 5.51–52 note: `urbe Mycenae` gave no label for the odd form. Now says `Mycenae` is taken as a genitive singular dependent on `urbe` (a plural name would stand in the ablative, `Mycenis`). This is the drafter's flagged form; the label is a judgement, not verifiable from the lexicon here, and the note states it as "taken as".

## Low

1. 5.1 `i`: dropped an invented "behind him" (`Aquilone` is a plain ablative); note's "ablatives of means" loosened to "ablatives".
2. 5.5 note: `sed` "placed second" is third in its clause; "postponed to the third place".
3. 5.8 note: `pelagus` described as "the accusative of the Greek-derived noun"; now "neuter noun (a Greek loanword) in the accusative".
4. 5.14 `l` "And what" for `Quidve` now "Or what".
5. 5.17 `l` added "it" ("pledge it") for `hoc`, which belongs to `caelo`. Removed.
6. 5.17 `i` "not even if Jupiter himself were to give me his pledge" echoes the familiar wording; now "not if Jupiter were to stand surety and give me his word could I hope…".
7. 5.21 `i` "nor to row hard enough" for `tendere`; now "strain".
8. 5.23 `i` "if I am right in remembering my courses by the stars" lost `servata… remetior`; now "if I truly remember the stars I watched and can measure my course back by them".
9. 5.34 note: `notae… harenae` (dative with the compound verb) was unlabelled. Added.
10. 5.36 `i` "Acestes had seen… and came running" mixed pluperfect with the historical present of `l`; now "saw… and ran". Note's "ships, by synecdoche for vessels" replaced by "('rafts', here simply 'ships')".
11. 5.42 `i` "the clear dawn" for `clara dies`; now "the next day, bright with the first light of the east".
12. 5.48 `i` "set up the altars in mourning" for `sacravimus`; now "hallowed the altars of our grief".
13. 5.57 `i` "a friendly harbour" for plural `portus… amicos`; now "harbours". A double space in the note removed.
14. 5.77 `i` "two bowls" for `carchesia` (tall cups); now "cups".
15. 5.83 `i` "whichever it is… along with me" kept the familiar rhythm of `quicumque est`; now "…nor the Ausonian Tiber, whatever stream it may be."
16. 5.89 `i` "against the facing sun" for `adverso sole`; now "the sun being opposite".
17. 5.103 scan: `subiciunt` read su-bi-ci-unt with a vowel i (the same quantities, but marks a long u in `sub`); entered as sub-jĭ-cĭ | unt, consonantal i after the prefix.

## Refused findings (checked, left as drafted)

- **5.4 `quae… causa` indirect question**: true as labelled (perfect subjunctive after `latet`, whole question the subject). Only the `tantum` label was false.
- **5.96 `bidentes`**: accusative plural, label true; the variant `bidentis` is morphological, mention kept.
- **5.13–14, 5.17–25, 5.26–31, 5.45–71, 5.80–83 speech marks**: “ on the first unit and ” on the last in `t`, `l` and `i` for all five speeches (10 units); counts 5/5 in each layer; the print's ” before `Sic` (5.14) is handled by the unit-7 note. Nothing to change. The `p` flags (lines 1, 8, 26, 35, 42, 72, 84) are right.
- **Packet variants**: `adstitit`/`astitit`, `aër`/`aer`, `Troïa`, `divom`, `Elymus`/`Helymus`, `fines`/`finis`, `Penates`/`penatis` orthographic or morphological; `demittere`/`dimittere` (5.29) changes the sense and is already noted. No further notes added.
- **5.17 `Aenea` as vocative**: label true (Greek-type vocative).
- **5.88 `Libystidis`, 5.77 `carchesia`, 5.85 `gyros`, 5.38 `Troïa… Criniso` notes**: labels true.
- **5.80–81 `i` "spirit and shade"** for plural `animae umbraeque`: kept (English singular for the one dead man); note now says the plurals are poetic.
- **`about`**: not touched (outside l/i/n/p); contents agree with the text.
- No echo found in `i` beyond those rephrased above; the two stock phrases (`Ore favete`, `nisi fallor`) are rendered in plain English, not in any known version's wording.

## Scansion: every line scanned by hand (103 lines)

Scanner fit confirmed with natural quantities on all lines not listed in the fixes. Lines with Greek eu: 5.7 and 5.66 (`Teucrorum`, `Teucris`, fixed); `Heu` (5.13) and `seu` (5.69) are correct as one long syllable (5.13 was fixed for `quianam`). Initial Ae-: 5.1, 5.17, 5.26, 5.44, 5.90 (all fixed), 5.102 `aena` (fixed); `aevi` (5.73) and `aethera` (5.13) were correct as one syllable. Consonantal i after a prefix or hiatus: 5.103 `subiciunt` (fixed), `inhorruit` (5.11, in short before h), `iam`/`Iamque`/`iamdudum` (5.3, 5.8, 5.27, 5.49: iam elided before a vowel where it does, long by position before a consonant), `iaculo`/`iaculis`/`iacit`/`iuvencos`/`iubet`/`Iuppiter` (correct), `Troia` (5.61, abl. Troiā, correct), `Troïa` (5.38, three syllables, as published 020), `Elymus`, `Mycenae`, `Gaetulis` (5.51, fixed), `Ausonium` (5.83), `Thybrim` (5.83, long Thy- by lengthening before br, as published 021), `Italos` (5.82, short I-, the only fit; as published 021).

**Hand scansions added to `scan-fixes.json`:** 5.1, 5.7, 5.13, 5.17, 5.26, 5.44, 5.47, 5.51, 5.55, 5.66, 5.90, 5.102, 5.103.

**Doubtful quantities left as the scanner or precedent gives them (for QUESTIONS.md):**
- **5.17 `Aenea`**: final -ā long (the only fit with natural quantities elsewhere); published 017 has short a in the same vocative.
- 5.38 `Criniso`: Crī-nī-sō, all long; the quantity of `ni` could not be confirmed.
- 5.10 `supra` with long `su-` (as published 018, 026, 030); 5.11 `tenebris` with long `ne` in the sixth foot, and 5.59 `sacra`, 5.78 `sacro` with lengthened `sa-` (muta cum liquida, as published 009, 018 and the `sacra` entries); 5.97 `nigrantis` with lengthened `ni-`; 5.83 `Thybrim`.
- 5.40 `gaza` with long ga- and `reduces` with short du- (redux, reducis); 5.73 `maturus` with long ma- (mātūrus); 5.77 `carchesia` with long che-.
- 5.8, 5.3 `iam` elided before a vowel (`nec iam amplius`, `quae iam infelicis`); 5.82 `Italos` with short I-.
- 5.84 `adytis` short y; 5.85 `gyros` long gy-.
