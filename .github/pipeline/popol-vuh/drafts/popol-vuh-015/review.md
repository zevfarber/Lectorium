# popol-vuh-015 — review

## Pass 1

I checked all 49 units against conventions.md, the packet and establishment log, QUESTIONS.md, the published parts 001–014, the
glossary and 014's review. A script compared every token's mt with that form's mt in 001–014. Every claim the notes credit to
Brasseur was checked in the OCR (lines 23765–24240). Every doubtful reading in the establishment log was traced to its unit's note.
Edits were made by script (load, change named fields, dump with ensure_ascii=False, indent=1). No t changed. After the edits, a
script check confirms that the 49 units tile the 20 pinned paragraphs exactly, that each paragraph starts a unit (U1, 3, 6, 9, 12,
14, 17, 18, 22, 24, 26, 29, 32, 34, 35, 36, 39, 41, 43, 46), and that every mt has one entry per WORD_RE token.

Counts: 1 major, 12 minor, 5 style.

### Changes

- U20 · l/i/n · major · `xa chilo coh ri ca chuch` was analysed as chilo 'look on' with coh 'we' as the doer ('we shall look on you as our mother'). coh is k- + oh, the absolutive 'we, us'. It cannot be the doer of a transitive verb, which takes ca 'we' (as xca tiho in the same speech). The English followed Brasseur's 'nous vous regarderons comme notre mère', which reverses who is looking. · Now read as ch- + i- 'you (pl.)' (the plural of respect of ¶3's chi bano) + il + -o, with coh 'us' as the object: l "only let-you(?)-look-on-it us the our mother", i "only look on us (?), our mother, grandmother". The note says this is a guess and gives Brasseur's division and his person.
- U20 · n · minor · iviy was analysed as "i- 'your (pl.)' + viy, v- + iy", which puts 'my' inside 'your' · Now iv- 'your (pl.)', the form of i- before a vowel (modern iw-), + iy. The note now contrasts this with ix viy in ¶12 (v- 'my').
- U5 · l/i/n · minor · `maui xil chi qui vach` was glossed "she-saw". xil has no ergative prefix: 'she saw it' is xril, as in ¶2's xril atit. The draft's own U43 reads xil rumal as passive · Now passive: l "not was-seen any-more their face", i "and their faces were seen no more". The note explains the form.
- U16 · l/i/n · minor · the same xil was glossed "she-saw", in a unit that itself has xril for 'she saw' · Now l "was-seen any-more", i "their faces were seen no more". The note cites Brasseur's 'on ne revit plus'.
- U5, U16 · mt/n · minor · `chi` 'any more' was given mt chi. The glossary's chi has "chik — again: chic with its final c shared", and the published parts give this chi as chik 31 times (002–013, before cut, ri, vi, pa, vchac, naipuch…) · mt chik for U5's chi and for U16's second chi (the parallel of U5). U16's first chi (`Ma chi cu`) is left as written. This answers drafter question 6 for these two places.
- U11 · n · minor · in `are cut qui chu ꜩeeh atit`, qui was labelled 'them' (inferred). An object 'them' before a transitive verb is e (absolutive), not qui · The note now says qui is not clear, and gives qui 'truly' (as qui ꜩih) as a guess suggested by Brasseur's 'il y avait bien de quoi faire rire'. mt ki is kept by the letters.
- U21 · i · minor · `Que nabax ri caꜩ` (que, ongoing) was rendered as a wish, "Let our elder brothers be remembered". `ta chuxoc` (optative) was rendered as a statement, "for so it has come to be". The mi + completive forms were rendered as plain past · i "Our elder brothers are remembered (?), and so let it be: they have been known (?), they have been named Hunbatz and Hunchouen, as they are called".
- U25 · l · minor · `ruꜭ ratit` was glossed "with-her her-grandmother". The note says r- is 'his' (the grandmother of each brother). `ruꜭ pu qui chuch` lacked the second 'with-her' · l "with-her his-grandmother, with-her also their mother".
- U8 · i · minor · "only hold back your laughter": 'only' has no word behind it (qui is unclear in the note) · i "hold back your laughter".
- U15 · i · minor · 'of every kind' renders macama, a doubtful reading and a guess (l macama(?)), but it was unmarked in i · i "of every kind (?)".
- U35 · n · minor · the note said that Brasseur "prints tam here and in ¶20". His text (OCR line 24094) reads `mavi ahilan tum` here, and tam only in ¶20 (24184) · The note now says so.
- about · minor · "sit their grandmother down with them" makes the grandmother's sitting causative. The text has `xcube puch ri catit cuꜭ`, 'she sat down with them' (intransitive). Brasseur's 'faisant asseoir' is free · Now "sing and play the flute and the drum, their grandmother sitting with them". The rest of the about was checked against the text and is accurate.
- U23 · n · minor · xax 'truly' is consistent with 001/008/009. But qui nimarizah has no x- of its own, while xqui yoc beside it does · The note adds that xax may be xa 'only' + the verb's x- written on xa (inferred). l is kept.
- U26 · i · style · the couplet `chuvach catit, chuvach pu qui chuch` was collapsed to "before their grandmother and their mother" · "before their grandmother and before their mother".
- U33 · i · style · "all by itself? (?)" · "all by itself (?)?".
- U37 · n · style · chavil was given as ch- + a- 'you (one)' + il; before a vowel the prefix is av- · Now "av- 'you (one)', the form of a- before a vowel (modern aw-)".
- U44 · l · style · `mi xoh coꜩic` (completive) was glossed "we are-tired" · "we became-tired".
- U5 · n · style · this note was rewritten together with the change above, so it no longer says "with its c not written".

### Findings considered and refused

- U1 vcamic uk'amik, U29 xqui cam xki k'am: these are the only mt that differ from a published mt for the same letters (006/007's vcamic is ukamik 'his death', a different word). The 'take' verb cam is k'am in 002, 005, 006, 008, 009, 010, 012 and 013, and Brasseur writes q here (u qamic, x-qui qam). 014's switch to the letters concerned the different form cucaam / caam. Kept; the note points to the open question.
- U8 Catiha mt Katija: the English takes ca as 'we', which elsewhere has mt qa. The reading is doubtful and the analysis a guess, so the letters are respelled and nothing is restored. Kept.
- U33 `ma cu qui chi tahin … chutuquel` as a question that expects 'yes' (drafter question 10). A plain negative contradicts the story (the hoe works by itself, ¶14–15), and Brasseur's French has no negative. The question reading is the least forced; it is marked (?). Kept.
- U9 `xe oc chi vloc`: chi could be chic 'again' with its c shared (parallel to `que xahou chic`), as in U5. The note leaves it unclear and mt chi. It stays so, because Brasseur also prints `chi uloc` and gives no 'again' at this point.
- U41 chu ꜩiloh tz'iloj (tz' supplied on the plain ligature): this follows 009's Junb'atz' and 010's restored ejectives. The word tz'il 'dirty' is certain, so the mt rule (restore where the word is certain) allows it. 011's tzotz rule concerned replacing a letter (z → s), not supplying a mark. Kept; drafter question 5 is left for the owner.
- U25 coheic k'oje'ik, U34 catoh q'atoj, U49 acab aq'ab', U1 cohom q'ojom, U41/U34 cab q'ab': certain words, with Brasseur's letter agreeing. This is the 007/010 practice. Kept.
- U15 ꜩac tzaq, muꜩumac mutzumaq, caꜫruxruh kaq'ruxruj: ꜩac tzaq matches the published entry for the same letters. caꜫ follows 010's kaq' by the letters (QUESTIONS 010/2). Kept.
- U40 choc chok (drafter question 2): the ch- + oꜫ analysis is inferred, so the letters are kept. Kept.
- U44 queꜭha 'they say' against the glossary's 'their food', and U8/U17 xque as future + 'them': correct readings, for the glosser to broaden. Not a unit change.
- U2 xu binaah (active, doer not stated) rendered "was given its name" in i: the passive English avoids inventing a doer, and l and n give the active form. Kept.
- U40 chapon "-on, with the thing seized named after it": a loose description of the -on form, but not wrong for this sentence. Kept.
- U22 ahzib with plain z: Brasseur prints áhtzib, but the MS has z and 014's ahzibab has the same letters. Kept.
- Inferred senses (yoc, toloc, tuyuba, bacala, puquih, cupuh, xpocolih) are marked in the notes but not (?) in i. The house marks guesses in i, not every inferred sense, as 014 did. Kept.
- Establishment log: every doubtful reading and every reading against Brasseur is in its unit's note (Eia catit U6, Catiha china U8, xchi ca bano U13, Xavi cu ꜫuz and tacchih U10, chitila U11, macama U15, yuc U45, piz la U41, quicah U29, xaqui U32, pa cabix U46, co cochoch U25, xe ꜭobic U21, ꜫatoh U42, iviy / viy U20, U28, U31, tum / tun U35, U47, caam U34, chuti U49, coh U49, acab U49; u qamic U1, cui / cuiu / cuyu U4, U8, U14, huiub U12, iaol / iaoc U37, U43, iacatahinac U47, pu holom and quehe viri U42, que banou U49, chutuquel U33). Nothing to change.
- The OCR confirms the other Brasseur quotations in the notes, including 'Voyez-vous', 'retenez votre rire', 'jusqu'au milieu de la salle', 'à la terrasse de la maison', 'en mémoire de nos aînés', 'Pigeon-Ramier', 'S'étant enveloppé la tête', xa + log 'gratuitement', Sarigue and Porc-Epic.

### Open questions for the owner

1. ¶8 `xa chilo coh ri ca chuch`: now read 'only look on us (?), our mother' (coh as object), against Brasseur's 'we shall look on you as our mother'. Please confirm.
2. `chi` 'any more' is now mt chik (U5, U16), as in the published parts. The drafter had asked whether to supply the k.
3. The 'take' verb (uk'amik, xki k'am here), with QUESTIONS 007/3, 008/3, 009/4, 014/1.
4. tz' supplied in tz'iloj; tum against Brasseur's tam in ¶20 (his OCR has tum in ¶15, against the establishment log's "tam both").

## Pass 2

A fresh read of all 49 units (grammar labels against the form, K'iche' → l word by word, l against i, couplets, house
renderings, mt per word against the MS letters and the published mt) and of every gloss.json entry (106 new, 20
__broaden__ as received). Brasseur's OCR was opened only to check meanings the notes and glosses credit to him (the
animal list, lines 24186–24189 and 24233–24237; the xalog note, 24125–24127 and 24176–24177). Edits by script (load,
change named fields/keys, dump with ensure_ascii=False, indent=1). No t changed.

Counts. Units: 0 major, 1 minor, 0 style. Gloss: 0 major, 13 minor, 5 style (15 entries touched in the minor rows, 5 in the style rows; two __broaden__ entries removed).

### Changes — units

- U36 · mt/n · minor · `acan oc` had mt `ok` ('enter'). After a verb of motion this oc is the directional ending, and the published parts give `acan oc` as `aq'an oq` five times (012 u17, u69, u75, u81; 013 u22), as the glossary's "-oq — ending after a verb of motion". · mt `oq`; the note now says that oc is the ending of direction, with the 012–013 precedent.

### Changes — gloss.json

- xmucun · minor · "(inferred) … not otherwise known": the glossary already has `mucun` "mukun — look, see; verb", and the unit does not mark the word inferred. · "looked; x- completive + mukun 'look, see' (the person is not written)".
- cuyu, cuiu · minor · given without a label, though they are the same verb as cui, which is inferred. cuiu's example "chu kuyu 'she held back it'" took the person from chu. · both "(inferred)"; cuiu's example now the whole phrase, "chu kuyu ka utze' 'she held back her laughter'".
- ꜫuz · minor · not labelled a doubtful reading, though the establishment log calls it the weakest reading in the part; "q' read from the tresillo" was wrong: the MS has a q/g-shaped letter + u, and ꜫ is printed after Brasseur's guz. · "(doubtful reading, guess) … the manuscript has a q/g-shaped letter + u, printed ꜫ after Brasseur's guz".
- tum · minor · "the manuscript has tun with two minims" applied to both places; ¶15 (0049 l.39) has a clear tum, and only ¶20 has tun. · "once written tun, with two minims".
- chapon · minor · "seize (it)" made it transitive; -on is the form without a doer prefix, followed by the thing seized. · "seize, take hold; chap 'seize' + -on, a form with no person prefix for the doer, the thing seized named after it", with the whole phrase as example.
- xaloc · minor · "loq 'love'" misspelled the modern word (Brasseur's log = loq') and missed the published `loc` "lok — aimlessly … in xa lok". · "xa 'only' + lok, as xa lok 'aimlessly' (Brasseur: xa + log, from 'love', 'gratuitement')". The OCR confirms the note (log, primitif de logo, aimer).
- banou, banouic · minor · "they who did it", "those who did it": persons that are in que / xe, not in the token. · "do, did it, with the doers named; b'an 'do' + -ow …", with the whole phrases as examples; banouic now points to the glossary's xbanouic.
- iaol · minor · given without a label, where both published senses of yaol are "(inferred)". `iaol` is not a glossary key (checked; `yaol` is). · "(inferred) … the yaol of earlier parts written with i".
- __broaden__ chu · minor · the new segment claimed 'she', which the old entry already covers (u- 'he, it' is the singular, with no gender), and stated the plural-doer reading (U22) as fact. · 'she' dropped; "chu — (inferred) ch- + u-, singular, with plural doers named after the verb (are puch chu sik'ij ri ajsib', ajkot …)".
- __broaden__ xe · minor · "xe' — under, beneath (xe' ki pam)" duplicates the old "xe' — the foot, the bottom of …, before the noun"; 014 printed the same xe i pam (mt xe') without a broadening. · removed; the token keeps the glossary entry.
- __broaden__ oc · minor · "ok — after aq'an, marks the direction 'up'" duplicated the old "-oq — ending after a verb of motion" and gave it the mt of 'enter' (see U36). · removed; the glossary entry covers oc (oq) as it stands.
- __broaden__ coh · minor · "puma" was given as certain; the glossary's ꜭoh has "read as puma, uncertain; Brasseur 'lion'", and Brasseur's list here has le Lion. · "koj — (inferred) puma; noun, as ꜭoh (Brasseur 'Lion'), written with plain c …".
- __broaden__ pixabah · minor · the new "instruct, give orders to" repeated the old "charge, counsel", while U17's sense ('call out, summon', with vbic) was not covered. · "pixab'aj — (inferred) call out, summon, with ub'ik 'thither' (xke qa pixab'aj ub'ik …), after Brasseur 'nous les appellerons'".
- __broaden__ vtiu · style · "in the list of animals" tied the entry to one place. · "utiw — coyote; noun, with u- part of the word, as in the name Junajpu Utiw (Brasseur 'Chacal')".
- __broaden__ hunchic · style · "the other, one more" repeated the old "one more". · "junchik — the other (are k'uri junchik 'and the other'); jun 'one' + chik".
- cui · style · the example mixed spellings ("maui xu kuy"). · "mawi xu kuy".
- icah · style · "the tool the twins fell trees with" tied the meaning to the story. · "axe; noun (ki ikaj 'their axes' is written joined, quicah)".
- acab · style · "the toggle restores the q' and b'": b → b' is ordinary respelling, not a restoration. · "restores the q'".

### Findings considered and refused

- U20 `xa chilo coh ri ca chuch`: i- 'you (pl.)' could address the grandmother and the mother together (as ¶11's ix catit, ix pu ca chuch) rather than the plural of respect, and coh after the verb is odd for an object. Both readings are guesses and the unit already marks it (?), with Brasseur's division in the note. Not changed.
- U22 `chu ziquih` with plural doers: kept in the unit (singular u- with an overt plural doer named after the verb); the broadening now marks it inferred.
- U33 question reading, U1/U29 'take' verb mt, U41 tz'iloj, the restored marks (q'ojom, k'oje'ik, q'atoj, aq'ab', q'ab'): pass 1's reasons stand.
- mixquina 'hoe', cutam 'stump': senses after Brasseur, but unmarked in the units and fitted by the story (the hoe clears the ground, the dove sits on the stump); left unlabelled, as the units have them.
- xque, queꜭha, chi, vcamic, xꜩeenic, xil, pixab, yoc, choc, la, quiz, huna, ꜩac broadenings: each starts with the published entry whole + " · ", adds a reading the old entry lacks, and matches the units' mt and sense. Kept.
- All other 92 new entries: modern form = the units' mt for every occurrence (script); meaning and labels match the notes; no 'here' / 'in this passage'. Kept.
- The animal list (iac Sarigue, vtiu Chacal, aꜫ Sanglier, ziz Porc-Epic, coh Lion) and the Xmucur, tronc d'arbre, pioche, charrue, gratuitement quotations were found in the OCR as cited.

### Script check (after the edits)

The 49 units tile the 20 pinned paragraphs exactly; each paragraph starts a unit (U1, 3, 6, 9, 12, 14, 17, 18, 22, 24,
26, 29, 32, 34, 35, 36, 39, 41, 43, 46); every mt has one entry per WORD_RE token; t unchanged from pass 1; every one of
the 282 distinct lowercased word tokens has an entry in the glossary, gloss.json or __broaden__; gloss.json keys are
exactly the 106 of novel-forms.json plus __broaden__ (now 18); every __broaden__ value starts with the published entry +
" · "; every gloss modern form equals the units' mt for that token, and the only mt that differs from the published mt for
the same letters is vcamic uk'amik (the open 'take' question).
