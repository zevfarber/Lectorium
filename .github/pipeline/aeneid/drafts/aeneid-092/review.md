# Review — aeneid-092 (Aeneid XII.107–215), adversarial reviewer

**Severity counts:**
- **Major: 10.** Wrong scansions on 10 lines: 108, 110, 117, 162, 166, 175, 185, 189, 195 and 197. The packet flagged only 110. The other nine had costs of 0.0 to 1.8 and were not flagged.
- **Medium: 4.** The advisory lede was wrong, *saetigeri suis* was read as a sow, the 211 note made a false claim, and 211 had no scansion (it would block the build).
- **Low: 20.** That is 19 text edits and 1 syllable-division scan-fix (178).
- **Refused or upheld without change: 22.**
- **Scan-fixes added: 15.** They were written straight into `scan-fixes.json` by `drafts/aeneid-092/add_scan_fixes.py`, with keys 12.108, 12.110, 12.117, 12.162, 12.166, 12.175, 12.178, 12.185, 12.189, 12.195, 12.197, 12.208, 12.209, 12.210 and 12.211. They are appended after 12.88 in the existing `{"sc": [...], "why": "..."}` format. The git diff shows additions only.

Nothing blocks the build. There is one point for the run lead on the audio of 211 (see "For the run lead").

## How the review was done

**Pass 1** went through all 48 units word by word. I checked:
- `l`, `i` and `n` against the Latin;
- every grammatical label and every elision list, line by line;
- the speech marks: Juno 142–153, Juno 156 and 157–159, Aeneas 176–194, and Latinus 197–211 with the parenthesis at 206. Each layer has 6 “ and 6 ”;
- the four rule-5b misprints against `source/aeneid-greenough.json`;
- the cross-reference to 12.13 (*concipe foedus*), which I checked in the source and found right;
- the `p` flags at 107, 113, 134 and 161, which are all right.

I hand-scanned all 109 lines by quantity and compared each with the scanner's fit. `scan_check.py` is 091's, pointed at 092. Sources were the Latin, the pinned source and memory of the public-domain references only. No translation was opened.

**Pass 2:**
- I re-read every changed field.
- I re-read every `l` for words carried into the wrong line, which found 140 *honorem*.
- I re-read every `i` for drift from `l` and `n`, which found 192–193 *sollemne*, and for remembered phrasing.
- I re-checked the units that end at a comma (109, 169, 186, 207). All four read on sensibly into the next unit.

**Script runs.**
- The drafter's file round-trips byte-identically through `aeneid_lib.jdump`. A copy of it was kept outside the repo.
- `review_edits.py` runs once from the drafter's file. It applies 24 field edits plus the advisory lede, and asserts that each old string occurs exactly once.
- The guards confirm:
  - `t`, `ln`, `p`, `v`, `title`, `titleEn`, `part` and `about` are unchanged;
  - `l` has as many lines as `t`;
  - no `i` contains a line break;
  - notes run 41–108 words;
  - `t`, `l` and `i` each have 6 “ and 6 ”.
- `review_check.py` is 091's, with `EXEMPT = {159}` and `NOTE_MARKS = {156, 159, 206}`. It prints no faults and `BUILD REPLICA: OK`.
- `scan_check.py` applies all 15 entries. It gives sc for 48 of 48 units, with no metre failures and no line-up failures. The only report left is COSTLY 137, which is right (see below).
- `make_units.py` was not touched and still holds the drafter's strings. Build from `units.json`; do not re-run `make_units.py`.

## Scansion

### Major (one per line)

| line | scanner (cost) | right reading |
|---|---|---|
| 108 | 1.8 | The scanner split *Ae-* (A-e-ne as a dactyl). The line is Ae-nē \| ās ă-cŭ \| ĭt Mar \| t(em) et sē \| sus-cĭ-tăt \| ī-rā (14). |
| 110 | 2.0 (flagged) | *Iūlī* has three syllables, Ĭ-ū-lī, so the fifth foot is a dactyl: …lā-tŭr Ĭ \| ū-lī (15). The scanner read *Iu-* as a consonant, making a spondaic fifth foot. |
| 117 | **0.0** | *Teucrique* has one *eu*: …rī Teu \| crī-quĕ pă \| rā-bant (15). The scanner read Te-u as short-short (16). |
| 162 | 1.5 | *quadriiugo* is quā-drĭ-jŭ-gō, as at 10.571: quā-drĭ-jŭ \| gō vĕ-hĭ \| tur cur \| rū cui \| tem-pŏ-ră \| cir-cum (15). The scanner made *quadri* one syllable (14). |
| 166 | 1.2 | The *Ae-* split: hinc pă-tĕr \| Ae-nē \| ās Rō… (14). |
| 175 | 1.5 | The *Ae-* split: Tum pĭ-ŭs \| Ae-nē \| ās stric… (14). |
| 185 | **0.0** | *Iūlus* has three syllables: cē-dĕt Ĭ \| ū-lŭs ă \| grīs nec \| post ar \| m(a) ul-lă rĕ \| bel-lēs (15). The scanner read *Iu-* as a consonant, lengthened *-det* by position, and counted 14. Both fits are metrical, but the house rule (1.267, 1.556 and many entries since) is that Iulus is always trisyllabic. |
| 189 | 0.3 | *Teucris* has one *eu*: nōn ĕ-gŏ \| nec Teu \| crīs Ĭ-tă \| lōs pā \| rē-rĕ iŭ \| bē-bō (15). The scanner read Te-u short-short (16). |
| 195 | 1.2 | The *Ae-* split: Sīc prĭ-ŏr \| Ae-nē \| ās sĕ-quĭ… (15). |
| 197 | 0.6 | The vocative *Aenēā* has three long syllables (as 8.496), and *măre* is short-short: Haec ĕ-ă \| d(em) Ae-nē \| ā ter \| ram mă-rĕ \| sī-dĕ-ră \| iū-rō (15). The scanner had a short *-nē-* and a long-long *mare*. |

### Medium

**211.** The line is UNRESOLVED because of the extra word *gesture*. The entry scans the line without it: in-clū \| sit pă-trĭ \| bus-quĕ dĕ \| dit ges \| tā-rĕ Lă \| tī-nīs (15). *gesture* is left unmarked, like an elided word, because the build requires one sc string per printed word.

The scanner gives no sc to a unit that contains an unresolved line, so 208, 209 and 210 needed carrier entries ("Confirmed by hand"). Their contents are the scanner's own fits, each checked by hand.

### Low

**178.** Syllable division only: *con-iunx*, not *co-niunx*, as at 12.17. The quantities were already right.

### Checked by hand and found right, so no entry

- **137 (COSTLY 2.0).** *Trōumque* has two syllables plus *-que*, and the scanner's fit is right: Lau-ren \| tum Trō \| umqu(e) ă-cĭ \| ēs ur \| bem-quĕ Lă \| tī-nī.
- **122** *Trō-ĭ-ŭs*.
- **127** *Mnestheus*, with one *eu*.
- **186** *Aeneadae*, where the scanner has *Ae-* right.
- **193** *Teucri*, which the scanner has right.
- **144** *ascendēre* (= *-ērunt*), with a long *-dē-*. The scanner has it right, and so does the note.
- **181**: *fontisquĕ* lengthened at the beat before *fl-*. This is the only fit; it is now pointed out in the note (L10).
- **182** *rēligio*.
- **192** *Sācra*, long by position.
- **198** *dū-plex*.
- **133** *sub-*.
- **207**: no elision anywhere in the line.

There is no hiatus and no half-line in this part.

## Medium (text)

- **M1 (advisory lede).** The lede said "Juno recalls that Jupiter took Juturna's maidenhood (140–141)". But 140–141 is the poet's parenthesis, which comes before Juno's speech opens at 142. The lede now reads "In a parenthesis just before Juno speaks, the poem says that…; Juno then speaks of the other Latin women…".
- **M2 (170, `l` `i` `n`).** *saetigeri fetum suis* was rendered "of a bristly sow". *saetigeri* is masculine (*saetiger, -era, -erum*), so *sus* here is not a sow. All three layers now say "swine", and the note says why.
- **M3 (211 note).** The note said "'gesture' is not Latin", which is false: *gestūre* is the vocative of *gestūrus*. It now reads "'gesture' makes no sense here and breaks the metre". The rule-5b opening is kept.

## Low

**`l`:**
- **L1 (121–122).** "from the full / columns pour themselves, gates" read as "from the full columns". It is now "from the full / gates the columns pour themselves out", which keeps *portis* in its own line.
- **L2 (140–141).** *honorem* stands in 140, so "as an honour" moves up to line 3.
- **L3 (158).** "or do you stir up war" read as a question. It is now "or you, stir up war".

**Notes:**
- **L4 (139).** *diva deam* was called "two forms of the word". *diva* and *dea* are different words, so it is now "two words for 'goddess'".
- **L5 (140–141).** "paid her with immortality" did not match the note's own gloss of *honorem* as power over waters. It is now "gave her this honour in return". The `about` can keep "whom Jupiter made immortal" (cf. 878–879).
- **L6 (148).** *tua moenia* "Ardea" is now "most likely Ardea".
- **L7 (166).** "The sentence begun at 166" is now "begun at 161", since *reges… procedunt* runs from 161 to 169, as the same note says later.
- **L8 (174).** Added the missing elision *paterisqu(e) altaria*.
- **L9 (177).** *quam propter* is "the preposition after its object". *quam* is a relative pronoun, not a noun.
- **L10 (181).** Added a pointer: the first *-que* of *fontisque* counts long (as *ensemque*, 12.89).
- **L11 (185).** Added that *Iulus* has three syllables here as at 110 (scan-fix 12.185).
- **L12 (210).** Added the missing elision *ol(im) arbos*. The note had said "No elisions".
- **L13 (213–214).** *rite sacratas… pecudes* does not frame a line, because it runs across the line-end. The note now says so.
- **L14 (118).** *focos* "portable braziers" went beyond what can be checked. It is now "fires for the sacrifice, set beside the altars", and `i` "fire-pans" is now "hearth-fires".
- **L15 (123).** The Etruscans "came to Aeneas in Book X" is now "sailed with Aeneas in Book X". He won them in VIII.

**`i`**, as precautions against remembered published phrasing (L16–L18) and one drift (L19):
- **L16 (115).** "breathe daylight from their raised nostrils" is now "blow the daylight out through their lifted nostrils".
- **L17 (140).** "Jupiter, high king of heaven" is now "the king who reigns in the heights of the sky".
- **L18 (156).** "This is no time for tears" is a stock rendering of this line in published versions. It is now "Tears do not suit this hour".
- **L19 (192–193).** "the sovereignty that is his by right" had drifted from *sollemne* and from `l` and `n` ("accustomed", "established"). It is now "the sovereignty that long custom has made his".

**Scan-fix:** L20 is 178, listed above.

## Refused or upheld (no change)

1. **12.156 `tempus, ”ait`: upheld as a rule-5b misprint for `tempus,” ait`.** The source has exactly this, and it is the Perseus closing-mark spacing pattern (6.155, 10.113, 12.45 and others). `t` is as printed. `l` and `i` close and reopen correctly, and the note opens in the rule-5b form.
2. **12.159 `audendi. ”Sic`: upheld.** The source has exactly this. The handling follows 6.407 and 12.45:
   - the stray mark heads the unit `”Sic exhortata…` in `t`;
   - `l` and `i` close Juno's speech after *audendi.*;
   - both notes (159a and 159b) open with the print's reading.
3. **12.206 `hoc ”(dextra`: upheld as a misprint for `hoc” (dextra`.** The source has exactly this. It is the same case as 6.406 `hunc ”(aperit` (aeneid-044), and is handled the same way: `l` and `i` close before the parenthesis, and 207 reopens with “.
4. **12.211 `gesture gestare`: upheld as a misprint (extra word) for `gestare`.** Without *gesture* the line is a regular hexameter, and with it no hexameter fits. *gesture* makes no sense in the clause, and the Latin Library has no word there.

   One caveat for the record: only the Perseus-derived pinned source is local. Whether Greenough's 1881 page itself prints *gesture* could not be checked. It could be a transcription slip, or a stripped correction tag left behind by "tags stripped" in `archive_aeneid.py`. Either way rule 5b applies: `t` is as printed, `l` and `i` follow *gestare*, and the note opens "The print has…".
5. **Advisory 140–141: kept, with the lede corrected (M1).** `claude/content-advisory.md` is not in the checkout. As the conventions summarise it, sexual violence always earns an advisory. *erepta pro virginitate* ("her maidenhood snatched away") names a rape by Jupiter, so the rule fires. This is the same footing as aeneid-063's Sabine women: named in a phrase, not described.

   The `more` text is accurate. Juturna does return to it at 878 (*haec pro virginitate reponit?*). The mention of the other Latin women (143–144) is fine as context. Nothing else in the part triggers an advisory: the sacrifice at 214 *viscera vivis eripiunt* is ritual animal slaughter, which no trigger covers.
6. **"(from memory)" claims, all upheld as true:**
   - Hesiod makes Latinus a son of Circe, the Sun's daughter (Theogony, close to 1011–1013). That makes *avi* right, and Virgil's own descent from Faunus is at VII.47–49.
   - Livy I.24 (the fetial's pig, struck with a flint) is cited twice. Both uses are right.
7. **Unmarked facts, upheld:**
   - the Feriae Latinae on the Alban Mount;
   - the Lacus Iuturnae in the Forum;
   - Agamemnon's oath-list in Iliad III (Zeus, Sun, rivers, earth, the powers below);
   - the Iliad III elders on the gate;
   - Achilles' sceptre oath in Iliad I;
   - L&S on *limus* (the purple-bordered apron of sacrificial attendants) and on *cedo*, "turn out";
   - Asilas on the Trojan side (X, XI).
8. **107 "'saevos', -os after v": upheld.**
9. **113 *dies* feminine "as often of a fixed day": upheld** (Allen & Greenough's rule).
10. **134–136 *e summo… tumulo* taken together: upheld** as one standard construction. `l` keeps the two phrases apart; the note's reading is defensible.
11. **144 *ingratum… cubile* as "unwelcome", hateful to the wronged wife: upheld** as an interpretation.
12. **147 `l` "Where" for *Qua*: upheld.** It is literal, and the note gives "in so far as".
13. **149 *imparibus… fatis* as an ablative of attendant circumstance: upheld.**
14. **172 *Illi* = the kings: upheld.**
15. **203–205 *vis* as the subject of *effundat… solvat*: upheld.**
16. **211 *patribus… Latinis* as "the elders of Latium": upheld.**
17. **Elision lists in the other 44 units: checked line by line, all right.** The only gaps were the two added (174 and 210).
18. **The units ending at a comma (109, 169, 186, 207) are sound.** Each next unit begins with a word that carries the syntax on (*tum*, *-que*, *sin*, *cum*).
19. **Speech marks: correct** in `t`, `l` and `i`, 6 and 6, as listed above.
20. **The `about`: no change.** It is accurate, including "whom Jupiter made immortal" (878–879) and the Iliad III–IV truce.
21. **The 110 note "Iuli has three syllables" and the 162 note "qua-dri-iu-go" were already right.** Only the scanner was wrong (now fixed).
22. **No set piece and no new house rendering: upheld.** `new-renderings.md` says "none", which is correct.

## For the run lead

- **`scan-fixes.json`** now holds 15 new keys, 12.108 to 12.211 as listed above, appended after 12.88. Nothing else in the file changed.
- **Audio, 12.211.** The 211 entry leaves *gesture* with no quantity marks, which is the only way to satisfy the build's one-string-per-word rule. `latin_verse.py` treats a wholly unmarked word as elided: it drops nothing and runs it into *gestare*. So the audio will still voice the stray *gesture*.

  If you want it silent, that needs a change in `latin_verse.py`, or a rule-5 source correction with a re-pin. I touched neither.
- **QUESTIONS.md (rule-5b record):**
  - 12.156 `tempus, ”ait` should read `tempus,” ait`;
  - 12.159 `audendi. ”Sic` should read `audendi.” Sic`;
  - 12.206 `hoc ”(dextra` should read `hoc” (dextra`. These are three more cases of the spacing pattern of item 82.
  - 12.211 `gesture gestare` should read `gestare`: an extra word, unmetrical. Whether the slip is Greenough's or Perseus's is unchecked; it may be a stripped correction tag in the TEI.
- **Advisory:** kept, with the lede corrected (M1). Drop it if you rule that a one-phrase mention of Jupiter's rape of Juturna does not meet "sexual violence always". I judged that it does, as aeneid-063 did for the Sabine women.
- **Scansions resting on judgement:**
  - 185 *Iūlus* trisyllabic. The scanner's disyllabic reading also scans, but it goes against house practice and Virgil's usage.
  - 181 *fontisquĕ*, lengthened. This is the scanner's own fit and the only one.
- **Unchecked from memory:** Hesiod Theogony (Latinus son of Circe); Livy I.24 (fetial and pig); Iliad I and III references.
- **No new house renderings, no set pieces.**
