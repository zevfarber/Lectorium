# mabinogi-005 — review

## Pass 1

Reviewer pass 1 (2026-11-12). I read all 134 units and the "about" summary against conventions.md, packet.md (the established text and the establishment log) and the published mabinogi-001 to 004. I used mabinogi-004/review.md as the model for this report. Aids were Strachan, Morris-Jones, Silvan Evans and GPC, from knowledge. I read the third witness, Rhŷs & Evans 1905 (Red Book text, `source/raw/rhys-evans1905_djvu.txt`, printed pp. 26–33), for the whole passage. I also checked one spot on its page image (p. 31, PDF p. 45): the extra word in unit 91. No English translation was consulted. Edits were made by a Python script (load, modify, dump with ensure_ascii=False, indent=1). No `t` was touched.

**Unit numbers below are 0-based.**

Counts: **2 major, 17 minor, 11 style** (30 rows).

### Changes

| unit | field | severity | what was wrong | what was done |
|---|---|---|---|---|
| 68 | l, i, n | major | This unit falls across the drafters' seam. It contradicted unit 31 on a disputed word. Unit 31 renders *tryded prif rieni* as "one of the Three Chief Ancestresses" and says the sense of *rieni* is uncertain. Unit 68 rendered it "third chief maiden" / "one of the three chief maidens" and stated as fact that "*rieni* is a form of *rhiain* 'maiden'". | l and i now match unit 31 ("the-third chief ancestress"; "one of the Three Chief Ancestresses"). The note points back to the council and repeats that the sense is uncertain. In the same l and i, "the King of the Island" was lowercased to "king", as in unit 35. |
| 85 | n | major | *a wnelynt* was called the present subjunctive. *gwnelynt* (3 pl. -ynt) is the imperfect subjunctive. The present subjunctive is *gwnelont*. | "the imperfect subjunctive (third person plural) of gwneuthur, the mood of a supposed case". |
| about | about | minor | It was the two drafters' texts joined together. Matholwch left for his ships twice ("makes for his ships" … "Matholwch leaves the court in anger"). The rod was "as tall as himself", but the text says *kyuref a chyhyt* 'as thick and as long'. The end, "to come over to Britain and settle", left out what Bendigeidfran answers (Llasar gave him the cauldron; he spread them through his realm). It also left out the payment in colts and Tal Ebolion. | Rewritten as one summary of four sentences, checked against the text. |
| 3 | i | minor | "sons of Euroswydd, by his own mother Penardim" reads as Euroswydd's own mother. *o'e uam ynteu* means Bendigeidfran's mother. | "sons of Euroswydd by Bendigeidfran's own mother, Penardim". |
| 24 | l, n | minor | *ual y bydynt* was given in l as "they-may-be" and was not labelled. *bydynt* is the habitual imperfect, as *ban uydynt* is in unit 4. | l "they-would-be". The note labels the form and points back to unit 4's form. |
| 28 | n | minor | *uuwyt* was "softened after the adjective that stands first". The cause is the unwritten relative *a* of the abnormal sentence. The same note gives that cause for *uu* a clause later. | Cause corrected. |
| 35 | i | minor | "This is how they sat:" puts *Sef* back in the English. The house drops *Sef*, and 003 and 004 render the identical *Sef ual yd eistedyssont* without it ("They sat with …"). | "The king of the Island of the Mighty sat with Manawydan … on one side of him and Matholwch on the other …". |
| 53 | i | minor | "This is how it came:" (*Sef ual y doeth*) has the same fault. | "He was told that his horses had been maimed and spoiled …". |
| 85 | i | minor | "What they concluded was this:" has the same fault (the house lists "This is what …" as avoided). | "The counsel they reached was that if they refused it …", following 004's *Sef penyt …* → "The penance laid on her was …". |
| 59 | n | minor | This unit is the first after the seam. The note explained the abnormal sentence again in full (it is flagged in unit 0), and it repeated the spelling notes (u = v, -t = -d). | Cut back to a nudge ("the abnormal sentence again, as at the opening of the branch"). The spelling line was dropped. |
| 76 | n | minor | *genhadeu* was "softened as the object of the verbal noun". An object directly after a verbal noun is not softened. The softening comes from the adverb *etwa* standing between them. | Cause corrected. The note adds that the Red Book also has *gennadeu*. |
| 78 | n | minor | *am pob un* was not noted. After *am* one expects *bob*, and the Red Book has *am bop*. | Added. |
| 79 | l | minor | "against my will I-for-my-part was-done that" is garbled. *o'm anuod inheu* is 'of my un-will, mine', and *y gwnaethpwyt* 'that was done'. | "against my-will my-own that was-done that". |
| 91 | n | minor | The note said "The Red Book has a few more words in the middle that are not clear in its print." On the page (Rhŷs & Evans p. 31) it is one word, printed clearly as *amy6arth* and underlined, standing before *a gaei*. It is its sense that is unclear. | "Before a gaei the Red Book has a further word, printed amywarth (underlined by its editors), whose sense is not clear." The log item *yn ymdidan* (manuscripts' reading; *yr* is the editors' mending) was already stated plainly and is kept. |
| 92 | n | minor | *uychanet* was called "an abstract noun formed from bychan with the ending -et". *-et* is the equative ending. This is the equative used as a noun of degree, as 004 has it for *tywyllet*, *truanet* and *gamhet*. | Corrected. The note says the form is written softened and does not invent a cause. |
| 94 | n | minor | The note repeated the "abstract 'smallness'" label for *bychanet*. | It now says "the equative of bychan used as a noun". |
| 96 | n | minor | *delediwaf* was said to come from an adjective "deledyw", taking *d* as the radical. The verb stands after the particle *a*, which softens it. The base is most likely *telediw* 'fair, comely, complete' (GPC). | It now says "most likely ← telediwaf, softened after a (t > d)", with the meaning, and that the Red Book has the same form. The doubt about the exact sense stays. |
| 111 | n | minor | "The nested speech of the story begins here" was wrong. The nested speech (single quotes) begins at unit 115. What begins here is Matholwch's story. | "Matholwch's story begins here and runs on to the end of his long speech; the giant's words inside it are marked with single quotes." |
| 126 | n | minor | *a gwr a pob dwy uegin*: the unspirated *pob* after *a* 'with' was not noted. | Noted (one expects *phob*). |
| 4 | n | style | The cause of the softening of *uydynt* was not given. | "softened after ban (= pan 'when')". |
| 19 | i | style | *a uynnhei ef* is imperfect, and the note calls it "the courteous 'would'". The i had "does he want?". | "would he want?". |
| 55 | n | style | The softening of *gyn* (← *kyn*) was not mentioned. | "gyn ← kyn 'as, so', softened like gystal". |
| 61 | n | style | "it is dropped in i" is a remark about the translation, not about the Welsh. | Removed. |
| 64, 78, 91, 92, 94, 105, 123 | n | style | Across the seam, drafter A wrote the verb as *kaffael* (units 21, 30, 50), as 004 does. Drafter B wrote "cael". | "of kaffael" throughout. |
| 65 | l | style | "And no-one did-not-bring" changed the Welsh order (*ny duc neb*) and garbled it. | "And not brought anyone a-journey worse …". The double negative in unit 129 (*neb ny dieghis*) stays, because its order is the Welsh order and the note explains it. |
| 70 | i | style | *o'e kynghor* was "its council" in i but "his council" in l. *'e* is 'his'. | "of his council". |
| 72 | n | style | The unsoftened *tebygaf* had no witness. | Added that the Red Book also has *mi atebygaf*. |
| 101 | l, i, n | style | The name was left in manuscript spelling, *Tal Ebolyon*. Names in English take modern forms (004 gives *Twryf Uliant* as Twrf Liant). | l and i "Tal Ebolion". The note gives both spellings. The pun on *ebolyon* 'colts' and the doubt about the name's real origin are kept. |
| 113 | n | style | "the Red Book prints the word differently" did not say how. | "the Red Book prints auorles". |
| 116 | l | style | *Llyna* was "That-is", which is the l for *sef*. The house l for *Llyna* is "There-is" (001 u31, 003 u21 and u71, 002 u64). | "‘There-is the journey". |

### Establishment-log items: all stated plainly
- *Penardim* (3): the name as both manuscripts write it; Williams's *Penarddun* is mentioned; the English keeps Penardim.
- *dangos ef* (56): the note gives the Red Book's *dangos mae ef* and says that nothing is supplied and the words are construed as printed.
- *gwnaetpwyt* (70): called a readable slip for *gwnaethpwyt*, with the Red Book's form with *h*.
- *Bronwen* (68): the spelling is kept, and the note says it occurs once and is Branwen elsewhere.
- *yn ymdidan* (91): the manuscripts' reading; *yr ymdidan* is the editors' mending. The construction is said to be hard.
- *hyny* (98): = *hynny*; Evans's suspension mark is dropped.
- *gossed* (111): a slip for *gorssed*; the Red Book has *gorssed*; kept as written.
- *a'r mi* (116): a slip for *a'r mis*; Evans prints *ar mi*, the Red Book *armis*.
- supplied *mis* (119): the note says it is supplied from the Red Book and why.
- The words not supplied in unit 79 ("[a'e uys bychan]") are mentioned.

### Red Book citations checked
I checked every Red Book reading cited in the notes against the Rhŷs & Evans text and found them right. They are in units 1, 11, 14, 31, 32, 33, 37, 44, 49, 50, 54, 55, 56, 70, 74, 85, 88, 108, 111, 116, 124 and 133. The one exception is unit 91, which is corrected above.

### House renderings, formulas, names
- Ie → Yes in every unit (25, 54, 72, 75, 76, 115).
- heb ef / heb ynteu / heb wynt → "said he" / "said he-for-his-part" / "said they" in l, and "he said" / "they said" in i.
- Arglwyd → Lord. Dioer → l "Assuredly", i "Indeed", as in 001 and 004. A wyr / A wr → "O men" / "O man" in l and "Men" / "Man" in i, as in 002.
- Duw a dalo yt → "may God repay you" (95).
- gwyrda → noblemen (2, 119). unben → chieftain (92). kyuoeth → realm (120, 133).
- Sef is dropped in i everywhere after the changes above.
- Ynys y Kedeirn → the Island of the Mighty throughout.
- A script found no manuscript name form left in any l or i except the deliberate Penardim.

I did not recognise any phrase in i as remembered from a published translation.

### Findings refused
- **31, keeping "Chief Ancestresses"**: an alternative reading, *rieni* for *rianed* 'maidens', was considered. The note already gives it and calls the sense uncertain. Choosing between the two is not the reviewer's job. What mattered was that units 31 and 68 agree (fixed).
- **37, *Uendigeituran* "softened after the verb"**: the softening of a subject directly after its verb is a real Middle Welsh pattern, and the note says only "sometimes". Kept.
- **65, *waeth* "softened after the noun it follows"**: *kyrch* is masculine, so this is not the regular adjective rule. But the note asserts no false rule, and I could not give a surer cause. Kept.
- **75, i "there is no good in his going away in enmity"**: the note says plainly that the sense of *ymwaret* here comes from the context. I had no firmer rendering to offer. Kept.
- **122, i "for nobody could fight them out"**: this is an interpretation, but it is the plain sense of *herwyd ymlad*, and the note gives the literal words. Kept.
- **42, i "sharing out lodging"**: "lodging" is not in the Welsh. The note explains that *rannyat* here is the allotting of quarters, and unit 43 bears this out. Kept.
- **129, l "And no-one did-not-escape"**: this is the Welsh order and doubled negative (*neb ny*), and the note explains it. Kept.
- **132, i "And how"**: the "And" is not in the Welsh, but it is harmless for a follow-up question. Kept.
- **10, *gyweirach* "written softened" with no cause**: the note is honest, and no single rule covers the case. Kept.

### Verification
After the edits, a script confirmed that units.json has 134 units and that every `t` equals the corresponding `t` in cut.json, character for character.

## Pass 2
