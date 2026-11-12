# mabinogi-004 — review

## Pass 1

Reviewer pass 1 (2026-11-12). I read all 161 units and the "about" summary against conventions.md, packet.md (the established text and the establishment log) and the published mabinogi-001.json, mabinogi-002.json and mabinogi-003.json. Aids were Strachan, Morris-Jones, Silvan Evans and GPC, from knowledge. I read the third witness, Rhŷs & Evans 1905 (Red Book text, `source/raw/rhys-evans1905_djvu.txt`, printed pp. 18–25), for the whole passage. Evans 1907 was checked on the page image at three points: col. 29 (*du hun*), col. 30 (*arýwnaethoed*) and col. 35 (*uu hun*). No English translation was consulted. Edits were made by a Python script (load, modify, dump with ensure_ascii=False, indent=1). No `t` was touched.

**Unit numbers below are 0-based** (the index into `sentences`), which is also how the drafter's request list counts.

Counts: **0 major, 19 minor, 5 style** (24 items).

### Changes

| unit | field | severity | what was wrong | what was done |
|---|---|---|---|---|
| about | about | minor | The summary said Teirnon "cuts off a great claw" and finds the child "in swaddling of brocade". In the text he strikes off the arm at the elbow (unit 60). The brocade is a mantle wrapped round the child (unit 66), and *yn y gorn* is uncertain. | It now says "strikes off at the elbow the arm of a great claw that reaches in through a window, and finds at his door a baby boy wrapped in a mantle of brocade". |
| 6 | n | minor | The note gave no witness for the hard *na bydy gyuoet ti a rei*. | It now says the Red Book has the same words. The reading and the i are kept (see verdicts). |
| 18 | l, i, n | minor | *Och* was "Alas!" in both l and i. In 003 (unit 14) the house rendering is l "Och!" and i "Oh!". "Alas" is also on the house's avoided list (for *Oy a Duw*). | l "Och!" and i "Oh!", and the note points back to the last part. |
| 25 | n | minor | The note misquoted the Red Book as *an taered ni an chwech*. The Red Book reads *an whech*. | Corrected to *an whech* (whech = chwech). |
| 26 | i | minor | The formula *Ac ar y kynghor hwnnw y trigwyt/y trigyssant* was "they agreed" here and "they settled" in unit 106. A repeated formula should get the same English. | "And on that counsel they settled." |
| 29 | l | minor | "that we-never-saw ever" doubled the negative: *na welsam eiroet* is 'that we did not see ever'. | "that we-did-not-see ever". |
| 34 | n | minor | *ym kyffes y Duw*: the note took *ym* as 'my' but gave no evidence for it. | It adds that the Red Book has *ym kyffes i y Duw*, and the affixed *i* confirms 'my'. |
| 34 | n | minor | *differaf* was given under *differaw*, but unit 88 gives the same verb as *differu*. | Both notes now say *differu* 'protect, defend, save'. |
| 35 | n | minor | "drwc ← drwg, softened as the object" treated the final -c as a mutation. The radical is *drwg*, and the soft form of d (dd) would not show in this spelling. | The note now says so. |
| 59 | n | minor | *ar prafter* (no softening) and *fenestyr* had no witness. | It adds that the Red Book has *ar praffter* (also unsoftened) and *ffenestyr*. |
| 65 | n | minor | The note on the log item *yn agoret* rested on the image alone. | It adds that the Red Book also has *yn agoret*, so the reading is supported. |
| 66 | n | minor | *yn y gorn* had no witness. | It adds that the Red Book appears to read the same. The note still calls the sense uncertain. |
| 78 | n | minor | *uy mot y ueichawc*: the note said *beichawc* is softened "as after the predicative yn" but did not say what *y* is. | It now says that *y* stands for the predicative *yn*, as in the Red Book's *yn ueichawc*, and that *beichawc* is softened after it. |
| 87 | n | minor | *o'e dwyn*: the note said "the part played by o here is not clear". In fact *o'e* is the regular Middle Welsh spelling of *y'w* (modern *i'w*), 'to his/their'. | Explained, with the Red Book's *oe dwyn*. l and i already had the right sense. |
| 104 | n | minor | *a gaffwn*: "ni settles it" did not say that *ni* appears only in the Red Book. | It now says the Red Book's added *ni* settles the reading as plural, and that the White Book is read the same way. |
| 124 | n | minor | The log slip *a wnaethon* was noted plainly, but no witness was given. | It adds that the Red Book has *a wnaethant*. |
| 126 | n | minor | *wely dy* was called "the imperative of gwelet". The imperative is *gwel*. *wely* is the second-person singular present *gwely*, softened, from *(a) wely di* 'do you see?', with the question particle absorbed. This is the source of later *weldi*. | Note corrected. The Red Book's *weldy* is kept as the cross-reference. |
| 126 | l | minor | The l "see-you" followed the wrong analysis. | "And you-see you there your son". The i is unchanged. |
| 144 | n | minor | *tra parhawyf* (no softening after *tra*) had no witness. | It adds that the Red Book writes *trabarhawyf*. |
| 26 | n | style | The base was *trigaw* here but *trigyaw* in units 106 and 139. | Made *trigyaw* to match. |
| 53 | l | style | "there-would-not-know anyone" was garbled. | "would-not-know anyone". |
| 88 | n | style | The gloss of *differu* was brought into line with unit 34. | "'protect, defend, save'". |
| 114 | i | style | The vocative *A wreicda* was "Good lady". The house avoids "lady" for *gwreic*, and unit 102 renders *gwreicda* as "noblewoman", as the l does. | "Noblewoman," |
| 159 | i | style | *o dyledogyon* was "of the noble lineages", but *dylyedogyon* are persons (men of birth), as the l has it. | "of the nobility of this island". |

### Drafter's requested checks: verdicts
- **4** *a'e harglwyd ac eu brawduaeth*: correct. *gwr kymeint a gerynt* is 'a man they loved so much', and the two phrases stand in apposition to it ('and their lord and their foster-brother'). The h after 'e 'their' is rightly explained. The Red Book has the same. Kept.
- **6** *na bydy gyuoet ti a rei*: the labels are right (*bydy* is 2 sg. future; *gyuoet* is softened as a complement). The compressed sense ('you will not live as long as some') is the natural one, and the note says it is compressed. Red Book support was added.
- **15** *hwech wraged*: right. *hw* for *chw* is the same spelling as *ymhwelut* (unit 65). The softening is stated as found, with no invented cause. Kept.
- **19** *bychan a dial oed*: the note is honest that the *a* is unclear, and the Red Book has it too. Kept.
- **25** *ni byd yn taered ni an chwech*: the construction is uncertain and the note says so. The i ("her word alone will count for nothing against the six of us all insisting") interprets more than the l does, but it gives the plain sense of the plot. I found no better construction to put in its place, so I kept it and corrected only the Red Book quotation.
- **31** *du hun*: **checked on the image (col. 29, PDF p. 47). Evans prints *du hun*.** It is a genuine White Book reading, not in the log, and it is properly noted as a slip for *dy hun* (the Red Book has *dy hun*).
- **34** *ym kyffes y Duw*: correct. The Red Book's *ym kyffes i y Duw* confirms it (added).
- **40** *ac ar y wnaethoed*: the note (read *a ry wnaethoed*: relative *a* plus perfective *ry*) is the right analysis. **On the image (col. 30, PDF p. 47) Evans prints *arýwnaethoed* run together, so the division *ar y* in the established `t` is ours, and it contradicts the note.** By that analysis `t` should read *ac a ry wnaethoed*. The text is not changed here (see owner question). The note stands.
- **51** *Twryf Uliant*: right. The name is modern (Twrf Liant) in l and i.
- **53/58** *moei/moi*: right (the imperfect of repeated action, and the verbal noun).
- **56** *dileith*: right; the note calls it rare.
- **59** *fenestyr, prafter*: right. Red Book support was added.
- **66** *yn y gorn*: uncertain and flagged; l "swaddling(?)". Kept, with Red Book support added.
- **78** *uy mot y ueichawc*: right. The note now explains *y* = *yn*.
- **52** *yn y ty*: right. The article reading with "his" in i is reasonable for Teirnon's own house. Kept.
- **87** *ymoprau; o'e dwyn*: *ymoprau* is right as rare and uncertain. The *o'e* note was fixed (see table).
- **95** *a chwedyl wrthaw; bare Y rodet*: right. Both are noted with the Red Book. Kept.
- **97** *yn lut, douot*: right ('persistently', with an uncertainty flag; *douot* is 'a find, a foundling').
- **101** *goueileint, gamhet*: right (*gofeilint* 'anxiety'; *kamhet* the equative of *cam*, softened after *o*).
- **102**: right. The log's *ganthaw/udunt wy* number shift is stated, with the Red Book's *gantunt*.
- **104** *a gaffwn*: right as 1 pl. present. The wording on *ni* was fixed.
- **113** *uu hun*: **checked on the image (col. 35, PDF p. 50). Evans prints *uu hun*.** It is a genuine reading, properly noted (the Red Book has *vy hun*).
- **114** *uynet*: right (the verbal noun softened after its subject in the *y* + subject + verbal noun construction).
- **126** *wely dy*: corrected (see table).
- **136** (speaker): right. No *heb* tag; the "we" is Teirnon's household. Kept.
- **141** *o'r byd*: right (*o* + *ry*, 'if'). The Red Book has the same.
- **142** *dyn uwy y galar*: the label is right, and the note is honest that the cause of the softening is uncertain. The Red Book has *v6y*. Kept.
- **145** *Os ynteu a uyd*: right ('if he lives'). The note says the words leave it bare.
- **149** *ymyrrwys*: the sense is uncertain and the note says so. Kept.
- **155** *yn llwydannus garedic*; **157** *seith cantref* (the Red Book has *gantref*); **158** *wreika* (the subject softened when separated from its verb): all right. Kept.

### The log's slips: all mentioned
*vn* (18), *diffetheeist* (31, with the Red Book's identical form), *yn agoret* (65), *ganthaw/udunt wy* (102), *Pan doethant/Pann doethont* (110, 111), *a wnaethon* (124), *Toryfliant* (150), *nit adnappo uot* (129), *A thriphet* (104). Each is stated plainly as printed. Nothing is supplied from the Red Book, and no note claims a supplement.

### House renderings and names
- teulu: household-troop / warband (38).
- gwyrda: noblemen (39, 40, 146, 149).
- kyuoeth: realm (1, 144, 150, 153, 155).
- Ie: Yes (9, 19, 75).
- unbenn: chieftain (111).
- Duw a dalo yt: may God repay you (94, 140).
- Y rof i a Duw: between me and God (131, 144).

Sef is dropped in every i. A script found no manuscript name form (Riannon, Dyuet, Twryf/Toryf, Kicua, Keredigyawn, Ystrat, Seissyllwch, Annwn) left in any l or i. The *heb y* + name note matches 001–003. I did not recognise any phrase in i as remembered from a published translation.

### Findings refused
- **56, i "what plague it is"**: *dileith* is 'ruin, destruction'. "Plague" is on the avoided list only for *gormes*. Here it stands for an agent of destruction, which "ruin" would not give in idiomatic English. Kept.
- **25, i**: see the verdict above. The i is an interpretation of a construction that is admittedly uncertain, and there is no firmer one to replace it with.
- **19, l omits the *a* of *bychan a dial***: the note explains it. Putting it into the l would add nothing a reader could use.
- **40, changing the note to fit *ar y***: the note's analysis is the better one. The fault is the word division in `t`, which is for the owner to decide.
- **129, l without "[anyone]"**: the note states that the subject is understood. Supplying a word in the l would look like a textual supplement.
- **95, i "and to give word of it"**: it reads one possible sense of a phrase the note marks as uncertain. Kept.
- **160, i "Mabinogi" for *Mabynnogyon***: the note justifies it, and the l keeps the form.

### For the owner (QUESTIONS)
- **Unit 40, word division.** Evans prints *arýwnaethoed* (col. 30 l. 4) run together. The established text divides it *ar y wnaethoed*. The drafted note, which I accept, analyses it as *a ry wnaethoed* (relative *a* + perfective *ry*). The Red Book has *ac a wnathoed*. Should the established text be re-divided *ac a ry wnaethoed*? If so, `t` of unit 40 and the l and n would follow.

### Verification
After the edits, a script confirmed that units.json has 161 units and that every `t` equals the corresponding `t` in cut.json, character for character.

## Pass 2

Reviewer pass 2 (2026-11-12) covered the glossary draft `gloss.json` and gave units.json a second reading.
- **Glossary:** I checked all 401 new entries and all 38 broadenings against the text and against the unit notes as they stand after pass 1, on each of these points:
  - the lemma, its modern form, and "(no modern form)" where there is none;
  - meaning, part of speech and gender;
  - tense, mood and person;
  - the mutation and its cause.
- **Broadenings:** for each of the 38 broadenings a script confirmed that the old entry from known-forms.json is kept unchanged, character for character, before the " · ".
- **Aids:** the same as in pass 1, together with the Red Book text.
- **How the edits were made:** by Python script (`ensure_ascii=False, indent=1`). Every changed glossary entry was rewritten whole.
- **Checks after the edits:**
  - the 401 keys still equal novel-forms.json, and `__broaden__` still has 38 entries;
  - no bracketed editorial remark ("[… uncertain]" etc.) is left anywhere;
  - units.json still has 161 units, and every `t` equals cut.json.

In the table below, "maj" marks an entry that taught something false about the form itself (lemma, meaning, person, part of speech). Wrong mutation causes, examples and gender are minor. Example glosses and name spellings alone are style. Unit numbers are 0-based.

Counts: **16 major, 65 minor, 9 style** (90 table rows covering 109 glossary entries; the one units.json change, the unit 95 note, is counted with its glossary row *synyeit*).

### Changes — glossary (new entries)

| key | sev. | what was wrong | what was done |
|---|---|---|---|
| edewis | maj | It was given as an invented verb *edewi* 'omit'. It is the 3 sg. preterite of *adaw* 'leave' (as unit 2's note has it). | adaw (gadael) 'leave, let go', a>e by affection. |
| brawduaeth | maj | Glossed as *brawdwriaeth* 'judgement, judge'. Unit 4 has 'foster-brother', and the Red Book's *brawtuaeth* confirms it. | brawduaeth (brawdfaeth) 'foster-brother', brawt + maeth. |
| golles | maj | Glossed as "1 sg. preterite 'I have lost'". It is the 3 sg. preterite, used without an object ('has been lost'), as unit 18 has it. | Corrected, with the mutation after *neur* (neu + ry). |
| diuetha, diffetheeist | maj | The modern form was given as *diffeithio*, which is a different verb ('lay waste'). | diuetha / diffethaw (difetha). The *-eeist* spelling is noted as kept as written. |
| thygyawd | maj | The lemma was *tygu*, which means 'swear'. | tygyaw (tycio) 'avail'. |
| kynnadeu (+ wneuthur) | maj | It was read as *kynnadl* 'conference' ("to hold assemblies"). It is the plural of *kennat* 'messenger' (unit 40; the Red Book has *kennadeu*). The drafter had flagged the gender. | kennat (cennad), noun f. (also m.), plural kynnadeu: 'to send envoys to Pwyll'. The example under *wneuthur* was corrected to match. |
| heppil | maj | It said "no modern form" (the modern form is *epil*), "no mutation" (the h- comes from *yn* = *ein* 'our'), and gave the example as "leaving a brood in a mare". | eppil (epil); h- after ein 'our'; 'losing the offspring of our mare'. |
| moi | maj | Called "3 sg. preterite … the short stem". It is the verbal noun carrying the narrative (unit 58). | Verbal noun, with its subject after it. |
| tywyllet | maj | Given as a noun 'darkness' with an invented modern form. It is the equative of *tywyll*, used as a noun of degree (unit 63). | tywyll; equative tywyllet. |
| truanet | maj | Given as the noun *truanedd*. It is the exclamatory equative of *truan* (unit 97). | Corrected. |
| gamhet | maj | Given as a noun *camhet* (cf. *camwedd*). It is the equative of *cam* (unit 101). | Corrected. |
| dwf | maj | The lemma was given as *dwf*. It is *twf*, softened after *y* 'his' (unit 85). | twf (twf), t>d after y. |
| douot | maj | The meaning was given as 'doubt, misgiving'. It is 'a find, the foundling' (GPC *dofod*; unit 97). | douot (dofod). |
| lut | maj | The meaning was given as 'secrecy'. The note reads it as *glut* 'tenacious', softened after adverbial *yn*: 'persistently'. | glut (glud), rare, meaning uncertain. |
| elwissen | maj | Given as 'profit, gain' (cf. *elw*). It is *elusen* 'alms' (unit 104). | elwissen (elusen) 'alms, a charitable deed'. |
| druein | maj | Treated as a singular ('O wretched one'). *truein* is the plural, and the address is to the women. | Plural 'wretches'. |
| dryded | min | The mutation was said to come "after predicative yn". *yn* 'in' does not soften. The softening is that of the unwritten article (the Red Book has *yny dryded*). | Cause corrected. |
| trymuryt | min | Given "no modern form". | (trymfryd); b softened inside the compound noted. |
| dietiued | min | Given "no modern form". | (dietifedd); the softening of d after yn is not shown. |
| perhey | min | Had a "[form uncertain]" bracket, but the form is regular. | Bracket removed, and the Red Book's identical form noted. |
| kerych | min | The conjunction was written "after chyt". | "after kyt 'though'". |
| damwein | min | Given as "noun f.", but the example *y damwein hwnnw* is masculine. | "here masculine (now f.)". |
| deffroyssant | min | It said "no mutation after phan". *pan* softens; dd is not shown in the spelling. | Corrected. |
| lloski, dienydyaw | min | Said "ll- not mutated after yn" and glossed "in putting to death". *yn* here is *ein* 'our' (units 19, 25). | Corrected in both. |
| gellast | min | Gave "(cf. gast)" as the modern form. | (gellast). |
| lladwn, irwn, byrwn, thaerwn | min | Called "present subjunctive, hortative", while unit 24 calls them imperatives. The lemma of *irwn* was the modern form only. | "1 pl. imperative (-wn)", and iraw (iro). |
| trigwyt, trigyssant | min | The lemma *trigo* did not match the notes' *trigyaw*. | trigyaw (trigo). |
| du | min | Did not say that *du* is a slip. | It now says it is a slip for *dy*, that Evans prints *du* (checked on the image in pass 1), and that the Red Book has *dy*. |
| hawl | min | The lemma *hawlu* did not match the note's *hawlyaw*. | hawlyaw (hawlio). |
| kyffes (+ broadening ym) | min | Both read *ym* as "in my", against unit 34. | Both now say 'by my confession to God', with *ym* = 'my', and give the Red Book's *ym kyffes i y Duw*. |
| wirioned | min | Given as "noun m., soft after the possessive y 'its'". The softening shows the noun is feminine here, after the article (unit 36). | Corrected. |
| kigleu, gigleu, glywssont | min | The lemma was *clybot*, but the notes use *klywet*. | klywet (clywed). |
| wnaethoed | min | Had a "[cause uncertain]" bracket. | The softening is now said to be after perfective *ry* (*ar y* read as *a ry*), as in unit 40. The Red Book's *ac a wnathoed* is given. The division is the open owner question from pass 1. |
| yskynuaen | min | The example was garbled, and the m in the compound was not noted. | Corrected; modern form (esgynfaen). |
| odieithyr | min | The modern form was misspelt *odieithr*. | (oddieithr). |
| gyffranc | min | Given as "noun m.", softened after "the possessive/article". | Noun f. here, softened after the article. |
| uliant | min | Gave *liant* 'flood', had a bracket, and did not match the unit 51 note's *lliant*. | It now reads *lliant* 'flood, sea', says the u- is unexplained, and gives "meaning uncertain". |
| wybydaf (+ broadening ony) | min | Glossed 'until I learn'. *ony* is 'unless' (the oath in unit 56). | 'if I do not find out'. |
| dileith | min | Said "no modern form" (the note has *dilaith*) and had a bracket. | (dilaith); "a rare word, exact sense uncertain". |
| telediw, delediwhaf | min | The lemma was the invented spelling *teledyw*. | telediw (no modern form). |
| prafter | min | Said "no mutation", while the note says the softening after *ar* is not written. | Corrected, with the Red Book's *ar praffter*. |
| fenestyr | min | The lemma was written *fenestyr*. | ffenestyr (ffenestr), f for ff, with the Red Book's *ffenestyr*. |
| diskyr | min | Said "no modern form" and had a bracket. | (disgyr) 'scream, shriek'. |
| adaw | min | Said "g- lost by soft mutation", but nothing mutates here: *adaw* is a form of the verb without g-. | Corrected. |
| dynnyon | min | Said "no mutation after the article y". *y* here is 'to' (unit 77), and its dd is not shown. | Corrected. |
| duunaf | min | Had a "[meaning uncertain]" bracket. dy- + un 'agree' is clear. | Bracket removed. |
| kyuelynet | min | Said "the m- lost". The m is softened (written u). | Corrected. |
| ymoprau | min | The meaning 'busy oneself, keep company' did not match the note's 'bargain, strive, coax' (from *gobr*), and it had a bracket. | Matched to the note, with "meaning uncertain". |
| adu | min | The example said "let him be taken to the water". *o'e dwyn* is 'to take them' (unit 87, as corrected in pass 1). | Corrected. |
| synnyaw | min | The modern form was given as *synnu* ('be surprised'). | (synio), as in the note. |
| ponyt | min | Said "no modern form". | (ponid). |
| hywedu, hywed | min | Said "no modern form". | (hyweddu), (hywedd). |
| adaf | min | Read as *gadu* softened after a. Unit 93 takes it as *adaw*, with no mutation. | Matched to the note. |
| guastrodyon | min | The plural *gwastrodion* was given as the modern form of the singular. | (gwastrawd). |
| synyeit (+ unit 95 n) | min | The gloss said "impersonal imperfect subjunctive [form uncertain]", while the note said "verbal-noun form". | Both now give both analyses and call the form uncertain. The Red Book's *synnyeit* is added. |
| goueileint | min | The modern form *gofalaint* is not in use. | "(no modern form; cf. gofal)". |
| yscaualwch | min | The modern form *ysgafalwch* is doubtful, and it had a bracket. | "(no modern form)"; 'leisure, an opportunity'. |
| wreicda | min | 'good woman, noble lady', with the modern form *gwraig dda*. | (gwreigdda) 'noblewoman', the house rendering. |
| thriphet | min | Given as a single noun *triphet* (no modern form). It is *tri pheth* written as one word (unit 104). | Corrected, with both spirant mutations and the slip noted. |
| gaffwn | min | Given as a present subjunctive 'we may get'. Unit 104 has a present with future sense. | Matched to the note. |
| eturyt | min | Said "no modern form; cf. adfer". | (edfryd). |
| pann | min | Said "no mutation before d-". | "causes soft mutation, not shown on d-". |
| uym, pryder | min | Said "causes nasal mutation (p>mh)" and "nasal-mutated" without saying it is not written on the noun. | Both now say the nasal is written only on the possessive. |
| thebygaf | min | The lemma *tybyaw (tybied)* does not fit *thebygaf*. | tybygu, tebygu (tybio). |
| oedit | min | The example "the feast that was being held" misanalysed it (unit 119). | Corrected. |
| hardelw | min | Gave 'care, rearing', "no modern form", and a bracket. | ardelw (arddelw) 'claim, avowal, protection', as in unit 125. |
| dalu | min | Said "after the particle y". | "after the preposition y 'to'". |
| parhawyf | min | Said "no mutation". | The softening after *tra* is not written; the Red Book has *trabarhawyf*. |
| meu | min | Said "no modern form". | (meu). |
| ymyrrwys | min | The modern form *ymyrru* was invented, the meaning was 'go, proceed', and it had a bracket. | (ymyrryd); 'go in with, join'; "sense here uncertain". |
| toryfliant | min | Had no modern form and no note that it is kept as printed. | (Twrf Liant); Evans's *tozyfliant*, kept as printed. |
| amgeledus | min | Gave "cf. amgeledd". | "cf. ymgeledd". |
| chwpplaf | min | The lemma *cwpl* was invented. | kwbyl (cwbl). |
| garedic | min | Had a "[cause uncertain]" bracket. | The cause is now stated as in unit 155. |
| ystrat | min | Given as noun f. | Noun m. |
| wreika | min | The cause was given as "after the noun uryt", with a bracket. | Now: the subject of *doeth*, separated from its verb (unit 158). |
| walltlydan | min | The modern form *gwalltlydan* was invented. | "(no modern form)". |
| dyledogyon | min | Said "no mutation". | The softening after *o* is not shown. |
| mabynnogyon | min | Was given as a regular plural of a lemma *mabynnogi*. | Matched to unit 160: occurs only here, commonly taken as a scribal form. |
| broadening gorn | min | The new reading was 'corner, angle', against the unit 66 note. | It now says: apparently a wrapping or swaddling, meaning uncertain, softened after *y* 'his'. |
| broadening wely, dy | min | *wely* was called an imperative "soft-mutated after ac". | It now says *(a) wely di* 'do you see?', with the question particle absorbed (unit 126 as corrected). |
| eisswys | style | The example gloss 'and by then' did not match the note. | 'and in that, nevertheless'. |
| pylgeint | style | The example 'and the dawn' misread *tu a'r*. | 'and towards the dawn-hour'. |
| amouyn | style | The example 'secretly'. | 'persistently'. |
| mynho | style | The example 'who may wish him'. | 'who may wish it'. |
| edrychwch | style | The example 'see that it does not suit best'. | 'consider whether … may not suit him best'. |
| kynydwys | style | The example 'there was added'. | 'he gained'. |
| ymhwelut | style | Did not say that hw is for chw. | Added, with the Red Book's *ymchoelut*. |
| broadening diolwch | style | The example 'thanks and gain'. | 'thanks and alms-merit'. |
| uynnawd, kicua, wynn, gohoyw, gloyw, cassnar | style | The modern names were misspelt *Cicua* and *Gwynn*, and gohoyw had a "[meaning approximate]" bracket. | Cigfa and Gwyn; bracket removed. |

### Changes — units.json (second reading)
| unit | field | severity | what was wrong | what was done |
|---|---|---|---|---|
| 95 | n | (counted with *synyeit* above) | The note stated *synyeit* as a verbal noun without doubt. | It now gives both analyses and calls the form uncertain, with the Red Book's *synnyeit ar y march*. |

I found nothing else on the second reading that pass 1 had missed. The pass-1 edits were re-read in place.

### Glosser's queries: verdicts
- **Unwritten soft mutation after *a* in d- forms** ("soft mutation after a not shown (d for dd)"): this is right throughout, and it was kept.
- **perhey**: the form is regular. **golles**: 3 sg., corrected. **kynnadeu**: f. (also m.), corrected. **wnaethoed**: *a ry*. **garedic**, **wreika**: causes stated.
- **brawduaeth, douot, lut, elwissen, hardelw, ymyrrwys, ymoprau, dileith, diskyr, yscaualwch, duunaf, uliant, gohoyw, synyeit**: each was decided as in the table above.
- **nogyt**: "(no modern form; cf. nag)" was kept as it stood.
- **Modern forms:**
  - Supplied: gellast (gellast), tywyllet (tywyll, as an equative), amgeledus ("no modern form; cf. ymgeledd"), hywedu (hyweddu), ponyt (ponid), heppil (epil).
  - Left as "(no modern form)": differu, moi, telediw.

### Findings refused
- **ymdaeru, ymdaraw, taered, euryn**: the modern forms (or the lack of one) given by the glosser were left alone. I could not confirm a better form from the aids, and the rule is not to invent one.
- **The different treatments of *tybygu* (unit 48) and *tebygu* (unit 114) in the notes**: both forms are attested. The gloss now names both, and the notes were not touched.
- **galar "no mutation after y 'her'" (unit 142)**: this agrees with the l ("greater her grief than she"). Kept.

### For the owner (QUESTIONS)
No new question. The unit 40 word division (pass 1) is still open. The glossary entries for *wnaethoed* and *ac* are written to the *a ry* reading, but they can stand with either division.
