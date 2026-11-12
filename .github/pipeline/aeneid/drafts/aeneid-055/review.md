# Review — aeneid-055 (Aeneid VII.601–705), adversarial reviewer

I reviewed this part in two passes.

**Pass 1** covered all 43 units, word by word. I checked `l`, `i` and `n` against the Latin, every grammatical label, every cross-reference and every historical or mythological claim. I also checked the drafter's two doubtful rule-5b calls (7.623, 7.695), the Latin Library variants (7.638 *frementis*/*trementis*, 7.684 *pascit*/*pascis* and 7.703 *ex agmine*/*examine* change the sense and are noted; the rest are spelling), and every `i` for remembered English. I worked from the Latin, the pinned source and memory of the public-domain reference works. No translation was opened and nothing was searched. In-poem cross-references were checked against the pinned source:
- I.6–7 (*genus unde Latinum, / Albanique patres, atque altae moenia Romae*) and I.293–294 (*claudentur Belli portae*)
- 7.594–600 (Latinus's refusal; *saepsit se tectis*, 600)
- X.163, which repeats 7.641 *Pandite nunc Helicona, deae, cantusque movete* word for word (added to note 641)
- the internal back-references 615, 626, 642, 651 and 655

I also checked one habit of the print by script. Of the 387 semicolons that end a line in Greenough's text, 7.623 is the only one followed by a capitalised common word (see R1).

**Pass 2** re-read every edited field in full and made two more changes (P2-1, P2-2).

**Scansion.** I hand-scanned all 105 lines by quantity. I then ran the scanner in-process, the way `build_aeneid.py` calls `SL.scan_story`, and compared it with my scansion syllable by syllable. Every new `scan-fixes.json` entry was checked against a replica of the build's word-match rule (`strip(sc) == WORD_RE.findall(line)`) and the validator's rule: six feet, 12–17 syllables, one ×, five –⏑⏑/–– feet and a sixth –×/⏑×. For the half-line, the check was the validator's half-line rule (feet 1..k with k < 6, one ×, a `why` that begins "Half-line"). Each `why` gives a syllable count, and a script checked that count against its entry. A replica of the build's scansion step, reading the fixes from `scan-fixes.json` itself, gives an **empty scanner report**: the four COSTLY flags and the UNRESOLVED half-line are all cleared. All 105 lines pass the validator's check, and **all 43 units get `sc`**. The half-line 702 closes the unit 698–702, so lines 698, 699 and 701 needed carrier entries, and 700 needed a real fix.

**What was edited, and how.**
- `units.json` was edited by Python script. Each old string was asserted to occur exactly once in the named field.
- `t`, `ln`, `p` and `v` were checked unchanged in all 43 units, by script against a copy taken before any edit. `title`, `titleEn` and `part` are unchanged, and `about` has one phrase changed (item 35). 21 units changed.
- `l` still has the same number of lines as `t` in every unit, and no `i` has a line break.
- No note is over 140 words. The drafter's 659 (168 words) and 698 (155) were trimmed to 139 and 128.
- **`make_units.py` was not touched.** It still holds the drafter's strings, so re-running it would undo this review. Build from `units.json` as it stands.
- The diff to `scan-fixes.json` only appends: 176 insertions, 0 deletions, trailing newline kept. The new keys come after 7.598, in line order.
- The build was not run (it writes the published files and the manifest). Its scansion step and the validator's scansion check were replicated instead.

**Speech marks.** There are none in this stretch: `t`, `l` and `i` each have 0 “ and 0 ”.

**Severity counts: major 8, medium 9, low 28 (26 in pass 1, 2 in pass 2). Refused findings: 18. Scan-fixes entries added: 16.**

## Changes — pass 1

### Major
1–8. **Scansions the scanner got wrong with no flag.** Each line fit six feet, so nothing warned, but the quantities or syllables were wrong. Each line now has a hand entry.
   - **7.627 *arvina… subigunt***: the scanner made *vī-nā* short-short and *sŭ-bĭ-* long-long. *Arvīnā* is an ablative. Hand scansion: ar-vī | nā pin | guī sŭ-bĭ | gunt-qu(e) in | cō-tĕ sĕ | cū-res.
   - **7.630 *Atina potens***: the scanner made *nă* and *pŏ-* (of *potens*) long. Hand scansion: tē-lă nŏ | vant Ā | tī-nă pŏ | tens Tī | bur-quĕ sŭ | per-bum. With short *pŏ-*, this is the only fit, and it needs a long Ā- and long ī.
   - **7.675 *centauri Homolen Othrym***: the scanner made *Hō-* long and the accusative *-lĕn* short. Hand scansion: dē-scen | dunt cen | tau-r(i) Hŏ-mŏ | lēn Ō | thrym-quĕ nĭ | vā-lem, with O long by position before *thr*.
   - **7.681 *late legio comitatur***: the scanner made *lā-tē* short-short and *lĕ*, *cŏ* and *mĭ* long. Hand scansion: Cae-cŭ-lŭs | hunc lā | tē lĕ-gĭ | ō cŏ-mĭ | tā-tŭr ă | gres-tis.
   - **7.692 *cuiquam***: the scanner split *cui* into cŭ-ĭ, which is post-Augustan. *Cui* is one syllable in Virgil (as at 7.654, and in the entries at 1.448 and 2.677). Hand scansion: quem nĕ-quĕ | fās ig | nī cui | quam nec | ster-nĕ-rĕ | fer-rō. Both readings fit, so see the doubtful list.
   - **7.693 *desueta***: the scanner read dĕ-sŭ-ē-ta. The u is a consonant, as in *adsuetum* (the 7.487 entry). Hand scansion: iam prī | dem rĕ-sĭ | dēs pŏ-pŭ | lōs dē | suē-tă-quĕ | bel-lō.
   - **7.700 *sese… referunt***: the scanner made *sē-sē* short-short and *rĕ-fĕ-* long-long (as at 7.472 and 7.529). Hand scansion: cum sē | s(ē) ē pas | tū rĕ-fĕ | runt et | lon-gă că | nō-rōs.
   - **7.705 *urgueri***: the scanner read four syllables. The u after g is a consonant (as *urguet* at 7.241 and 7.566). Hand scansion: ur-guē | rī vŏ-lŭ | crum rau | cā-r(um) ad | lī-tŏ-ră | nū-bem.

### Medium
9. **7.631** (COSTLY 2.0), **wrong as flagged**: the scanner elided *turrigerae* and made its *rĭ* and *gĕ* long. The line has hiatus at *turrigerae Antemnae* and a spondaic fifth foot. Hand scansion: Ar-dĕ-ă | Crus-tŭ-mĕ | rī-qu(e) et | tur-rĭ-gĕ | rae An | tem-nae.
10. **7.633** (COSTLY 2.0), **wrong as flagged**: the scanner read *aenos* as ae-nos with a diphthong and lengthened *-cas*. *Aēnus* has three syllables, and *thōrācăs* has the short Greek accusative plural ending. Hand scansion: um-bō | num crā | tīs ă-lĭ | ī thō | rā-că-s(ă) | ē-nōs, 14 syllables.
11. **7.702** (UNRESOLVED), the half-line *pulsa palus.*: pul-să pă | lūs, a dactyl and one syllable, entered as at 7.248, 7.439 and 7.455.
12. **Carriers 7.698, 7.699 and 7.701**: the scanner's fits are right (checked by hand, and *Āsia* at 701 has its long A). Without them, the unit 698–702 would get no `sc`.
13. **7.634** (COSTLY 2.0): I confirmed the scanner's parse by hand and entered it to clear the flag. It is a spondaic line: aut lē | vīs ŏ-crĕ | ās len | tō dū | cunt ar | gen-tō.
14. **7.659** (COSTLY 2.0): I confirmed the scanner's parse by hand and entered it to clear the flag: col-lĭs Ă | ven-tī | nī sil | vā quem | Rhē-ă să | cer-dos. The fifth foot needs a long e in *Rhea*.
15. **Note 609, a false scansion label**: the note said "'aerei' scanned as three syllables, 'ae-re-i'". It is two syllables here, ae-rei by synizesis, and that is the only fit (the scanner has it right). The note now says so and contrasts *aerea* (615), which keeps three syllables.
16. **Note 659, Hercules**: "Hercules, who grew up in that Argive city" (Tiryns) was wrong, since Hercules was raised at Thebes. The note now reads "named from the Argive city of his family".
17. **`i` 649, a remembered-English echo**: "Lausus, the breaker of horses" echoes the best-known English formula for Homer's ἱππόδαμος. It now reads "Lausus, who could master horses and hunt wild beasts down".

### Low
18. **`l`/`i`/`n` 601, *protinus***: "from the first" misreads the word, which means "from then on, in unbroken succession". `l` now reads "which thereafter the cities…". `i` is recast as "In Hesperian Latium there was a custom which the cities of Alba kept holy in their turn, and which Rome… keeps now…". This also moves `i` away from the bare literal opening, which many versions share. The note now glosses *protinus*. (The note change is counted here.)
19. **Note 616**: "'Hoc… more'… framing the sentence" was wrong, because *Hoc* opens line 616 and *more* opens 617. It now reads "the noun held over to the next line".
20. **Note 623**: the claim "(other editions have a colon or full stop)" could not be vouched for and was cut. The evidence from Greenough's own print replaces it (see R1).
21. **Note 629**: "Elision runs through the last line" missed the hiatus. The note now gives the hiatus at *turrigerae Antemnae* and the spondaic fifth foot.
22. **Note 633**: "'aenos' = 'aeneos'… the contracted form" was wrong. The note now reads "the poets' form beside 'aeneus', three syllables, 'a-ē-nos'".
23. **Note 659, the Tiber**: "which flows out of Etruria" now reads "the river of the Etruscan border".
24. **Note 659, length**: 168 words, trimmed to 139. Cut: the orthographic variant *exstincto* (spelling only), "without a preposition", and "with no hint of force".
25. **Note 678**: "in apposition to 'fundator' four lines earlier" now reads "three lines earlier" (678 to 681).
26. **Note 682**: "Greenough's 'pascit' is the usual reading" was a claim about editions that I cannot vouch for. It now reads "is kept".
27. **Note 686, the Plataeans**: "the opposite custom of the Plataeans in Thucydides" was wrong, because it was a single break-out and not a custom. It now reads "Compare the reverse in Thucydides (Book 3): the Plataeans broke out of their besieged town with only the left foot shod, for a sure footing in the mud."
28. **`l` 691 (line 692)**: "whom it is right for no one with fire nor to lay low with steel" was garbled. It now reads "whom neither is it lawful with fire for anyone nor to lay low with steel", which follows the Latin order.
29. **Note 695**: "most editions have a comma here" now reads "the sense calls for a comma". The Fescennine etymology is hedged ("was said to have given its name"). The misprint sentence was tightened, and the note is now 130 words.
30. **Note 698**: "the swan of early Latin verse", an epithet I cannot vouch for, was cut. The Ennius point now reads "Some have heard in the singing a compliment to Ennius, who claimed Messapus as his ancestor." The note was trimmed from 155 words to 128.
31. **`i` 641, an echo precaution**: "Throw Helicon open now, goddesses, and stir up your songs" now reads "Now, goddesses, open Helicon and wake your songs".
32. **`i` 652, an echo precaution**: "deserved a father other than Mezentius" now reads "deserved, indeed, not to have Mezentius for his father".
33. **Note 641**: the Book X catalogue now says that its invocation opens with this same line (X.163, checked against the pinned text).
34. **`about`**: "ploughshares and pruning-hooks are forged into swords" is not in this text, where the love of the plough gives way and the fathers' swords are re-forged; that image is Georgics 1.508. It now reads "the plough is forgotten and old swords are forged anew".
35–43. **Scansion pointers added to notes**, to go with the fixes:
   - *inexcīta* (623)
   - *arvīnā* (626)
   - *aenos* three syllables and 634 spondaic (633)
   - *ācer* and *Cātillus* (670)
   - *Hŏmŏlēn* and the elision of *centauri* (674)
   - *lātē* and *lĕgĭō* (681)
   - *cuiquam* and *dēsuēta* (691)
   - *sēsē* and *rĕfĕrunt* (698)
   - *urgueri* three syllables (703)

   The pointers for 629 (hiatus, spondee, *Ātīna*) are part of item 21, and those for 659 (*silvā*, *Rhēa*) are in the rewritten note (item 24).

## Changes — pass 2
- **P2-1 (low)**: the new sentence in note 674 had a doubled "and… ; and". It now reads "…and 'centauri' elides into it. 'Othrymque' is Greenough's Latinised accusative of Othrys."
- **P2-2 (low)**: in `i` 652, the two dashes read as a parenthesis that broke the sense. It now reads "all to no purpose: a youth who deserved to be happier under a father's rule, and deserved, indeed, not to have Mezentius for his father."

## Scan-fixes entries added (16)
Appended after 7.598 in line order, each with its reason:
- 7.631 and 7.633 (packet COSTLY flags, both wrong); 7.634 and 7.659 (COSTLY, confirmed)
- 7.702 (UNRESOLVED half-line); 7.698, 7.699 and 7.701 (carriers)
- 7.627, 7.630, 7.675, 7.681, 7.692, 7.693, 7.700 and 7.705 (no flag, wrong syllables or quantities)

Each matches its line's words under `WORD_RE`. The fifteen full lines each have six feet, five –⏑⏑/–– feet then –×, 13–16 syllables and one ×. 702 passes the validator's half-line rule. In the replicated build all 16 apply, the scanner report is empty, and all 105 lines pass.

## Hand-scan notes on the special lines (scanner right, no entry)
- **Greek eu**: *ceu* (674, 699) is one syllable, which is right. *euntibus* (676) is ĕ-un-, not the Greek diphthong, and is right. There is no *Teucri* or *Eurus* in this part.
- **Initial Ae-**: *Aeneadis* (616), *aeterna* (609), *Aequos* (695), *aeratas* (703) and *aetas* (680) are right. *aerei* (609) is ae-rei by synizesis and right (see item 15). *aerea* (615) is ae-rĕ-a and right. *aeriam* (704) is ā-ĕ-rĭ-am (Greek ἀέριος), four syllables, and right. *aenos* (633) is fixed.
- **Consonantal i/u**: no prefixed *-iicio/coniunx* forms in this part. Right: *iubebatur* (617), *iuvat* (628), *iuga* (639), *iuxta* (649), *iuventus* (672), *Iunonis* (683), *iam*, and *angues* (658, u consonantal). Fixed: *desueta* (693) and *urgueri* (705).
- **Hiatus**: only 631 (fixed). Every other vowel meeting is an ordinary elision (e.g. *Hesperio in* 601, *sacrae et* 608, *Ausonia atque* 623, *centauri Homolen* 675, *sese e* 700).
- **Other lines checked and right**: *rēligione* (608); *inexcīta* (623) and *excīti* (642); *lēvīs* "smooth" (626, 634); *Hĕlĭcōna* (641); *Mēzentius*, long by position before z (648, 654); *Gēryŏne* and *Tīrynthius* (662); *Hĭbēras* (663); *Cātillus* and *ācer* (672); *Ăniēnem* (683); *Sōractis* (696); *Āsia* (701); the 13-syllable lines 609, 622, 642, 655, 671, 678 and 687; and *cui* as one syllable at 654.

## Doubtful quantities and readings entered or left on the only fit
- **7.630 *Ātīna***: the long Ā- and long ī are needed by the meter once *pŏtens* is short. Not checked against a dictionary.
- **7.631, hiatus *turrigerae Antemnae***: entered as hiatus with a spondaic fifth foot. This is the only fit under natural quantities, and I recall the line among Virgil's hiatus lines, but I did not check it against an edition.
- **7.692 *cuiquam***: entered with *cui* as one syllable. The scanner's trisyllabic cŭ-ĭ also fits; I chose Virgil's usage.
- **7.675 *Ōthrym***: O is long by position before *thr* (a stop and liquid, so the lengthening is optional), on the only fit with *Hŏmŏlēn*.
- **7.659 *Rhēa***: long e, as the fifth foot needs (entered as confirmed).
- **7.672 *Cātillus*, *ācer***: long first vowels on the scanner's fit and the only fit. *Cātilus* is long in Horace too. No entry.

## Refused findings
- **R1 — 7.623 *ante;* + *Pars***: the drafter's "doubtful, keep" call is **upheld**. A script over the pinned text found that, of 387 line-final semicolons, this is the only one followed by a capitalised common word, so one of the two is very probably a slip. But it cannot be told which one: a full stop for the semicolon, or a lower-case *pars*. The sense is the same either way, so rule 5b's "doubtful → keep and say so" applies. The note now gives this evidence in place of an unverifiable claim about other editions.
- **R2 — 7.695 *Faliscos.* + *Hi***: the drafter's "doubtful, keep" call is **upheld**. The stop leaves 695 without a verb, and the sense wants a comma with *habent* governing both lines. But the capital *Hi* agrees with the stop, so this is a consistent (if harsh) editorial punctuation, not an obvious slip of type. The unit takes 695–697 together, `l` keeps the print's stop, and `i` reads them as one sentence. Kept.
- **R3 — `l` 635 "sickle" against `i` "pruning-hook"**: both render *falx*, and the note covers both. Kept.
- **R4 — note 601, *cum prima* = *cum primum*, with *prima* adverbial**: the standard reading. Kept.
- **R5 — note 607, the Janus closures**: Numa, once after the First Punic War, then Augustus in 29 BC. This is Livy's account, from memory. I.293–294 was checked against the pinned text. Kept.
- **R6 — note 604, the Carrhae standards** (53 BC, recovered by diplomacy in 20 BC): right. Kept.
- **R7 — note 620, Ennius's *Belli ferratos postes portasque refregit*, quoted by Horace**: right from memory (Satires 1.4; no line number is given in the note). Kept.
- **R8 — note 635, Georgics 1.508 *et curvae rigidum falces conflantur in ensem***: right from memory. Kept.
- **R9 — Homer**: these are kept, and the line numbers fit my recollection of the Greek, but none was checked against a text:
  - Iliad 2.484–493 (the invocation) in note 641
  - 2.485 and 2.486 (paraphrased, uncited) in notes 645 and 646
  - Nireus (uncited, 2.671–674) in note 649
  - the swans of the Cayster (uncited, 2.459–463) in note 698
  - the silver ankle-clasps on greaves (uncited) in note 633
- **R10 — note 652, *dignus… qui… esset* as a relative clause of characteristic after *dignus***: an acceptable label (Allen & Greenough treat it with clauses of purpose and characteristic). Kept.
- **R11 — note 611, the *cinctus Gabinus***: the description follows Servius in substance. Kept.
- **R12 — note 678, Caeculus's story in Servius**: right in substance from memory (the spark, the exposure, the fire, the small eyes). Kept.
- **R13 — note 659, *Rhea sacerdos* "otherwise unknown", not Rhea Silvia**: the standard view. Kept.
- **R14 — note 691, Ennius claiming descent from Messapus (Servius), Messapus surviving the poem**: right from memory. Kept.
- **R15 — note 670, Tibur's three Argive founders**: hedged already ("sons (or grandsons)"). Kept.
- **R16 — `i` 703, "No one would have thought" for *putet***: natural English for the potential in narrative. Kept.
- **R17 — cosmetic syllable divisions in the scanner's fits** (*im–pe–xum* 667, *in–ne–xus* 669, *des–cen–dunt*): the quantities are right, so there are no entries (as aeneid-053 R15 and aeneid-054 R14).
- **R18 — further `i` echoes**: nothing more found. "Gates of War", "snow-white swans among the clear clouds" and "They marched in measured step" are plain renderings, not a translator's turns. `title`, `titleEn` and `part` are our own and unchanged.

## For the owner (QUESTIONS.md)
- **Misprints (rule 5b)**: none called. Two are kept as doubtful:
  - 7.623 *ante;* + capital *Pars*: unique in the print, but which mark is the slip cannot be told.
  - 7.695 *Faliscos.* + capital *Hi*: the sense wants a comma, but the capital agrees with the stop.
- **Doubtful quantities**:
  - 7.630 *Ātīna*
  - 7.631, hiatus with a spondaic fifth foot
  - 7.692 *cui* as one syllable (both readings fit)
  - 7.675 *Ōthrym*, long by position
  - 7.659 *Rhēa*

  None was checked against an edition.
- **`make_units.py` is stale**: `drafts/aeneid-055/make_units.py` still holds the drafter's strings. Re-running it would discard this review.
- **`gloss.json` is missing**: there is no `drafts/aeneid-055/gloss.json` (only `known-forms.json` and `novel-forms.json`). `build_aeneid.py` reads it and will stop without it.
- **Unchecked attributions, from memory**:
  - Iliad 2.484–493
  - Livy on the Janus closures
  - Ennius as quoted by Horace
  - Georgics 1.508
  - Thucydides Book 3 on the Plataeans
  - Servius on Caeculus, on the *cinctus Gabinus* and on Ennius and Messapus
  - Horace Odes 1.9 (*Soracte*)
  - Lucretius's *luminis oras*

  None was checked against a text in this run.
