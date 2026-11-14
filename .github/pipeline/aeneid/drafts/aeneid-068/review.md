# Review — aeneid-068 (Aeneid IX.446–529), adversarial reviewer

I reviewed this part in two passes.

**Pass 1** covered all 40 units word by word. I checked `l`, `i` and `n` against the Latin, every grammatical label, every elision list, every "framing" claim, every cross-reference and every attribution made from memory. I also checked the drafter's misprint call (none) and the doubtful 9.501 `Illionei`, the bracketed 9.529, the half-lines 467 and 520, the no-advisory decision, the Latin Library variants, the `about`, the title and part names. I read every `i` for echoes of the well-known English versions, most closely 446–449 (*Fortunati ambo*) and the mother's lament, 481–497.

I worked from the Latin, the pinned source and memory of the public-domain reference works (Lewis & Short, Allen & Greenough, Greenough's notes, Conington, Servius). No translation was opened and nothing was searched.

In-poem cross-references were checked against the pinned source: 1.120, 1.521, 1.559, 1.611, 4.173–188, 4.311, 4.584–585, 4.631, 4.667, 7.212, 7.249, 7.645, 7.648, 7.691, 7.803, 8.478–495, 9.184–196, 9.216–218, 9.284–289, 9.297–298, 9.324–328, 9.335–338, 9.359, 9.365–366, 9.373–374, 9.390 and 9.442–445. Numa is not named anywhere in 9.314–445, as the drafter says. Two references were slightly off: the wish for fame is 9.194–195, not 9.195–196 (item 17), and 9.287–289 gives Euryalus's reason as not bearing her tears, not sparing her (item 27).

**Pass 2** re-read every edited field in full and made two more changes (P2-1, P2-2).

**Scansion.** I hand-scanned all 84 lines by quantity. I then ran the scanner in-process, the way `build_aeneid.py` calls `SL.scan_story`, and compared its output with mine syllable by syllable.
- **The scanner was wrong on 9 lines**: 448, 477, 482, 485, 490, 501, 510, 511 and 516. Only 501 was flagged (COSTLY 3.5). Each now has a hand entry (items 1–9).
- **Half-lines 467 and 520** (UNRESOLVED) each have a "Half-line" entry.
- A unit with an unresolved line gets no `sc` at all, so the **other lines of those units have carrier entries**, using the scanner's own fit after a hand check: 465 and 466 (unit 465–467) and 518 and 519 (unit 518b–520, which begins mid-line 518).

Every new `scan-fixes.json` entry was checked by script against a replica of the build's word-match rule (`strip(sc) == WORD_RE.findall(line)`). Each was also checked against the validator's metre rule:
- full lines: six feet, 12–17 syllables, one ×, five –⏑⏑/–– feet then –×/⏑×
- half-lines: feet numbered 1..k with k < 6, one ×, and a `why` that starts "Half-line"

Each `why` gives a syllable count, and the script checked that count against the entry.

I then ran a replica of the build's scansion step, reading the fixes from `scan-fixes.json` itself:
- all 15 entries apply
- **all 40 units get `sc`**
- all 84 lines pass the validator's metre check
- after the fixes, the scanner report is empty.

**What was edited, and how.**
- `units.json` was edited by Python script. Each old string was asserted to occur exactly once in the named field. The file is written with `aeneid_lib.jdump` (`indent=1`, `ensure_ascii=False`, no trailing newline, as the drafter's file).
- `t`, `ln`, `p` and `v` are byte-for-byte as the drafter left them in all 40 units. A script checked this against a copy of the drafter's file taken before any edit. `title`, `titleEn`, `part` and `about` are unchanged.
- **15 units changed.** `l` has the same number of lines as `t` in every unit, and no `i` has a line break.
- **Speech marks.** `t`, `l` and `i` each have 1 “ and 1 ”: “ in the 481a unit (*Hunc ego te…*), ” at the end of the 495–497 unit (*vitam.”*). This is right; it is the only speech in the part.
- **Note lengths.** Every note is now 30–139 words. Four were over the validator's 140: 446–449 (175), 485–489 (235), 500–502 (141, then 172 with the misprint opening) and 528–529 (147). Item 16 has the details.
- **`make_units.py` was not touched.** It still holds the drafter's strings, including the old `Illionei` note, so re-running it would undo this review. Build from `units.json` as it stands.
- The diff to `scan-fixes.json` only appends: 160 insertions, 0 deletions, trailing newline kept, formatting as before (a round-trip of the old file through `json.dumps(indent=1, ensure_ascii=False)` was byte-identical before appending). The new keys follow 9.384, in line order.
- The build and the validator were not run (`build_aeneid.py` has no dry-run mode). Their scansion steps were replicated instead.
- **`drafts/aeneid-068/` has no `gloss.json`.** The build needs one. That belongs to the glosser's step, not this review.

**Severity counts: major 9, medium 7, low 17 (15 in pass 1, 2 in pass 2). Refused or upheld-without-change findings: 22. Scan-fixes entries added: 15 (9 wrong lines, 2 half-lines, 4 carriers).**

## Changes — pass 1

### Major (scanner wrong; each now has a scan-fixes entry)
1. **9.448, *Aeneae* (unflagged).** The scanner split *Ae-* into A-e and made *-ne-* short (16 syllables). Right: dum dŏ-mŭs | Aē-nē | ae Că-pĭ | tō-l(i) im | mō-bĭ-lĕ | sa-xum (15).
2. **9.477, *femineo ululatu* (unflagged).** The scanner made *fē-mī-* long-long and *-neo* one syllable, which gives *fēmĭneus* a long ĭ. Right: hiatus, as the drafter and the note say: Ē-vŏ-lăt | īn-fē | līx et | fē-mĭ-nĕ | ō ŭ-lŭ | lā-tū (15).
3. **9.482, *requies* (unflagged).** The scanner read *requ-ies* as two syllables (15). Right, as the 8.46 entry: sē-ră mĕ | ae rĕ-quĭ | ēs pŏ-tŭ | īs-tī | lin-quĕ-rĕ | sō-lam (16).
4. **9.485, *ignota canibus* (unflagged).** The count was right but the quantities wrong: the scanner had short *-nō-* and *-tā*, and long *că-nĭ-*. Right: Heu ter | r(a) ig-nō | tā că-nĭ | būs dă-tă | prae-dă Lă | tī-nis (15).
5. **9.490, *Quo sequar… artus avolsaque* (unflagged).** The count was right but the quantities wrong: the scanner had long *se-*, and short *-tūs* and *ā-*. Right: Quō sĕ-quăr | aut quae | nunc ar | tūs ā | vol-să-quĕ | mem-bra (14).
6. **9.501, flagged COSTLY 3.5.** The drafter is right that the fit is wrong. The scanner took *Iu-* as consonantal and made the fifth foot spondaic (15). Right: Ī-lĭ-ŏ | nēi mŏ-nĭ | t(u) et mul | tum lă-crĭ | man-tĭs Ĭ | ū-lī (16), with *Ĭūlī* three syllables as at 9.293 and 9.310. The entry scans *Ilionei* but marks it on the printed word (`Il–li⏑o⏑2nei–`), as the 7.340 entry does for *inventus*.
7. **9.510, *Teucri* (unflagged).** The scanner split Te-u (15). Right: om-nĕ gĕ | nus Teu | cr(i) ac dū | rīs dē | trū-dĕ-rĕ | con-tis (14).
8. **9.511, *adsueti* (unflagged).** The scanner read ad-sŭ-ĕ-tī, with a short *ē* (14). Right: the *u* is consonantal, as in the entries at 7.33 and 7.487, giving ad-suē | tī lon | gō mū | rōs dē | fen-dĕ-rĕ | bel-lo (13).
9. **9.516, *Teucri* (unflagged).** The scanner split Te-u (14). Right: im-mā | nem Teu | crī mō | lem vol | vunt-quĕ rŭ | unt-que (13).

### Medium
10. **Note 9.500–502, the misprint (orchestrator's finding, applied).** Greenough spells the name with one *l* everywhere else: *Ilionei* at 1.120 and 7.249, *Ilioneus* at 1.521, 1.559, 7.212 and 9.569, *Ilionea* at 1.611, and *Ilione* at 1.653 (verified in the pinned source). So under rule 5b, 9.501 `Illionei` is a clear misprint.
    - The note now opens "The print has 'Illionei', a misprint for 'Ilionei', corrected here; t keeps the print, …", in the wording of the published notes at 6.666 and 8.323. It cites 1.120 and 7.249.
    - The note uses *Ilionei* throughout. `l` and `i` already said "Ilioneus".
    - `t` is as printed. The scan-fixes entry scans the corrected name (item 6).
11. **`i` 9.446–449, a remembered echo.** "no day will ever erase you from the remembrance of the ages" is close to a well-known modern version. "holds his sovereign rule" is close to the familiar "sovereign sway". It now reads: "If there is any power in my songs, no day will ever lift you out of the memory of time, so long as the house of Aeneas dwells beside the Capitol's unmoving rock and the Roman father keeps his empire." "lift you out" renders *eximet*.
12. **`i` 9.485–489, a remembered echo.** "never led you out to burial, never closed your eyes or washed your wounds… soothing an old woman's cares at the loom" follows the cadence of the familiar versions. It now reads: "Ah, you lie in a land you never knew, given as prey to the dogs and birds of Latium, and I, your mother, did not walk before you to the grave, did not press your eyelids shut or bathe your wounds, or wrap you in the robe I was speeding on for you night and day, my loom the solace of an old woman's cares."
13. **`i` 9.495–497, a remembered echo.** "…hurl this hated head of mine down to Tartarus, since in no other way can I cut short this cruel life" is close to a familiar version, clause by clause. It now reads: "…take pity, and with your bolt drive this hateful head of mine down beneath Tartarus, since there is no other way for me to end this cruel life.”"
14. **Note 9.485–489, an attribution, and a reading that is really an interpretation.** "an older reading, preserved by Servius, took 'funera' as an old feminine noun". This is not a different reading, since the letters are the same; it is a way of taking *funera*. I cannot stand behind the Servius attribution from memory. It now reads "some ancient readers took 'funera' as an old feminine noun".
15. **Note and `l` 9.492, a wrong label.** "'hoc' the internal accusative" is wrong. *sequor* is transitive, so *hoc* is simply the object of *secuta (sum)*: "is it this I have followed?" The note now says so. `l` "For this did I… follow?" turned *hoc* into a purpose phrase; it is now "This did I by land and sea follow?". `i` ("Was it for this that I followed you…") is idiomatic English for the same thing and is kept.
16. **Four notes over the validator's 140 words, cut to fit.**
    - **446–449**: 175 → 129. Cut the gloss on *dum*; cut "that Virgil always uses for nouns in '-ius' and '-ium'" (an overstatement anyway); tightened the *pater Romanus* sentence.
    - **485–489**: 235 → 135. Cut the glosses on *produco*, *pressive*, *veste tegens*, *anilis* and "plural for singular"; shortened the Iliad 1.4–5 and 22.510–514 references.
    - **500–502**: 172 → 137, after the misprint opening was added. Cut "the reason she must be taken away", *corripiunt*, and the paragraph on the spelling, which the opening now covers.
    - **528–529**: 147 → 139. Cut the gloss on *memorare*; tightened the 7.645 sentence.

### Low
17. **Note 9.446–449**:
    - "'memori… aevo'… framing 'vos'" was inexact. The words frame *vos eximet*, and the note now says so.
    - The reference for the friends' wish for glory was 9.195–196. Line 196 is about the road. It now reads "Nisus's wish (9.194–195, 'mihi facti fama sat est')".
18. **`l` 9.453**: "the chiefs at once, so many, in one slaughter" translated *una* twice. "at once," is cut.
19. **Note 9.452–454**: "Serranus was the young gambler" stated an inference as fact, as 067's P2-3 found. It now reads "the young man who had played (probably at dice) far into the night".
20. **Note 9.452–454**: "('-gu-' is a consonant and a vowel here, 'gw')" was muddled. It now reads "(the 'u' after 'g' is a consonant here, 'gw')".
21. **Note 9.459–460**: "'prima… Aurora'… framing the two lines with 'croceum… cubile'" was false: *prima* is the third word of 459. It now reads "her name held back to the second line, where 'croceum… cubile' frames 'linquens Aurora'".
22. **`i` 9.475–476**: "the spun wool" was wrong for *pensa*, which is the day's allotment of wool still to be spun. The line also leaned on a familiar phrasing ("the warmth… drained from"). It now reads "Suddenly the heat of life left the poor woman's very bones; the shuttle was jolted from her hands, and her day's wool unwound as it rolled."
23. **Note 9.477–480**: "'infelix'… her standing word" was false; the word is not used of her elsewhere. It now reads "the word used of her son at 9.390" (*Euryale infelix*, checked).
24. **Note 9.481–483**: "'illa… requies'… framing the line" was false, because *illa* ends 481. It now reads "framing 'senectae sera meae'".
25. **`i` 9.481–483**: "cruel boy" added *boy*. It now reads "bring yourself to leave me alone, you cruel one?". "bring yourself" gives the force of *potuisti*.
26. **Note 9.483–484**: "left without telling her, to spare her (9.287–289)" misstated his reason. At 289 he says he could not bear her tears. It now reads "because, he said, he could not bear her tears". "Elisions" with one elision is now "Elision".
27. **Note 9.490–491**: "'quae… tellus'… framing the whole question" was false, because *Quo sequar, aut* precede it. It now reads "framing what it holds".
28. **`i` 9.491–492**: "Is this all of you…" added *all*. It now reads "Is this what you bring home to me of yourself, my son?"
29. **`i` 9.493–494**: "Run me through… cut me down first of all" leaned on familiar wording. It now reads "Pierce me, if there is any pity in you; turn every spear you have on me, Rutulians, and let me be the first your steel destroys:"
30. **Note 9.500–502**: "his mother would be as a mother to him" was ambiguous, since *him* could be Euryalus. It now reads "He had promised Euryalus to take his mother as his own (9.297–298)".
31. **Note 9.528–529**: "The ancient commentators say Virgil takes the phrase from Ennius". I believe it is Macrobius (Saturnalia 6.1), who lists Virgil's borrowings, not a commentator, and I cannot confirm it. Softened to "Ancient writers on Virgil quote the line of Ennius he adapts".

## Changes — pass 2
- **P2-1 (low), note 9.485**: the quoted phrase "'canibus… Latinis alitibusque… data praeda'" put the words out of the Latin order. It now reads "'canibus data praeda Latinis alitibusque'".
- **P2-2 (low), note 9.492**: item 15's paraphrase "what all her following came to" slipped out of her voice. It now reads "'was this the end of all my following?'".

Pass 2 also re-checked:
- **Every "framing" claim in the part**, against the line as printed. After items 17, 21, 24 and 27, all are right. These include 465 *arrectis… in hastis*, 473 *pavidam… per urbem*, 475 *subitus… calor*, 483 *te… missum*, 495–496 *tuo… telo*, 512 *infesto… pondere* and 518 *caeco… Marte*.
- **Every elision list against the scanner's elisions** (and against the hand entries for 477, 485, 501 and 510), line by line. All 40 notes are right, including the cross-unit elisions *Numaqu(e) Ingens* and *Euryal(i) At*. 477 and 529 correctly list none at the hiatus and *et meministis*.

## Scan-fixes entries added (15)
These are appended after 9.384 in line order:
- **9.448**: *Aeneae*, Ae- split (15 syllables)
- **9.465**: carrier for half-line 467, the scanner's fit (14)
- **9.466**: carrier for half-line 467, the scanner's fit (14)
- **9.467**: Half-line, *Eu-rў-ă | l(i) et Nī | sī* (6)
- **9.477**: hiatus *femineo ululatu* (15)
- **9.482**: *requiēs* three syllables (16)
- **9.485**: *ignōtā cănĭbus*, wrong quantities with the right count (15)
- **9.490**: *sĕquar… artūs āvolsa*, wrong quantities with the right count (14)
- **9.501**: flagged COSTLY; *Ĭūlī* three syllables, *Ilionei* for the print's *Illionei* (16)
- **9.510**: *Teucri*, eu one syllable (14)
- **9.511**: *adsuēti*, consonantal u (13)
- **9.516**: *Teucri*, eu one syllable (13)
- **9.518**: carrier for half-line 520, the scanner's fit (14)
- **9.519**: carrier for half-line 520, the scanner's fit (15)
- **9.520**: Half-line, *mis-sĭ-lĭ | būs cer | tant* (6)

## Hand-scan notes on the special lines (scanner right, no entry)
- **Greek *eu***:
  - 475 *Euryal(i) At*: Eu-rў-ă-l(i) at sŭ-bĭ | tūs…, COSTLY-free.
  - 481 *t(e) Euryal(e) aspicio*, with two elisions and no hiatus: Hūnc ĕ-gŏ | t(e) Eū-rў-ă | l(e) ās-pĭ-cĭ | ō Tū | n(e) īl-lă sĕ | nēc-tae. The drafter's scansion is confirmed, and the note's elision list matches.
- **Initial *Ae-***: 468 *Aeneadae* is read right (Ae-nĕ-ă-dae). Only 448 *Aeneae* was wrong (item 1).
- **Consonantal i/u**:
  - 474 *adlabitur* is divided a-dla but has the right quantities (ad- long). Display only.
  - 494 *conicite* is cō-nĭ-cĭ-t(e), with the right quantities. Display only, as *obicit* (QUESTIONS 37/38).
  - Right as read: 453 *exsangui* (gw, then elision); 486 *iaces* (ya-); 514 *iuvat*; 461 and 515 *iam*.
- **Synizesis**: 480 *dehinc* is one syllable, as the drafter and note say. The scanner reads it so.
- ***Etruscam* (521)**: short Ĕ-, read right by the scanner (quās-sā-băt Ĕ | trūs-cam).
- **Hiatus**: only 477. **Half-lines**: 467 and 520.
- **Quantities checked and right**:
  - *Fortūnātī*, *Sīquid* (446); *mĕmŏrī* (447); *Căpĭtōlī* (448); *praedā*, *pŏtītī* (450); *Rhamnēte* (452); *ūnā* (453); *Nŭmā-* (454); *sēminecis*, *tepidā-* (455)
  - *Tīthōnī* (460); *ātrō*, *tābō* (472); *rĕlīquit* (475); *rădĭī*, *rĕvŏlūta* (476); *āmens* (478); *festīna* (488); *tēlā*, *sōlābar*, *ănīlis* (489)
  - *hōc* (491); *terrā-* (492); *absūmite* (494); *Īdaeus* (500); *āctā* (505); *densā*, *cāsus* (514); *lāt(e)* (517); *tegmina* (518); *Mēzentius* (522); *ēdiderit*, *dēmīserit* (527)

## Refused or upheld findings
- **R1 — "No misprint calls" (drafter)**: upheld except 9.501 (item 10). No lower-case after a stop and no joined closing mark in 446–529.
- **R2 — Speech marks**: **upheld**. “ is on the 481a unit and ” on the 495–497 unit, in `t`, `l` and `i` alike. There are no other speeches.
- **R3 — 9.529 bracketed**: **upheld**. It is kept in [ ] in `t`, `l` and `i`. It repeats 7.645 (checked: there it has a capital *Et* and ends with a colon).
- **R4 — No advisory**: **upheld**. The heads on spears (465–472) and the imagined body left to dogs and birds (485–491) are each a line or two in Homer's idiom. That is less graphic than 067, which got none. The drafter's drop-in lede/more is sound if the owner rules otherwise for IX–XII (QUESTIONS 61).
- **R5 — Latin Library variants**: upheld.
  - 456, 463–464, 481, 486, 514 and 529 change the sense and are noted.
  - 501 is now the misprint, and the note mentions the Latin Library's *Ilionei*.
  - 446, 487, 490, 493, 495, 505, 512 and 525 are orthographic and rightly ignored.
- **R6 — 481 hiatus at *te Euryale***: refused. The drafter asked about it; elision is the ordinary reading, and the scanner agrees.
- **R7 — Note 9.471, *movebant* with *ora* as subject**: kept. It is the usual reading, and the note gives the other.
- **R8 — Note 9.475, *miserae* dative of disadvantage**: kept. A genitive with *ossa* is possible, but the dative is the usual account.
- **R9 — Note 9.465, *visu* "ablative of respect"**: kept. A&G class the supine in *-u* so.
- **R10 — Note 9.481, "the only speech by a mourning mother in the poem"**: kept. I know of no other: Hecuba's words in Book II are not a lament, and Amata mourns no child.
- **R11 — Note 9.467, "some sixty lines stand incomplete"**: kept. QUESTIONS 9 has ~58.
- **R12 — Note 9.523, "repeats 7.691 exactly"**: kept. The words are identical; only the capital *At* and the commas differ.
- **R13 — Note 9.459, "repeated exactly from 4.584–585"**: kept. Checked; only the final stop differs.
- **R14 — Note 9.446, "ancient readers were already unsure" about *pater Romanus***: kept. This is the commentators' known debate (emperor, senate, Capitoline Jupiter), stated without a source.
- **R15 — Note 9.503, the Ennius *at tuba terribili sonitu taratantara dixit***: kept. It is a famous fragment, and the note names no source for it.
- **R16 — Note 9.505, Camilla "warrior-queen" of the Volsci (7.803)**: kept. She leads them and is called *regina* in Book XI (11.499, 11.703, 11.801).
- **R17 — Note 9.500, "Idaeus et Actor… otherwise little known"**: kept. Neither man is otherwise important (the Idaeus of 6.485 is Priam's charioteer).
- **R18 — Attributions from memory, kept; I can stand behind each**:
  - Iliad 18.175–177 (Hector would set Patroclus's head on the stakes)
  - Iliad 22.437–448 (Andromache at the loom, the shuttle falls)
  - Iliad 22.510–514 (the clothes she will burn)
  - Iliad 1.4–5 (dogs and birds)
  - Iliad 11.1–2 and Odyssey 5.1–2 (Dawn from Tithonus's bed)
  - Iliad 11.218–220 and 14.508–510 (invocations before slaughters)
  - Iliad 2.484–486 (the invocation before the catalogue)
  - the laments of Hecuba and Andromache in Iliad 22 and 24
- **R19 — `i` read for echoes and kept**: 446 "How fortunate you both are!"; 459–460; 473–474; 477–480; 481a "is this how I must look on you?"; 492 "over land and sea" (a stock English phrase); 503–524; 525–529. None is distinctive enough to change.
- **R20 — Drafter's hand scansions of 467, 477, 480, 501, 520 and 521**: all confirmed and entered as above.
- **R21 — `about`, `title`, `titleEn`, `part`**: unchanged. The `about` agrees with the text ("the word of Ilioneus" is already spelled right). `part` and `titleEn` carry IX.446–529.
- **R22 — The orchestrator's exact opening sentence for 9.501** ("The print has Illionei, a misprint for Ilionei, corrected here."): applied with the house's single quotes round the Latin words, and continued "; t keeps the print, …", as every published misprint note is (6.666, 8.323).

## For the owner (QUESTIONS.md)
- **Misprint (rule 5b)**: 9.501 `Illionei` for *Ilionei*. The edition has one *l* in all seven other places where the name occurs (1.120, 1.521, 1.559, 1.611, 7.212, 7.249, 9.569), and in *Ilione* at 1.653. `t` is as printed, `l`/`i` are corrected, and the note opens with the print's reading. The scan-fixes entry scans *Ilionei*.
- **Kept as printed**: 9.529 bracketed, in [ ].
- **Advisory**: none. Upheld; see R4. The ruling for Books IX–XII asked in QUESTIONS 61 would settle this part too.
- **Scansion**:
  - There are 15 entries. 9 lines were wrong, only one of them flagged; the other 6 entries are 2 half-lines and 4 carriers. After the fixes the build report should be empty.
  - **One cross-part point.** QUESTIONS 28 says 4.667 *femineo ululatu* was published on the scanner's fit (long *-mī-*, synizesis *-neo*), with the hiatus parse "unconfirmed". This review holds that the hiatus parse is right, as entered here for 9.477. *fēmĭneus* has a short ĭ, so the scanner's fit gives a false quantity. If you agree, 4.667 needs the same entry and aeneid-030 a rebuild. I did not add it, since it is outside this part.
- **Unchecked attributions, all from memory**:
  - the Iliad and Odyssey places in R18
  - Ennius *quis potis ingentis oras evolvere belli* (I believe Macrobius 6.1 quotes it)
  - the *at tuba… taratantara* fragment
  - the ancient debate on *pater Romanus*
  - *funera* taken as an old feminine (now unattributed)
  - "some sixty" half-lines
- **Stale files**:
  - `make_units.py` still holds the drafter's strings, including the old `Illionei` note, so re-running it would discard this review.
  - `drafts/aeneid-068/` has no `gloss.json` yet, and the build needs one.
