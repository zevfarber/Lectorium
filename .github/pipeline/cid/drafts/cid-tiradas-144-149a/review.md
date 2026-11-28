# Review — cid-tiradas-144-149a (vv. 3329–3408 incl. 3359b; tiradas 144–149)

**Counts.** Pass 1 (units.json): 4 error · 6 weak · 4 style (14 changes). Pass 2 (gloss.json): 9 error · 14 weak ·
6 style (29 entries changed, 4 broaden entries added).

Checked: all 35 units (`t`/`l`/`i`/`n`) against the pinned packet, conventions.md, the pilot and the published parts
(grep of cid-tiradas-*.json for escaño, red, viga lagar, premió, rogadores, Merced, Ferrando, riebtos, menos valedes);
the scan, PDF pp. 337–343 (printed 333–339), whole at zoom 1.4, with clips at zoom 2.2–6 of the footnotes to 3343,
3344, 3350 (both pages), 3373, 3377, 3385 and the italics of 3373. Every rubric (144–149) and every footnote quoted in
the notes (3329, 3330, 3336, 3339, 3343, 3344, 3350, 3354, 3355, 3356, 3359, 3360, 3365, 3366, 3367, 3373, 3377, 3379,
3380, 3385, 3394, 3400) was compared letter by letter with the print. Cross-references checked in source/established:
675, 847, 1376, 1881, 1906, 2080, 2084, 2172–73, 2280–2301, 2683, 2908, 3253, 3254, 3296, 3313–3314.

The `t` fields joined by "\n" equal the packet's 81 verses in order (script, before and after editing); no `t` changed;
every `l` has as many lines as its `t`. Keys of gloss.json = novel-forms.json + `__broaden__`; every `__broaden__` key is
in known-forms.json, and every value added there starts with the known entry whole + " · " (asserted).

Edit scripts: scratchpad `rev144/fix_units.py`, `rev144/fix_gloss.py`; originals kept as `rev144/*.orig.json`.

## Pass 1: units.json

1. 3343–3345 · n · error · the quotation of Pidal's note to 3344 drops a comma: the print has "(yollo lidiaré, 3367,
   lidiártelo, he, ego tibi litiabo)" · comma restored; the English says how it is punctuated on the page.
2. 3349–3351 · n · error · the quotation of Pidal's note to 3350 reads "o debía perder la vida. Por esto": the print (PDF
   339, zoom 4) has a comma, "vida, Por esto" · restored, and the parenthesis on accents now says so. The accents were
   confirmed: debia (p. 338) and tenia (p. 339) without, the second debía with; "tu lo confesarás" (tu unaccented) as
   quoted.
3. 3355–3356 · n · error · the cross-reference quoted v. 1906 as "por conssagrar con ifantes de Carrión"; the
   established text has iffantes · corrected.
4. 3385 · n · error · Pidal's headword quoted as "das paz": the print (zoom 6) has "das pas", its last letter the same
   italic s as in das (the italic z of dezir and Gonzálvez on these pages is a different shape) · now "das pas (so printed,
   for das paz)".
5. 3331–3334 · n · weak · "fizist = feziste" gives a form that is not the base of fizist · now "fizist = fiziste (modern
   hiciste), 'you did', with the final -e dropped".
6. 3343–3345 · i · weak · "I challenge your body" is not real English. The note keeps the formula and Pidal's 'te reto
   tu persona' · `i` now "I challenge you in your own person as a wicked man and a traitor"; `l` keeps "the body".
7. 3359b–3360 · n · weak · the [venidos] / mismos passage settled as far as the page allows (see "Readings" below) ·
   rewritten: the footnote glosses a word mismos the printed line lacks; venidos is in italics, Pidal's supply; both fit
   í-o; the note must refer to a reading mismos at this place that Pidal replaced, but the page does not say whether it
   is the manuscript's or an earlier text's. Still marked uncertain.
8. 3373–3375 · n · weak · "flushed with food and wine" stated as fact; the wine is not in the text · now "flushed from
   his meal (that wine had a part in it is our inference)".
9. 3377–3378 · n · weak · Pidal's "no concebían" was rendered "could not bear" · now "could not conceive".
10. 3379–3380 · n · weak · Pidal's "que el Cid tomase parte demasiado directa, como pequeño propietario, en el arreglo de
    los molinos y cobranza de la molienda" summarized as "took a small owner's hand" · now "took too direct a part, like a
    small proprietor, in the repair of the mills and the collecting of the toll".
11. 3394–3396 · l · style · [rogador] was "[asker]"; the published v. 2080 has rogadores "petitioners" in `l` · now
    "[petitioner]".
12. 3394–3396 · n · style · rogador gloss aligned: "'petitioner' (as rogadores at v. 2080), the go-between …".
13. 3381 · n · style · "Quil = quien + le": the form is qui · now "qui (= quien) + le".
14. 3367–3369 · n · style · "the que repeats after the aside" (no earlier que in the sentence) · now says that sabed takes
    the que clause, with fijas del Çid put first.

Verified and left (no change): all other quotations exact, including 3329, 3330, 3336, 3339, 3343 (small e of era after
the full stop; así accented), 3354, 3355 (headword aparecidos without cedilla), 3356, 3359, 3365, 3366, 3367, 3373 (Ansuor
Gonzálvez; infantes lower case), 3377 (vió, diría, habíamos, mío accented; concebian not quoted), 3379 (río, Váyase),
3380, 3394 (Iñigo unaccented on the page, Jiménez), 3400 (bendición without cedilla); the six rubrics; the paragraph
indent at 3392; italics of A[n]su[o]r (n and o italic) and of 3394–3396.

Refused:
- 3341 "a sos vassallos, víolos": kept. The object-first reading fits the comma and v. 3385, and the note gives the
  alternative.
- 3371 "de quando dicho has" as quanto: kept. It is flagged as our reading. Compare 3313 de quanto dicho has.
- 3378 darie nuevas "renown": kept. Pidal's paraphrase is 'recibir nobleza', and the known entry for nuevas already has
  'renombre, fama'.
- 3379 F[o]sse: kept as an uncertain optative fuesse ('Váyase'); a reflexive se is left open.
- 3381, 3385, 3394–3396: kept. Each is already stated as our reading.
- 3346 "turns ... to both Infantes (vos, plural)": kept. Varones in 3347 confirms the plural.
- Íñigo with an accent in `i`: kept, although Pidal prints "Iñigo" without one (he accents no capital I). This is the
  modern spelling of his "hoy Iñigo".
- 3329 "Speak, Fernando": kept.

## Pass 2: gloss.json

Errors (the sense or the analysis was wrong):
1. dexósle · the subject was given as "he" with "let him seize him". The subject is the lion: now "it let (itself), let him
   … 'it let him take it by the neck'", with Pidal's paraphrase.
2. riébtot · the lemma "riebtar" is invented; the verb in the text is reptar (reptado, v. 3391). It is now "reptar + te",
   and the example uses Pidal's 'te reto tu persona' in place of "in person".
3. consagrar · "consecrate, make binding" was wrong. It is now "to become kin by marriage", Pidal 'emparentar', with
   v. 1906 cited and modern consagrar excluded.
4. yollo · "yo + lo" dropped the te. Pidal gives yot lo, 'yo te lo lidiaré', so it is now "yo + te + lo".
5. telo · the token was lemmatized as "fazer + te + lo". The token is only te + lo, and the entry now says so.
6. quil · the example "give him in marriage to the men of Carrión" contradicted the unit's reading. It now matches the
   unit ("let him marry into the house of Carrión", a reading).
7. otorgarás · "admit, grant … closest reconocerás" missed Pidal's 'confesarás'. It is now "you will confess, admit", with
   = confesarás.
8. simenones · the etymology "son of Simeón/Ximeno" is invented. It is replaced by Pidal's Enneco Semenones 'o Iñigo
   Jiménez'.
9. rogador · "suitor" was wrong: the rogador is the envoy, not the suitor. The entry also carried a stray "reading
   uncertain". It is now "petitioner, the go-between who asks for the bride", from Pidal's note to 3394, with v. 2080 cited.

Weak (thin, or not from Pidal):
1. apareçidos · uncertainty removed. Pidal's 'no se hubiesen efectuado' is added.
2. fuessen · the unexplained "MS fuessen" is dropped.
3. lidiaré · Pidal's sense of the challenge formula is added: 'sustentar por medio de una lid judicial, una acusación'.
4. linpios · Pidal's gloss is added, and the example is now quoted as printed.
5. alevoso · "a traitor" collided with traidor. It is now "treacherous, faithless; a treacherous man", kept apart from
   traidor.
6. fústed · Pidal's 'fuístete a meter' is added.
7. vestist · "put on" is now "put on, wore", matching Pidal's 'nunca más vestiste'.
8. darie · the example now gives renown, not "news", with Pidal's paraphrase and the use at 3381.
9. ovirna · "near Burgos" came from general knowledge. It is replaced by Pidal's "the Ubierna runs past Vivar".
10. maquilas · "Arabic" came from general knowledge and is dropped. Pidal's definition and 'cobrar maquilas' are added.
11. picar · it is now marked as our gloss of the trade sense, with Pidal's 'picar sus molinos'.
12. fártaslos · "stuff them" is now "glut them, sicken them", with the sense marked as a reading.
13. bendiçión · Pidal's 'como mujer legítima' is added.
14. __broaden__ otorga · the imperative sense is now "confess, own", Pidal 'confiesa esto', where it was "admit, grant …
    reconoce".

Style:
1. calla · "hush, traitor" is now "be silent, treacherous man", consistent with the unit.
2. ojarra · "Basque-looking" is now Pidal's "a Basque name (otsoarra 'lobuno')".
3. yéñego · Pidal's 'Yéñego, hoy Iñigo' is added.
4. __broaden__ cuerpo · "in person; reading from context" is now Pidal's 'te reto tu persona'.
5. __broaden__ recabdo · the example is now the line as it stands, "there was little sense in what he said".
6. __broaden__ es · the drafted "es de … the infante of Navarre's man" misparsed the line, since del goes with
   [rogador]. It now reads "the one is the infante of Navarre's petitioner".

Added to `__broaden__` (forms the glosser left uncovered in this part's senses):
- fosse: the scornful wish at 3379 ('Váyase'), with the reflexive left uncertain;
- paz: dar paz 'give the kiss of peace' ('besas');
- prender: prender maquilas 'collect' ('cobrar');
- do: fasta do 'until' ('hasta que despertó').

Left as they were: miente, desató, fizist, metístet, metistet, vales, çercamos, curiar, fos, esperó, traidor, éstot,
verdadero, quedó, repentimos, bivan, sospiros, retraydo, ardido, saliste, dirás, mintist, fincado, armiño, rastrando,
vermejo, almorzado, molinos, suele, almuerzas, âmigo, falsso, amistad, calle, reptado, lidiarán, acaban, infante, ifante,
reinas, callaron, ascuchó; broaden di, o, menos, malo, viene, quanto, fo, partir, qual, ca.

## Readings left uncertain
- 3360 [venidos] / footnote "mismos, ripio, igual que en 847". The page cannot settle whether mismos is the manuscript's
  word. The 1908–11 apparatus would settle it, and it was not consulted.
- 3341: a sos vassallos, víolos is read as the object put first; "turned back to his vassals" is the alternative.
- 3371: quando is read as quanto.
- 3378: darie nuevas is read as "give us renown".
- 3379: F[o]sse is read as an optative of ir. Whether a reflexive se is run in is open.
- 3379: picar los molinos is read as "dress the millstones". This is our trade gloss.
- 3381: Quil darie … a casar is read as "who would let him marry …".
- 3385: fártaslos is read as his breath at the kiss of peace.
- 3394–3396: the effect of the restorations (envoys, not princes) is our account.
- 3375: that wine is behind his red face is our inference.

## House renderings (drafter's proposals)
Confirmed:
- alevoso "treacherous-one" in `l`, "treacherous man" in `i`, kept apart from traidor "traitor" (v. 3383).
- lidiar of a charge "I-will-fight" in `l`, "maintain (against you) in combat" in `i` (Pidal's note to 3344).
- otorgar of the beaten man "confess" (Pidal 'confiesa', 'confesarás', vv. 3329, 3350).
- Yéñego Simen[ones] "Íñigo Jiménez" in `i`; Ojarra kept so.
- infante/ifante de Navarra, de Aragón "Infante" in `l`, "the prince of Navarre / of Aragon" in `i`; Navarra, Aragón
  "Navarre", "Aragon" in `i`.
- rio d' Ovirna "the river Ubierna".
- maquilas "mill-tolls" in `l`, "toll of meal" in `i`.
- dar paz "give the kiss of peace".
- a ondra e a bendiçión "in honour and with the Church's blessing" in `i`.

Amended:
- rogador: "petitioner" in `l`, as rogadores at v. 2080 (104-104c), not "asker"; "speaks for", the go-between, in `i`.
- Riébtot el cuerpo: "I-challenge-you the body" in `l`, "I challenge you in your own person" in `i`. "I challenge your
  body" is rejected for `i`.
