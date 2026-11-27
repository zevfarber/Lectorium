# popol-vuh-018 — review

## Pass 1

I checked all 63 units against conventions.md (the toggle rules and the house renderings table), runbook.md, ../run3/RUNBOOK.md
section 2, QUESTIONS.md (with the 018 establish entry and its two README-5b corrections), the packet and establishment log, the
drafter's notes, the published parts 001–017 (009–011 for the lords, the roads and the houses; 016–017 for the latest practice),
the glossary, and 017's review. A script compared every token's mt with the mt of the same form in 001–017. Every new form's mt
was read against its manuscript word under the toggle rules. Every grammatical label in the notes was read against the form
(person markers, ergative/absolutive, completive/incompletive, active/passive, agent focus). `l` was read against the K'iche' word
by word, and `i` against `l`. Every claim the notes credit to Brasseur was checked in the OCR (lines 24997–25530: his K'iche' text,
his French and his footnotes), along with his 010 notes on Cala (22291) and zakitok (22445). Every doubtful reading in the
establishment log was traced to its unit's note. The speaker attributions in the roll-call (¶3) and the ball argument (¶8) were
checked tag by tag.

Edits were made by script (load, change named fields, dump with ensure_ascii=False, indent=1). After the edits, a script check
confirms:
- no `t` changed;
- the 63 units tile the 9 pinned paragraphs exactly;
- each paragraph starts a unit (U1, 5, 9, 25, 29, 34, 39, 49, 59);
- every mt has one entry per WORD_RE token.

Counts: 0 major, 11 minor, 5 style.

### Changes

- U2, U10, U14, U18, U44 · mt/l/n · minor · `chi` read in the notes or in `l` as chic 'again' kept mt chi. The published practice
  gives chik wherever chi stands for chic (31+ places; QUESTIONS 015 point 3). Examples are 004's and 009's Are chi cu(ri) and
  011/012's chi vi. U2's xe icou chi vi cut is also the parallel of 010's xe eco chi cut chupan, which has chik. · mt chik in
  U2 (icou chi vi), U10 (ma chi vi xꜭhavic), U14 (xꜭha chi roo), U18 (xꜭha chi Ahalpuh) and U44 (Are chi cu ri). `l` "(chi)"
  is now "again" in U2, U14 and U18. The notes say chi is chic without its c. U11's ca chi rox is left chi, because there the
  reading really is unclear.
- U2 · n · minor · Brasseur prints chuva cumuk, where the established text has chua. The note quoted his cumuk but not his chuva,
  and the establishment log is silent. · Added to the note. Flagged for the establisher (below).
- U16–U23 · l/n · minor · xti 'when the Nth was bitten' has no ergative written, and the note and `i` read it as passive in sense.
  But `l` had "when it-bit". · `l` now has "when was-bitten" in all eight units. The U16 note now says it is passive in sense, as
  xtiic is, with Brasseur's 'au moment où il était également piqué'.
- U16 · n · minor (speaker attribution) · The note said "The one who asks 'What has bitten you?' is each time the next to be
  bitten." That is Brasseur's attribution, and it contradicts the draft's own reading. In U15, Vucub Came's question closes with
  xꜭha chic, so the tag is the same asker going on. The tags of U16–U23 have the same shape. · The note now gives the reading
  the text supports: the same asker goes on. It gives Brasseur's (the next seated one, as he is bitten) as the alternative,
  quoting him.
- U16–U23 · i · style · "he said in turn" suggested a change of speaker, against the reading above. · "he went on".
- U33 · l/n · minor · `xquiz cut v vach` was labelled "they finished their faces", but no qui- 'they' is written. xquiz is
  x- + quiz, intransitive. ¶7 reads the same form that way (habi xquiz ri chah 'the torch was not used up'), and 010 writes
  xqui quiz for the transitive 'they used up'. · `l` "it-was-finished then its-face". The note explains the form and keeps
  Brasseur's sense as inferred. `i` ("They went through them all, face by face") still fits and is kept.
- U35 · l/n · minor · `xe rah oc` was glossed "they-wanted enter" in `l`, but `i` and the note have 'they were wanted to'. Neither
  said what xe and r- are. · `l` "them-it-wanted enter". The note now says that xe is the absolutive 'them' and r- the ergative
  'it, he' (the fixed xrah construction of 014/016/017, with the lords as the ones wanting).
- U54 · l/i/n · minor · `chi coh` was labelled "'shall be put', with no person written", a passive. A bare transitive root with
  no -x is not a passive. As elsewhere in this part (Chi quihila U30, Chi biyh tah U50), chi is ch- + i- 'you (pl.)'.
  Brasseur prints ch'y coh, 'n'employez pas celle-là'. · `l` "you-shall-put". `i` "Not that one shall you put in play, but this
  one of ours," said the boys. The note now says this.
- U26 · n · minor · `are chi biyh` was called "the optative, 'that he say'". No chu- 'he' is written. Brasseur's reading of
  `xucut` ('le dernier qui était assis dans le coin') was not given. · The note now reads it as 'to say', with no person written
  (inferred), and gives xucut as 'side, corner' with Brasseur's 'corner'.
- U47 · mt/n · minor · Achinac had mt Achinaq, with no tie to a known q word. Under 007's rule (QUESTIONS 007 point 1),
  Brasseur's k (= q) gives q only when the note ties the word to a known q word. · mt Achinak. The note gives Brasseur's achinak
  and the rule.
- U43 · n · minor · Brasseur prints Ma cu quitzih ri chah 'in truth' here, and supplies '(brûlèrent)' in his French. The
  manuscript has xqui ꜩih. The note did not mention the difference, and the establishment log lists xqui ꜩih only as a letter
  form. · Added to the note, with the established text followed. Flagged for the establisher.
- U7 · n · minor · Brasseur prints chi tzubah where the text has cha ꜩubah, and neither the note nor the log said so. · Added.
  Flagged for the establisher.
- U7 · n · style · "que 'them'" did not show the ongoing c- of que a tio. · "(c-, the ongoing mark, + e 'them')".
- U30 · n · minor · Brasseur takes ri cubulic as the one to be greeted ('Adorez le roi, leur dit-on, celui qui est là assis'),
  not as the speaker. The note gave his 'to tempt' but not this. · Added; either reading is possible from the words.
- U60 · n · style · "toc, which Brasseur takes as 'flint'": he does not say so here. He renders 010's zakitok as 'blanc silex'
  (OCR 22445), and here he prints zaki tog with his g. · The note now says exactly this, and says the toggle keeps 010's tok by
  the letters.
- U3 · n · style · mt yik'ow supplies the ejective on an inferred word. The note did not give its support, which is Brasseur's
  x-qui yiqou, with his q (= ꜭ) as in his iqou, and the published ik'ow. · Added.
- about · style · "the one beside him asks his name": in the text he calls him by name and asks what bit him. · Reworded.

### mt against the published parts

After the edits, these forms have an mt that differs from the published mt for the same letters. Each is a different word or a
different person:
- `caca` kaqa 'red' (001's caca k'a ka 'still'). This is 012's ruling for plain-c 'red' (kaq).
- `quetaam` qetaam 'we know' (014's ketaam 'they know').
- `chiquech` chiqech 'for us' (published chikech 'to them').
- `toc` tok in zaqui toc, as 010/012's Saqitok (published toq 'when').

The forms with several published mt were each checked against person and sense:
- ca, chique, que and cuꜭ go by person (narrative k-, the speakers' own 'we/us' q-, as 014–017);
- cah is qaj 'go down' (as 007/010/012/014) and xcah is xkaj 'want' (006/014);
- he is je 'go' and je' 'tail' (010/014/016/017);
- ha is ja 'house', while 010's hal ha gives halha jalja';
- cab 'second' is kab' (as 008/009's numeral), against q'ab' 'hand';
- oc 'enter' is ok, while hun oc is oq;
- vvb alone is uub'.

All other known forms match the published mt.

### Rulings on the drafter's open points

1. ꜩubah tz'ub'aj and ꜩonox tz'onox: accepted. This is the practice of 015–017 (tz'iloj, tz'onoj, tz'apij, etz'), which is still
   open as a whole.
2. caca kaqa: accepted, under 012's ruling (plain-c 'red' is kaq). 010's ꜫaꜫa be stays q'aq'a with 010 point 2 / 012 point 1.
3. xi tiouic: the note's 'you' (perhaps ix, respectful) is accepted as inferred. Brasseur writes mi-x-y tiouic throughout.
4. U57's untagged line and Ꜭha chic: kept unassigned and marked (see Refused).
5. The glosser broadenings the drafter lists are needed. To them add **chi** (chik 'again' in U2/U10/U14/U18/U44, already in
   the published entry), **achinac** with mt achinak, **xquiz** (intransitive 'it was finished', U33/U46) and **coh** (U54
   'you (pl.) put', through ch- + i-). Pass 2 will check them.

### Refused

- U24 (roll-call end): Quicrixcac as the speaker of "Naquila mi xi tiouic?" and Quicre as speaking to him. By the count,
  Quicrixcac is more likely the one addressed (Brasseur's reading). But in every tag of this roll-call, xꜭha chic X has X as the
  speaker (U21 ꜭha chic Chamiaholom), and the text is rendered as written, with the note giving Brasseur. Kept.
- U53, U56 (ball argument): the manuscript's tags are followed, against Brasseur, who gives "Re ba chi ca coh…" and "He bala
  xa hu chil" to the boys. Brasseur's own K'iche' text shows why: he puts each tag before the speech that follows it (x-e cha
  Xibalba : Ma ta hare-ta…). Ximénez's tags follow their speeches throughout the part, and the draft's sequence makes sense on
  its own: the lords insist on their ball, the boys give way with Vꜩ bala, and the lords' ball is thrown. Defensible. Kept.
- U57: the untagged "Ma bala, xa holom coh." is left unassigned. Since tags follow speeches, it could also belong with the boys'
  "Ꜭha chic" under the one tag xeꜭha ꜭaholab. Brasseur gives it to Xibalba. The note already says it may be either side's.
  Kept.
- U13: v cab culel 'second' where the count needs the fourth is printed and rendered "the next one seated", and the note gives
  Brasseur's u cah. Kept.
- U3 mt yik'ow: the identity of the word is inferred. But Brasseur's q agrees, and the published icou is ik'ow (007/010 rule).
  Kept; the support is now in the note.
- U48 ca catat katat: Brasseur prints qatat here (q = k') and gatat in 016. The published 016 has katat by the letters, so it is
  kept with 016. Whether 'burn' k'at (010) should be restored in both is an open question for the owner.
- U7 xuꜭhaxic "xu- + ꜭhax": the published analysis of v in xvꜭhax / vꜭhax (QUESTIONS 011 point 5) is still open. Kept.
- U2 halha jalja': the drafter's notes list halha among words "left by the letters", but the mt follows 010's hal ha jal ja',
  where that glottal was supplied. This is consistent with the published part. Kept.
- U11 ca chi rox: chi left as chi, because the note marks the division as doubtful.
- U14 roo: kept by the letters, as 011's Roo.
- U37 Brasseur "h'yx": the OCR reads h'vx (y/v OCR noise). The establishment log reads it the same way. Kept.
- Establishment log: every doubtful reading is in its unit's note (camol qui ta U6; cha ꜩaconizah, xa vech U7; curi U8; ca chi
  rox U11; the bracket U12; Xa hina quichila U13; tacchiinel U30; the blot and the stroke U32; xa ꜫaꜫa hu ꜫex U43; Hun aꜫab,
  chi yocouic U45; ca catat U48; the struck taam … xeꜭha U50; ri que U55; Ꜭha chic U57; tocob U63). So are the t/h, r/v and a/u
  letter forms, catem (cafem) and hix. Both README-5b corrections open their notes with the manuscript reading: U32 "The
  manuscript has calata cala xic, …" and U38 "The manuscript has pa queꜫum maha, …". Nothing to change.
- Brasseur: the quotations and readings the notes credit to him are in the OCR, allowing for OCR noise. They include: 'les
  gradins précipités', cumuk, 'eaux bouillonnantes', the Molay note, Pa-puh-ya and its footnote, 'ils n'y touchèrent pas du
  pied', Caka be / 'le chemin Rouge', qamol and 'recueillir les nouvelles', 'Mord-les', 'finis par les mordre tous',
  ch'a izakonizah, x'av'ech, 'couverts de leurs ornements', 'Ah! ay!', the missing Ahi xꜭha Huncame, Xahina quichina given to
  Hun-Came, 'quoi donc vous a piqué', u cah culel, r'oo, the eleventh-lord footnote, the Quiqxic / Quiqre / Quiqrixgag footnote,
  'chacun de ceux qui commandaient', 'le poil de la jambe', 'que celui-ci s'arracha', lakchiinel and 'pour les tenter', Cala
  (010 note 22291), ka tem, chohim-abah 'pierre chauffée', 'tout allumées', zakarie, caka hu gexvach and 'quelque chose de rouge
  à la place', 'veilleurs', gaga / 'des lucioles', agab, yogouic and 'ils furent gardés', Mi-x-e ca chako and 'Ils sont tombés
  dans le piége', qatat and 'notre cœur en est brûlant', 'avec nous', qoheic, 'les envoyèrent chercher', 'Allons', 'Qui saurait
  dire d'où nous venons?', 'jetons notre ballon élastique', va ke, the chil footnote (Tesoro, 'écorcher'), 'pour un chil',
  'mais pour une tête de lion', 'C'est dit!', 'le jeu commença avec ceux de Xibalba', 'anneau', 's'élançant … bondissant',
  'le sol du jeu de paume', qu'yv'ah, 'nous', togob and 'En vérité, malheureux que nous sommes!'.

### Open decisions for QUESTIONS.md

1. For the establisher: there are three places where Brasseur differs from the established text and the log is silent:
   - ¶1 `chua cumuc` (B. chuva cumuk);
   - ¶2 `cha ꜩubah` (B. chi tzubah);
   - ¶7 `Ma cu xqui ꜩih ri chah` (B. Ma cu quitzih ri chah).

   The images should be rechecked if 018 is revisited.
2. Speaker tags: Brasseur consistently reads a tag as opening the next speech; this draft, like the earlier parts, reads it as
   closing the one before. This decides the roll-call (U16–U24) and the ball argument (U53–U57); the owner may want to confirm
   it as a house rule.
3. catat 'burning' is katat by the letters (016, 018), though Brasseur writes qatat / gatat and 010 restored k'at 'burn'.
   Decide together.
4. Achinac is achinak by 007's rule; if 'who' achinaq is accepted as certain, change it.
5. The tz' supplied on the plain ligature (tz'ub'aj, tz'onox) remains part of the open 015–017 question.


## Pass 2

This pass read all 63 units again as a fresh read: the labels, `l` against the K'iche', `l` against `i`, the house renderings, and mt against the toggle rules and the published parts (the comparison script was run again on 001–017). It also checked every gloss entry: 62 novel keys and 13 broadenings from the Sonnet glosser. Pass 1's changes were checked and found right. Brasseur's ball-argument passage (OCR 25504–25570) and his lords' footnote (25294–25296) were reread for the attributions.

Gloss checks, by script and by reading:
- Every gloss value's modern form was compared with the units' mt for that token.
- Every novel form has an entry, and there is no extra key.
- Every broadening starts with its popol-vuh-glossary.json entry, copied whole, + " · ".
- Every known token was checked against its glossary entry for this part's sense, which found five missing broadenings.
- Each entry's morphology and (inferred)/(guess) flags were read against the units' `l` and `n`.

Edits were made by script (load, change named fields, dump with ensure_ascii=False, indent=1, as the files were). No `t` changed. After the edits, a script check confirms:
- the 63 units tile the 9 pinned paragraphs exactly;
- each paragraph starts a unit (U1, 5, 9, 25, 29, 34, 39, 49, 59);
- len(mt) equals the number of WORD_RE tokens in every unit;
- every novel form has a gloss entry;
- every broadening begins with its current glossary entry + " · ";
- hooks.assemble + hooks.validate, run in memory with the merged glossary, give no errors or warnings, and no form is left uncovered.

`r3.py validate` was not run, because it needs the built story file and this pass does not build.

Counts. Units: 0 major, 1 minor, 1 style. Gloss: 0 major, 11 minor, 5 style.

### Unit changes

- U26 · l · minor · Pass 1 changed the note on `are chi biyh` to 'to say' (no chu- 'he' written), but `l` still had "that he-says". · `l` is now "this to-say its-name …".
- U8 · n · style · The note said "curi is cut 'then' + ri". The letters are cu + ri, as the published k'uri (k'u + ri) has it. · "cu 'then' (the short form of cut) + ri 'the'".

The fresh read found nothing else to change. All of these were checked again and are right:
- the labels: the ergative/absolutive prefixes, ch- + a-/i- commands, the passives xuꜭhaxic, xe vꜭhax, xe vchaxic and xe ꜩonox, the -ou agent-focus xi/xe tiouic, the antipassive xe tacon, and xahauax;
- the speaker tags of ¶3 and ¶8, tag by tag;
- the couplets in `i` (U26, U46, U47, U48, U62);
- the house renderings (Vꜩ bala, poy/aham che, Queꜫuma Ha, ahau, the lords' English names, Ahalq'ana).

The mt comparison is unchanged from pass 1. caca kaqa, quetaam qetaam, chiquech chiqech and toc tok are the only forms that differ from the published mt, and each is a different word or person.

### Gloss changes

- yicou · minor · "they crossed, waded" gave the form a person it does not carry (the 'they' is qui-). · "(inferred) cross, wade across (it); …".
- hu · minor · The entry was marked (guess), but both units mark hu = hun as inferred (U43, U56). · Now (inferred).
- alanic · minor · The morphology "al + -ik" left out the -an. · "al … + -an + -ik".
- ꜫaꜫa (broadening) · minor · The new reading had the head form q'aq', but the mt is q'aq'a. It also repeated the 'red' example of the old entry. · "q'aq'a — (inferred) fire; q'aq' 'fire' + -a, … (xa ꜫaꜫa chicop …; Brasseur gaga, 'des lucioles')".
- que (broadening) · minor · It said "a possessive pronoun after a noun", but in va que and ri que the pronoun follows a demonstrative or the article and stands alone. · "qe — ours; q- + e, standing alone as 'ours' (…, of the ball); Brasseur va ke 'la nôtre'".
- coh (broadening) · minor · Not needed, so removed. The published entry already has "koj — put, place; transitive verb (inferred)" and "koj — we, us (ongoing)". The 'you (pl.)' of chi coh belongs to chi, whose published entry has ch- + i-. Pass 1's request for it is refused for this reason.
- chec (broadening added) · minor · The only published entry is "carry her off" (ch- + ec), but U27 reads chec as 'leg, shin'. · Added "(inferred) leg, shin; …; perhaps the modern ch'ek 'knee', not restored".
- vah (broadening added) · minor · The only published entry is "hid" (evah), but U62's qui vah is 'you (pl.) want'. · Added "(inferred) want; w- + aj, the iw- 'you (pl.)' before a vowel with its i written in the qui before it, after Brasseur qu'yv'ah".
- re (broadening added) · minor · No published entry has 'this', but U53's Re ba is 'this (one)'. · Added "(inferred) this (one); …, the sense from the setting".
- xi (broadening added) · minor · The published entry has x- + i(n) 'me', x- + i- 'you (pl.)' ergative, and 'I'. None of these is the roll-call's reading (13 taps, U13–U24): the absolutive 'you' (ix with its x not written), as the units read it. · Added "(inferred) x- completive + i(x) 'you (pl.)', the absolutive object, …, said to one person out of respect; after Brasseur 'quoi donc vous a piqué'".
- ꜭha (broadening added) · minor · The published entry is 'says, said'. U57's Ꜭha chic is a command, 'say it again', marked doubtful. · Added "(guess) say (it)!, the bare root as a command; Brasseur 'C'est dit!'".
- ꜩubah · style · "the tz' and b' supplied". The b' is ordinary respelling, not supplied. · "the tz' supplied on the plain ligature".
- calainic · style · "they greeted" gave the noun a person. · "greeting, to greet; … (xe calainic 'they greeted')".
- cachaco · style · "we have beaten them" fixed the tense and the object, which come from mi xe. · "we beat (them); … the ending of a transitive verb, … (mi xe cachaco 'we have just beaten them')".
- ꜩonox · style · "they were asked" gave the form a person. · "be asked, was asked; … (xe ꜩonox 'they were asked')".
- chiquech (broadening) · style · "; also 'to them' above" repeated the old entry. · Removed.

The other novel entries were checked against their units and kept. They are true to the form, flagged as the units flag them, and general to the form. The Brasseur quotations were found in the OCR, among them 'Sang-d'Épervier' (25296) behind 'Hawk Blood'. The 12 remaining broadenings from the glosser each add a sense the old entry lacks and copy it whole: chi, tio, ti, cut, xquiz, que, ꜫaꜫa, caca, toc, chiquech, quetaam, ꜩih. Three of them (que, ꜫaꜫa, chiquech) were edited above; the rest are kept as written.

### Refusals

- coh broadening (pass 1's request): refused, as above; the published senses cover every use here.
- chi broadening: its old entry already has chik 'again' (c shared with the next word) and chik 'any more' (c not written), so the new reading is close to them. It is kept, because 'again, in turn' with the c simply not written (chi vi, chi roo, chi Ahalpuh) is the reading pass 1 gave five units, and the reader taps it there.
- camic: a broadening 'death' (U62 Xa camic) was considered and dropped. The published 'died, dying' is close enough.
- U15 i "he said in his turn": kept. Here the tag follows Vucub Came's first question to Xiquiripat, so "in his turn" is right, unlike U16–U23, where pass 1 made it "he went on".
- ꜩih broadening's example "'they lit the torch'" drops the negation of U43 (Ma cu xqui ꜩih). It is a fragment illustrating the verb, so it was not changed.
- vacac is flagged (inferred) and vvc and vahxac are not, though all three take their q from the known numerals (waqaq, wuq, wajxaq). The units do not flag them either, so the gloss was left as it is.

### For the owner

No new open decisions. Pass 1's list stands (the three Brasseur differences for the establisher, the tag-closes-speech rule, catat/k'at, Achinac, the tz' on the plain ligature). The drafter's proposed house renderings were not added to conventions.md.
