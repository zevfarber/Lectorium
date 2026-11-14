# Review — aeneid-075 (Aeneid X.276–361), adversarial reviewer

**Severity counts: major 10, medium 3, low 17 (15 in pass 1, 2 in pass 2). Refused or upheld-without-change findings: 12. Scan-fixes entries added: 12 (9 wrong full lines, 1 half-line, 2 carriers).**

## How the review was done

**Pass 1** covered all 36 units word by word. I checked `l`, `i` and `n` against the Latin, every grammatical label, every elision list, every "framing" claim, every cross-reference and every attribution made from memory. I also checked:
- the speech marks
- the rule-5b handling at 298 and 335
- the bracketed line 278 and the half-line 284
- the Latin Library variants (293, 307, 350)
- `about`, `title` and `part`

I searched the text for other misprints and found none. I read every `i` for echoes of the well-known English versions, especially 284, the simile at 356–359, and 361.

Sources: the Latin, the pinned source and memory of the public-domain reference works. No translation was opened and nothing was searched.

**Cross-references checked in the pinned source:**
- IX.126 (*At non audaci Turno fiducia cessit*, so "almost the same" is right) and IX.127 (= 278 word for word)
- VII.691–692 (Messapus *Neptunia proles*, *quem neque fas igni … nec sternere ferro*)
- VII.706–709 (Clausus and the *Claudia … gens*)
- VII.723 (Halaesus *Agamemnonius, Troiani nominis hostis*) and VII.727 (Aurunci beside him)
- VIII.506 and X.153 (Tarchon)

The one factual error was the gloss on IX.126 (Medium 1).

**Pass 2** re-read every edited field in full. It re-checked speech marks, line counts (`l` has the same number of lines as `t` in every unit, and no `i` has a line break) and note lengths (41–112 words). It made two more changes (P2-1, P2-2).

**Scansion.** I hand-scanned all 86 lines and compared them syllable by syllable with the scanner, run in-process the way the build calls it. The helper is `drafts/aeneid-075/scan_check.py` (074's, with the part id changed).
- **Packet flags.** 284 (UNRESOLVED) is a half-line: it has an entry, and 285 and 286, which share its unit, have carrier entries. 350 (COSTLY 2.6) is **right** and gets no entry: Trēs quŏ-quĕ | Thrē-ĭ-cĭ | ōs Bŏ-rĕ | ae dē | gen-tĕ sŭ | prē-ma (16). *Threicios* has four syllables (Θρηΐκιος) and *Boreae* three; the cost is only the long ē before a vowel.
- **Nine full lines are wrong with no packet flag:**
  - initial *Ae-* split: 287, 311, 313, 332, 343
  - Greek *eu* split: *Teucros* 309
  - wrong quantities with the right count: 279 (*vōtīs*, *ădest*), 316 (*Phoebĕ*, *căsūs*, *ēvadere*), 337 (*thōrāca*, *sĭmul*)
- **Right as the scanner reads them:**
  - *coniugis* 280 and *coniciunt* 330 (consonantal i, the prefix syllable long)
  - *deiecit* 319, *traiecto* 339 and 348
  - *huic* 338 (one syllable), *steterunt* 334 (short e), *Graium* 334 (two syllables), *Iliacis* 335, *Alcanor* 338 (the metre needs *-cā-*), *Idas* 351 (*Ī-*), *Troianae* 360

Every entry was checked by `drafts/aeneid-075/add_scan_fixes.py` (dry run, then `--write`):
- against the build's word-match rule
- against the validator's metre rule (the half-line rule for 284)
- against the syllable count stated in its own `why`

A replica of the build's scansion step, reading `scan-fixes.json`, gives these results:
- all 12 entries apply
- **all 36 units get `sc`**
- no unit's `sc` is out of line with its words
- no line fails the metre check
- the only report left is the correct COSTLY at 350

**What was edited, and how.**
- **Scripts.** `units.json` was edited only by `review_edits.py` (pass 1: 19 field edits plus one in `about`) and `review_edits_pass2.py` (pass 2: 2 edits). Each old string was asserted to occur exactly once in its field. The file was written with `aeneid_lib.jdump`; the drafter's file round-tripped byte-identically before any edit.
- **Untouched fields.** `t`, `ln`, `p` and `v` were checked by script against a copy taken before any edit, and are unchanged in all 36 units. `title`, `titleEn` and `part` are unchanged.
- **Units changed:** 0, 1, 3, 14, 15, 16, 24, 26, 29, 32, 34, 35.
- **`make_units.py` was not touched.** It still holds the drafter's strings, so build from `units.json` as it stands.
- **`scan-fixes.json`.** The change only appends (137 insertions, 0 deletions), with new keys after 10.263 in line order.
- **Build and validator not run.**

## Changes — pass 1

### Major (scan-fixes)
- **M1. 10.279** (cost 0.0, unflagged). The scanner had *vŏtĭs* short-short and the a of *adest* long. Right: Quod vō | tīs op | tās-tĭs ă | dēst per | frin-gĕ-rĕ | dex-tra (14).
- **M2. 10.284**, half-line (UNRESOLVED): Au-den | tīs For | tū-nă iŭ | vat (8). **Carriers 10.285 and 10.286** (scanner right, 14 each) are entered because the three lines form one unit, and without them the whole unit would get no `sc`.
- **M3. 10.287** *Interea Aeneas*. The scanner split Ae- (16). Right: In-tĕ-r(e) | (a) Ae-nē | ās sŏ-cĭ | ōs dē | pup-pĭ-bŭs | al-tis (15).
- **M4. 10.309** *Teucros*. The scanner split eu (15). Right: tō-t(am) ă-cĭ | (em) in Teu | crōs et | con-tr(a) in | lī-tŏ-rĕ | sis-tit (14).
- **M5. 10.311** *Aeneas*. The scanner split Ae- (14). Right: Ae-nē | ās ō | men pug | nae strā | vit-quĕ Lă | tī-nos (13).
- **M6. 10.313** *Aenean*. The scanner split Ae- (16). Right: Ae-nē | ān pĕ-tĭt | huic glă-dĭ | ō per | qu(e) ae-rĕ-ă | sū-ta (15). *petĭt* is short, so it is the present, as the note says.
- **M7. 10.316** (right count, wrong quantities). The scanner had *Phoebē* long, *sā-crum*, *cāsŭs* and *ĕvadere*. Right: et tĭ-bĭ | Phoe-bĕ să | crum cā | sūs ē | vā-dĕ-rĕ | fer-ri (15). *casus* is accusative plural.
- **M8. 10.332** *Fidum Aeneas*. The scanner split Ae- (15). Right: al-mă Vĕ | nus fī | d(um) Ae-nē | ās ad | fā-tŭr Ă | chā-ten (14).
- **M9. 10.337** (right count, wrong quantities). The scanner made *tho-ra-* short-short and *-ca si-* long-long. Right, with *thōrāca* (Lewis & Short *thōrax, ācis*): Mae-ŏ-nĭs | et thō | rā-că sĭ | mul cum | pec-tŏ-rĕ | rum-pit (15).
- **M10. 10.343** *Aenean petiit*. The scanner split Ae- (15). Right: Ae-nē | ān pĕ-tĭ | it sed | nōn et | fī-gĕ-rĕ | con-tra (14).

### Medium
1. **Note 276–277, IX.126.** The note said "where Turnus faced the Trojan ships before they became nymphs". In the source, IX.126 comes *after* the change (IX.77–122). It now reads "where Turnus kept his nerve after the Trojan ships had turned into nymphs".
2. **`i` 313b–314.** "and drank from the side he laid open" made Aeneas the one who drinks. It now reads "and drained the blood from his side, laid open".
3. **`about`.** "kills two of the brothers" was wrong: Maeon dies, and Alcanor's arm is crippled (*moribunda*). It now reads "kills one brother and cripples another's arm, while a third, aiming back, only grazes Achates". "the spears he once threw at the Greeks" is now "the spears that once stood in Greek bodies at Troy".

### Low
- **L1. Note 276–277.** *audaci Turno*: "dative of possession" (a label for use with *sum*) is now "dative of reference, where English uses a possessive".
- **L2. Note 276–277.** Elision typo "praecipir(e) et" corrected to "praeciper(e) et".
- **L3. Note 278–279.** Added "'votis' with long 'o', from 'voveo'", to match M1.
- **L4. Unit 280b–282a (`l`, `i`, `n`).** *referto* has the same subject as *esto*, *quisque*. `l` now reads "now the great let him recall / deeds, the glories of the fathers". `i` now reads "now let him call to mind the great deeds, the glories of his fathers". The note now says "third-person future imperatives, both with 'quisque' as subject … 'let him recall'".
- **L5. Note 310b–313a.** Added "'Ae-' one syllable", to match M5 and M6.
- **L6. `l` 313b–314.** "in the side he drains, laid open" is now "the side he drains, laid open".
- **L7. Note 315–317a.** Added "'casus' accusative plural, object of 'evadere'", to match M7.
- **L8. Note 333–335a.** "the relative clause after its sense" was unclear. It now reads "the relative 'quae' placed after its verb, its antecedent the spears understood from 'ullum'".
- **L9. Note 336b–337.** Added "(tho-ra-ca, the first two syllables long)", to match M9.
- **L10. Note 342–344.** *Achatae* is not a "Greek genitive". It is now "genitive in '-ae', the Greek name in '-es' declined in the first declension".
- **L11. Note 342–344.** Added "'Ae-' one syllable", to match M10.
- **L12. Note 352b–354a, Halaesus.** "a follower of Agamemnon's line who settled in Italy" went beyond the text. It is now what VII.723 says: "'Agamemnonius', of Agamemnon's house or following, an enemy of the Trojan name".
- **L13. Note 356b–359.** *magno… aethere* does not frame *discordes… venti*, because *venti* stands outside it. It now reads "enclosing 'discordes', with 'venti' … after it".
- **L14. `i` 356b–359.** Recast from the Latin to drop stock phrasing ("warring winds", "hangs long in doubt", "locked in resistance", with "locked" repeated at 361). It now reads: "As when, in the great sky, winds at odds with one another stir up battle, matched in spirit and in strength, and neither the winds themselves nor the clouds nor the sea give way, and the struggle stays long undecided, everything braced and straining against everything:"
- **L15. `i` 360–361.** "foot is locked against foot, and man pressed close on man" is now "foot holds fast against foot, and man is crowded hard on man". This keeps clear of any remembered published wording of this famous line.

## Changes — pass 2
- **P2-1. `i` 342–344.** "he was not allowed to strike him in return" left it unclear who "him" was. It now reads "he was not granted a hit on Aeneas in return".
- **P2-2. Note 315–317a.** Added "with short final '-e'" after "'Phoebe', vocative", to match M7.

## Refused or upheld without change
1. **10.350, flagged COSTLY.** The scanner is right, and no entry was added (see Scansion above).
2. **284 rendering.** The drafter's `l` "Those who dare, Fortune helps," and `i` "Fortune lends her help to those who dare," are kept. They avoid the familiar English proverb and every published wording I can recall.
3. **Rule-5b handling at 298 and 335.** Upheld. Each first note opens with the required sentence, the stray ” begins the next unit's `t`, and the `l`/`i` marks close the speech on the right unit. The speech marks balance in all three layers.
4. **278 bracket note.** Upheld. It says the line is spurious, repeats IX.127, and is kept in [ ] in all three layers.
5. **284 half-line note** ("more than fifty" unfinished lines). Upheld; the usual count is about 58.
6. **Variant notes at 293, 307 and 350.** Upheld.
7. **313 *petit* as a present.** Upheld: the metre needs a short -ĭt.
8. **The dative label on *egressis* (283) and *viris* (280).** Upheld as datives of reference.
9. **Attributions from memory, kept as written.** I am confident of each:
   - Terence *Phormio* 203 *fortis fortuna adiuvat*
   - Iliad 15.494–499, 5.311–318, 4.127–133, 16.765–769 (already marked "perhaps"), 13.130–131 and 16.215
   - the claim that children born by caesarean were sacred to Apollo (no ancient author is named)
   - Asclepius cut from his dead mother
   - Clausus and the Claudii, and Messapus (checked in VII)
10. **Ships landing stern first (287).** Upheld as standard background.
11. **Misprints.** No others found. *Audentis Fortuna iuvat,”*, with the comma inside the mark, is as printed.
12. **Advisory: none (upheld).** This is ordinary battle killing; the Lichas birth detail is clinical and not graphic.

## Scan-fixes entries added (12)
| key | reason | syllables |
|---|---|---|
| 10.279 | *vōtīs*, *ădest* (quantities) | 14 |
| 10.284 | Half-line (UNRESOLVED) | 8 |
| 10.285 | Carrier for 284 (scanner right) | 14 |
| 10.286 | Carrier for 284 (scanner right) | 14 |
| 10.287 | *Aeneas*, initial Ae- | 15 |
| 10.309 | *Teucros*, Greek eu | 14 |
| 10.311 | *Aeneas*, initial Ae- | 13 |
| 10.313 | *Aenean*, initial Ae- | 15 |
| 10.316 | *Phoebĕ*, *căsūs*, *ēvadere* (quantities) | 15 |
| 10.332 | *Aeneas*, initial Ae- | 14 |
| 10.337 | *thōrāca*, *sĭmul* (quantities) | 15 |
| 10.343 | *Aenean*, initial Ae- | 14 |

## For the owner (QUESTIONS.md)
- **10.284 *Audentis Fortuna iuvat*.** This is a famous tag that is not on the set-piece list. The drafter asks whether it should become a house rendering. I support the current wording: `l` "Those who dare, Fortune helps", `i` "Fortune lends her help to those who dare".
- **10.361 *haeret pede pes densusque viro vir*.** This is arguably a set piece too. The rendering was rephrased in review (L15); the owner may want to fix one.
- **Unchecked attributions from memory.** These are kept and believed right, but not verified against a text:
  - Terence *Phormio* 203
  - Iliad 15.494–499, 5.311–318, 4.127–133, 16.765–769, 13.130–131, 16.215
  - children cut from the womb being sacred to Apollo (Servius's explanation, not named in the note)
- **Advisory:** none taken.
