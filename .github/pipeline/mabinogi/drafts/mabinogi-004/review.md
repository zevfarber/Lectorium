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
