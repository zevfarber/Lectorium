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

## Pass 2

Reviewer pass 2, 2026-11-24 (a different reviewer from pass 1). I read conventions.md, runbook.md, ../run3/RUNBOOK.md §2,
packet.md (text and establishment log), units.json and gloss.json as left by pass 1, pass 1's review, novel-forms.json,
popol-vuh-001..004.json, popol-vuh-glossary.json, the 004 review and wordre.py. For meaning I used only Brasseur 1861 (OCR
lines 19840–20100, K'iche', French and notes) and the glossary; no modern translation was opened or recalled. I made every
edit by script; no `t` was changed and no unit was added, removed or moved.

Units: I went through all 44 again (grammar labels against forms, K'iche' → l word by word, l ↔ i, couplets, the house
table, uncertainty labels, every establishment-log item, the about). I re-ran the MS-form → mt comparison against 001–004
by script: the only difference is still `xac` → xaq 'leaf' against 004's xak 'blackened', two words, as pass 1 said. I
checked every cross-reference in the notes against 001–004 (Ta chuxoc, xchicacam, Hunahpu Vuch, chuꜭhaxic, vvlih, acanic,
xe chacanic, ꜭhaquix, que ꜩac vloc, ꜩam, copon, quiꜭohe, maha oc, chivih, nay pu ve, xnohix, bala, cuval/yamanic, vachinic,
ruma) and the Brasseur claims against the OCR. All held except the two below (units 3 and 42).

Gloss: I checked all 121 entries and all `__broaden__` values against the text and the final mt, by script and by reading.
Every key is a lowercased token of the text; every novel form in novel-forms.json has an entry; every head equals the mt of
its token (vcaam differs only in the capital of the sentence-initial Uk'aam); every `__broaden__` value begins with the
glossary entry verbatim. I also went through the 120-odd known forms against their glossary entries and broadened seven
that this part uses in a sense the glossary does not cover.

Afterwards the JSON parses, len(mt) == len(WORD_RE.findall(t)) for all 44 units, and the units' `t`, joined in order,
give back the packet's 18 paragraphs exactly.

Counts: **major 0 · minor 19 · style 12** (31 rows; units 4, gloss 27).

### Changes — units.json

| unit | field | sev. | what was wrong | what was done |
|---|---|---|---|---|
| 3 | l, i, n | minor | l "vcual → his-jewels(?), vyamanic → his-precious-stones(?)", i the same order. The senses were swapped against 004 (yamanic 'jewels', raxa cuval 'green stones'), 003 and the glossary (cuval 'green stone, precious stone', yamanic 'jewels'). | l "his-precious-stones(?), his-jewels(?)"; i "his precious stones, his jewels"; n now says which is which, as in the macaw's boast. |
| 42 | n | minor | "Brasseur akalab, his k = q". Brasseur prints acalab (OCR `Quehecu ri oh acalab`), so the note's argument from his k was false. | "Ximénez and Brasseur both write plain c; the toggle shows ak'alab', the modern word, with its ejective restored as certain". |
| 38 | n | minor | "ca- 'we' … + achbilah": ca- + achbilah would be caachbilah. Before a vowel the 1pl ergative is c- (q-; Brasseur k'achbilah, his apostrophe). | "c-, the form of ca- 'we' before a vowel, is the ergative subject …". |
| 40 | n | style | Same for cachbilan. | "c- 'we' (ca- before a vowel) + achbilan". |

### Changes — gloss.json

| key | field | sev. | what was wrong | what was done |
|---|---|---|---|---|
| caib | value | minor | "cab 'two' with -ib'" would give kab'ib'; and it was pinned to e caib ꜭaholab. | "numeral, ka'- with -ib' (the root of ukab' and ukab'al)". |
| vubah | value | minor | "w- before the vowel (written v)" named a prefix w- that is not there; the "as in chi ca vubah" pinned it. | "transitive verb from ub' + -aj, written with an initial v (w) before the vowel; the toggle respells the letters". |
| vcual | value | minor | "his precious stone … the cuval of the macaw's boast": pinned; now given with the glossary sense of cuval. | "his precious stones (inferred); u- + kuwal (cuval) 'green stone, precious stone', written without its v". |
| chuchaxic | value | minor | "ch'a(w) 'say' + -ik" left out chu- and the passive -x-. | "chu- + ch'a 'say' + -x- (passive) + -ik", as the glossary's chuꜭhaxic. |
| xi | value | minor | "they (did) me" is no gloss; the absolutive was unnamed. | "x- completive + i(n) 'me', the absolutive object, n not written (inferred); written apart before the ergative prefix and verb". |
| cachbilah | value | minor | "with the object marker kix": kix is k- + ix, an absolutive pronoun, not a marker; "qa- 'we'" before a vowel is q-. | "q- 'we' (qa- before a vowel, the ergative) + achb'ilaj; the object, kix 'you (pl.)', stands before it". |
| cachbilan | value | minor | qa- for q- as above. | "q- 'we' (qa- before a vowel) + achb'ilan". |
| acalab | value | minor | "plural of akal 'child' (modern ak'al) + -ab'": the root was given in a non-form. | "ak'al 'child' + plural -ab'". |
| __broaden__ coh | value | minor | New reading "(chi ca coh wi uyab' …; inferred, from the verb coh 'put'; the toggle shows koj)": circular, pinned, and about the toggle. | "koj — put, place; transitive verb (inferred)". Old entry kept whole in front. |
| __broaden__ vxe | new | minor | Glossary "its foot, its base"; here Vae vxe 'its root, its beginning' of an account. | Added "uxe' — its root, its beginning (of an account)". |
| __broaden__ vꜫih | new | minor | Glossary "its sun"; here 'his day' of a person (l his-day; Brasseur 'his glory'). | Added "uq'ij — his day (of a person; Brasseur 'his glory'); sense uncertain". |
| __broaden__ vvach | new | minor | Glossary "its face"; here vvach tapal 'the fruit of the nance' (note 21). | Added "uwach — its fruit (the face a tree shows); noun". |
| __broaden__ ꜩam | new | minor | Glossary "nose, beak tip (the macaw's beak)"; here ꜩam vteleb 'the tip of his shoulder'. | Added "tzam — tip, end". |
| __broaden__ chirech | new | minor | Glossary "about it, of it"; here xquibih chirech 'they spoke to him'. | Added "chirech — to him, to her (after a verb of saying)". |
| __broaden__ chivih | new | minor | Glossary "about yourselves" (004's taking thought); here 'behind you' in the plain sense (note 39). | Added "chiwij — behind you (pl.), in the plain sense". |
| __broaden__ hunahpu | new | minor | Glossary "name, also a day"; here also one of Zipacna's mountains. | Added "also the name of a mountain (Brasseur: the Volcán de Fuego)". |
| ꜭaze | value | style | "sense in context uncertain (Brasseur 'man not yet living')" pinned to the line. | Removed; the general entry kept. |
| vyamanic | value | style | "a word of the macaw's boast" pinned. | "his jewels (inferred); u- + yamanik 'jewels, precious things'". |
| cacabeh | value | style | Quoted the draft's line and division. | "(uncertain) meaning not known; perhaps 'glory in' (a guess, after Brasseur); letters respelled". |
| chaah | value | style | "in chire chaah" pinned. | "play (inferred, perhaps at ball); after Brasseur's note". |
| racuh | value | style | Glossed as a finite "scraped" and pinned to chu racuh vchi. | "scrape (inferred); with uchi' 'his mouth', 'cry out' (Brasseur)". |
| tacal | value | style | "alighted, struck, landed" listed the three lines. | "set, come to rest (inferred); said of alighting, striking, landing". |
| chiquih | value | style | "qa- 'our' (qu before a vowel)". | "q- 'our' (qa- before a vowel, written qu)". |
| mam | value | style | "as in ca mam 'our grandsons'" pinned. | "grandfather; also grandson (Brasseur …); noun". |
| ꜩiz | value | style | Long, about the draft's toggle decision. | Shortened: coati, in the name; plain tz ligature, the toggle follows the known word. |
| __broaden__ mama | value | style | "said of the old man Saqi Nimaq" pinned. | "mama — old man; noun". |
| __broaden__ atit | value | style | "said of the old woman Saqi Nima Tz'iis" pinned. | "atit — old woman; noun". |

### Refused / left

- **Tz'iis for `Ꜩiz` (unit 37, gloss ꜩiz).** Kept, with pass 1's reasons: the name is certain (001/003 Tz'iis from ꜯ), and 004's ꜫaa → kaa set the precedent of the known word over the letter. **For the owner:** the published glossary entry `zaqui` spells the name Saqi Nimaq Tz'yis, against Tz'iis everywhere in the mt (001, 003, 005) and in the ꜯyꜩ entry. Not touched here; it should be made Tz'iis at build or by the owner.
- **wub'aj (vubah, quivubah) and uub'axik.** Kept. Letter for letter (v → w before a vowel), as the rule for uncertain forms requires; the exact modern form of the verb is not certain, and nothing is restored.
- **Uk'aam (unit 30), xkamow, kama.** Kept as pass 1 left them: k'am restored only where the verb is certain (xquicam, xnucam, Vcaam); the two unclear forms respelled.
- **Unit 6, telen/cabichal joined in i.** Left, as pass 1: neither word is known.
- **Unit 12 "Look, all of you".** Left: from Brasseur's own note on the K'iche' ("vous autres regardez"), and said so.
- **Unit 2 xꜭha singular with a plural subject; unit 28 xmeho with no ergative prefix.** Left: the notes say exactly this.
- **about.** Checked: every event is in the units and in order. "to say that they are healers" is the old couple's own claim, as the text has it. No change.
- **Gloss entries not changed** (checked): every other entry's head, meaning and morphology match the unit notes; uncertain senses are marked "(inferred)" or "(uncertain)".
- ***For the establisher:*** the log lists `acalab` among words where "Brasseur has q, k or g"; Brasseur prints acalab with plain c.
