# Review — aeneid-048 (Aeneid VI.801–901), adversarial reviewer

I reviewed this part in two passes. In pass 1, I checked each of the 46 units word by word: `l`, `i` and `n` against the Latin, every grammatical label, every citation and every historical claim (the kings, Brutus, the Decii, Drusi, Torquatus, Camillus, Caesar and Pompey, Mummius, Aemilius Paullus, Cato, Cossus, the Gracchi, the Scipios, Fabricius, Serranus, the Fabii and Fabius Maximus, and both Marcelli). I also checked the speech marks, the two misprint decisions (README rule 5b), the bracketed line 901, and every `i` (and `l` where avoidable) for remembered English. I worked from the Latin, the pinned source and memory of the reference works only. No translation was opened. Pass 2 re-read every edited field in full and made two further changes (P2-1, P2-2).

I then hand-scanned all 101 lines by quantity and compared each with the scanner's output. The scanner was run in-process, the way `build_aeneid.py` calls `SL.scan_story` on the units. Every new `scan-fixes.json` entry was checked against a replica of the build's word-match rule (`strip(sc) == WORD_RE.findall(line)`) and of the validator's six-foot rule (feet 1–6, 12–17 syllables, one ×, five –⏑⏑/–– feet and a sixth –×/⏑×). The half-line 835 was checked against the validator's half-line branch instead: its `why` starts with "Half-line", it has feet 1..k with k < 6, and it has one ×. I then ran a replica of the build's scansion step with the fixes applied. All 9 entries applied. The scanner report is empty, which clears the packet's COSTLY flags at 831 and 832 and the UNRESOLVED at 835. All 101 lines pass.

`t` is untouched. The cut tuples in `make_units.py` are unchanged. The regenerated `units.json` has the same `t`, `ln`, `p` and `v` in all 46 units. I checked this by script against a copy taken before any edit. `title`, `titleEn` and `part` are unchanged. `about` has three phrases changed (L1, P2-1, P2-2). Edits were made to the strings in `make_units.py` by a Python replace script, with each old string asserted to occur once. `units.json` was then regenerated with `make_units.py`. `build_aeneid.py` was not run. The diff to `scan-fixes.json` only appends (106 insertions, 0 deletions). `new-renderings.md` was updated to match.

**Speech marks**: `t`, `l` and `i` each have 3 “ and 4 ”. The extra ” closes Anchises's speech from 756 at 853, which has no opening mark in this part. The validator will warn about it, and the warning is expected.
- Anchises (from 756): → 853 (” after *superbos.*).
- Anchises: 855 → 859 (“ at *Aspice*, ” after *Quirino.*).
- Aeneas: 863 → 866 (“ at *Quis*, ” after *umbra.*).
- Anchises: 868 → 886 (“ at *O gnate*, ” after *munere*, before Greenough's dash).

All four agree across `t`, `l` and `i`, unit for unit.

**Severity counts: major 4, medium 18, low 29 (27 in pass 1, 2 in pass 2). Refused findings: 24 (listed at the end).**

## Changes — pass 1

### Major
1–4. **Scansions the scanner got wrong without a flag.** Each now has a hand entry.
   - **6.814 *desueta***: the scanner read *dĕ-sŭ-ē-ta* as four syllables, with the prefix short. It is *dē-suē-ta*, three syllables, with u consonantal as in *suesco*. Hand scansion: Tul-lŭs ĭn | ar-mă vĭ | rōs et | iam dē | suē-tă trĭ | um-phīs. (The same error was published at 2.509; see "For the owner".)
   - **6.836**: the scanner made the -phā- and -tā of *triumphātā* short (ablative absolute with *Corintho*), and the Ca- and -pi- of *Căpĭtōlia* long. Hand scansion: Il-lĕ trĭ | um-phā | tā Că-pĭ | tō-lĭ(a) ăd | al-tă Cŏ | rin-thō.
   - **6.880**: the scanner made the -mā- and -tō of *armātō* short and both syllables of *pĕdĕs* (foot-soldier) long. Hand scansion: ob-vĭ-ŭs | ar-mā | tō seu | cum pĕ-dĕs | ī-rĕt ĭn | hos-tem.
   - **6.901**: the scanner made the -co- and -ra of *ancŏră* long and *dē* and *prō-* short. Hand scansion, the same as the 3.277 entry: An-cŏ-ră | dē prō | rā iă-cĭ | tur stant | lī-tŏ-rĕ | pup-pēs. *Prōrā* is ablative after *de*, so long by nature.

### Medium
5–9. **Scansion: the known blind spots and the packet's flags.**
   - **6.860 *Aeneas***: the scanner split Ae- into two short syllables (A-ĕ-nĕ-ās). Hand scansion: At-qu(e) hīc | Aē-nē | ās ū | nā nam | qu(e) ī-rĕ vĭ | dē-bat.
   - **6.835** (packet flag, UNRESOLVED), half-line: prō-ĭ-cĕ | tē-lă mă | nū san | guĭs mĕ-ŭs. That is three feet and a fourth begun, with × on the last syllable, entered in the form of the earlier half-lines (5.815, 6.94). In *proice* the i is consonant and vowel at once, so *prō-* is long. *Sanguis* is two syllables, its -is long by position before *meus*.
   - **6.834** (carrier): this line shares a unit with 835. The build gives no `sc` to a unit with an unresolved line, so without this entry 834 would reach the validator with no scansion (cf. 1.559). The entry is the scanner's own fit, checked by hand: tū-quĕ prĭ | ōr tū | par-cĕ gĕ | nūs quī | dū-cĭs Ŏ | lym-pō.
   - **6.831** (packet flag, COSTLY 2.0): I confirmed the scanner's parse by hand and entered it to clear the flag: dē-scen | dens gĕ-nĕr | ad-ver | sīs in | struc-tŭs Ĕ | ō-īs. *Eōīs* needs a short E here (see the doubtful list).
   - **6.832** (packet flag, COSTLY 2.7): I confirmed the scanner's parse by hand and entered it: Nē pŭ-ĕ | rī nē | tant(a) ă-nĭ | mīs ad | suēs-cĭ-tĕ | bel-la. The u of *adsuescite* is consonantal.
10. **845 `quo`, rule 5b, overturned.** The draft corrected *quo* to *Quo*, saying that Greenough "begins every other sentence after a question mark with a capital". That is not true of the edition. A search of the pinned source finds a small letter starting a new sentence after a question mark at 1.583 (*omnia tuta vides*) and 11.414 (*oremus pacem*). It also finds the same after ! at 4.65, and the series-continuing *an*, *aut* and *quosve* at 1.329, 2.45 and 4.409. aeneid-007 published 1.583 without comment. A small letter after a question is therefore a habit of this print, not a clear misprint, and rule 5b excludes "the source's own… habits". The note now reads: "Greenough prints 'quo' with a small letter after the question mark, as he does elsewhere (1.583, 11.414), so it is kept as printed; it begins a new question all the same." The reading is unchanged.
11. **844 comma, rule 5b, overturned the other way.** The draft kept *te sulco Serrane, serentem* as a doubtful reading. A vocative closed by one comma and not opened by any is a dropped mark that allows only one reading. The precedents treat a dropped mark as a rule-5b misprint: 3.286 (`clipeum.` for a comma) and aeneid-039 (a dropped colon and parenthesis). The note now opens: "The print has 'sulco Serrane, serentem', with no comma before the vocative, a misprint for 'sulco, Serrane, serentem', corrected here; t keeps the print; l and i give the reading." `l` and `i` already read it that way. This needs a QUESTIONS.md line (below).
12. **Note 832–833, a wrong label**: "'Animis' may be dative ('accustom your minds to') with 'tanta… bella' as the object" glossed the construction as if *animis* were the object. It now reads: "'Adsuescite' is here transitive, with 'tanta… bella' as its object and 'animis' a dative: 'do not make such wars familiar to your minds'."
13. **Note 838–840, Aeacides**: "the Macedonian kings claimed descent from Aeacus" was too broad. The claim belongs to Perseus, through Achilles. The note now reads: "Perseus counted Achilles, grandson of Aeacus, among his forebears (Propertius sneers at him for aping his ancestor Achilles). Some have thought of Pyrrhus of Epirus, whose royal house traced itself to Achilles's son." The Paullus/Pydna identification stays as the usual one.
14. **Note 857–859, Quirinus**: "an old law ascribed to Numa is said to have assigned the third such spoils to Quirinus" took "third" in that law as the third occasion. It now reads: "An old law ascribed to Numa, reported by Festus, gave 'third' spoils to Janus Quirinus, though what 'third' means in that law is disputed; other accounts have Marcellus dedicate his to Jupiter Feretrius, like the first two."
15. **i 851–853, the set piece.** The draft opened with "As for you, Roman", which has the shape of the best-known "But you, Roman, remember". It also had "to show mercy to those who submit", which is close to "show mercy to the conquered" and "spare those who submit". It now reads: "Your task, Roman — never forget it — is to rule the peoples by your sovereign power (these will be the skills that are yours), to establish peace and make it their custom, to spare whoever yields, and to fight the haughty until the war is done.” `l` is kept as drafted (see R8). `about` was brought into line (L1).
16. **l 893–896, the Gates of Sleep** (flagged by the drafter): "There are twin gates of Sleep… by which to true shades easy exit is given" ran a known version's sequence (twin Gates of Sleep / easy… true shades) in the same order. It now reads "There are paired gates of Sleep, of which the one is said / to be of horn, through which to genuine shades an easy exit is granted;". In 895, "wrought of gleaming ivory" is now "wrought of white-glowing ivory" (*candenti*). Only "false dreams", the bare literal of *falsa insomnia*, is kept.
17–22. **Remembered English in `i`**: each of these ran close to a known version, clause for clause.
   - **888–892**: "had set his heart on fire with longing for the glory to come, he tells him then of the wars… instructs him about the Laurentine peoples… how to avoid each hardship or how to endure it" is now "When Anchises had taken his son through it all, sight by sight, and kindled in him a passion for the renown that lay ahead, he goes on to tell the hero of the wars that next await him, teaches him about the peoples of Laurentum and the city of Latinus, and shows how he may escape each trial, or bear it."
   - **886–887**: "So they roam here and there through the whole region, across the wide fields of air, and look on everything" is now "So, ranging far and wide over the whole region, through the broad plains of air, they take in every sight."
   - **879–881**: "drove his spurs into the flanks of a foaming charger" is now "raked a foaming horse's shoulders with his spurs". This also renders *armos* (shoulders), not "flanks".
   - **868–870**: "do not seek to learn of the vast sorrow of your people; fate will only show this youth to the world" is now "My son, do not ask about the great grief your descendants will bear. The fates will let the earth have one glimpse of him, no more; they will not allow him to stay."
   - **866**: "But a black night hovers round his head with its dismal shadow" is now "But dark night flits about his head and wraps it in gloom." *Circumvolat* means "flits", not "hovers".
   - **847–850**: "Others, I am sure of it, will beat out bronze that seems to breathe" (the shape "I doubt not… beat out the breathing bronze") is now "Others — I readily grant it — will hammer bronze into figures that breathe, with a subtler hand, and coax living features out of marble; they will argue cases more ably, chart with the pointer the courses of the sky, and name the stars as they climb:".

### Low
24. **`about` (L1)**: "to spare those who submit and to fight down the proud" ("fight down" is near "battle down the proud") is now "to spare whoever yields and to fight the haughty until the war is done", to match the set piece.
25. **Note 801–805**: this was 148 words, over the limit. Two glosses were dropped ("'Obivit' is 'went over'", "'Iuga' are 'yokes'"). `l` already shows both.
26. **Notes 806–807 and 900**: "most editors now print/read" is now "many editors", for *virtutem… factis* and *limite*.
27. **i 809–812**: "I recognise the locks and the white beard… to a mighty throne" is now "I know that hair and the grizzled chin: it is the Roman king who… sent out from little Cures, a poor country, to wield great power." The old version was close to "the white hair and beard" and "to mighty empire".
28. **Note 812–815**: added "'Desueta' is three syllables, dē-suē-ta, the u a consonant, as in 'suesco'", to go with the scan fix.
29. **i 822–823**: "Unhappy man, however later ages will judge that act… will win the day" is now "Ill-starred father! Whatever later generations make of that act, love of his country will carry the day, and a measureless hunger for praise."
30. **Note 824–825, Camillus**: "recovered the standards and gold" put the standards in Livy, who has only the gold. The note now reads: "in Livy's story… won back the ransom gold; Virgil has him bring home the standards ('referentem signa')".
31. **Note 826–829**: added that *fulgere* (826) is the old third-conjugation form with a short e, as the metre shows.
32. **i 834–835**: "and you be the first, you be the one to hold back… throw down the weapons from your hand, my own blood!" was awkward and close to "cast the weapons from your hand, my blood". It now reads: "and you, you first, be the one to forbear, you who draw your descent from Olympus: let the weapons fall from your hand, you who are of my blood! —".
33. **Note 834–835**: "'Proice' is 'proiice'" is now "the imperative of 'proicio', 'throw away', three syllables, prō-ĭ-cĕ: the i serves as consonant and vowel at once, so the first syllable is long".
34. **Note 838–840, a wrong label**: "'Achilli'… a Greek genitive in '-i'" is now "an old genitive in '-i' (from the by-form 'Achilleus'), like 'Ulixi'". The *armipotentis* gloss was dropped to keep the note under 140 words.
35. **i 841**: "Who could pass you by in silence, great Cato" is now "Who would let you go unnamed, great Cato, or you, Cossus?"
36. **Note 841**: Cossus's "(437 BC)" is now "(437 BC, in Livy's account)". Livy himself raises the dating question.
37. **i 842–844**: "twin thunderbolts of war… mighty on a little… sowing seed in your furrow" is now "the house of Gracchus, or the two Scipios, war's double thunderbolt, Africa's undoing, or Fabricius, a power on slender means, or you, Serranus, scattering seed along your furrow?". The note now quotes Lucretius's own words ("Scipiadas, belli fulmen") and drops "'Libya' is Africa" and "including the reforming tribunes" for length.
38. **Note 851–853**: "The most quoted lines" is now "Among the most quoted lines". "'Superbos'… answers 'animam superbam' of 817" was dropped, because that claim cannot be supported. Two glosses were shortened to keep the note under 140 words (it had been 162).
39. **i 865**: "What a stir of companions round him! What a presence there is in the man himself!" is now "How his companions throng and clamour round him! What greatness shows in the man himself!"
40. **l 867**: "with tears having begun, rising up" was garbled. It is now "Then father Anchises, having begun, with tears welling up:".
41. **i 872–874**: "the new-built tomb" is now "the freshly raised mound".
42. **i 875–877**: "lift his Latin forefathers so high in their hopes… take such pride in any son" is now "raise such hopes in his Latin ancestors, nor will the land of Romulus ever glory so in any child it has nursed".
43. **i 878–879**: "his goodness" was weak for *pietas*. It is now "his dutiful heart".
44. **i 882–883**: "tear the cruel web of fate" added a metaphor that is not in the Latin. It is now "shatter fate's harsh decree".
45. **l 885**: "let me heap up gifts" made *dona* the object. It is now "with these at least let me load — gifts —", because *his… donis* is the instrument.
46. **Note 883–886**: "'Spargam', 'adcumulem' and 'fungar' are jussive subjunctives" is now "'Adcumulem' and 'fungar' are hortatory subjunctives…; 'spargam' could be future or subjunctive, and goes with them".
47. **Note 888–892**: added the line number of the Helenus line, "(3.459, 'fugiasque ferasque')". It was verified in the pinned source.
48. **l/i 897–899**: in `l`, "he cuts his way" is now "that one cuts his way", which shows the change of subject at *ille*. In `i`, "cuts a straight path" took *recto* from 900; it is now "cuts his way back".
49. **Note 901**: "which some manuscripts add here" is now "It repeats 3.277 word for word, and is thought to have been added here…". I cannot vouch for the manuscript claim from memory.
50. **Note trims after edits**: 838–840 (143 → 133), 842–844 (148 → 138) and 851–853 (146 → 137). No note is now over 140 words.

## Changes — pass 2
- **P2-1 (low)**: in `about`, "whom fate will only show to the world" repeated the shape changed in i 868–870. It is now "whom fate will let the world glimpse and then take away".
- **P2-2 (low)**: in `about`, "one of horn for true shades" is now "one of horn for shades that tell the truth", to match the change to `l` 893–894.

## Scan-fixes lines added (9)
These 9 entries were appended at the end of `scan-fixes.json`, each with its reason. The existing entries are unchanged: the diff only appends (106 insertions, 0 deletions).
- 6.814
- 6.831
- 6.832
- 6.834 (carrier)
- 6.835 (half-line)
- 6.836
- 6.860
- 6.880
- 6.901

Each entry matches its line's words under `WORD_RE`. The eight full lines each have six feet, five dactyls or spondees, then –×, 13–16 syllables and one ×. The 835 half-line has feet 1–4 and one ×. In the replicated build with all fixes applied, the scanner report is empty and all 101 lines pass.

## Hand-scan notes on the special lines (scanner right, no entry)
- **Initial Ae-**: *Aeaciden* (839) is right. The scanner took Ae- as the diphthong, then a short a: Aē-ă-cĭ | dēn. *Aeneas* (860) is fixed. *aeripedem* (802) is right, aē-rĭ-pĕ-dem.
- **Greek eu**: there is none in this part. *Heu* (828, 878, 882) is a Latin diphthong and is right.
- **Consonantal i after a prefix**: *deiecto* (862) is dē-iec-tō, right. *subiectis* (853) has the right quantities: the scanner divides it su–biec, but sub- is long by position before the doubled i, the same cosmetic division as *obicit* at aeneid-044. *proice* (835) is in the half-line entry. *Troiae* (840), *Caietae* (900), *iacitur* (901), *iuxta* (815), *iam* (814, 816) and *iactantior*/*iactabit* (815, 877) are right.
- **Hiatus**: none. Every vowel meeting is an ordinary elision, before h- included (*ille autem*, *imperium hic*, *atque hic*, *propria haec*, *saltem adcumulem*). *Ille es* (845) is prodelision.
- **Others checked and right**: *pācārit* (803); *Līber*, *Nȳsae* (805); *ăd-hūc* (806); *prŏhĭbet* (807); *Cŭribus* (811); *Cui* and *dein-* as monosyllables (812, 890); *rĕsĭdēs* (813); *Brūtī* (818); *Drūsōs* (824); *Torquātum* (825); *fulgĕre* (826); *Mŏnoecī* (830); *Mȳcēnas*, scanned My- short (838); *Scīpiadās* (843); *cunctandō*, *restituīs rem* (846); *excūdent*, *aliī* (847); *rădiō* (850); *supērēminet* (856); *patrī* (859); *formā* (861); *instar in* (865); *praeterlābēre* (874); *Īliacā* (875); *quā* (882); *mănibus*, "hands" (883); *āĕris* (887); *Cāiētae* (900).

## Doubtful quantities entered on the only fit
- **6.831 Ĕōīs**: the E is short here, and only that fits foot 5. The word is Ēōus at 1.489 (entry there), so the E is variable in Virgil. Here the metre settles it.
- **6.811 Cŭribus** (scanner's fit, no entry): the u is short, the only fit in foot 2.
- **6.844 Fābricium** (scanner's fit, no entry): the first syllable is long. It is long either by nature or by position before *br*, so the scansion is the same either way.

## Refused findings
- **R1 — 901 = 3.277**: verified in the pinned source. The text is identical, except that the line here begins a sentence inside Greenough's bracket. Kept, with the manuscript claim hedged (item 49).
- **R2 — 640–641 cite at 887**: verified (*Largior hic campos aether et lumine vestit / purpureo…*). Kept.
- **R3 — Ennius at 846 via Cicero**: kept. *Unus homo nobis cunctando restituit rem* is Ennius's *Annals*, quoted by Cicero (*De Senectute* 10, and *De Officiis* 1). The note says only "a line Cicero quotes", which is safe.
- **R4 — Lucretius "belli fulmen"**: kept and made exact (item 37). Lucretius 3, *Scipiadas, belli fulmen, Carthaginis horror*. The note cites the book, not the line.
- **R5 — Octavia fainting, in Donatus**: kept. The story is in the Donatus Life (the recitation of Books II, IV and VI to Augustus, with Octavia fainting at *tu Marcellus eris*). The note words it as "an old story".
- **R6 — Aeacides, Perseus vs Pyrrhus**: the Perseus reading is kept as the usual one, and Pyrrhus stays as an alternative. Only the descent claim was corrected (item 13). The note does not mention that Pyrrhus died at Argos. That would be a tempting link to *eruet ille Argos*, but it is speculative.
- **R7 — Helenus line behind 892**: verified, 3.458–460 (*Illa tibi… et quo quemque modo fugiasque ferasque laborem / expediet*). Kept, and the cite was added (item 47).
- **R8 — l 851–853**: kept as drafted. It is word for word ("these for you will be the arts" is the bare literal of *hae tibi erunt artes*), and it avoids every listed echo, including "war down the proud".
- **R9 — i 878–879 "old-fashioned honour"**: kept. It is not a known version's phrase, and it keeps *prisca*.
- **R10 — i 882–883 "You are to be Marcellus."**: kept. It avoids "you shall be Marcellus" and leaves both readings in the note open.
- **R11 — i 883–886, the lilies**: kept. "Bring lilies by the heaped handful… a rite that can change nothing" is clear of the familiar wordings.
- **R12 — i 855–856 "towers in victory over all the others"**: kept. *Supereminet omnes* has few ways into English, and this is not a known version's full clause.
- **R13 — l 847–850 "breathing bronzes", "plead causes better"**: kept, as word-for-word `l`. `i` was moved (item 23).
- **R14 — 6.839 *Aeaciden***: no entry is needed (scanner right). See the hand-scan notes.
- **R15 — 6.853 *subiectis*, 6.862 *deiecto***: no entries. The quantities are right, and only the syllable division at *su–biec* is cosmetic (the same open question as QUESTIONS.md item 37/38).
- **R16 — Caesura marks**: the new entries carry ‖ where the main caesura is clear (836, 880, 860, 901). Neither the build nor the validator needs the mark.
- **R17 — Latin Library variants**: the sense-changing ones are already noted in `n`: *virtutem… factis* (806), *primam* (810), *prementur* (827), *pacique* (852), *ibi* (897), *limite* (900) and *qui* (865). The rest are orthography or morphology and are rightly noted as such or ignored.
- **R18 — Note 812–815, "'Tullus'… held back to the middle of the clause"**: kept. The name is the subject of *subibit*, set inside the relative clause that describes him, so the description is fair.
- **R19 — Serranus as C. Atilius Regulus, consul 257 BC**: kept. This is the usual identification. The sowing story is attested (Cicero, *Pro Roscio Amerino*; Pliny), and the note gives it as "was said".
- **R20 — Note 862, "about nineteen years old"**: kept. Marcellus was born in 42 BC and died in 23 BC.
- **R21 — Note 874, the Mausoleum**: kept. Marcellus was the first to be laid in Augustus's Mausoleum on the Campus Martius.
- **R22 — Note 823, "'Cupido' is feminine"**: kept. That is right for the common noun, and *immensa* confirms it.
- **R23 — Note 856, "only Romulus, Cossus and Marcellus ever won them"**: kept. It is the canonical list.
- **R24 — `title`, `titleEn`, `part`**: these are our own and borrow no translation's heading. Unchanged.

## For the owner (QUESTIONS.md)
- **6.844, a new rule-5b misprint**: `sulco Serrane, serentem` should read `sulco, Serrane, serentem`. `t` is as printed (it must match the pinned source), `l`/`i` read the comma, and the note opens with the print's reading. There is no emend list for the Aeneid, so the correction is to be recorded in QUESTIONS.md.
- **6.845 `quo`**: not a misprint (item 10), so it is kept as printed. If the drafter staged a QUESTIONS.md line correcting it, drop that line.
- **2.509 *desueta*, already published (aeneid-014)**: the published `sc` reads dĕ-sŭ-ē-ta, four syllables (`de⏑su⏑4e–ta⏑`), which is the same scanner error as 6.814. The quantities are wrong and the line still has six feet, so the validator passed it. 1.722 (aeneid-008) has it right. A `scan-fixes.json` entry for 2.509 and a rebuild of aeneid-014 would correct it. 7.693 (*desuetaque bello*) will meet the same error.
- **3.277 entry's reason**: the existing entry's `sc` is right, but its `why` says the ra of *prora* is "lengthened before the consonantal i of iacitur". *Prōrā* is ablative after *de*, long by nature. The 6.901 entry gives the right reason. 3.277 was left unedited, because the file is append-only.
- **From memory, worded as attributions**: Festus on Numa's law of the *spolia opima* (859); Propertius on Perseus aping Achilles (840); Livy's dating of Cossus (841). None was checked against the text in this run.
- **Doubtful quantity on the only fit**: 6.831 Ĕōīs (short E; long at 1.489).

## After review (run)

The build refused the cut after `munere”—` at 886 (the source prints no space before `Sic`), so the units ending at 886 and 887 were merged into one five-line unit (883–887), as at 2.604 and 4.127; the note says so. `t` still tiles the source. 45 units published (46 in the review above).
