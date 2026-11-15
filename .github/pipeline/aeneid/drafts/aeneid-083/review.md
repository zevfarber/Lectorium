# Review — aeneid-083 (Aeneid XI.100–224), adversarial reviewer

**Severity counts: major 4, medium 4, low 27. Refused or upheld without change: 14. Scan-fixes entries added: 16 (11.100, 11.106, 11.111, 11.115, 11.116, 11.120, 11.134, 11.148, 11.161, 11.162, 11.164, 11.168, 11.170, 11.175, 11.184, 11.186).**

All four majors are scansion findings. The one packet flag (11.170) was a wrong fit. Fifteen wrong lines were not flagged:
- four with initial Ae- split or misdivided;
- five with Teucri split;
- four with wrong quantities but the right syllable count;
- two with the wrong syllable count.

## How the review was done

**Pass 1** went through all 69 units word by word. I checked:
- `l`, `i` and `n` against the Latin;
- every grammatical label and every elision list;
- every cross-reference;
- the speech marks, the Latin Library variants, `about`, `title`, `part`, `titleEn` and the `p` flags (100, 139, 182, 203: right).

**Sources.** I used the Latin, the pinned source and memory of the public-domain references. No translation was opened.

**Pass 2:**
- I re-read every field that pass 1 changed.
- I re-read all `l` for misattached words. This gave the `l` fixes at 21, 25, 52, 55, 60, 61 and 65 and the label fix D4.
- I re-read all `i` for distinctive remembered phrasing. This gave the recasts at 108, 182 and 188.
- I restored the drafter's file and re-ran `review_edits.py` from it once, with all edits in one script: 33 replacements, each old string asserted to occur exactly once.

**Checks in the script and against a copy taken before any edit:**
- `t`, `ln`, `p`, `v` and the top-level fields are unchanged.
- Only `l`, `i` and `n` changed, in 32 fields.
- `l` has as many lines as `t`, and no `i` has a line break.
- Notes run 15–139 words.
- `l` and `i` each have 3 “ and 3 ”, as `t` does.

**What was edited, and how:**
- **`units.json`** was edited only by `review_edits.py`, written with `aeneid_lib.jdump`. The drafter's file round-tripped byte-identically.
- **`make_units.py` was not touched.** It still holds the drafter's strings, so build from `units.json` and do not rerun `make_units.py`.
- **`scan-fixes.json`** was appended to by a copy of 082's `add_scan_fixes.py`, with this part's `NEW` table, kept in the session scratchpad: I was not to add files to the draft folder. The script checks each entry against:
  - the build's word-match rule;
  - the validator's metre rule;
  - the syllable count stated in its `why`.

  The 986 earlier entries are unchanged and in order, and there are now 1002.
- **Replica of 082's `scan_check.py`** (part id changed; also in the scratchpad). With the fixes applied, the build's scansion step and the validator's metre check give:
  - `sc` on all 69 units;
  - no report left (the 11.170 COSTLY flag is cleared);
  - no metre failures;
  - no misaligned units.
- **Build not run**, as instructed.

## Scansion

I hand-scanned all 125 lines and compared each one syllable by syllable with the scanner. There are no half-lines and no hypermetric lines in this part.

**Packet flag:**
- **11.170 (COSTLY 2.2, bracketed): wrong.** The scanner split the initial Ae- of *Aeneas*. The line reads *quam pĭŭs | Aenē | ās et | quam mag | nī Phrўgĕs | et quam* (14 syllables).

**Unflagged lines that are wrong (15):**
- **Initial Ae- split (cost 1.2):** 106, 120 and 184 (*Aeneas*).
- **Initial Ae- misdivided (cost 0.0):** 115 *Aequius huic*. The scanner divided *Aequ-ius* and *hu-ic*. The quantities come out the same by accident, but the syllables and the audio do not.
- **Greek eu split:** 116, 134, 164, 168 and 175 (*Teucri/Teucros*). Line 134 has 13 syllables, with four spondees before the fifth-foot dactyl.
- **Wrong quantities with the right count (cost 0.0):**
  - 100: *ōrātōrēs ădĕrant*. The scanner had *ŏrătōres ādērant*.
  - 111: *ōrātīs? ĕquĭdem*. The only fit lengthens *-tis* in the arsis at the pause after the question, as at 1.314 and 7.174. The scanner had *ōrătĭs Ēquī-*.
  - 148: *nōn Ēvandrum*, as at 11.55.
  - 162: *tēlīs ănĭmam*. The scanner had *tĕlĭs Ānīmam*.
- **Wrong syllable count:**
  - 161: *Trōŭm* is two syllables, and *gĕnĭtor* has short *ge-* and *-ni-*. The scanner made *Troum* one syllable and lengthened *ge-* and *-ni-*.
  - 186: *subiectis*, with consonantal i after the prefix: *sūb-iēc-tīs*. The scanner read *su-bi-ec-tis*.

**Lines hand-checked and right:**
- **Evander (Greek eu, written E-):** 140, with long Ē.
- **Consonantal i:**
  - 158 *coniunx*;
  - 194 *coniciunt* (*cōnĭcĭunt*);
  - 125 *Troiane* and 131 *Troiana*.
- **Ae- and ae inside words:** 104 *aethere*, 125 *aequem*, 174 *aetas*.
- **Hiatus:** none in the part.
- **Interjection *O*:**
  - At 124 (*refert: O fama*) and 152 (*haec, O Palla*) it stands unelided, as an interjection does.
  - At 158 *Tuqu(e) O* the *-que* elides into it. The scanner has all three right.
- **Other points:**
  - 152 and 169 *Pallā*: the Greek vocative has a long final a, which the scanner's fit gives.
  - 174 *ĭdem*: neuter, with *robur*.
  - 197 *bŏŭm*.
  - 200 *sēmusta*.
  - 217 *Turniqu(e) hymenaeos*.
  - 219 *Ītaliae*.
  - 151 *dolore est* and 178 *tua est* (prodelision): the scanner elides the vowel before *est* instead of the *e* of *est*. The count is the same, and the house leaves this alone (7.263).

**Cosmetic only (no entry):** the caesura placement at 207, 212 and 214. The quantities are right in all three.

| key | reason (short) |
|---|---|
| 11.100 | quantities *ōrātōrēs ădĕrant*; 14 syllables |
| 11.106 | Ae- one syllable; 14 |
| 11.111 | *ōrātīs* lengthened at the pause, *ĕquĭdem*; 14 |
| 11.115 | *Ae-quĭ-ŭs*, *huic* one syllable; 15 |
| 11.116 | *Teu-* one syllable; 14 |
| 11.120 | Ae-, *Ill(i) obstipuere*; 15 |
| 11.134 | *Teu-*; 13 |
| 11.148 | *nōn Ē-*; 14 |
| 11.161 | *Trō-ŭm* two syllables, *gĕnĭtor*; 15 |
| 11.162 | *tēlīs ănĭmam*; 16 |
| 11.164 | *Teu-*; 14 |
| 11.168 | *Teu-*; 15 |
| 11.170 | bracketed; Ae-; flag cleared; 14 |
| 11.175 | *Teu-*; 14 |
| 11.184 | Ae-; 14 |
| 11.186 | *sub-iec-tis*, consonantal i after the prefix; 15 |

Every `why` gives the scansion foot by foot.

## Changes

**Major (scansion, scan-fixes.json only)**
- **M1.** Initial Ae- was split at 106, 120, 170 and 184, and misdivided at 115 (*Aequius*). Only 170 was flagged.
- **M2.** *Teucri/Teucros* had the eu split at 116, 134, 164, 168 and 175. None was flagged.
- **M3.** Wrong quantities with the right count at 100, 111, 148 and 162. None was flagged.
- **M4.** Wrong syllable count at 161 (*Troum* contracted, *genitor* lengthened) and 186 (*subiectis*). Neither was flagged.

**Medium**
- **D1. Unit 100–101, note: wrong cross-reference.** The note said "as in Evander's welcome of the Trojans (VIII.116)". At VIII.116 it is Aeneas who holds out the olive branch, to Pallas, on reaching Pallanteum. Corrected.
- **D2. Unit 177–179, note and `i`.**
  - The note called the *quod… moror* clause "a 'quod' clause as subject". It is not the subject of *causa est*. It states the fact that *causa* accounts for. Corrected.
  - `i` began "If I drag out a life…", which turned the fact into a condition. It is now "That I still drag out a life I hate, now that Pallas is dead, has one reason: your right hand…".
- **D3. Unit 149–151, note.** "loosed 'dolore', 'by grief', which had choked it" contradicted itself. *dolore* is now given as an ablative of cause with *vix*: the way was scarcely opened, for grief.
- **D4. Unit 156–158, note and `l`.**
  - The note had "'iuvenis', genitive, with 'miserae'". *miserae* agrees with *Primitiae*, not with *iuvenis*. Corrected.
  - `l` had "of the young man wretched", which gave *miserae* to the young man. It now reads "First-fruits of the young man, wretched ones, and of war close at hand".

**Low: notes**
- **L1. 110–111.** Added that *ōrātīs* is lengthened at the pause, to match the new scan-fix.
- **L2. 113–114.** *nostra… hospitia* now reads "split across the line-end", not "frame the line-end" (082 L5 wording).
- **L3. 118.** The note read "'vixet', Greenough's 'vixet'… an old form Virgil keeps once here".
  - *vixet* is the transmitted reading, not a Greenough peculiarity.
  - "once" could not be verified.
  - Now: "a syncopated (shortened) form… an old form".
- **L4. 119.** *miseris… civibus* do not frame the line. They enclose *supponite*.
- **L5. 135–138.** *Ferro… bipenni* enclose the second half of 135. It is not a "line-end" frame.
- **L6. 149–151.** "The Latin Library and many editors read 'Pallante reposto'" is now "The Latin Library reads… (so too, from memory, most modern texts)". This marks an unverified claim as unverified.
- **L7. 152–153.** Added that *Palla* has a long final -a here, as the metre shows.
- **L8. 161–162.** *obruerent* is now "imperfect subjunctive where prose would have the pluperfect". The past-wish sense was already given.
- **L9. 169–171.** "without them, 'alio' means 'than this one'" is now "'non alio' means 'with no other (funeral) than this one'".
- **L10. 176.** *regi*: "now king of the Trojans and the Etruscan alliance" is now "king of the Trojans and now leader of the Etruscan alliance". Aeneas is the Etruscans' leader (X.156 *externo commissa duci*), not their king.
- **L11. 184–185.** Tarchon was called "Aeneas's ally since Book VIII". The alliance is offered in VIII and sealed at X.153–154 (checked in the source). The note now says so.
- **L12. 203–204.** *miseri… Latini* do not frame the line. They enclose *diversa in parte*.
- **L13. 211–212.** *confusa… ossa* now reads "split across the line-end".
- **L14. 222–224.** *multa… fama* do not frame the last line. They enclose *virum meritis sustentat*.

**Low: `l` construal and layout**
- **L15. 116–117.** "it was fitting to have met" is now "it was fitting to clash". *concurrere* is a present infinitive.
- **L16. 130–131.** "on shoulders Trojan" is now "on shoulders, Trojan ones". *Troiana* goes with *saxa*.
- **L17. 139–141.** "of so great a forerunner grief" is now "of so great, the forerunner, a grief".
- **L18. 188–190.** "the grieving of the funeral fire" is now "the grieving, of the funeral, fire". *maestum* goes with *ignem*.
- **L19. 193–195.** "from the slain stripped Latins" is now "from the slain, stripped, Latins". *derepta* goes with *spolia*.
- **L20. 204–208.** "a huge slaughter heap" is now "of confused, a huge, of slaughter, heap".
- **L21. 208–209.** "with frequent shine fires" is now "with frequent, shine, with fires".
- **L22. 215–217.** "the dire curse war" is now "the dire they curse, war". The line had lost its verb's subject and read as a noun phrase.

**Low: `i` accuracy and echo recasts**
- **L23. 154–155.** "how strong is the pull of fresh glory…, and how sweet the honour" drifted from *quantum… posset*, which governs both subjects. Now "what power new glory in arms has, and the honour, so sweet, of a first battle".
- **L24. 215–217.** "boys robbed of their fathers" is now "of their parents" (*parentibus*).
- **L25. 108–109.** "What undeserved misfortune, Latins, has entangled you in so great a war" is close to a remembered older version. Now "Latins, what fortune you never deserved has caught you up in so great a war".
- **L26. 182–183.** "the Dawn had brought out her kindly light for unhappy mortals, bringing back… work and toil" is close to a remembered version. Now "Dawn had lifted her life-giving light over suffering mortals, and with it brought back their tasks and their toil".
- **L27. 188–190.** "girt in gleaming armour… ran round the burning pyres" echoes a familiar phrasing. Now "Three times, belted in their shining armour, they ran their course round the burning pyres".

## Refused or upheld without change

1. **220 lowercase `ingravat` after a stop.** Upheld as a rule-5b misprint. It has the same handling and note opening as 7.290, 8.9 and 9.683, under the open QUESTIONS item 43.
2. **149 `Pallanta reposto`.** Kept as printed, as a doubtful reading, not a misprint. The printed text construes: *feretro reposto*, with *super* governing *Pallanta*. The note gives both readings, and the sense is unchanged (L6 softened only the claim about editors).
3. **173 `in armis`.** Kept. The Latin Library reads *in arvis*. Greenough's reading is translated and the other is noted. Both construe, so this is not a misprint.
4. **124 `i`, "great in fame and greater still in arms".** Kept. It is literal, and any close version takes this shape.
5. **199–202 `i`, "could not tear themselves away… set thick with blazing stars".** Kept. The first is the Latin itself, and the second is not a stock phrase.
6. **192 `i`.** Kept. It agrees with the published 2.313 (aeneid-012).
7. **120–121 *conversi oculos… atque ora tenebant*.** The note treats *oculos* as an accusative of the part with *conversi*, and lets *tenebant* govern too. Kept: it is defensible, and the note says how it is taken.
8. **122–123 *odiis et crimine*, "ablatives of manner".** Kept. Cause would also do, and the sense is the same.
9. **112 *Nec veni, nisi… dedissent*, "indicative for vividness".** Kept.
10. **166–168 *Volscorum*, "perhaps standing for the enemy at large".** Kept. It is hedged.
11. **210 note, "The bodies have burned for two days".** Kept. It follows from *Tertia lux*.
12. **151 and 178 prodelision.** No entries. The scanner's elision gives the same count (house practice, 7.263).
13. **152 and 169 *Pallā*.** No entries. The scanner's own fit has the long -ā.
14. **Caesura placement at 207, 212 and 214.** No entries. This is cosmetic, as at 080–082.

## Cross-references

**Checked in the pinned source, all right after D1 and L11:**
- VIII.116: Aeneas's olive branch (D1).
- VIII.169: the right hand joined in alliance.
- XI.35: *crinem… solutae*.
- XI.45: *Non haec… promissa*.
- XI.54–55: Aeneas's exclamations.
- XI.60–63: *mille viros*.
- XI.83–84: the trophies.
- II.313: the same half-line as 192.
- VI.179–182: woodcutting with *ornos* and *cuneis*.
- IV.173ff: Fama.
- X.153–156: Tarchon's alliance (L11).

**Unchecked, from memory, and agreeing with the drafter:**
- Iliad 7: the Trojan embassy for a burial truce.
- Iliad 23: the wood for Patroclus's pyre.
- Iliad 23.13: three times round Patroclus.
- Iliad 23.15: sand and armour wet with tears.
- Homer's "wretched mortals".

These are plausible and stated plainly. None needed softening.

## For the owner

- **Rule-5b misprint.** 11.220 `ingravat`, lowercase after the full stop ending 219 (QUESTIONS item 43 pattern). The publishing run should add the QUESTIONS.md entry; the reviewer may not touch QUESTIONS.md.
- **Doubtful readings kept as printed:**
  - 11.149 `Pallanta` (Latin Library `Pallante`);
  - 11.173 `armis` (Latin Library `arvis`).

  If either is ruled a misprint, only the opening of that note changes.
- **Bracketed lines.** 11.170–171 are kept in [ ] in `t`, `l` and `i`. The note of unit 169 says what changes with and without them.
- **Quantities resting on the metre:**
  - 11.111 *ōrātīs*, lengthened at the pause;
  - 11.152 and 11.169 *Pallā*.
- **Unchecked attributions.** See Cross-references above.
- **Build.** Not run. Build from `units.json` as it stands, and do not rerun `make_units.py`.
