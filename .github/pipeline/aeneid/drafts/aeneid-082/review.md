# Review — aeneid-082 (Aeneid XI.1–99), adversarial reviewer

**Severity counts: major 4, medium 4, low 17. Pass 2 found 2 of the low findings (L16, L17) and revised the `l` fix of D4. Refused or upheld without change: 12. Scan-fixes entries added: 9 (11.2, 11.4, 11.31, 11.36, 11.55, 11.58, 11.73, 11.92, 11.95).**

All four majors are scansion findings. Two packet flags (11.31, 11.58) were wrong fits, and the third (11.4) was right. Six wrong lines were not flagged: four with initial Ae- split, one with Teucri split, and one with wrong quantities.

## How the review was done

**Pass 1** went through all 46 units word by word. I checked:
- `l`, `i` and `n` against the Latin
- every grammatical label and every elision list
- every cross-reference
- the speech marks, the Latin Library variants, `about`, `title`, `part`, `titleEn` and the `p` flags (1, 29, 59: right)

**Sources.** I used the Latin, the pinned source, and memory of the public-domain references. No translation was opened.

**Pass 2:**
- I re-read every field that pass 1 changed, and re-read all `l` for misattached words, which gave L16 and L17 and a better `l` for D4.
- I then restored the drafter's file and re-ran `review_edits.py` from it, with all the edits in one script (24 replacements, each old string asserted to occur exactly once).
- A script then checked the following against a copy taken before any edit:
  - `t`, `ln`, `p`, `v` and the top-level fields are unchanged.
  - Only `l`, `i` and `n` changed, in 21 fields.
  - `l` has as many lines as `t`, and no `i` has a line break.
  - Notes run 44–123 words.
  - `l` and `i` each have 5 “ and 5 ”.
  - No translator's name appears.

**What was edited, and how:**
- **`units.json`** was edited only by `review_edits.py`, and written with `aeneid_lib.jdump`. The drafter's file round-tripped byte-identically.
- **`make_units.py` was not touched.** It still holds the drafter's strings, so build from `units.json` and do not rerun `make_units.py`.
- **`scan-fixes.json`** was appended to only by `add_scan_fixes.py` (081's script with a new `NEW` table). The 977 earlier entries are unchanged and in order, and there are now 986.
- **`scan_check.py`** is 081's helper with the part id changed. With the fixes applied, the replica of the build's scansion step and the validator's metre check gives:
  - `sc` on all 46 units
  - no report left
  - no metre failures
  - no misaligned units
- **Build not run.** `build_aeneid.py` has no dry-run or `--help` option: it reads `sys.argv[1]` as the part id and always writes its output.

## Scansion

I hand-scanned all 99 lines and compared each one syllable by syllable with the scanner. There are no half-lines and no hypermetric lines in this part.

**Packet flags:**
- **11.4 (COSTLY 2.0): the scanner is right.** The line reads vō-tă dĕ | um prī | mō vic | tor sōl | vē-băt Ĕ | ō-o. *deum* is two syllables, and *Eōō* has a short E-, as at 3.588 (the same line-end) and 6.831. I made an entry only to clear the flag, as at 9.811.
- **11.31 (COSTLY 2.0): wrong.** The scanner made *sĕnĭor* long-long and ran *-o E-* into one short syllable. The line has a hiatus, *Parrhasiō Ēvandrō*, and a spondaic fifth foot.
- **11.58 (COSTLY 2.0): wrong.** The scanner made *Iu-* consonantal and *-dis* long. *Ĭūle* has three syllables (house practice), so the fifth foot is a dactyl, *per-dĭs Ĭ | ū-le*.

**Unflagged lines that are wrong (6):**
- **Initial Ae- split (cost 1.2):** 2, 36, 73 and 95 (*Aeneas*).
- **Greek eu split (cost 0.0):** 92, *Teucrique*, where the scanner counted 16 syllables.
- **Wrong quantities with the right count (cost 0.0):** 55, *Haec mea magna fides! At non, Evandre*. The scanner made *-nă* and *fĭ-* long, and *nōn* and *Ē-* short.

**Lines hand-checked and right:**
- **Ae-:** 89 *Aethon*.
- **Evander (Greek eu, written E-):** 26 and 45, with long Ē.
- **Consonantal i after a prefix:** 87 *proiectus*.
- **Other points:**
  - 25, 61 and 76 *supremus*: *su-* is short at 25 and long at 61 and 76, which is position before *pr* (mute and liquid). The scanner has all three right.
  - 70 *cui*, one syllable.
  - 69 *hyacinthi*.
  - 57 *Ei*, one syllable.

**Cosmetic only (no entry):** 56 *ads–pi*. The caesura at 96 falls after *ad*. The quantities are right in both lines.

| key | reason (short) |
|---|---|
| 11.2 | Ae- one syllable; *quamqu(am) et*; 15 syllables |
| 11.4 | Scanner confirmed (COSTLY 2.0); short E of *Eoo* as 3.588; 14 syllables |
| 11.31 | Hiatus *Parrhasiō Ēvandrō*, spondaic fifth foot, *sĕnĭor*; 14 syllables |
| 11.36 | Ae-, *ver(o) Aeneas*, *ses(e) intulit*; 14 syllables |
| 11.55 | Quantities *magnă fĭdēs*, *nōn Ē-*; 15 syllables |
| 11.58 | *Ĭūle* three syllables, *perdĭs*; 15 syllables |
| 11.73 | Ae-; 14 syllables |
| 11.92 | *Teu-* one syllable; 15 syllables |
| 11.95 | Ae-, *gemitū-qu(e) haec*; 15 syllables |

Every `why` gives the scansion foot by foot. `add_scan_fixes.py` checks each entry against the build's word-match rule, the validator's metre rule and the syllable count stated in its `why`.

## Changes

**Major (scansion, scan-fixes.json only)**
- **M1.** Initial Ae- was split at 2, 36, 73 and 95. None of these was flagged.
- **M2.** *Teucrique* at 92 had the eu split. Not flagged.
- **M3.** 55 had wrong quantities with the right count. Not flagged.
- **M4.** The packet flags at 31 and 58 were wrong fits (see Scansion).

**Medium**
- **D1. Rule-5b placement at 97/98.** The drafter put "The print has 'vale. ”Nec'…" in unit 98 and "see the next unit" in unit 97, citing 081. That is 081's *drafter* placement, which 081's reviewer reversed (081 review D5) to match 077, 078 and 080. Changed to match:
  - The note of unit 97 now opens with the print's reading.
  - The note of unit 98 now opens "The closing speech mark printed at the head of this unit belongs to Aeneas's speech (see the note before)."
- **D2. Unit 24, `i` speech marks.** `i` began “Go,” he said, “and honour…, which reopened a speech already open since 14. `i` had 6 “ against 5 ”. The leading “ is removed, as in `l` and as at 7.121 (aeneid-050). `l` and `i` now balance 5/5.
- **D3. Unit 67, note, elision list.** The note said "No elisions", but line 67 has *iuven(em) agresti*. Corrected.
- **D4. Unit 55–57, `l`.** "will you pray for, for your son, death" construed *nato* as a dative. It belongs to the ablative absolute *sospite… nato*. `l` now reads "nor, with safe, a dread / will you pray for, your son, death, as a father". `i` and the note were already right.

**Low: labels and notes**
- **L1. Note 2–4.** Added that *et… -que* means "both… and"; `l` shows "both" without explaining it.
- **L2. Note 5–8.** *Mezenti* was called "Greenough's genitive". The single *-i* is Virgil's regular genitive for names in *-ius*, so it is now described that way.
- **L3. Note 18–21.** *adnuerint* was labelled "future perfect". Inside the purpose clause it is a perfect subjunctive standing for a future perfect (the two forms are the same). The note now says so.
- **L4. Note 29–33.** Added the spondaic fifth foot to the hiatus note, to match the new scan-fix.
- **L5. Note 36–38.**
  - *tunsis… pectoribus* now reads "split across the line-end", not "framing the line-end" (081 L6 wording).
  - *regia* was glossed "the hall where the king's son lies". It now reads "Aeneas's quarters in the camp, where Pallas lies".
- **L6. Note 55.** The note said each of the three exclamations starts with a demonstrative, but 53 *Infelix* does not. It now reads "the last two".
- **L7. Note 86–87, `terrae.~.~.`.** The rule-5b opening is kept. The note now adds that the marks are probably a slip of the electronic text, not of Greenough's page. I removed "the owner may know what they stand for", which addressed the owner inside a reader's note.
- **L8. Note 98–99.** *altos… muros* now reads "split across the line-end", not "framing the line-end".

**Low: `l` construal and layout**
- **L9. 12–13.** *ovantis* goes with *socios*, but "he urges, exulting" read as if it described Aeneas. Now "he urges them, exulting as they were".
- **L10. 34–35.** "the grieving Trojan women" gave *maestum* to the women. Now "as to their grieving hair".
- **L11. 67–70.** "a girl's reaped thumb" is now "a girl's thumb reaped".
- **L16 (pass 2). 39–41.** "on the smooth gaping breast" attached *patens* to the breast. Now "gaping on the smooth breast, the wound".
- **L17 (pass 2). 78–79.** "the Laurentine prizes of the battle" attached *Laurentis* to the prizes. Now "of the Laurentine, prizes, of the battle".

**Low: `i` echo recasts and register**
- **L12. 5–8.** "a trophy to you, great lord of war" is a familiar phrasing. Now "a trophy for you, great god, mighty in war".
- **L13. 42–44.** "Poor boy… Fortune grudged me, just when she came to me smiling" is now "Pitiable boy… was it you that Fortune, coming to me in gladness, begrudged me". This is also consistent with 081's *miserande puer*.
- **L14. 55.** "So much for my solemn pledge!" is now "This is what my great pledge has come to!"
- **L15. 97–98.** "and for all time I say goodbye" is too casual for the register. Now "I bid you farewell". The stock phrase "hail and farewell for ever" is still avoided.

## Refused or upheld without change

1. **24 `“Ite, ait,` as a rule-5b misprint.** Kept. It has the same handling and note opening as 6.46, 6.52, 7.121 and 8.499 (QUESTIONS item 44). `l` already had the right marks.
2. **87 `~.~.` treated as a misprint.** Kept as rule 5b, with the note softened (L7). The marks appear nowhere else in the poem. Whether they encode something (a lacuna sign?) could not be checked against the TEI.
3. **26–28 `i`, "whom a black day carried off".** Kept. It matches the published house rendering of the identical line VI.429 (aeneid-044).
4. **54 `i`, "So this is our homecoming, this the triumph we looked for!"** Kept. It is literal, and any close version takes this shape.
5. **59–63 `i`, "a small comfort for so great a grief".** Kept. It is generic.
6. **76–77, `i` "with the other" against the note's "probably the second of the pair".** Kept. `i` has to choose, and the note gives the doubt.
7. **22 hendiadys and 14–15 *quod superest* taken with what precedes.** Kept. Both are defensible, and the notes say how they are taken.
8. **82 *sparsuros*.** Kept, with the Latin Library's *sparsurus* noted, as the drafter had it.
9. **37 *foribus* (way, or dative).** Kept.
10. **Cosmetic syllable division at 56 and the caesura at 96.** No entries, as 080 and 081.
11. **25, 61 and 76 *supremus*.** No entries. The scanner handles the variable *su-* correctly.
12. **Advisory.** None added. The captives for sacrifice (81–82) are stated, not described, and Acoetes's mourning gestures take two words.

## Cross-references

**Checked in the pinned source, all right:**
- VI.325–330: the unburied wait a hundred years (329).
- VI.429: the same line as 28.
- X.479–489: Turnus's spear through the shield, corslet and chest (482–485).
- X.495–500: the belt.
- X.517–520: four plus four young men taken alive for sacrifice.
- XII.940–952.
- IV.264: identical to 75 except for a comma.
- IX.435–437: the cut flower and the poppies for Euryalus.
- VIII: the Etruscan command, 503–507.

**Unchecked, from memory, and agreeing with the drafter:**
- Iliad 8.306–308 (the poppy)
- Iliad 8.185 (Aethon)
- Iliad 17.426–440 (the horses weep)
- Iliad 23.175–176 (twelve Trojans)
- Catullus 101.10
- "an old-fashioned compound of the kind Ennius made" (*bellipotens*)

These are plausible and stated plainly; none needed softening.

## For the owner

- **Rule-5b misprints:**
  - 11.24 `“Ite, ait,`: the pattern of QUESTIONS item 44.
  - 11.98 `vale. ”Nec`: a closing mark joined to the next word.
  - 11.87 `terrae.~.~.`: unique in the source. It is probably an encoding artefact; if it means something, only the note changes.
  - The publishing run should add the QUESTIONS.md entry. The reviewer may not touch QUESTIONS.md.
- **Validator mark counts.** `t` has 4 “ and 3 ” as printed. `l` and `i` balance (5/5).
- **Doubtful quantity resting on the metre.** 11.4 *Ĕōō*, with short E- (long at 1.489).
- **Unchecked attributions.** See Cross-references above.
- **Build.** Not run (no dry-run mode). Build from `units.json` as it stands, and do not rerun `make_units.py`.
