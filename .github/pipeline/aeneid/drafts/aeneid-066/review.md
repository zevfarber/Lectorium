# Review — aeneid-066 (Aeneid IX.224–313), adversarial reviewer

I reviewed this part in two passes.

**Pass 1** covered all 39 units word by word. I checked `l`, `i` and `n` against the Latin, every grammatical label, every elision list, every cross-reference and every historical or mythological claim. I also checked the drafter's three rule-5b misprint calls (9.250 `pectora. ”Sic`, 9.280 `fides. ”Contra`, 9.292 `omnis. ”Percussa`), the missing mark after `parentis` at 9.289, the *aut*/*haud* handling at 9.283, *patriae pietatis* at 9.294, the Latin Library variants, the `about`, the title and part names, and every attribution made from memory. I read every `i` for echoes of the well-known English versions, with 9.247, 9.281, 9.294 and 9.312–313 read most closely.

I worked from the Latin, the pinned source and memory of the public-domain reference works (Lewis & Short, Allen & Greenough, Greenough's notes, Conington, Servius). No translation was opened and nothing was searched.

In-poem cross-references were checked against the pinned source: 1.16, 1.121, 1.267–288, 2.296–297, 2.771–789, 4.522–532, 4.528 (bracketed), 5.715–718, 9.8–11, 9.117, 9.164–167, 9.171, 9.177, 9.196, 9.216–223, 10.824 and 11.794–795. All say what the notes say. One claim was incomplete (item 17): Aeneas is not "with Evander" now; he has gone on to the Etruscans (9.10–11).

**Pass 2** re-read every edited field in full and made three more changes (P2-1 to P2-3).

**Scansion.** I hand-scanned all 90 lines by quantity. I then ran the scanner in-process, the way `build_aeneid.py` calls `SL.scan_story`, and compared its output with mine syllable by syllable.
- **The scanner was wrong on 11 lines**: 226, 228, 232, 241, 248, 249, 255, 290, 291, 293 and 310. Of these, 232, 241, 291, 293 and 310 were flagged. Each now has a hand entry.
- **295 is a half-line** (*Tum sic effatur:*), which the scanner returns as UNRESOLVED. It now has a half-line entry. 296 shares its unit, so it gets a carrier entry; without one, unit 295–296 gets no `sc` at all.
- **The other two flagged lines are right**: 281 and 304. They get no entry (see the hand-scan notes).

Every new `scan-fixes.json` entry was checked by script against a replica of the build's word-match rule (`strip(sc) == WORD_RE.findall(line)`). Each was also checked against the validator's metre rule: six feet, 12–17 syllables, one ×, five –⏑⏑/–– feet and a sixth –×/⏑×. For the half-line, the check was numbered feet 1..k with k < 6 and one ×. Each `why` gives a syllable count, and the script checked that count against the entry.

I then ran a replica of the build's scansion step, reading the fixes from `scan-fixes.json` itself:
- all 13 entries apply
- **all 39 units get `sc`**
- all 90 lines pass the validator's metre check (89 hexameters and one half-line)
- after the fixes, the scanner report holds only COSTLY 281 and 304. Both are hand-checked right, and neither blocks the build.

**What was edited, and how.**
- `units.json` was edited by Python script. Each old string was asserted to occur exactly once in the named field. The file is written with `aeneid_lib.jdump` (`indent=1`, `ensure_ascii=False`, no trailing newline, as the drafter's file).
- `t`, `ln`, `p` and `v` are byte-for-byte as the drafter left them in all 39 units. A script checked this against a copy of the drafter's file taken before any edit. `title`, `titleEn`, `part` and `about` are unchanged.
- **18 units changed.** `l` has the same number of lines as `t` in every unit, and no `i` has a line break.
- **Speech marks**: 7 “ and 7 ” in each of `t`, `l` and `i`, on the same units.
- **Note lengths.** Every note is now 44–138 words. Five notes were over the validator's 140 (224: 149, 247: 161, 257: 163, 263: 161, 288: 142) and were trimmed (item 41).
- **`make_units.py` was not touched.** It still holds the drafter's strings, so re-running it would undo this review. Build from `units.json` as it stands.
- The diff to `scan-fixes.json` only appends: 148 insertions, 0 deletions, trailing newline kept, formatting as before (a round-trip of the old file through `json.dumps(indent=1, ensure_ascii=False)` was byte-identical before appending). The new keys follow 9.204, in line order.
- The build and the validator were not run. Their scansion steps were replicated instead.
- **`drafts/aeneid-066/` has no `gloss.json`.** The build needs one. That belongs to the glosser's step, not this review.

**Severity counts: major 12, medium 5, low 27 (24 in pass 1, 3 in pass 2). Refused or upheld-without-change findings: 20. Scan-fixes entries added: 13.**

## Changes — pass 1

### Major
1–11. **Scansions the scanner got wrong.** Each line now has a hand entry with its reason.
- **Initial *Ae-* split (3 lines)**:
  - 9.228 *quisve Aeneae*: quid fă-cĕ | rent quis | v(e) Ae-nē | ae iam | nun-tĭ-ŭs | es-set (14 syllables; the scanner had 15).
  - 9.241 *quaesitum Aenean et moenia Pallantea*, flagged COSTLY 5.2: quae-sī | t(um) Ae-nē | ān et | moe-nĭ-ă | Pal-lan | tē-a (13 syllables), a spondaic fifth foot as at 9.196. The scanner left *quaesitum* unelided, made *-ne-* short and split *moe-* into *mo-e*.
  - 9.255 *pius Aeneas*: ac-tū | tum pĭ-ŭs | Ae-nē | ās at | qu(e) in-tĕ-gĕr | ae-vi (14 syllables; the scanner had 15).
- **Greek *eu* in *Teucri* split (2 lines)**: 9.226 (duc-tō | rēs Teu | crum prī | m(i) et dē | lec-tă iŭ | ven-tus, 13) and 9.248 (nōn tă-mĕn | om-nī | nō Teu | crōs dē | lē-rĕ pă | rā-tis, 14). The scanner had one syllable more each time.
- ***Iulus* read with a consonantal I (3 lines, all flagged)**: Ĭ-ū-lus is three syllables, as in the 12 earlier entries for this name (1.556, 5.570, 7.107 and others).
  - 9.232: rem mag | nam prĕ-tĭ | um-quĕ mŏ | rae fŏ-rĕ | prī-mŭs Ĭ | ū-lus (16).
  - 9.293: Dar-dă-nĭ | dae lă-crĭ | mās an | t(e) om-nīs | pul-chĕr Ĭ | ū-lus (15). The line ends with the same words as 5.570.
  - 9.310: prō-sĕ-quĭ | tur vō | tīs nec | nōn et | pul-chĕr Ĭ | ū-lus (14).
- **Wrong quantities with the right count (2 lines, unflagged)**:
  - 9.249 *talis animos*: *tālīs* (accusative plural) is long in both syllables and *ănĭmos* short in both. cum tā | lī-s ă-nĭ | mōs iŭ-vĕ | n(um) et tam | cer-tă tŭ | lis-tis (15). The scanner had *tă-lĭs* | *ā-nī*.
  - 9.290 *solare inopem*: *sōlor* has a long ō and ā, *ĭnops* two shorts, and *tu* elides into *oro*. at t(u) ō | rō sō | lā-r(e) ĭ-nŏ | p(em) et suc | cur-rĕ rĕ | lic-tae (14). The scanner had *sŏ-lă* | *rī-nō*.
- **9.291, hiatus (flagged COSTLY 2.1)**: *tui: audentior* does not elide. With elision there is no fit, so the long ī of *tuī* stands in hiatus at the sense pause, as at 1.16. Hanc sĭ-nĕ | mē spem | fer-rĕ tŭ | ī au | den-tĭ-ŏ | rī-bo (15 syllables). The scanner ran *tui* into one syllable and made *-re* of *ferre* long.

12. **9.295–296, the half-line.** 295 *Tum sic effatur:* is a half-line: Tum sīc | ef-fā | tur (5 syllables). It is entered as a half-line, so the validator applies its hemistich rule. 296 gets a carrier entry: the scanner's own fit, Spon-dē | dig-nă tŭ | īs in | gen-tĭ-bŭs | om-nĭ-ă | coep-tis, checked by hand. Without these two entries the unit gets no `sc` and the build stops on UNRESOLVED.

### Medium
13. **Note 9.287–288, a wrong label.** The note had "'huius' and 'pericli' both hanging on 'ignaram'". *pericli* is a partitive genitive with *quodcumque* ("whatever there is of danger"); only *huius* depends on *ignaram*. It now says so.
14. **Note 9.281–283, a false elision.** The note listed "Elision 'secund(a) aut'". *secunda* ends line 282 and *aut* begins 283, and 282 is a complete hexameter (dis-sĭ-mĭ | l(em) ar-gŭ-ĕ | rit tan | tum for | tū-nă sĕ | cun-da), so nothing elides across the line end. The elision the line has, *dissimil(em) arguerit*, was missing. The note now gives it and says *secunda* does not elide.
15. **Note 9.291–293, a false elision.** "Elision 'tu(i) audentior'" was wrong: with that elision the line has no fit. It is a hiatus (item 11), and the note now says so and shows the feet.
16. **Note 9.263–266, an unverifiable claim.** "no other story of Aeneas taking it survives, and ancient commentators were puzzled by it" rested on memory I could not check (what Servius says about Arisba). It now reads "its capture by Aeneas is not told elsewhere in the poem", which the pinned source confirms (*Arisba* occurs only at 9.264).
17. **Note 9.226–228, Aeneas's whereabouts.** "who is away up the Tiber with Evander (Book 8)" is out of date at this point: Iris has just told Turnus that Aeneas has gone on beyond Evander to the cities of Corythus and is arming the Lydians (9.8–11). It now reads "who has gone up the Tiber to Evander and on to the Etruscans (Book 8; 9.8–11)".

### Low
18. **`l` 9.224**: "throughout the lands" dropped *omnis*. It now reads "throughout all the lands".
19. **Note 9.224–225**: "who left the gate" now reads "who left their post" (*statione relicta*, 9.222). The Iliad 10 sentence was shortened (see item 41).
20. **`l` 9.226**: the note rightly says there is no "but" in the Latin, but `l` began "but the leaders". It now reads "(but) the leaders". `i` keeps "but", as English needs it.
21. **Note 9.226–228**: added that *Teucrum* is two syllables with the Greek *eu* one long sound, which agrees with the 9.226 entry.
22. **Note 9.226–228**: the elision *quisv(e) Aeneae* was missing. It is added, with "(Ae-nē-ae, three syllables)", which agrees with the 9.228 entry.
23. **Note 9.234–236**: the elision *nev(e) haec* was missing (Ae-nĕ-ă | dae nē | v(e) haec nos- …). It is added.
24. **Note 9.240–243**: "No elisions" was wrong; *quaesit(um) Aenean* elides. Added that *Aenean* is three syllables, and that the line ends in a spondaic fifth foot, as at 196. Both agree with the 9.241 entry.
25. **`i` 9.250**: "by the shoulders and the right hand" now reads "the right hands" (*dextras*, of both men).
26. **Note 9.247–251**: "'talis', accusative plural" now adds "(tālīs)", which agrees with the 9.249 entry.
27. **Note 9.253–256**: "'pius Aeneas'" now adds "(Ae-nē-ās, three syllables)", which agrees with the 9.255 entry.
28. **`i` 9.260**: "whatever hope I have" did not match `l` ("trust") or the note ("confidence"). It now reads "whatever confidence I have".
29. **Note 9.263–266**: the elisions *dab(o) argento* and *atqu(e) aspera* were missing. Both are added.
30. **Note 9.270–271**: "No elisions" was wrong; *ips(um) illum* elides. It is added.
31. **Note 9.281–283**: "the reading most editors prefer" for *haud* is a count I cannot check. It now reads "a reading many editors prefer".
32. **`l`/`i`/note 9.289 *nequeam***: "that I could not" made a past of a present subjunctive. `l` and `i` now read "that I cannot", and the note says "present subjunctive".
33. **Note 9.288–290, the rule-5b opening**: "The print has no mark after 'parentis' at the end of 289, a misprint (a stop dropped), corrected here" did not follow the rule's form. It now reads "The print has 'parentis / at tu' with no mark, a misprint for 'parentis; at tu', corrected here", and adds that the lower-case *at* rules out a full stop and that a colon would read the same.
34. **Note 9.288–290**: "he is clasping Ascanius's hand" is not in the Latin. It now reads "the right hand is the one that pledges faith".
35. **Note 9.288–290**: the elision *t(u) oro* was missing. It is added, with the quantities *sō-lā-re* and *ĭ-no-pem*, which agree with the 9.290 entry.
36. **Note 9.293–294**: "'pulcher Iulus'" now adds "(I-u-lus, three syllables, as at 232)", which agrees with the 9.293 and 9.310 entries.
37. **`l` 9.296**: "Be pledged things worthy…" made *Sponde* passive. It now reads "Pledge (yourself) things worthy…".
38. **Note 9.295–296**: "'digna… omnia'… framing the line" was wrong; the two words frame *tuis ingentibus*, not the line (which runs from *Sponde* to *coeptis*). It now says so.
39. **`l` 9.298–299**: "nor for a birth such the gratitude / small awaits" did not match the note, which rightly takes *manet* as transitive with *partum* as its object. It now reads "nor a birth such does gratitude / small await".
40. **Note 9.308–310**: added that the metre makes *omnis* short, so nominative singular with *manus*. Prō-tĭ-nŭs | ar-mā | t(i) in-cē | dunt quōs | om-nĭ-s ĕ | un-tis; a long accusative *omnīs* would not scan. This confirms the note's reading.
41. **Note lengths over 140 words**, all trimmed with no loss of substance:
    - 224 (149): "is an old contrast: it opens" was shortened.
    - 247 (161): the misprint explanation was shortened, and two glosses were cut (*memorans*, the second half of *sub numine*).
    - 257 (163): *Immo*, *Nise* and *Vesta* were said more briefly.
    - 263 (161): "*pocula* is held over" was cut, and *Arisba*, *talenta* and *Sidonia* were said more briefly.
    - 288 (142): *inopem… relictae* was said more briefly.

## Changes — pass 2
- **P2-1 (low), note 9.263–266**: item 41 left "'cups in a pair', the distributive, of things in pairs", which said the same thing twice. It now reads "the distributive numeral".
- **P2-2 (low), note 9.224–225**: item 19's trim left "A sleeping world against those who stay awake", which lacked a verb. It now reads "A sleeping world set against those who stay awake opens Iliad 10". "Instrumental ablative" now reads "ablative of means", A&G's term, as used elsewhere in this part (9.245).
- **P2-3 (low), note 9.224–225**: P2-2 put the note at 142 words. "(you'll see this constantly)" after Greenough's *-is* was cut, because that pattern was flagged many parts ago. The note is now 138 words.

Pass 2 also re-checked every "framing"/"enclosing" claim in the part: 224, 239, 244, 252–253, 260–261, 296, 299, 304, 305, 308–309 and 312. After item 38, all are right.

## Scan-fixes entries added (13)
These are appended after 9.204 in line order:
- **Initial *Ae-* (3)**: 9.228, 9.241 (flagged) and 9.255
- **Greek *eu* in *Teucri* (2)**: 9.226 and 9.248
- ***Iulus*, three syllables (3, all flagged)**: 9.232, 9.293 and 9.310
- **Wrong quantities, same count (2)**: 9.249 *tālīs ănĭmos* and 9.290 *sōlāre ĭnŏpem*
- **Hiatus (1)**: 9.291 *tuī | audentior* (flagged)
- **Half-line (1)**: 9.295
- **Carrier (1)**: 9.296

Each entry matches its line's words under `WORD_RE`. Each hexameter entry has six feet, five –⏑⏑/–– feet then –×, 13–16 syllables and one ×. The half-line has feet 1–3 and one ×. Each `why` states the count, and each count was checked by script.

## Hand-scan notes on the special lines (scanner right, no entry)
- **9.281, flagged COSTLY 2.1, right**: Eu-rў-ă | lūs mē | nul-lă dĭ | ēs tam | for-tĭ-bŭs | au-sis (15 syllables). *Eu-* is one syllable.
- **9.304, flagged COSTLY 2.0, right**: au-rā | tum mī | rā quem | fē-cĕ-răt | ar-tĕ Ly | cā-on (14 syllables). *mīrā* is the ablative with *arte*, and *Lycāōn* is three syllables (Λυκάων).
- **Other *eu* lines are right**:
  - *Euryalus* at 9.231 and 9.281
  - *Mnestheus* at 9.306, two syllables: Dat Nī | sō Mnes | theus pel | l(em) hor | ren-tis-quĕ lĕ | ō-nis (13)
- **Other *Ae-* line**: 9.235 *Aeneadae* (Ae-nĕ-ă-dae) is right. That line has *nev(e) haec* elided (item 23).
- **Consonantal i**:
  - *iuventus* (226), *iuvenum* (249, 309), *huius* (287) and *iam* (271, 276) are right.
  - There is no prefix + i compound in this part.
- **Hiatus**: only 9.291 (item 11).
- **Other quantities checked**:
  - *adnīxī* (229); *ălăcres* and *admittĭĕr* (231); *Rŭtŭlī* and *sŏlūtī* (236); *ātĕr* (239); *fortūnā* abl. (240); *Ălētēs* (246, 307)
  - *dēlēre* (248); *salūs* (257); *penātīs* (258); *cānae*, *penetrālia* (259); *mihī* (260); *Bīna* (263); *dēvictā* (264)
  - *tripodas*: *-das* is long by position before *geminos* (265)
  - *crātēra*, *antīquum*, *Sīdōnia* (266); *Ītaliam*, *potīrī* (267); *sortī* (271); *propiōribus* (275); *Īlia* (285); *Ăcestae* (286); *perīcli* (287)
  - *Creūsae* (297); *rĕdŭcī* (301); *ĕădem* (302); *Gnōsius*, *vāgīnā*, *ĕburnā* (305); *Prōtĭnus* and short *omnĭs* (308)
- **9.225 *corda oblita***: the scanner makes *d(a) ob-* long by position before *bl*. That is acceptable (muta cum liquida), and the line scans either way, so there is no entry.

## Refused or upheld findings
- **R1 — 9.250 `pectora. ”Sic`**: **upheld** as a rule-5b misprint, the pattern of 9.117 and 9.221. The note opens with the print's reading. Because the mark is joined to *Sic*, the unit rightly runs on to 251 *rigabat.*
- **R2 — 9.280 `fides. ”Contra`**: **upheld** on the same grounds. The unit runs on to *Euryalus:*.
- **R3 — 9.292 `omnis. ”Percussa`**: **upheld** on the same grounds. The unit runs on to *lacrimas;*.
- **R4 — 9.289, no mark after `parentis`**: **upheld** in substance. The 5b opening was reworded (item 33). See "Ruling on 9.289" below for rule 5.
- **R5 — 9.283 `aut`**: **upheld as handled**. *aut adversa* is a manuscript reading with a sense of its own (I answer for my courage; fortune may fall either way), not a misprint, so rule 5b does not apply. `l`/`i` follow Greenough, and the note gives the Latin Library's *haud* because it changes the sense. Only "most editors" was softened (item 31).
- **R6 — 9.294 *patriae pietatis***: **upheld**. The note gives both readings, "toward a father" (most) and "his father's" (some). `i` follows the first. Both are ancient, and the note does not overstate either. The parallel at 10.824 was checked in the source.
- **R7 — COSTLY 281 and 304**: hand-checked right, so no entries were made.
- **R8 — Latin Library variants**:
  - 238 *proxuma*, 251 *voltum*, 289 *lacrumas* and 305 *Gnosius* are orthography. The notes name Greenough's spelling, which is harmless.
  - 226 (LL omits *et*) and 287 (LL omits *est*) do not change the sense and are rightly not noted.
  - 283 *haud* changes the sense and is noted (R5).
- **R9 — `i` 9.247 "Gods of our fathers"**: kept. It is the plain sense of *Di patrii* and a stock phrase, not a distinctive echo.
- **R10 — Note 9.224, Iliad 10 opens with Agamemnon sleepless while the rest sleep**: kept (from memory, logged).
- **R11 — Note 9.263–266, *dat* "present for 'gave'"**: kept. It is the usual explanation (the gift still stands as Dido's).
- **R12 — Note 9.270–271, *sorti* dative of separation**: kept. It is the dative with a compound of *ex-*. An ablative "from the lot" would come to the same thing.
- **R13 — Note 9.297, *mihi* "dative of possession"**: kept. With *erit… genetrix* it is that or a dative of reference, and the label is defensible.
- **R14 — Note 9.289, *quod nequeam* as what the witnesses vouch for**: kept. A causal reading (the reason he leaves her unsaluted) is also possible, but the note's construction is sound.
- **R15 — Note 9.295 "nearly sixty such unfinished lines"**: kept. It is deliberately unspecific (compare "more than fifty" at 9.167).
- **R16 — Note 9.300, Aeneas used to swear by his son's head**: kept. *per quod pater ante solebat* says exactly that.
- **R17 — `i` 9.313 "to come to nothing"**: kept. It renders *inrita*, and I know no version that uses it here.
- **R18 — Note 9.231, *admittier* "belongs to old prayers and laws"**: kept. It is standard (A&G on the *-ier* infinitive).
- **R19 — Note 9.226–228, "'de' set between adjective and noun"**: kept. *de* stands inside the frame *summis… rebus*.
- **R20 — `about`, `title`, `titleEn`, `part`**: unchanged. The `about` agrees with the text throughout, checked line by line. That includes Ascanius giving his sword to Euryalus (implied at 303, and the usual reading) and Aletes exchanging helmets with Nisus. `part` and `titleEn` carry IX.224–313.

## Ruling on 9.289 (README rule 5)
- **It is a missing-punctuation case, rule 5 in kind, not a letter misprint.**
  - The *quod* clause ends with the line, and *at tu* opens a new clause, so a mark must stand after *parentis*.
  - Greenough capitalises *At* after a full stop (81 times; the one exception is 8.488), so the lower-case *at* means the lost mark was almost certainly not a full stop.
  - This is the only place in the pinned poem where a line ends with no mark and the next begins with *at* in a new clause. (1.542–543 *arma / at sperate* is a different case: the *at* answers a *si* clause.)
- **The mark to add is a semicolon**: source line 9.289 should read `dextera, quod nequeam lacrumas perferre parentis;`.
  - The draft's `l` and `i` already supply a semicolon.
  - Greenough's other line-final pauses before a lower-case *at* are `:` 4 times, `;` 3 times and `,` 4 times. A colon cannot be excluded, but it would read the same.
- **Caveat**: Greenough's page could not be checked. 8.137 and 8.336 were left as notes for exactly that reason, and the draft as it stands follows that precedent.
- **If rule 5 is applied**:
  - Add `;` at the end of 9.289 in `source/aeneid-greenough.json`.
  - Re-pin aeneid-066's `sha256` in `parts.json`. 9.289 lies only in this part.
  - In unit 27 (ln 288), change `t` line 2 to end `parentis;`.
  - Delete the note's first two sentences, from "The print has 'parentis / at tu'…" to "…a colon would read the same."
  - Log it in `LOG.md`.
- I did not edit the source or `parts.json`.

## For the owner (QUESTIONS.md)
- **Misprints (rule 5b)**: `t` is as printed and `l`/`i` are corrected, with each note opening with the print's reading:
  - 9.250 `pectora. ”Sic`, 9.280 `fides. ”Contra` and 9.292 `omnis. ”Percussa`: closing marks joined to the next word, as 9.117 and 9.221.
  - 9.289 `parentis / at tu` with no mark: corrected to a semicolon in the reading text. It could instead be a rule-5 source correction (`;` added to the source and aeneid-066 re-pinned); see the ruling above.
- **Kept as printed**: 9.283 `aut adversa` (Latin Library `haud`), a genuine reading, noted.
- **Scansion**: the build report should list only COSTLY 281 and 304, both hand-checked right.
  - 13 entries:
    - 9.228, 9.241 and 9.255 (*Ae-*)
    - 9.226 and 9.248 (*Teucri*)
    - 9.232, 9.293 and 9.310 (*Ĭūlus*)
    - 9.249 (*tālīs*) and 9.290 (*sōlāre ĭnŏpem*)
    - 9.291 (hiatus *tuī | audentior*)
    - 9.295 (half-line) and 9.296 (carrier)
  - The only choice that could be argued is 9.291. The hiatus rests on there being no fit with elision, as at 1.16.
- **Unchecked attributions, all from memory**:
  - Iliad 10: Agamemnon awake while the Greeks sleep; Diomedes and Odysseus killing the sleeping Thracians; Dolon promised Achilles' horses; Meriones lending Odysseus a bow, a sword and a leather helmet; the heroes lent weapons
  - Iliad 9: Agamemnon's offer of tripods, talents of gold, seven women, and twenty Trojan women if Troy falls
  - Iliad 2: Arisbe as an ally of Troy
  - Catullus 64.142 *quae cuncta aerii discerpunt irrita venti*
  - *haud* as "a reading many editors prefer"
  - "most take *patriae* as 'toward a father'"
  - Lycaon of Cnossos "otherwise unknown"
  - *inque salutatam* "a much-quoted example" of tmesis
  - "nearly sixty" half-lines in the poem
- **Stale files**:
  - `make_units.py` still holds the drafter's strings, so re-running it would discard this review.
  - `drafts/aeneid-066/` has no `gloss.json` yet, and the build needs one.
