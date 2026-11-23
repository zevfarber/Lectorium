# Review: cid-tiradas-112-114 (tiradas 112–114, vv. 2278–2337)

Checked against the pinned packet; Pidal 1923, PDF pp. 275–279 (printed 271–275: text and italics, the cantar
heading, the rubrics of tiradas 112, 113, 114 and 115, and the footnotes 2280, 2281, 2282, 2285, 2286 b, 2289,
2291, 2295, 2298, 2299, 2300, 2301, 2309, 2310, 2311, 2312 b, 2314, 2320, 2322, 2324, 2326, 2329, 2333, 2337);
the established texts for the cross-references (253, 1053, 1711); the published parts for house renderings;
`conventions.md`; `known-forms.json`, `novel-forms.json`.
`t` integrity (by script, before and after the edits): all `t` joined by "\n" equal the 62 packet verses in
order; 27 units, none over 3 verses, none across a tirada break; every `l` has as many lines as its `t`; no `t`
was touched. Both files edited by script (json load/replace/dump, indent 1, ensure_ascii=False).

## Pass 1: units.json

1. 2278 (vv. 2278–79) · n · **weak** · "The last s of s[o]s is read as roman, but it may be italic too: that
   letter is at the limit of the scan and the reading is uncertain." On the 300-dpi image the line is well inside
   the type area and the final s of sos is plainly roman (only the o is italic), as pinned. The hedge asserted a
   scan problem that does not exist. Done: sentence removed; the note still says the o of s[o]s is Pidal's.
2. 2317 (vv. 2317–18) · l · **weak** · `l` "for they-saw" while the note (rightly) calls veyen the imperfect
   'they were seeing'. Done: `l` "for they-were-seeing"; `i` "they saw" kept (real English).
3. 2292 (vv. 2292–94) · l + n · **style** · mesnadas "retinues": the house keeps "retinues" for escuelas
   (conventions, 104-104c); mesnadas has been "household-troops"/"troops" in `l` (84-86, 91-94, 64-68). Done:
   `l` "household-troops", note "'household troops' (as in earlier parts)". `i` "my men" kept.
4. 2319 (vv. 2319–21) · n · **style** · catamos glossed 'we looked at' without its tense; the form is ambiguous
   (present = preterite) and the glossary called it present. Done: "preterite, the same form as the present:
   Pidal's paraphrase puts it in the past, at the marriage" ('Al casarnos … miramos').
5. 2328 (vv. 2328–30) · i · **style** · "as the Creator may help you": the house `i` for sí vos vala el Criador
   is "so may the Creator help you" (83-83a, 104-104c). Done.
6. 2336 (vv. 2336–37) · n · **style** · "Pidal's next rubric puts the gap at about fifty lines": the rubric says
   "50 versos" flat. Done: "fifty lines". The rest of the lost-folio note checked against the rubric of 115
   (Mensaje de Búcar.—Espolonada de los cristianos. Cobardía del infante Fernando (Laguna del manuscrito, 50
   versos que se suplen con el texto de la Crónica de Veinte Reyes). — Generosidad de Pedro Vermúdez): right, and
   it follows the conventions (prose not included, the chronicle named).

Points the brief asked to weigh, judged:
- Rubric 113: the drafter's quotation "El rey de Búcar de Marruecos ataca a Valencia" is exactly what Pidal
  prints (the odd "rey de Búcar" is his). The English "King Búcar of Morocco attacks Valencia" is right. Kept.
- Rubrics 112 and 114 and the heading "Cantar tercero / La afrenta de Corpes": exact. Kept.
- 2312b: wholly italic on the scan, no margin number; Pidal's footnote numbers it "2312 b". The note says the
  line is his restoration and the b his, citing the footnote: right. 2286b is printed in his margin: right.
- Every "Pidal's note" checked against the footnotes listed above: accurate in wording and reference (2285
  comp. 1053; 2289 → v. 2322; 2291 Quevedo's quatrain verbatim; 2312 b → v. 1711; 2314 Búcar p. 29 and sil
  oviestes contar; 2320 vv. 1374, 1888; 2322 comp. 2289; 2324 vv. 2169, 2177; 2326 v. 253; 2333 v. 2271 and the
  fuero confirmed by doña Urraca 1109). Glosses not attributed to Pidal (escaño, brial, viga lagar, etc.) are
  not presented as his.
- Italics: every bracket described rightly (se[d]í, [Çid], [los], s[o]s, el[l]e, Ferran[t], Gonçal[v]ez,
  [ifant de Carrión], vi[d]o, Di[a]g, po[r]a, vi[di]estes, avie[n], ve[e]r, so[n]).
- Grammar labels confirmed: sedí, yazie(s), durmie, veyen, avien (imperfects); alçasse (imperfect subjunctive);
  vala, salve, sean, ayan (present subjunctive); folgad, idlos, sabed (imperatives); remandrán, vençremos,
  abremos (futures, syncopated/epenthetic); valer nos ha (split future); vi[d]o, vío, ovo, oviestes, vi[di]estes,
  tovieron (strong preterites); premió (premer), envergonçó, adeliñó; the enclitics saliós, desatós, metiós,
  tornáronse, liévalo, mandólo, Alegravas, Qués, sil, sol, dos, para'; a part salidos son (ser + participle);
  fincadas ha (participle agreeing with the object).
- Internal cross-references (2281, 2282, 2287, 2289, 2296, 2298, 2271) and external ones (253, 1053, 1711): right.

Refused / left as drafted:
- 2288 `i` "ran out through the door" for salió: a fair lift in real English, the panic is in the scene. Left.
- 2306–08 `i` "until my Çid … ordered it stopped": the sequence is in the lines; left.
- 2300–01 `l` "leading-by-the-hand" beside the note's "by the halter": the note explains adestrar from diestro
  and Pidal's 'como de diestro'; the `l` is transparent enough. Left.
- 2317–18 `i` "and had no relish for the sight": de que may take moros or tiendas as antecedent; the English
  keeps both open. Left.
- 2313 fincadas ha read with Búcar as subject, 'there are' offered: properly hedged. Left.
- Restored letters carried into English words ("h[i]s", "sa[w]", "a[re]", "se[e]"): house practice; left.

Pass 1 counts: error 0 · weak 2 · style 4 (6 items).

## Pass 2: gloss.json

1. yazies · **error** · glossed as plain imperfect yazer 'he was lying', the enclitic se of Yazies (yazie + se,
   Pidal 'estábase echado') missing. Done.
2. catamos · **error** · "present 1st pl.; we look at": preterite here (Pidal 'Al casarnos … miramos'). Done.
3. trevo · **error** · "me is an ethic dative": me is the reflexive of (a)treverse (Pidal 'me atrevo a
   vencerlos'). Done.
4. __broaden__ arrancar · **error** · same ethic-dative claim. Done: new reading kept, with Pidal's paraphrase.
5. __broaden__ me · **error** · new reading "ethic dative … with no change of sense": wrong (reflexive of
   treverse), and the known entry already has "reflexive 'myself'". Done: broaden deleted.
6. ferrant · **error** · "the elder Infante": invented; the poem says nothing of their ages. Done: "one of the two
   Infantes of Carrión".
7. diag · **error** · "the younger Infante": same. Done.
8. sedí · **weak** · "he was sitting, was seated … sedíe with the final -e lost": here simply 'was (staying)' in
   Valencia, as the unit says; the -í is the imperfect ending beside sedié, nothing "lost". Done.
9. red · **weak** · "netted enclosure … sense of 'cage' taken from the context": Pidal glosses it 'reja, jaula'.
   Done.
10. alçasse · **weak** · "the exact sense … inferred from the context and uncertain": Pidal 'donde se
    escondiese'. Done.
11. __broaden__ dos · **weak** · "the sense of alçasse is uncertain": same. Done.
12. adestrando · **weak** · "sense inferred": Pidal 'lo lleva como de diestro'. Done, 'lead (as a horse) by the
    halter'.
13. enbaídos · **weak** · "the exact sense is inferred from context and uncertain": Pidal 'avergonzados,
    corridos'. Done.
14. raçión · **weak** · "sense from context": Pidal 'no tomen parte en la batalla'. Done.
15. __broaden__ fiera · **weak** · "sense from context": Pidal 'fieramente, mucho'. Done.
16. premió · **weak** · lemma "premir … an old verb with no modern form": the unit's premer (Latin premere) is the
    lemma; Pidal 'bajó la cabeza'. Done.
17. juego · **weak** · "the spectacle, the scene": the Çid forbids it, so it is the jesting at the Infantes'
    expense, as the unit has. Done; __broaden__ tal brought into line ('such sport as').
18. remandrán · **weak** · "syncopated from remaner + an": silent on the d grown between n and r (remanrán >
    remandrán), the point of the form. Done.
19. __broaden__ assí · **weak** · missing: here 'so greatly' (Pidal 2298 'de tal modo, mucho'). Added.
20. __broaden__ sobre · **weak** · missing: here 'around' (Pidal 2285 'alrededor de', comp. 1053). Added.
21. sobrevienta, cuntió · **style** · Pidal's 'mala sorpresa … les aconteció' added; "= aconteció, aconteció a
    ellos" tidied.
22. saliós, desatós · **style** · "he got out / he got himself loose": the subject is the lion. "it".
23. ifant · **style** · "spelt ifant before de Carrión" → ifante with its final -e dropped, restored by Pidal.
24. cuello · **style** · both uses of al cuello (worn 'about the neck', taken 'by the neck', Pidal 2300).
25. oviestes · **style** · "if you ever heard it told" → 'if you have heard tell of him', Pidal 'si oísteis de
    él' (sil = si + le).
26. __broaden__ valençia · **style** · "sat my Cid" → 'was' (as sedí); "Valencia vienen çercar" spelt as printed.
27. __broaden__ fincan · **style** · "over their lord" → 'around' (Pidal).
28. __broaden__ tovieron · **style** · "considered them abashed" → 'held (them) shamed' (Pidal on enbaídos).

Checked and kept: durmie, çercan, gonçalvez, cámara, abierta, torre, metiós, esçaño, viga, lagar, brial,
suzio, çercado, qués, levantó, envergonçó, rostro, liévalo, llamando, responde, color, cinquaenta, búcar,
pérdida, bibdas, osados, desean, idlos, conortar, ayan, vençremos, sonrrisando, tenedes, blancas, desseo,
folgad; __broaden__ de, león, enbraçan, sol, ovo, todo, maravilla, tornáronse, cuer, part, sabidor.
Every __broaden__ (20) is the known-forms entry whole + " · " + the new reading (checked by script). The keys of
gloss.json minus __broaden__ equal novel-forms.json (57). The 199 known forms were checked against this part's
uses; don ('de lo cual'), ya ('O!'), i ('there'), so ('I am'), ha ('has'/'there is'), veyen, alegravas, sabor,
aguisado, a (dative before ifantes), por, sí, vusco, evades already cover them.

Refused:
- brial "no modern word in use": brial survives only as an archaism; harmless. Left.
- envergonçó "he was abashed": the lion; the lemma line is what counts. Left.

Pass 2 counts: error 7 · weak 13 · style 8 (28 items).

## For conventions.md
- mesnadas "household-troops"/"troops" in `l` (kept distinct from escuelas "retinues").
- sí vos vala el Criador: "so may the Creator help you" in `i`.
- Ferrant / Diag Gonçalvez "Fernando / Diego González" in `i` (manuscript forms in `l`); no seniority between
  the Infantes is stated in the poem.
- Búcar "Búcar" in `i`; Quarto "Quarto" (vv. 1711, 2312b).
