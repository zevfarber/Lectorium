# Review — popol-vuh-005

## Pass 1

Reviewer pass 1, 2026-11-24. I read conventions.md, runbook.md, ../run3/RUNBOOK.md §2, packet.md (the text and the
establishment log), popol-vuh-001/002/003/004.json, popol-vuh-glossary.json, the 004 review, wordre.py and the draft
units.json (44 units). For meaning I used only Brasseur 1861 (OCR lines 19740–20200, K'iche', French and notes). No
modern translation was opened or recalled. I looked at crops of i0023 to place the page break (0023 begins `quix. huzuc
xꜩac …`, so the small k above `ri` belongs to unit 30, as the note has it) and to look at `zaquinimaꜩiz` and `chirihtac`.
I made every edit by script. No `t` was changed, and no unit was added, removed or moved.

I compared every mt with 001–004 by script (MS form → modern form). Every form that also occurs in 001–004 has the same
modern spelling, with one exception: `xac` → xaq 'leaf' (unit 23) against 004's `xac` → xak 'blackened'. These are two
different words, and the note says so. I checked every cross-reference in the notes against the published parts. I checked
every item of the establishment log against the notes, and each one is mentioned in the note of its unit.

Afterwards the JSON parses, len(mt) == len(WORD_RE.findall(t)) holds for all 44 units, and the units' `t`, joined in order,
give back the packet's 18 paragraphs exactly, paragraph by paragraph.

Counts: **major 0 · minor 8 · style 5** (13 rows).

### Changes

| unit | field | sev. | what was wrong | what was done |
|---|---|---|---|---|
| 27 | mt, n | minor | `vꜭhapa` → uchapa. The image has gh (ꜭh), and the letter rule gives ch'. 004 respelled the same case letter for letter: ꜭhaquix → ch'akix, where Brasseur prints chakix. In 001–004 every ꜭh is ch'. Brasseur's plain ch is no evidence, because he also prints x-cha for xꜭha. | mt is now uch'apa. The note keeps the modern verb chap with plain ch as information, gives Brasseur's habit, and says that the toggle follows the manuscript's letter, as with ꜭhaquix. |
| 3 | mt, n | minor | `vcual` → ukual. The note identifies the word with the cuval of the macaw's boast (004 `cuval` → kuwal, 003 `ahcuval` → ajkuwal). The same word in the same sense had a different modern form. | mt is now ukuwal. The note says that vcual is cuval written without its v (Brasseur qual), and that the toggle shows the kuwal of the last part. |
| 17 | n | minor | "xnohix … inferred, as in the second part". xnohix is in the third part (003, `Ta xnohix qui butic`). 002 does not have it. | "as in the third part". |
| 21 | n | minor | chacan → chaq'an (ch- + aq'an 'climb', as 004's acanic). The note did not say that the same letters, in 003's `xe chacanic`, were taken as one word 'go on all fours' (mt chakanik). | Added a sentence that gives 003's reading and toggle, and says that Brasseur's division ch'akan and the setting decide here. The reading is inferred. |
| 8 | l | minor | "it-is-said their-name mountains". vbi is v- 'its' (3rd singular), so 'their' was not in the form. | "its-name". |
| 28 | i | minor | "it was twisted off at the tip of the shoulder". l and n have xmeho 'was bent (back)' (inferred), and nothing gives 'off'. The coming away is xꜩac, which is already in i ("it came away"). | "it was bent back at the tip of the shoulder." |
| 38 | n | minor | "quix 'you (pl.)' (c- + ix)" left c- unnamed, and did not say which person is the absolutive object and which is the ergative subject. That is the point of the drafter's flag. | "quix is c-, the ongoing prefix, + ix 'you (pl.)', the absolutive, here the object …; ca- 'we' is the ergative subject …". The reading 'let us go along with you' is kept (see below). |
| 42 | i | minor | "will see us as only children". Nothing in `ri oh acalab` gives 'only', and Brasseur has "comme des enfants". | "will see us as children;". |
| 22 | i | style | "had been spied out". l has "had-been-seen", from il 'see'. | "had been seen by". |
| 33 | i | style | "are all loose". 'all' renders nothing. Xa is 'only, just'. | "are loose". |
| 34 | i | style | quiꜩih 'truly' was not rendered (l "truly"; Brasseur "en vérité"). | "until they truly come to take it back, those demons". |
| 42 | n | style | "yauic 'giving' (ya 'give' + -uic)". There is no ending -uic. | "ya 'give' + -ic, the verbal noun, with u (w) between." |
| 43 | n | style | "bala, left unexplained in the earlier parts". It occurs only in the third part (003 unit 13). | "in the third part". |

### Refused / left

- **Quix cachbilah tah (unit 38): 'let us go along with you'.** Kept. As the form is written, ix is the absolutive (the ones accompanied) and ca- is the ergative 'we' (the ones who accompany). Brasseur's own note gives "que vous nous accompagnions", word for word "that you we accompany". Only his French translation turns it round ("Veuillez nous accompagner"). The next lines agree: `Xa coh tere chivih` 'we only follow behind you', and the old couple are to say `ri cachbilan` 'whom we accompany' of the boys. The note gives both readings.
- **Tz'iis for `Ꜩiz` (unit 37).** Kept, but **the owner should confirm this.** The letter rule gives Tziis/Tzis: the image has the plain tz ligature, and I saw no comma. But the name is certain: Zaqui Nimac + Ꜩiz is the creators' Zaqui Nimac Ꜯyꜩ of 001, which 001 and 003 print as Tz'iis from Ximénez's own ꜯ. 004 set the precedent of the same word over the letter (`ꜫaa` → kaa, as 003's caa). The note says which letter the manuscript has and why the toggle shows Tz'iis. If the owner prefers the letter here, change only mt[6] of unit 37 to Tziis and the note's last clause.
- **k'isoq for `quizoc` (unit 3).** Kept. The verb k'is 'end' is certain. 001 already prints `vquizizil` → uk'isisil and `chiꜭiz` → chik'is. Brasseur has qiz-oc (his q = ꜭ), and the -oc ending is -oq as in chuxoq.
- **Uk'aam for `Vcaam` (unit 30).** Kept. The root is k'am 'take, carry', the verb of xquicam and xnucam in the same part (Brasseur qam, that is ꜭ, both times), and the glossary has cam → k'am. The doubled vowel is kept as written, because the exact form is inferred, as with 004's uncertain double-vowel words (cheel, iwuchaaj).
- **Hunhunahpu ×6, printed as written.** Kept. It occurs in units 25, 27, 28, 29, 30 and 35, and the note to unit 25 counts it right ("five times more"). Hunahpu occurs in units 0, 22 and 34. l and i keep the name as written. *For the establisher:* the log says "Hunhunahpu (0022–0023, ×5)". The text has six.
- **Embedded speech in ¶18 (units 40–41).** It is shown in i with inner single quotation marks, from ‘These are our grandsons … to ‘… out of teeth,’ you will say’. The note to unit 40 says where the words begin and that quix ꜭha closes them. This is right, and no change was needed.
- **Unit 6: the couplet qui telen, qui cabichal is given as one phrase in i ("carried on the shoulder").** Left. The conventions keep couplets as couplets, but neither word is known, and the note says that i follows Brasseur and joins the pair. Two English halves would be invention. If the owner wants the doubling seen, one option is "each of them with a blowgun, on the shoulder(?), at the side(?)".
- **Unit 37 i keeps the names untranslated (Zaqui Nimac, Zaqui Nima Tziz).** 001 translated the creator's name ("Great White Coati"), and 003 gave "Nimac, Great Coati". Here they are two persons' names, so keeping them in K'iche' follows the names rule, and the note gives the meaning and the link to 001. Left. A row for the house table may be wanted: Zaqui Nimac / Zaqui Nima Ꜩiz, l White Great(-ones) / White Great Coati, i the names kept.
- **xilom 'had been seen' (unit 22).** Left. -om is the participle ending of the preamble's ꜯibam 'written' and 003's aham 'carved', which are passive in sense, and the note says that the form is inferred.
- **quiyou, chin vlih (unit 14).** Left. Both are absolutive in (I) before a verb with an object (cah, ronohel vleu), which is odd for a transitive verb. The note marks both form and sense as inferred.
- **Unit 2's i "people will not live here".** Left. Brasseur reads 'not yet living', and the note gives both and calls the sense uncertain.
- **Unit 12's i "Look, all of you".** Left. 'Look' is from Brasseur's note ("vous autres regardez"), and the note to unit 12 says so.
- **about.** Checked against the text, and no change was needed. Every event it names is in the units, in order, and it adds nothing.
- ***For the establisher (not acted on, `t` pinned):*** at 2.5× the image of `chirihtac` (i0023) shows, after `chirih`, a tall looped stroke that may be the ß-ligature (ti) or an i + t, which would agree with Brasseur's `rihitak`. The log reads it chirihtac. The note's account (chi + rihtac 'old', inferred) does not depend on the difference.
- **Glosser (pass 2).** New keys must match the mt as now set: vcual → ukuwal, vꜭhapa → uch'apa. Known forms used in a new sense that may need `__broaden__`: `chacan` (if a chacanic-type key exists: here ch- + aq'an 'climb'), `xac` (xaq 'leaf', against 004's xak 'blackened'), `cam` (Vcaam), `bala` (here 'very well' with vꜩ, after Brasseur). The glossary's `zaqui` entry spells the name Tz'yis, against the ꜯyꜩ entry's Tz'iis. That should be made consistent at build.
