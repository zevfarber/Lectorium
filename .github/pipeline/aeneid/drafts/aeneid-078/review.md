# Review — aeneid-078 (Aeneid X.510–605), adversarial reviewer

**Severity counts: major 4, medium 4, low 21 (16 in pass 1, 5 in pass 2). Refused or upheld-without-change findings: 14. Scan-fixes entries added: 19 (15 wrong full lines, 1 half-line, 3 carriers).**

Majors: 1 naming error carried through every layer (*Mago* is the dative of **Magus**) and 3 scansion findings (the packet flags 524, 534, 575; twelve unflagged wrong lines; the half-line 580 with its carriers).

## How the review was done

**Pass 1** covered all 51 units word by word. I checked `l`, `i` and `n` against the Latin, every grammatical label, every elision list, every "framing" claim, every cross-reference and every attribution made from memory. All 51 elision lists are right (I checked each line for vowel or -m before a vowel or h, including line-end pairs, which correctly carry none). I also checked:
- the speech marks: seven “ and seven ” in each of `t`, `l` and `i`, each on the right unit (524/528, 531/534, 557/560, 580/583, 592/594, 597–598, 599/600). Two of the closings are the rule-5b pairs 580/583 and 592/594.
- the Latin Library variants (packet list). Only 539 *armis/albis* and 585 *hostem/hostis* change the sense, and both are noted; the rest are orthography, morphology or order.
- `about`, `title`, `part` and `titleEn`.

I read every `i` for echoes of the well-known English versions and recast four (P2-2 to P2-5).

Sources: the Latin, the pinned source and memory of the public-domain reference works. No translation was opened and nothing was searched.

**Cross-references checked in the pinned source:**
- VI.364 *per spes surgentis Iuli* (Palinurus) — right.
- IX.412 *Sulmonis* — a Sulmo killed by Nisus, one of Volcens' Latin horsemen; the note called him Rutulian (L3).
- IX.454 *Serranoque Numaque* — a Numa already dead before 562 (added to L11).
- XI.5–8 *tibi, magne, tropaeum, bellipotens* — the trophy words of 542 recur (L5).
- XI.81–82 *quos mitteret umbris inferias* — the sacrifice carried out (L3).
- XII.224 *formam adsimulata Camerti* (L11).
- VII.47–48 Faunus father of Latinus; VII.678–681 Caeculus, Vulcan's son, founder of Praeneste; VII.750–753 Umbro the Marruvian priest and snake-charmer; VII.745 the leader Ufens and VII.802 the river Ufens — all right.
- X.399 *biiugis*, X.453 *biiugis*, X.492 *Euandro*; Greenough prints both *Euandr-* and *Evandr-*.
- IX.571 *Liger* (short first syllable) for the half-line scansion.

**Pass 2** re-read every edited field in full and re-checked the speech marks (7/7 in each layer), the line counts (`l` has the same number of lines as `t` in every unit, no `i` has a line break) and note lengths (35–134 words). It made changes P2-1 to P2-5.

**Scansion.** I hand-scanned all 96 lines and compared them syllable by syllable with the scanner, run in-process the way the build calls it. The helper is `drafts/aeneid-078/scan_check.py` (077's, with the part id changed).
- **Packet flags:**
  - **524 (COSTLY 2.0) is wrong.** *Iuli* is three syllables, Ĭ-ū-lī (as 1.267 *cognomen Iulo*, 6.364): Per pă-trĭ | ōs mā | nīs et | spēs sur | gen-tĭs Ĭ | ū-li (14). The scanner read *Iu-* as one syllable.
  - **528 (COSTLY 2.4) is right**, and no entry was added: in-fec | tī-quĕ mĭ | hī Non | hīc vic | tō-rĭ-ă | Teu-crum, *mihī* long, *Teucrum* with Greek eu as one syllable. The cost is only the long *mihī*.
  - **534 (COSTLY 2.0) is wrong**, *Iulus* as at 524 (14).
  - **575 (COSTLY 2.1) is wrong.** *biiugis* is bĭ-jŭ-gīs, as 077's 453: In-tĕ-rĕ | ā bĭ-jŭ | gīs in | fert sē | Lū-că-gŭs | al-bis (15).
  - **580 (UNRESOLVED) is a half-line**, *Cui Liger* (3 syllables), handled as 077's 490. **Carriers 581, 582, 583** share unit 580–583 with it; the scanner is right on all three, but without the entries the unit gets no `sc`.
- **Unflagged lines that are wrong:**
  - **Initial Ae- split (cost 1.2, no flag):** *Aeneae* 511; *Aeneas* 530, 569, 578, 591, 599. The scanner wrote A-e as a dactyl; the published Book X entries (10.25, 10.48, 10.159…) all fix the same thing.
  - **Greek eu split (cost 0.0):** *Euander* 515 (*Pal-lās Eu | an-dĕr ĭn*).
  - **Consonantal i run together (cost 1.5):** *quadriiugis* 571 (quā-drĭ-jŭ-gīs, 16 syllables), *biiugos* 587 and 595.
  - **Wrong quantities with the right count (cost 0.0):** **536** (*cervīce*, *ōrantis*, *căpŭlō*; the scanner had *cervĭce*, *ŏrantis*, *cā-pū-*) and **538** (*sacrā* ablative with *vitta*, its *sa-* long by position, and *rĕ-dĭ-mī-bat*; the scanner had *să-cră* and *rē-dī-*, which *redimio* cannot have).
- **Checked and right as the scanner reads them:**
  - Teucri: *Teucris* 512, *Teucrum* 528; *Aegaeon* 565 (Ae-gae-ōn, the line spondaic to the fourth foot)
  - consonantal i after a prefix: *deiecerat* 546 (dē-jē-cĕ-răt), *proiecto* 587 (prō-jec-tō), *adiit* 517 (vowel i, ă-dĭ-ĭt), *Troiane* 598
  - *Troïus* 584 (Trō-ĭ-ŭs), *Iovis* 567 (one syllable, *Jŏ-*), *cui* (one syllable) 530, 538, 565
  - *genu(a) amplectens* 523 (elided, *gĕnŭ* two shorts); *linquēre* 559 (the future, as the note says); *vertēre* 593; *Ligerī* 584; *ācer* 577; *retrō* 573 (*re-* lengthened before *tr*)
  - **557 *iace* (cost 0.6)**: the only fit has the final *-ĕ* counting long under the beat at the full stop (*ĭ-ă | cē Nōn*). Accepted, and the note now says so (L9).
  - There is no hiatus in the part.

Every entry was checked by `drafts/aeneid-078/add_scan_fixes.py` (077's, with the part id and entries changed; dry run, then `--write`):
- against the build's word-match rule
- against the validator's metre rule (the half-line rule for 580)
- against the syllable count stated in its own `why` (the dry run caught one miscount in my 582 text, corrected before writing)

A replica of the build's scansion step, reading `scan-fixes.json`, gives these results:
- all 19 entries apply
- **all 51 units get `sc`**
- no unit's `sc` is out of line with its words
- no line fails the metre check
- the only report left is the correct COSTLY fit at 528

**What was edited, and how.**
- **Scripts.** `units.json` was edited only by `review_edits.py` (pass 1: the *Mago* → *Magus* rename, 17 occurrences across `l`, `i`, `n` and `about`, plus 27 edits, one of them to `about`) and `review_edits_pass2.py` (pass 2: 5 edits). Each old string was asserted to occur exactly once in its field. The file was written with `aeneid_lib.jdump`; the drafter's file round-tripped byte-identically before any edit.
- **Untouched fields.** `t`, `ln`, `p` and `v` were checked by script against a copy taken before any edit, and are unchanged in all 51 units. `title`, `titleEn` and `part` are unchanged.
- **`make_units.py` was not touched.** It still holds the drafter's strings (including "Mago"), so build from `units.json` as it stands and do not rerun `make_units.py`. `drafter-notes.md` also still says "Mago".
- **`scan-fixes.json`.** The change only appends (210 insertions, 0 deletions), with new keys after 10.492 in line order.
- **Build and validator not run** (left to the run).

## Changes — pass 1

### Major
- **M1. The name Magus (521 onward).** *Inde Mago… contenderat hastam*: *Mago* is the dative of **Magus**, -ī (Aeneas aims at him). The draft called the man "Mago" in `l`, `i`, `n` and `about` (17 times, units 521, 522, 524, 526, 528, 530, 531, 534, 535, 597 and `about`). All are now "Magus"; the note at 521 reads "'Mago', dative of 'Magus' (second declension), 'at Magus'". The run had already corrected the glossary entry.
- **M2. Packet flags 10.524, 10.534, 10.575.** See Scansion.
- **M3. Twelve unflagged wrong lines**: 10.511, 515, 530, 536, 538, 569, 571, 578, 587, 591, 595, 599. See Scansion.
- **M4. 10.580**, the half-line, with **carriers 10.581, 10.582, 10.583**. See Scansion.

### Medium
- **D1. Notes 570–571 and 575–576, *quadriiugis* / *biiugis*.** "the consonantal 'i' written double" / "the doubled consonantal 'i'" is false: these are *quadri-* / *bi-* + *iugum*, a vowel *i* then a consonantal *i*. Now: "'quadri-' + 'iugum': the first 'i' a vowel, the second a consonant, so qua-dri-iu-gis, four syllables" and "'bi-' + 'iugum', bi-iu-gis, three syllables, 'bi-' short and the second 'i' a consonant, as at 571 and at 399 two parts back". The 575 note also said *biiugis… albis* frames the line, but *Interea* comes first; now "enclosing 'infert se Lucagus'".
- **D2. 572–574, *longe gradientem*.** The note read "striding long, with great steps" (rightly: Homer's hero coming on with long strides), but `l` ("from afar striding") and `i` ("striding at them from far off") read *longe* as "from far". `l` and `i` now follow the note ("with long strides advancing"; "coming on with long strides and roaring terribly"), and the note names the Homeric phrase without a line reference.
- **D3. Note 547–549, *vimque adfore verbo* (drafter's open point).** "Perhaps a spell or a vow is meant, a word with power in it" has no support that I can vouch for. Replaced with the plain sense: "That is, he trusted that what he boasted would come true."
- **D4. Note 537–539.** Greenough's old imperfect *redimibat* (= *redimiebat*) was not explained, and the scansion (M3, 538) shows *sacra* is the ablative with *vitta*. Both are now in the note. `l` already read "with sacred ribbon".

### Low
- **L1. `l` 510.** "And now no rumour" blurred *Nec iam*; now "And no longer a rumour".
- **L2. Note 510–512.** *tenui discrimine leti* is not an "ablative of measure"; now "an ablative describing their situation… the dividing line, here between life and death".
- **L3. Note 517–520.** The Sulmo of IX.412 is one of Volcens' Latin horsemen, not called Rutulian; now "a Sulmo is killed in Book IX, IX.412". Added XI.81–82 for the sacrifice and "(VII.802), not here the leader Ufens of VII.745" (wording finished in P2-1).
- **L4. Note 535–536.** "*Sic fatus*… the deponent participle with present sense" contradicted its own gloss "having so spoken" (as 077 L4); now "active in meaning like all deponents".
- **L5. Note 541–542.** Added that the trophy words come back at XI.7–8 (*tibi, magne, tropaeum, bellipotens*), verified.
- **L6. Note 545–546.** *totum… orbem* does not frame the line (*et* first); now "enclosing 'clipei ferro deiecerat'".
- **L7. Note 552–553.** "he draws it back to throw" claimed more than *reducta* says; now "for the stroke".
- **L8. `i` 554–556.** *deturbat caput* with *truncum* is a beheading; "struck his head to the ground" is now "struck his head off to the ground".
- **L9. Note 557.** Added that *iace*'s final *e* counts long at the pause, as the `sc` will show.
- **L10. `i` 557–558.** "No loving mother" lost *optima mater*, "your excellent mother" (the note's irony); now "Your fine mother will not lay you in the earth".
- **L11. Note 561–564.** "A Camers appears alive again in Book XII" overstated XII.224, where Juturna takes his form; now stated exactly, with the Numa already killed at IX.454, "small inconsistencies in a poem left unrevised at Virgil's death". The Amyclae story is now "an old story told by the ancient commentators" (it is Servius's; see QUESTIONS).
- **L12. `l` 565–568.** "from fifty mouths fire / and breasts blazed" made *pectora* a subject; now "and from breasts blazed".
- **L13. Note 580–583.** In Iliad 5 Sthenelus drives off Aeneas's horses at Diomedes' order; "Diomedes… took his horses" is now "his horses were taken".
- **L14. Note 586–589.** *telo* softened (drafter's doubt): "probably the sword he was whirling (577), used in place of a whip".
- **L15. Note 594–595.** Liger is not "left helpless in it": he slips down from the chariot (596). Now "cannot escape".
- **L16. `about`.** "the one boasting, the other begging" was wrong (Liger does both; Lucagus speaks not at all); now "in one chariot, Liger first boasting, then begging". *Mago* renamed under M1.

## Changes — pass 2
- **P2-1. Note 517–520.** The pass-1 insertion left the tense clause dangling; now "…of VII.745; the present tense is for their home country."
- **P2-2. `i` 510–512 (echo).** "a surer messenger who speeds to Aeneas… a hair's breadth" is close to stock versions; now "It is no longer mere rumour of the disaster: a more certain informant speeds to Aeneas with word that his men are within a hair of death, and that it is time to help the routed Trojans."
- **P2-3. `i` 557 (echo).** "Lie there now" is the stock English of this line and of its Homeric model; now "Lie where you are now, you dreaded warrior."
- **P2-4. `i` 559–560 (echo).** "hungry fish will lick your wounds" is stock; now "fish that have gone unfed will lap at your wounds".
- **P2-5. `i` 569–570a (echo).** "raged in victory over the whole field, once his blade had grown warm" is close to stock; now "so, once his sword-point had grown warm, Aeneas raged his fill across the whole plain, a conqueror."

## Refused or upheld without change
1. **Rule 5b at 583 and 594 (`terris. ”Vesano`, `deseris. ”Haec`). Upheld.** Each first note opens with the required sentence; the stray ” begins the next unit's `t`; `l` and `i` close the speech on the unit ending *terris.* / *deseris.* and carry no mark in the next unit; the pair balance holds, exactly as 077's 451/495.
2. **517 *Sulmone creatos* (open point).** Upheld: the note gives father or town, both of which the Latin allows; *quos educat Ufens* as the river is right for the present tense and now cross-referenced (L3).
3. **541 *ingenti umbra* (open point).** Upheld: the note gives both readings; `i` takes the darkness of death, a legitimate choice.
4. **553 *reducta… impedit* (open point).** Upheld (spear pinning corselet and shield), with "to throw" softened (L7).
5. **585 *hostem/hostis*.** Kept: one clause, and the sense (one target or both brothers) does change.
6. **591 *pius* as "dutiful".** Upheld. Earlier parts vary; "dutiful" fits the note's point about duty to Pallas and Evander.
7. **594 *ipse rotis saliens* as a sneer; 599 *Pluribus oranti* left open.** Upheld; the notes say what the Latin allows.
8. **Advisory: none. Upheld.** `claude/content-advisory.md` is not in the repository (checked; as QUESTIONS 36 notes), so I judged on conventions.md's summary. The suppliant killings are battle killing told without lingering. The taking of eight youths for human sacrifice (517–520) is four lines, stated not described, the act itself in XI.81–82, and the note names it plainly without softening. This matches the published practice (042's sacrifice, 067–068's battle violence, no advisory). QUESTIONS item 61 (a general ruling on battle violence in IX–XII) is still open; human sacrifice should be added to that question.
9. **528 flagged COSTLY.** The scanner is right; no entry added.
10. **557 *iace* long.** The scanner's fit is the only one; no entry added (note added, L9).
11. **Note 515–517, *mensae* "plural for singular".** Upheld; a reasonable reading of Evander's feast.
12. **Note 531–532a, the relative clause "standing as the object" of *parce*.** Upheld as a loose description; *parco* in the sense "keep" with the talents as what is kept.
13. **Echo check, kept:** `i` 581–583 (as literal as the Latin forces), 597–598, 599–600 (*Die, and do not be a brother who deserts his brother* is the drafter's own turn, not a stock one).
14. **Attributions from memory, kept as written.** I am confident of each: Iliad 21.26–32 and 23.175–176 (the twelve youths); 6.45–50 (Adrastus); 21.64–96, 99–105, 122–127 (Lycaon); 1.401–404 (Briareus/Aegaeon); 5.297–327 and 20.288–340 (Aeneas saved from Diomedes and Achilles); the "more than fifty" half-lines (as 075/077).

## Scan-fixes entries added (19)
| key | reason | syllables |
|---|---|---|
| 10.511 | *Aenēae*, initial Ae- one syllable (cost 1.2, unflagged) | 15 |
| 10.515 | *Euander*, Greek eu (cost 0.0, unflagged) | 14 |
| 10.524 | *Iuli* three syllables (COSTLY 2.0) | 14 |
| 10.530 | *Aenēās* (cost 1.2, unflagged) | 14 |
| 10.534 | *Iulus* three syllables (COSTLY 2.0) | 14 |
| 10.536 | *cervīce*, *ōrantis*, *căpŭlō* (cost 0.0, unflagged) | 15 |
| 10.538 | *sacrā* ablative, *redimībat* (cost 0.0, unflagged) | 15 |
| 10.569 | *Aenēās*, *toto* elided (cost 1.2, unflagged) | 14 |
| 10.571 | *quadriiugis* four syllables (cost 1.5, unflagged) | 16 |
| 10.575 | *biiugis* (COSTLY 2.1) | 15 |
| 10.578 | *Aenēās* (cost 1.2, unflagged) | 14 |
| 10.580 | Half-line (UNRESOLVED) | 3 |
| 10.581 | Carrier for 580 (scanner right) | 15 |
| 10.582 | Carrier for 580 (scanner right) | 14 |
| 10.583 | Carrier for 580 (scanner right) | 14 |
| 10.587 | *biiugos*, *proiecto* (cost 1.5, unflagged) | 15 |
| 10.591 | *Aenēās* (cost 1.2, unflagged) | 14 |
| 10.595 | *biiugos* (cost 1.5, unflagged) | 15 |
| 10.599 | *Aenēās*, *oranti* elided (cost 1.2, unflagged) | 14 |

## For the owner (QUESTIONS.md)
- **Rule-5b misprints 10.583 and 10.594** (`terris. ”Vesano`, `deseris. ”Haec`: closing mark joined to the next word). The publishing run should add the QUESTIONS.md entry that rule 5b asks for, as for 077's 451 and 495. The reviewer may not touch QUESTIONS.md.
- **Naming:** the drafter's "Mago" (521) is the dative of Magus; corrected throughout (and in the glossary by the run).
- **Doubtful readings, both ways in the notes:** 517 *Sulmone creatos* (father or town); 541 *ingenti umbra* (death's darkness or Aeneas's shadow); 547–548 *vim adfore verbo* (now the plain sense only); 553 *impedit*; 586 *telo* (probably the sword); 599 *Pluribus oranti*.
- **Unchecked attributions:** the Amyclae silence story (Servius's, written without naming him since he is not on the list of aids); Homer's "striding long" as the model of *longe gradientem* (no line given); the version in which Aegaeon fights Jupiter; suppliants under Zeus's protection.
- **Advisory:** none. Human sacrifice (517–520, carried out at XI.81–82) is stated, not described. `claude/content-advisory.md` is still missing. Item 61 (a ruling on battle violence in IX–XII) is still open; ask the owner to say whether human sacrifice needs an advisory, which would apply here and to the Book XI part.
