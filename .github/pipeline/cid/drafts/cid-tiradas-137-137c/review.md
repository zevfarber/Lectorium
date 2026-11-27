# Review — cid-tiradas-137-137c (vv. 3199–3249 incl. 3211b, 3216b, 3236b, tirada 137, third and last part)

Checked: every unit's `t`/`l`/`i`/`n` (21 units) against the pinned packet and conventions.md; the scan, PDF pp. 321
(rubric), 329–332 (printed 325–328) whole at zoom 1.4, and 254 (note to v. 1922), with clips at zoom 4–12 of v. 3204
*dio* and its footnote, 3206 *mi[o]s* (only the o italic), 3243 *sazón,*, the footnotes to 3211 (*práctica*,
*exigía*), 3215 (*primitivo,* — a comma; *asistían*, *más*), 3222 (*así*, accented), 3226 (*juvizio*), 3232 (*hacia*
and *habia* unaccented, *transmitía* accented), 3240 (*apreçiadura* / *apreciaduras*). Every Pidal footnote quoted in
the notes (3204, 3205, 3211, 3213, 3215, 3216b, 1922, 3218, 3219, 3222, 3224, 3226, 3227, 3232, 3234, 3240, 3241), the
rubric of 137 and that of 138 were compared letter by letter with the print: all exact. Italics of the part seen:
co[m]de 3208, 3211b wholly italic (unnumbered), mi[o]s 3206, t[a]n d[e]sfechos 3233, Ferran[d] Go[n]çál[v]ez
[odredes qué] 3236, lo s[o] 3248 (s roman). Paragraph indents confirmed at 3199, 3207, 3217, 3228, 3236, 3241.
Cross-references checked: v. 3135 (the judges Count Enrique and Count Remond, cid-tiradas-137-137b), v. 3036 (*do
Remond*), the house *veriedes* "you would have seen" (05-09, 35-39, 83-83a, 105-108, 115-117, 118-119), the house
manuscript names kept with brackets in `l` (Vermu[doz], A[n]su[o]r, Gonçál[v]ez in 132–137a).

The `t` fields joined by "\n" equal the packet's 54 verses in order (script); no `t` changed; every `l` has as many lines
as its `t`; both files parse after editing (asserted by the edit scripts).

**Establishment: no error found.** 3243 the mark after *sazón* is a clear comma at zoom 8 (the drafter thought it
damaged). 3206 *mi[o]s*: o italic, m-i-s roman, as pinned. 3204 *dio* printed plain, no accent or circumflex.

## Title

The given name "The Cid claims the dowry money" is changed. The poem says only *averes* / *tres mill marcos en oro e en
plata*; Pidal's rubric calls it *el ajuar*, which the house renders "trousseau" (axuvar, the bride's parents' gift), and
it is not the *arras* (house "dower", the husband's settlement). "Dowry" in English sits between the two and is
easily confused with "dower"; "trousseau" for three thousand marks of gold and silver would mislead. New title, after
Pidal's *Segunda demanda del Cid* and the text's own figure:
- titleEn: "The Song of the Cid — The Cid's second claim: the three thousand marks (tirada 137, lines 3199–3249)"
- part: "Tirada 137 (third part) · The Cid's second claim: the three thousand marks (lines 3199–3249)"
- **Not edited (not mine to edit):** parts.json still has `"name": "The Cid claims the dowry money"` for this part
  (and the packet header repeats it). The build takes titleEn/part from units.json, so the published file carries the
  new title; the owner/orchestrator may wish to update parts.json to match.

## Pass 1: units.json

1. 3202–3204 · n · weak. "dio is first person here (= di)" reduced Pidal's gloss 'di yo' to *di* and lost the pronoun
   his gloss names. Now: "Pidal's 'di yo' makes dio first person, 'I gave' (perhaps di with yo run on), not 'he gave'".
2. 3217–3219 · l · weak. *salien* rendered "go-out" in `l` while the note (rightly) calls it an imperfect among presents.
   `l` now "were-going-out" (`i` keeps the present, smoothing the tense-mixing).
3. 3220–3223 · i · weak. "They come back … and spoke as they pleased" read as a slip in English. Now "and speak as they
   please" (the note explains the present/imperfect pair).
4. 3207–3208 · i · style. "Then you should have seen" → "Here you would have seen": house rendering of *veriedes*
   (six published parts), and *Aquí* kept.
5. 3242–3245 · i · style. "You should have seen" → "You would have seen", same reason.
6. 3224–3227 · i · style. "we do not forbid him it" (awkward) → "we do not forbid it".
7. 3242–3245 · n · style. "The comma after sazón is damaged on the scan" removed: a clear comma at zoom 8.
8. 3242–3245 · n · style. *guarnizón* "hilt, cross-guard and scabbard": more than the word or Pidal says. Now "the
   sword's mounting".
9. 3199–3201 · n · style. Rubric quotation: the damaged last word now said to be read *pago* (drafter's notes said so,
   the note did not).
10. titleEn / part · weak. See **Title** above.

Rulings on the drafter's points:
- **1. Footnote accents** — confirmed: *exigía* (faint but present), *asistían*, *más* (3215), *así* (3222), *hacia*,
  *habia* without, *transmitía* with (3232), *más* (3241).
- **2. recudadas** — confirmed as printed; "a slip" is fair.
- **3. juvizio** — the italic z of this type (cf. *boz* in the note to 3211, same page set) looks like s; quoting
  juvizio is right.
- **4. apreçiadura / apreciaduras** — confirmed: cedilla on the first, none on the second.
- **5. 3211b** — wholly italic, unnumbered, no footnote; *do Remond* as printed. Right.
- **6. dio** — follows Pidal; note sharpened (item 1).
- **7. lo so** — "design" flagged as our reading; kept.
- **8. si** — interrogative si per Pidal's notes to 3216b and 1922 (quotes exact); "if" kept in `l`. Kept.
- **9. scornfully** — flagged as our reading; kept.
- **10. manfestados son** — Infantes as subject follows Pidal's 'reconocieron su deuda'. Kept.
- **11. dentro en la cort** — flagged as our reading; kept.
- **12. Tornárgelos quiero** — right: querer + infinitive, not a split future (the glossary entry, which said "to him",
  now "to them" in context: Pass 2 item 2).
- **13. ge 'from them'** — kept.
- **14. sazón** — "in prime condition, probably" as the glossary; comma not damaged (item 7).
- **15. Sobre** — "over and above" consistent with Pidal's 'descontando los 200 marcos'. Kept.
- **16. enpréstanles** — impersonal "they borrow" flagged; kept.
- **17. jogados** — uncertainty stated, alternative given; kept.
- **18. Title** — changed (see Title).
- **19. Nos … la … aquesta razón** — royal "we", doubled object noted. Kept.

Refused:
- Removing the brackets of Ferran[d] Go[n]çál[v]ez from `l`: the house keeps manuscript names with Pidal's brackets in
  `l` (Vermu[doz], A[n]su[o]r, Gonçál[v]ez, Dí[a]go in 132–137a); only common words go plain.
- Changing 3205 `i` "were carrying out" to a simple preterite: with the absolute gerund the overlap reads naturally.
- Questioning the subject of *manfestados son* (judges?): Pidal's 'cuando reconocieron su deuda' settles it.

## Pass 2: gloss.json

All 37 novel forms have entries; no extra entries (keys = novel-forms.json + `__broaden__`, asserted). Each
`__broaden__` value starts with the old entry whole + " · " (asserted by script); four broadens added.

1. manfestados · error. "declared … (themselves/their view); sense uncertain" ignored Pidal's note to 3224. Now
   'confessed', the active sense with son, Pidal 'cuando hubieron confesado', 'cuando reconocieron su deuda'.
2. tornárgelos · error. "to give back them to him … 'I want to give them back to him'": the ge is the Infantes,
   'to them'. Now 'to him/them' in general, 'to them' in the example; querer + infinitive, not a split future.
3. vedamos · error. "now vetar": modern vedar exists, vetar is 'to veto'. Now = vedamos, prohibimos.
4. assíl · weak. "so he takes pleasure; the le is a dative of interest": wrong sense and misnamed. Now 'so desire takes
   him', Pidal 'así le domina el deseo'.
5. acabaron · weak. "'they did their own part'" not the sense; Pidal 'llevaron a cabo, hicieron' added.
6. essol · weak. "for that reason … to him": the por is a separate token. Now 'that … to him', le cut to l.
7. apreçiadura · weak. "= tasación" (valuation) missed Pidal's 'especie (opuesto a dinero)'. Now 'payment in kind',
   Pidal quoted, = pago en especie.
8. enterguedes · weak. 'hand over' only; Pidal 'reintegren o paguen' added ('pay back'); metathesis stated plainly.
9. sso · style. Gloss limited to 'their'; now 'his, her, their' (general), s doubled after a vowel.
10. espesos · style. The example was given in the wrong order (*los han espesos*); now *espesos los han*, Pidal
    'los han gastado'.
11. recudades · style. "old -ades ending, with elided le before" tidied; Pidal 'respondáis', 'deis satisfacción'.
12. enterguen · style. Pidal 'paguen' added.
13. juvizio · style. Pidal 'juicio' added; 'as a judgement'.
14. quexarse, aduzir · style. "you would see" → "you would have seen" (veriedes, house); aduzir = aducir, traer.
15. recibiólo · style. Lemma *reçebir* → *recibir*, as the glossary's *recibió* and the printed form.
16. tenia · style. "in -ía" for a form printed *tenia*: now "printed without accent".
17. cumple · style. "sense close but not certain" dropped: cumplir 'suffice' is plain.
18. __broaden__ dio · error (added). The known entry gave only 'he gave'; here dio is 1st sg., Pidal 'di yo'.
19. __broaden__ si · weak (added). Interrogative si heading a direct question (Pidal's notes to 3216b and 1922) was
    missing.
20. __broaden__ fincó · weak (added). Known entry had 'planted, stayed'; fincó la boz 'the claim ended' needs 'ended'.
21. __broaden__ gonçálvez · weak (added). The known entry is pinned "here Asur González"; here it is Ferrand
    Gonçálvez, Fernando González: broadened.

Checked and right: ssí, demandasse, otorgo, fablavan, afinca, mandamos, pechar, ferrand, espendiésteslo, damos,
páguenle, préndalo, guarnizón, apreçiaron, pagaron, enpréstanles, ageno, escapan, jogados (uncertainty kept);
__broaden__ razón (old entry whole + " · dar razón de").
Refused: broadening *so* (lo so 'his own' and so 'their' both already there), *gelos* ('from him' dative of separation
covers 'from them'), *sazón*, *conssejo*, *sobre* ('besides' present), *es* (es a fer present), *salien*, *prende*,
*cumple*-family known forms (cumple is novel), *hemos* (the example is only an example).
