# popol-vuh-016 — review

## Pass 1

I checked all 56 units against conventions.md, the packet and establishment log, the drafter's notes, QUESTIONS.md, the
published parts 001–015, the glossary and 015's review. A script compared every token's mt with the mt of the same form in
001–015. Every claim the notes credit to Brasseur was checked in the OCR (lines 24185–24600, text and French). Every doubtful
reading in the establishment log was traced to its unit's note. Edits were made by script (load, change named fields, dump
with ensure_ascii=False, indent=1). No t changed. After the edits, a script check confirms four things: t is unchanged; the
56 units tile the 19 pinned paragraphs exactly; each paragraph starts a unit (U1, 5, 7, 9, 12, 13, 16, 18, 22, 26, 29, 32,
33, 37, 39, 43, 45, 49, 52); and every mt has one entry per WORD_RE token.

Counts: 0 major, 11 minor, 5 style.

### Changes

- U32, U41, U46, U47 · mt/n · minor · `ic` 'chile' had mt `ik'`, which supplies the ejective of ic 'moon'. The note to U32 called them "the word that is also 'moon'". The chile is modern ik, a different word from ik' 'moon', so there is nothing to restore. · mt `ik` in all four places (zaquil ic, cutum ic ×3). The notes to U32 and U41 now say that the chile is ik and is not the 'moon' word.
- U29 · mt/n · minor · `avetaam` had mt `aweta'm`, which restores a glottal stop. The published `vetaam` is `wetaam` 3 times (007 u51, 008 u32, 012 u41), with the double vowel kept. · mt `awetaam`. The note cites the published form.
- U15 · i/n · minor · `xu cam ri vhe queh` was read with the twins as the doers ("singular, though the twins are meant"). The twins' own verbs in this passage take qui- (xqui chap, xqui poroh). The same form in U20, `xu cam ri vhe cho`, is read by the draft itself as 'the rat took on its tail'. · The unit is now read like U20, marked inferred: i "So the deer came by its tail, and the rabbit by its tail (?): their tails became short (?)." The note gives the person marker, the parallel and Brasseur's reading (the twins). l already read "it-took" and is unchanged.
- U28 · l/i/n · minor · `ca rah` was labelled "'it is wanted'", a passive. It has the ergative r-, so it is active: 'one wants', with no doer named. i made the grandmother the subject ("your grandmother does not want them"), but the text has rumal ivatit 'because of your grandmother'. · l "one-wants-it … because-of your-grandmother". i "But no one wants them before your eyes, because of your grandmother, because it was for these that your fathers died." This keeps the pair of rumal clauses. The note explains the form.
- U36 · n · minor · `ca quil` was analysed as "k- + il 'see' with no doer". qu- before il is the 'they' of xquil 'they saw' (U46), so the form is 'they see (them)', meaning 'they are seen'. · The note now gives ca + qu- 'they' + il, and Brasseur's 'que nous voyions'. i "they are to be seen" is kept.
- U33 · l · minor · l left `quin vchah` and `quril` as bare brackets "(quin) (vchah) … (quril)", although the note analyses both and i renders them. · l "anything then I say(?), if she-sees-me(?) the your-grandmother?"
- U23 · i · minor · `Apa ꜭo vi` 'where is it' (l "Where there-is") was rendered "And what is it, then, that you have to tell?", which drops 'where'. · i "And where is it, then, this thing you would tell?"
- U21 · i · minor · "ready to pop out (?), squeezed by the boys": the text has only xrah biye cumal 'were about to go out, by them', and has no 'squeezed'. · i "which all but popped out (?) at the hands of the boys, Hunahpu and Xbalanque."
- U27 · n · minor · The note said that Brasseur omits `ri queꜩabal, xequel canoc`, and then cited his 'demeurés suspendus' for xequel. His K'iche' text omits the words, but his French renders them (OCR 24406–24408: 'ainsi que les instruments de leur divertissement, qui sont demeurés suspendus'). · The note now says both.
- U3 · n · minor · The note gave "chi ka riqo 'we shall find (them)'" as Brasseur's, but 'we shall find' is a gloss of riq and not his wording. His French is 'parviendrons-nous à surprendre'. · The note now quotes it.
- U32 · n · minor · "as Brasseur explains (pataxte …)": Brasseur's footnote (OCR 24396) says 'sorte de cacao de qualité inférieure … sert surtout de monnaie' and does not say pataxte. The glossary's pec is 'cave', a different word, and the note did not say so. · The note now quotes Brasseur, gives pataxte as the modern pek, and separates the word from pec 'cave'.
- U19 · i · style · "they cut it off (?)" for xqui cateh 'they blocked it' (Brasseur 'lui barrant le passage') reads as 'severed', in a passage about tails. · "they headed it off (?)".
- U9 · i · style · The couplet `chuti chicop, nima chicop` was collapsed to "all the animals, the small and the great". · "all the small animals and the great animals".
- U22 · n · style · "qui is k- with the in 'me' missing" was unclear (the i is written). · "qui is read as quin, k- + in 'me', with the n not written".
- U5 · n · style · "the -ou- form …, which names the doers" was vague. In 015 the form was `Apachinac coh michouic` 'who is tricking us', with the doer in front and oh as the one tricked. · The note now says this, and that here no doer is named.
- U46 · n · style · "as in a mirror" was stated as fact. · Marked inferred, with the reason (the rat is at the roof, so only its reflection can be in the bowl).

### mt against the published parts

After the edits, only four forms have an mt that differs from the published mt for the same letters. Each is justified:
- `cho` → `ch'o` ×15 (published cho 'lake' ×2, a different word). The word for rat and mouse is certain, so the mark is restored. Drafter question 1, left for the owner.
- `quih` → `q'ij` (U38, published quih kij 'juice', 1×). 'Noon' needs q'ij 'sun' (Brasseur gih). Drafter question 2, left for the owner.
- `caam` → `kaam` (U39 cu caam, published caam k'a'm 'vine' ×7). This is the 'carry' form, written by the letters as 012's and 014's cucaam (kukaam).
- `ic` → `ik` ×4 (published ic ik' 'moon'). The chile is a different word (see above).

Forms with several published mt (catit qatit/katit, cabix, ca qa/ka, xe/xe', ha ja/ja', vi wi/wi', chi chi/chik/chi', cab, cam, xcam, cu, cat, quib, que, xcah, vvb, chique, he) were each checked against person and sense. The draft's choices match the published distinctions in every case.

### Findings considered and refused

- cho ch'o, quih q'ij, the supplied tz' (ꜩapih family, ꜩonoh tz'onoj), quinac kinaq', iꜩocopih itzoqopij (c → q). Each is a certain word, under the mt rule and the 007/010/015 precedent (015 tz'iloj). The c → q change is ordinary respelling of Ximénez's c for /q/. Kept. Drafter questions 1–3 go to the owner.
- U2 `Xa vi xuban chi rib vleuh`, read as the work done by itself (drafter question 5). Brasseur reads 'ils en firent de même'. The singular u- fits the drafter's reading at least as well as the plural twins would, and the note gives both. Kept.
- U13 `xrah … qui chapo` and `mavi xu ya rib`, singular with plural participants. This is the fixed xrah construction of earlier parts, and the note says it is singular for the pair. Kept.
- U24 `chin biyh` and U33 `quin vchah`, with in- as the 'I' of a transitive verb. in- is the K'iche' 1sg ergative before a consonant (modern kinb'ij), so the label 'I' is right. Brasseur's division qui-nu for U33 is in the note's Brasseur quotation only implicitly, and it is not needed. Kept.
- U3 `chi ca rileo` mt qa: if the stem were il, r- would be 'he'. The reading is marked doubtful, and the mt follows Brasseur's ka + riq 'find'. Kept.
- U53 `xi bano` 'you (pl.) did': the glossary's xi is x- + i(n) 'me'. Here the twins ask the grandmother and the mother, so i- 'you (pl.)' is right. That is the glosser's broadening, not a unit change.
- U25 `xu ꜭhaxic`, called passive with the u written: this is the published xuꜭhaxic (006 u54, 012 u13), labelled the same way. Kept.
- U34 "Do not lose heart" for `Mavi chi ꜩac a ꜭux`: it is a common English phrase, but it is the literal sense of the K'iche' ('let your heart not fall'). Kept.
- U10 tiꜭil mt tik'il, against the published tiquil tikil: it is the same word, but the cuatrillo is the establishment's reading and the mt respells the letter. The note says so. Kept.
- Inferred senses that are marked in the notes but not (?) in i (cuchu, yopih, canahoc, colon vloc and others). The house marks guesses in i, as 014 and 015 did. Kept.
- Establishment log: every doubtful reading and every reading against Brasseur is in its unit's note (Cate/catte U1; ruꜭ with comma U2; xcam plain c, rileo U3; Naqui ri lo U5; qui bic U8; tiꜭil and the missing `ta xe petic, xe chauiheic conohel` U10; xa cuchu he, xcupu cab U14; yac, aꜫ U16; catat U17; pa cul U19; ꜫaꜫ U20; ꜭaholab U21; Ma ta qui camic, ꜭo/go U22; chabiyh U23; queꜩabal, xequel U27; cuvvn U32; vve quril U33; a ꜭux, ru ꜭhaxic U34; co U35; ca quil U36; quih U38; yacalic, libah chi U40; ca ha, the cu over ca U43; chupan U46; chel, chu tiho U48; xu ca cat, quum/tzuum U50; vbeel U51; ca ꜭux U53). Nothing to change.
- The OCR confirms the other Brasseur quotations in the notes. They include: 'ils en firent de même', 'nous veillerons', 'Peut-être', 'nous avons été joués', 'tout-à-l'heure', 's'armèrent', 's'y cachèrent', 'abrités … dans l'ombre', 'se rassemblèrent', 'chaque espèce s'unissant', yaclin and its footnote, 'leurs multitudes se pressant', 's'approchérent', 'le Lion, le Tigre', 'les queues rapprochées', 'une queue tout-à-fait courte', 'le Renard', 'le Sanglier', 'le Porc-Epic', 'brûlait de colère', 'tout le dernier', 'en sautant', 'lui barrant le passage', 'dans un mouchoir', 'le serrèrent vivement à la tête', 'voulaient l'étouffer', 'commença à porter la queue', 'pressés dehors', 'Que je ne meure pas', 'un peu', 'l'histoire de la pelote élastique', 'le chilé blanc', 'gardé ou d'oublié', 'tu le grignoteras', 'quoi donc je dirai' (footnote 3, with qui riri yv atit), 'tout prêts', 'ce coin de la maison', the tum footnote and 'xa pu ka ti ca kil vi', 'ayant avisé pour une nuit', 'à midi précis', 'Portant le Rat sans le montrer', yaçalic, 'délibérément', 'broyez', 'chilmol', 'on leur prépara', 'renversé l'eau de la cruche', 'allez donc nous chercher à boire', ch'y qama k'uquia, 'aucun besoin de boire', 'moucheron', 'nous étouffons faute d'eau', 'nous mourons de soif', 'le Rat alla couper', tzuum, 'Ils s'en emparèrent immédiatement', qu'euah, u heel hom, 'avec leur sarbacane', 'fatigués (d'attendre)', and 'comment leur fut livrée la pelote'. One quotation could not be checked: Brasseur's `Ma-ta qu'in camic` (U22), because the OCR is garbled at that point (24300). It is cited as the establishment log has it.
- The about was checked against the text and is accurate. "So the ball came to them" matches U56's (?) reading.

### Open questions for the owner

1. cho ch'o (restored) or cho by the letters (15 tokens).
2. quih in `tiquil quih` as q'ij.
3. The tz' supplied on the plain ligature for tz'apij and tz'onoj (with 015's tz'iloj).
4. U15: the deer and the rabbit "came by" their tails (the u- reading, parallel to U20), against Brasseur's twins.

## Pass 2

This pass covered all 56 units again and every gloss entry (75 novel keys and 11 broadenings from the glosser). It checked
pass 1's changes and found them right: ic → ik for 'chile', awetaam, the u- reading of U15, the active ca rah in U28, and
ca quil. The Brasseur quotations were checked again in the OCR, including the footnotes for yaclin (24268–24270), pek (24396)
and Xan (24518). Every gloss value's modern form was compared by script with the units' mt for that token, and all of them
match. Every broadening was checked against popol-vuh-glossary.json: each starts with the old entry, copied whole.

Edits were made by script (load, change named fields, dump with ensure_ascii=False, indent=1). No t changed. After the
edits, a script check confirms: the 56 units tile the 19 paragraphs exactly; each paragraph starts a unit (U1, 5, 7, 9, 12,
13, 16, 18, 22, 26, 29, 32, 33, 37, 39, 43, 45, 49, 52); len(mt) equals the number of WORD_RE tokens in every unit;
gloss.json loads and covers all 75 novel keys; and every one of the 18 broadenings starts with its glossary entry + " · ".

Counts. Units: 0 major, 2 minor, 1 style. Gloss: 0 major, 13 minor, 4 style.

### Unit changes

- U5 · i · minor · "as we found it when we came there just now" adds 'as we found it', which is not in the text (ta xoh opon mier 'when we arrived just now'). puch 'also' was dropped. · "and a great forest too over our field (?), when we went there just now, grandmother".
- U22 · l · minor · The l left (qui) bare, though the note reads it as 'I' (quin, with the n not written) and the i renders it. Pass 1 fixed the same gap in U33. · "Not (ta) I(?) dying by-you;".
- U19 · n · style · "has plain c (Brasseur cateh)" presents an agreement as if it were a difference. The OCR (24293) has x-qui cateh. · "with plain c as in Brasseur's cateh".

### Gloss changes

- cho (broadening) · minor · The new reading began "cho — rat", but the modern form must be the mt, ch'o. · "ch'o — rat, mouse; noun (modern ch'o), …".
- cateh · minor · The morphology was misnamed: "x- completive form xki katej". The form has no x-. · "katej — (inferred) block, head off; transitive verb (xki katej 'they blocked it'), …".
- ꜩapitah · minor · "the plain tz ligature supplies the tz'" was wrong. The ligature is plain, and the toggle supplies the tz'. · The entry now says so.
- vꜩin · minor · "tzin … with u-" took the u of utzin for a prefix. The verb is utzin 'be complete' (from utz 'good'), as the unit's note has it. · The entry is rewritten.
- iaclin · minor · "does not fit K'iche' grammar" was stated as fact, and the entry was not marked uncertain. This is Brasseur's footnote (OCR 24268–70), and the unit attributes it to him. · The entry is marked (inferred) and attributes the claim to Brasseur.
- cuxu · minor · The entry put the 'you shall' of cha into the form cuxu itself. · "gnaw (it); with cha 'you (command)', …".
- varah · minor · The entry put ca 'we' into the form. · Removed.
- quia (broadening) · minor · It was marked (inferred), but the unit calls the sense a guess. · (guess).
- cama (broadening) · minor · It duplicated the existing sense: the old entry 'taking, take (from k'am)' already covers 'fetch'. · Removed.
- quih (broadening added) · minor · The existing entry is kij 'juice', and it says explicitly 'not q'ij'. The units read tiquil quih as q'ij 'noon, sun' (U38). The glosser missed this. · Added "q'ij — (inferred) sun, day; in tikil q'ij 'noon' …".
- xiquin (broadening added) · minor · The existing entry has only 'ear', but U35 and U40 use xiquin ha 'the corner of the house'. · Added "xikin — corner (of a house) …".
- xi (broadening added) · minor · The existing entry has only x- + i(n) 'me', but U53 xi bano is 'you (pl.) did'. Pass 1 left this to the glosser, who missed it. · Added "xi — you (pl.) (did it) …".
- xcut (broadening added) · minor · The existing entry is 'was struck (guess); perhaps showed', but U42 has 'was ground'. · Added "xkut — (inferred) was ground …".
- caam (broadening added) · style · The existing entry has only k'a'm 'vine', but U39 cu caam has mt kaam 'carry'. · Added "kaam — (inferred) carry …".
- ti (broadening added) · style · The existing entry is 'eat (flesh)', but U41 and U42 use qa ti / qui ti 'our eating, their meal', a noun, and the food is not flesh. · Added "ti — (inferred) eating, a meal …".
- que, tah (broadenings added) · style · U23 que chabiyh, U51 que vah and U51 xqui mahix tah are unclear in the units, and neither existing entry has an unclear sense. · Added an "(unclear) … left unrendered" reading to each.
- xuban, ana, vquebal, numic · style · These were tidied. xuban was marked (inferred) although the form is certain; ana was capitalised; vquebal had only 'its', although the jar is hers; numic had "(inferred)" in the wrong place. · Corrected.

The other novel entries were checked against their units and were found to be true to the form, marked where the units mark them, and general to the form. Kept as written: poroh poroj, quinac kinaq', vz us, xcoz kos, mezcutahinac (mes 'sweep'), and the ꜩapih family.

### Refusals

- tum, ic, pec, va, tac, cat, cul, quebal broadenings: each adds a sense that is not already present and copies the old entry whole. Kept (quebal was tidied).
- I left the remaining doubtful-reading words without broadenings where the existing entry already covers the use: quil 'it is seen', chel, ya 'river', ha 'water', ca as the unclear particle, chi as the unclear particle, and pu 'in its'.
- U13 xrah … qui chapo (i "the twins tried"), U26 icahau 'your father' with i "fathers", and U42 lac 'plate' with i "bowl" are all within house practice. Not changed.
- The about paragraph agrees with the units, including U15's (?) reading, which it does not contradict. Not changed.

### Open questions for the owner (in addition to pass 1's four)

1. xan (U47): the modern K'iche'/Kaqchikel word xan may be 'mosquito'. If the owner confirms this, the gloss could say so. It now keeps xan as a name, after the text's own comparison with vz.
2. tiho (U48), published as "tij 'try'": in modern K'iche', tij is 'eat (tr.)', and 'try' is another verb. The sense 'she tried' rests on Brasseur ('qu'elle essaya'). The published entry was not changed here.
3. xvoro (U48) is labelled x- + wor + -o, but a transitive verb would want the ergative u- (xuworo). Either the v is the prefix or the prefix is unwritten. Left as drafted.
