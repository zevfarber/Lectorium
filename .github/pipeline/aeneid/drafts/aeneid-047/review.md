# Review — aeneid-047 (Aeneid VI.703–800), adversarial reviewer

I reviewed this part in two passes. In pass 1, I checked each of the 39 units word by word: `l`, `i` and `n` against the Latin, every grammatical label, every citation and every historical or mythological claim, the speech marks, the misprints (README rule 5b), the bracketed line 716, the repeated line 797 (= 4.482), and every `i` (and `l` where avoidable) for remembered English. I worked from the Latin and from memory of the reference works only; no translation was opened. Pass 2 re-read every edited unit in full and made two further changes (P2-1, P2-2).

I then hand-scanned all 98 lines by quantity and compared each with the scanner's output. The scanner was run in-process, the way `build_aeneid.py` calls `SL.scan_story`. Every new `scan-fixes.json` entry was checked against a replica of the build's word-match rule (`strip(sc) == WORD_RE.findall(line)`) and of the validator's six-foot rule (feet 1–6, 12–17 syllables, one ×, five –⏑⏑/–– feet and a sixth –×/⏑×). I then ran a replica of the build's scansion step with the fixes applied. All 13 entries applied. The scanner report is empty, which clears the packet's two COSTLY flags at 747 and 789. All 98 lines pass the six-foot rule.

`t` is untouched. The cut tuples in `make_units.py` are unchanged. The regenerated `units.json` has the same `t`, `ln`, `p` and `v` in all 39 units. I checked this by script against a copy taken before any edit. `title`, `titleEn` and `part` are unchanged. `about` has three phrases changed (item 63). Edits were made to the strings in `make_units.py` by a Python replace script, with each old string asserted to occur once. `units.json` was then regenerated with `make_units.py`. `build_aeneid.py` was not run. The diff to `scan-fixes.json` only appends (152 insertions, 0 deletions). `new-renderings.md` was updated to match.

**Speech marks**: `t`, `l` and `i` each have 5 “ and 4 ”. The unmatched “ is Anchises's second speech, which opens at 756 and runs past 800. The validator will warn about it, and the warning is expected.
- Anchises: 713 → 718 (“ in the unit at 713, ” at the end of the unit at 716).
- Aeneas: 719 → 721 (“ at 719, ” after *cupido?*).
- Anchises: 722, one line (“ and ” in the same unit; *suscipit Anchises* is outside the marks).
- Anchises: 724 → 751 (“ at 724, ” after *reverti.*).
- Anchises: 756 → (continues into aeneid-048).

All five sets agree across `t`, `l` and `i`, unit for unit.

**Severity counts: major 8, medium 24, low 33 (31 in pass 1, 2 in pass 2). Refused findings: 20 (listed at the end).**

## Changes — pass 1

### Major
1–8. **Scansions the scanner got wrong without a flag.** Each now has a hand entry.
   - **6.707**: the scanner made both syllables of *prātīs* short, and the u- of *ubi* and the a- of *apes* long. Hand scansion: āc vĕ-lŭt | īn prā | tīs ŭ-b(i) ă | pēs aes | tā-tĕ sĕ | rē-na.
   - **6.720**: the scanner made the -li- and -mis of *sublīmīs* short, and the a- and -ni- of *animas* long. Hand scansion: sub-lī | mīs ă-nĭ | mās ĭ-tĕ | rum-qu(e) ad | tar-dă rĕ | ver-ti.
   - **6.732**: the scanner made the -re- and -ni of *terrēnī* short, and the he- and -be- of *hebetant* long. Hand scansion: ter-rē | nī-qu(e) hĕ-bĕ | tant ar | tūs mŏ-rĭ | bun-dă-quĕ | mem-bra.
   - **6.757**: the scanner made the I- and -ta- of *Itala* long, and the -la and *de* short. *Ĭtălā* (ablative) has a short I-, as *Ĭtălō* does at 762, and the preposition *dē* is long. Hand scansion: glō-rĭ-ă | quī mă-nĕ | ant Ĭ-tă | lā dē | gen-tĕ nĕ | pō-tes.
   - **6.760**: the scanner made both syllables of *pūrā* short, and the iu- and -ve- of *iuvenis* long. Hand scansion: Il-lĕ vĭ | dēs pū | rā iŭ-vĕ | nis quī | nī-tĭ-tŭr | has-ta.
   - **6.768**: the scanner made Ca-, -pys and Nu- long, and *qui* and *te* short. Two monosyllables long by nature cannot be short before a consonant. Hand scansion: ēt Că-pys | ēt Nŭ-mĭ | tōr ēt | quī tē | nō-mĭ-nĕ | red-det. The -tōr of *Numitor* is long at the caesura (see the doubtful list).
   - **6.777**: the scanner made the co- and -mi- of *comitem* long, and the second syllable of *sēsē* and the Mā- of *Māvortius* short. Hand scansion: Quīn ĕt ă | vō cŏ-mĭ | tem sē | sē Mā | vor-tĭ-ŭs | ad-det.
   - **6.783**: the scanner made the -na of *una* long and the mu- of *mūrō* short. *Una* is nominative with *Roma* ("one city"), so its -a is short. Hand scansion: sep-tem | qu(e) ū-nă sĭ | bī mū | rō cir | cum-dă-bĭt | ar-ces. The final i of *sibī* is long (see the doubtful list).

### Medium
9–13. **Scansion: the known blind spots and the packet's flags.**
   - **6.703, 6.711, 6.769 *Aeneas***: the scanner split Ae- into two short syllables (A-ĕ-nĕ-ās). At 769 that gave 17 syllables. Hand scansions:
     - In-tĕ-rĕ | ā vĭ-dĕt | Aē-nē | ās in | val-lĕ rĕ | duc-ta
     - īn-scĭ-ŭs | Aē-nē | ās quae | sint ĕ-ă | flū-mĭ-nă | por-ro
     - Sil-vĭ-ŭs | Aē-nē | ās pă-rĭ | tēr pĭ-ĕ | tā-tĕ vĕl | ar-mis
   - **6.747** (packet flag, COSTLY 2.0): I confirmed the scanner's parse by hand and entered it to clear the flag. *Auraï* is au-rā-ī, with *sensum* and *atque* elided: ae-thĕ-rĭ | um sen | s(um) at-qu(e) au | rā-ī | sim-plĭ-cĭs | ig-nem.
   - **6.789** (packet flag, COSTLY 2.0): the scanner read *Iuli* as two syllables, with the i consonantal. It is Ĭ-ū-lī, three syllables, so the -nis of *omnis* is short before the vowel. Hand scansion: Rō-mā | nōs-quĕ tŭ | ōs hīc | Cae-săr ĕt | om-nĭs Ĭ | ū-lī.
14. **i 716–718, the bracket**: the bracketed `i` read "[These indeed I have long wished to speak of to you and set before your eyes,] …". This put *iampridem… cupio* from line 717 inside the bracket, so a reader who skips the spurious line also lost the main verb. It now reads "I have long wanted [to tell you of these and show them to you face to face,] to count over this offspring of my line, …". Only line 716 is inside the bracket, and the sentence reads whole without it.
15. **Note 743–744, the order of the stages**: the note said that this clause "is best taken as a side remark about the few, and 'donec' (745) as going back to the cleansing of the rest". That is one side of an open question, stated as settled. The note now gives both readings. In the first, *donec* goes with the few, who stay in Elysium until time leaves them pure fire and are not reborn. In the second, *pauci… tenemus* is an aside, and *donec* goes with the cleansing of the rest, who then go to Lethe (748).
16. **i 795–797, consistent with 4.482**: `l` 797 already matched aeneid-028 word for word. `i` ("where Atlas, who bears the heavens, turns on his shoulder the sky's axis studded with blazing stars") now ends as aeneid-028 does: "where Atlas the sky-bearer turns on his shoulder the axle of heaven, studded with blazing stars". *Caelifer* is kept as "the sky-bearer" where 4.482 had *maxumus*. The note now adds that Greenough prints *humero* at 4.482.
17–32. **Remembered English in `i`**: each of these ran close to a known version.
   - **707–709**: "as in the meadows on a cloudless summer day, when the bees settle on flowers…" is now "as when, in a meadow under the clear summer sky, bees alight on blossoms of many hues and crowd thickly round the white lilies — the whole plain is loud with their humming".
   - **713–715**: "souls to whom fate owes a second body… the waters that free from care" is now "souls for whom fate has other bodies in store; at the stream of Lethe they are drinking water that takes away all care, and drinking a long oblivion". The same phrase in `about` was changed too (item 63).
   - **719–721**: "come back once more to sluggish bodies" is now "go back once more into the slow weight of bodies". "What is this dreadful longing for the light…" is now "Why do the poor souls crave the light with so terrible a longing?"
   - **722–723**: "I will tell you, my son, and I will not keep you in suspense" is now "I will explain, my son, and not leave you hanging in doubt".
   - **724–727**: "are fed by a spirit within, and a mind spread through all their members" is now "draw their nourishment from a spirit inside them, and a mind, poured into every limb, keeps the whole bulk astir…". "the bright orb of the Moon" is now "the shining globe of the Moon".
   - **735–738**: "on their last day… not all the plagues of the body" is now "with the last light of day, the unhappy souls are still not rid of every ill, not wholly free of all the body's corruptions…".
   - **743–744**: "a few of us dwell on in these happy fields" is now "only a handful of us remain in possession of these glad meadows".
   - **748–751**: "may visit the vault of the sky once more and begin to wish to return into bodies" is now "may look once more on the curving sky above and start to want to go back into bodies".
   - **752–755**: "took his stand on a mound from which he could look over them all as they came toward him… and learn their faces as they passed" matched a known version almost clause for clause. It now reads "climbed a knoll from which he could review them all in their long column as they faced him, and pick out the features of each newcomer".
   - **760–762**: "holds by lot the place nearest the light" is now "has drawn the station closest to the daylight".
   - **763–766**: "your wife Lavinia will bear you late in your long life… a king and the father of kings" is now "whom, late in your long life, your wife Lavinia will bring up for you in the forests: a king, and sire of kings…". This also renders *educet* (rear), not "bear".
   - **767–770**: "the pride of the Trojan people… as distinguished for his sense of duty as for his arms" is now "the glory of the Trojan nation… as eminent for his piety as for his feats of arms".
   - **771–772**: "Look what strength they show" is now "See how much strength they make a show of".
   - **781–784**: "make her rule as wide as the earth and her spirit as high as Olympus… happy in a breed of heroes" is now "make her dominion match the lands of the world and her courage match Olympus… fortunate in her progeny of men".
   - **788–790**: "look at this people, your own Romans" and "Here is Caesar, and all the line of Iulus" were each near-verbatim. They now read "Bend both your gazes this way now: look at this nation, the Romans who are yours" and "Here stands Caesar, and the whole progeny of Iulus…" (see also P2-1).
   - **791–795**: "the man you have heard promised to you so many times… son of a god… the fields where Saturn reigned long ago" is now "This is the man, yes, this is he, whom you hear pledged to you again and again: Augustus Caesar, offspring of a god, who will found anew in Latium an age of gold, across the countryside that Saturn ruled in times long past, and push the bounds of empire beyond the Garamantes and the Indians".

### Low
33. **l 735–738**: "not yet every evil" misread *tamen* as temporal. It now reads "not, however, every evil".
34. **l 781–784**: "and seven, alone, for herself…" contradicted the note ("'una' is 'one', the single city"). It now reads "and seven, one city, for herself…".
35. **l 721**: "What so dread desire" is now "What so dire desire". *Dira* is the cognate, and "dread desire" is a known version's phrase.
36. **l 791**: "time and again" is now "rather often", which keeps the comparative *saepius* and drops a known phrase.
37. **l 720**: "to sluggish return" is now "to slow return" (*tarda*).
38. **Note 741**: "'Aliae… aliis' (741)" is now "(740–741)". *Aliae* is in 740.
39. **Note 710**: "held back to the start of 711" was wrong, because *inscius* comes first. It now reads "held back to 711".
40. **Note 724**: "Lucretius… whose favourite opening word is 'principio'" is now "who often opens an argument with 'principio'". "'Titania astra'… most simply the sun" is now "usually taken of the sun (itself called Titan…) together with the other stars", since *astra* is plural.
41. **Note 760, *hasta pura***: "given in Roman times as a prize for valour" is now "the hasta pura was a Roman military honour, and Servius takes it here as the prize for a first victory".
42. **Note 767, Livy 1.3**: "not in the order of the lists found in Livy" is now specific: "where Aeneas Silvius is the second king and Procas the father of Numitor". "Servius tells that a guardian…" is now "Servius has a story that a guardian…".
43. **Note 771, the civic crown**: "It is set back in time on these ancient kings, as founders of towns" stated a reason as fact. It now reads "Virgil gives it, out of its time, to these ancient kings, perhaps as saviours of their people and founders of towns". The 27 BC grant to Augustus is kept (Res Gestae 34).
44. **Note 777**: "genitive of quality" is now "genitive of description… 'of the blood of Assaracus'".
45. **Note 779**: "a double plume, the mark of Mars" is now "usually taken as a mark of Mars".
46. **Note 784**: "Lucretius describes her procession (2.600–643)" is now "in his second book (from 2.600)". I am sure of where the passage starts but not of the line where the procession ends.
47. **Note 789**: "'Caesar' is most likely Julius Caesar" is now "probably Julius Caesar… (some take it of Augustus, named in 792)".
48. **Note 791**: "a Roman general triumphed over the Garamantes… in 19 BC" now names L. Cornelius Balbus. "The climax of the pageant." was dropped, to bring the note from 146 words to 141.
49. **Note 703**: "'silvae'… which most later editors read" is now "which many editors read".
50–62. **Remembered English and small accuracy fixes in `i`**:
   - **703–705**: "deep in a hollow valley… a grove set apart… gliding past those peaceful dwellings" is now "far back in a recess of the valley, Aeneas catches sight of a grove shut off by itself, of undergrowth whispering in the wood, and of the stream of Lethe flowing along before those quiet homes". This also renders *reducta*, which means "set back", not "hollow".
   - **706**: "countless nations and peoples were drifting to and fro" is now "flitting this way and that, were peoples and nations past counting". *Volabant* means "flying", not "drifting".
   - **710–712**: "who crowd its banks in such a host" is now "that fill its banks in so great a company".
   - **728–729**: "beneath its gleaming floor" put the creatures under the sea-bed, but *aequor* is the surface. It now reads "beneath its plain of polished marble".
   - **730–732**: "fiery strength and a heavenly source… do not clog them" is now "a vigour of fire, and their birth is from heaven… do not slow them down" (*tardant*).
   - **739–740**: "pay the penalty for their old wrongdoing" is now "pay out in torment for ancient wrongs".
   - **741–742**: "washed away beneath a vast flood, or burned out with fire" is now "rinsed away under a great swirl of water, or burnt out of them by fire".
   - **743**: "each of us suffers what his own spirit has earned" is now "every one of us endures the ghostly lot that is his own". It is further from the "each of us must suffer his own…" shape and makes no claim about desert.
   - **745–747**: "the long passage of time, when its cycle has come round" is now "length of days, once time has run its full circle".
   - **756–759**: "what descendants of Italian stock await us, illustrious souls who will carry on our name… teach you your own destiny" is now "the descendants who wait for us from Italian blood, bright souls who will pass into our name — these I will set forth for you in words, and make your destiny known to you".
   - **777–779**: "a son of Mars will join his grandfather's company" is now "a child of Mars, Romulus, will attach himself to his grandfather as a companion".
   - **784–787**: "every one a dweller in heaven, every one a lord of the heights above" is now "all of them denizens of the sky, all of them possessors of the lofty realms above" (see also P2-2).
   - **798–800**: "the seven mouths of the Nile are troubled and afraid" is now "the sevenfold Nile is thrown into confusion at all its frightened mouths". "shudder at the oracles of the gods" is now "are already bristling with dread at the answers of the gods".
63. **`about`**: three phrases that echoed known versions were changed. "souls owed second bodies by fate" is now "souls for whom fate has other bodies in store". "all the line of Iulus" is now "the whole progeny of Iulus". "son of a god, who will bring back the golden age… where Saturn once reigned" is now "offspring of a god, who will found a golden age again in Latium, where Saturn once ruled".

## Changes — pass 2
- **P2-1 (low)**: in i 789–790, the pass-1 wording "destined to come out beneath the great pole of heaven" was flat. It now reads "destined to rise into the light beneath the great pole of heaven".
- **P2-2 (low)**: in i 784–787, the pass-1 wording "the Mother of Berecyntus" made her the mountain's mother. It is now "the Berecyntian Mother", which is her title.

## Scan-fixes lines added (13)
These 13 entries were appended at the end of `scan-fixes.json`, each with its reason. The existing entries are unchanged: the diff only appends.
- 6.703
- 6.707
- 6.711
- 6.720
- 6.732
- 6.747
- 6.757
- 6.760
- 6.768
- 6.769
- 6.777
- 6.783
- 6.789

Each entry matches its line's words under `WORD_RE` and has six feet. Each has five dactyls or spondees, then –×, 14–16 syllables and one ×. In the replicated build with all fixes applied, the scanner report is empty and all 98 lines pass.

## Hand-scan notes on the special lines (scanner right, no entry)
- **Initial Ae-**: *Aeneas* (703, 711, 769) is fixed. The scanner has *aestate* (707), *aequore* (729), *aetherium* (747, inside the fix), *aetherias* (762) and *aequabit* (782) right. Medial ae is also right: *Lethaeum* (705, 749), *Lethaei* (714, elided), *longaevo* (764), *Maeotia* (799, Mae-ō-tĭ-ă) and *caelifer* (796).
- **Greek eu**: there is none in this part.
- **Consonantal i after a prefix**: *coniunx* (764) is right as two syllables, co-niunx, with the first long. *huius* (781, 798) is right, hū-ius, with the first syllable long. Word-initial *iam*, *iacet* (795) and *iampridem* (717) are right. *iuvenes* (771) is right. *iuvenis* (760) is in the fix.
- **Hiatus**: none. Every vowel meeting is an ordinary elision, before h- included (*Inde hominum* 728, *terrenique hebetant* 732, *iampridem hanc* 717, *caelum hinc* 719). *Necesse est* (737) and *putandum est* (719) are prodelision.
- **Others checked and right**: *Ītaliā* (718, lengthened I as usual); *Ēlysium* (744); *ollīs* (730); *relīquit* (735); *exēmit* (746); *volvēre* (748); *Procās* (767, long by position anyway); *Nōmentum*, *Gabiōs* (773); *Pōmetiōs*, *Ĭnuī*, *Bōlam*, *Cŏram* (775); *Īlia* (778); *Berĕcyntia* (784); *Garamantăs* (794, Greek accusative -ăs); *Maeōtia* (799); *oblivia* (715, ob- long by position at the prefix boundary); *responsis* (799).

## Doubtful quantities entered on the only fit
- **6.768 Numitōr**: the -or is long at the penthemimeral caesura (the old long -ōr, as in the oblique cases). With a short -ŏr, the line has no fit.
- **6.783 sibī**: the final i is long, which is common for this word. With a short final i, foot 3 fails.
- **6.779 vĭdĕn** (scanner's fit, no entry): the e is shortened in *viden* (iambic shortening). That is the only fit.
- **6.773 Fĭdēnam** (scanner's fit, no entry): Fi- is short, the only fit in foot 5.

## Refused findings
- **R1 — 6.763 `silvius` (rule 5b)**: I agree with the drafter. A proper name in mid-sentence needs a capital, Greenough prints *Silvius* at 769, and only one reading is possible. The note already opens in the house form ("The print has 'silvius', a misprint for 'Silvius', corrected here… t keeps the print…; l and i give the reading."). No scan entry is needed, because the scanner reads the word correctly.
- **R2 — Rule 5b, other candidates**: none. *proxuma*/*Proxumus*, *incluta*, *inlustris*, *Mavortius*, *auraï*, *divom*, *complerint* and *Fidenam* are Greenough's spellings or Virgil's forms, not misprints.
- **R3 — Georgics 1.37 (*tam dira cupido*)**: verified and kept. *nec tibi regnandi veniat tam dira cupido* is G. 1.37.
- **R4 — Civic crown voted to Augustus, 27 BC**: kept. Res Gestae 34 records the oak crown over his door, by the senate's decree of January 27 BC.
- **R5 — Triumph over the Garamantes, 19 BC**: kept, with the general named. L. Cornelius Balbus triumphed in 19 BC after his campaign against the Garamantes (Pliny, *Natural History* 5.36). Indian embassies to Augustus are recorded in Res Gestae 31.
- **R6 — Livy 1.3 for the Alban kings**: kept and made precise (item 42). Livy's order is Silvius, Aeneas Silvius, Latinus Silvius, Alba, Atys, Capys… Proca, then Numitor and Amulius.
- **R7 — Servius on Silvius Aeneas's guardian**: kept, now worded "Servius has a story that…". I recall the note (a guardian who held the throne until the prince was in his fifties) but could not check Servius's text in this run, so the wording stays an attribution.
- **R8 — 780, Mars or Jupiter**: the note already gives both readings (Mars as *pater ipse*, with *superum* taken with *honore*, or Jupiter as *pater superum*). `i` follows the Mars reading, which is the more natural one after *Mavortius*. Kept.
- **R9 — Note 760, Servius on *hasta pura***: I am fairly sure that Servius explains it as the prize for a first victory, and the note now attributes the explanation to him. Flagged for the owner, because it is from memory.
- **R10 — Lucretius 2.600ff. (Cybele)**: kept, with the end of the range dropped (item 46).
- **R11 — i 795–797, "studded with blazing stars"**: this is a common shape for *stellis ardentibus aptum*. It is kept because aeneid-028 published it for the identical line 4.482, and consistency comes first (as 046's R3 did for II.792–794).
- **R12 — 776, *Haec tum nomina erunt…***: kept. `l` is word for word and cannot avoid resembling other literal versions. `i` ("In that age these will be famous names; today they are stretches of country that no one has named") avoids the familiar "nameless lands" endings.
- **R13 — i 733–734, "fears and desires… griefs and joys"**: kept. This is the literal rendering of the four verbs, and the rest of the sentence ("a prison without light… see the open air") is not a known version's.
- **R14 — i 771, "What young men they are!"**: kept. It is the bare sense of *Qui iuvenes!*.
- **R15 — 6.747 caesura**: the scanner's tokens are entered exactly, with no ‖. The third-foot caesura falls after the elided *sensum*. Neither the build nor the validator needs the mark (aeneid-045 R13, aeneid-046 R12).
- **R16 — Note lengths over 140 words**: only 791 (141, down from 146) is over the limit. It carries the identification, the golden age and the Garamantes. This is a warning, not a failure.
- **R17 — Latin Library variants**: *silvae* (704) and *posset* (754) are noted in `n`. *veluti*, *manis*, *aurai*, *omnis*, *proxima*, *viris*, *Mauvortius*, *tenentis* and *divum* are orthography or morphology. Each is already mentioned where useful, or rightly ignored.
- **R18 — Other citations verified and kept**:
  - Iliad 2.87–90 (the bees).
  - Plato, Republic 10, the myth of Er: the plain of Lethe, the river of Unmindfulness, and the thousand-year journey.
  - Odyssey 11, and the Roman funeral masks (Polybius's account, not cited).
  - Aeneid 1.288 (Iulus/Iulius), 1.430–436 (the bees at Carthage), 4.482, 6.695 (*saepius*) and 8.319–325 (Saturn in Latium).
  - The Magna Mater brought to Rome in 204 BC.
  - *Augustus* conferred in 27 BC, Julius Caesar deified in 42 BC, and Egypt taken in 30 BC.
- **R19 — 6.757 *Itala***: I did not treat this as doubtful. *Ĭtalus* has a naturally short I, lengthened only where the metre needs it (as *Ītalia* at 718). Here the metre needs it short, and *Ĭtălō* at 762 agrees.
- **R20 — `title`, `titleEn`, `part`**: these are our own and borrow no translation's heading. Unchanged.

## For the owner (QUESTIONS.md)
- **6.763 `silvius`**: a new rule-5b misprint (a lower-case s on a proper name). It is published as printed in `t`, with `l`/`i` reading *Silvius* and the note opening with the print's reading. There is no emend list for the Aeneid, so the correction is to be recorded in QUESTIONS.md.
- **Doubtful quantities on the only fit**: 6.768 Numitōr (lengthened at the caesura) and 6.783 sibī. The scanner's 6.779 vĭdĕn and 6.773 Fĭdēnam are right as far as I can tell.
- **From memory, worded as attributions**: Servius on the *hasta pura* (760) and on Silvius Aeneas's guardian (770). Neither was checked against Servius's text in this run.
- **6.743–751**: the note now presents the two standard readings of the order of the stages and does not choose between them.
