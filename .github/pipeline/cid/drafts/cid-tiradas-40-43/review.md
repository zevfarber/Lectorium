# Review — cid-tiradas-40-43 (tiradas 40–43, lines 778–835b incl. 796b, 800b, 826b, 835b)

Adversarial review against the pinned packet, Pidal's rubrics and footnotes on the scan (PDF pp. 181–185, read on
the image at 200 dpi, with crops at 500 dpi for Roy in v. 784, pode[d]es in v. 830 and commos in v. 791),
conventions.md, the pilot (01-04) and the preceding parts (24-26, 32-34, 35-39). All edits made by script (json
load/dump, ensure_ascii=False, indent=1). No `t` changed: the 62 `t` lines concatenated equal the packet's 62
lines exactly (checked by script after the edits); one `l` line per `t` line in all 24 units.

## Pass 1 — units.json

Counts: error 1 · weak 3 · style 7 (11 changes)

| unit (first words) | field | sev. | what was wrong | what was done |
|---|---|---|---|---|
| 782 Dize Minaya | n | error | "Roy … here printed wholly in roman, whereas at v. 828 Pidal prints R[o]y": false. At 500 dpi the o of Roy in v. 784 is the italic o, the same as in v. 828. The pinned `t` has "Roy" without the bracket (`t` not changed; for the owner) | note says the o is italic on the scan, so Pidal reads R[o]y, and the missing bracket is left for the owner; the matching "(contrast Roy in roman at v. 784)" in the 827 note corrected to "as at v. 784, where the pinned text lacks the bracket" |
| 785 Tantos moros | n, i | weak | sin dubda: the note gave 'without doubt' and, as a "perhaps", 'without holding back'. `i` then went further than both with "without stint". In Old Spanish dubda is 'doubt' and also 'fear' (dubdar 'to fear'; the known glossary entry has 'without fear, or … surely') | note gives both senses and says the line does not decide between them; `i` "without fear" |
| 832 A la tornada | l, n | weak | `l` "go-to-us to-overtake" makes nos a dative of direction. It is the object of conseguir: 'go [and] overtake us' | `l` "go-us to-overtake"; note adds that nos is the object of conseguir and that the d/n swap is the same as daldo (v. 823) |
| 829 ¿Ides vos | n | weak | pode[d]es: "appears to be in italics … the reading is not certain". At 500 dpi the second d is clearly the italic d | "the second d is in italics on the scan (checked at 500 dpi): Pidal's restoration" |
| 778 A Mynaya | n | style | missed that v. 781 repeats v. 501 word for word: the vow Minaya now says he has fulfilled (v. 782, Pidal's note on 498) | adds the echo of v. 501 |
| 785 Tantos moros | n | style | subject of a dexados given as "the Çid, or his host". Minaya, whose kills open the tirada, is just as possible | lists Minaya as well |
| 794 Esta albergada | n | style | averes largos 'riquezas abundantes' given as Pidal's without saying where. The footnote is on v. 804 | "Pidal (on v. 804)" |
| 801 A so castiello | l | style | `l` "To his castle", while the note and `i` take so as 'their' (the Moors' castle) | "To their castle" |
| 810 Oíd, Minaya | n | style | "D'aquesta = de esta" skips the form | "de aquesta, 'of this' (= de esta)" |
| 827 Agora davan | n | style | "Pidal compares v. 836 … with this line": the footnote is on v. 836 ('por la mañana se fué Minaya', comp. 827) | "Pidal, in his note on v. 836 (…), refers back to this line" |
| 834 Por lanças | n | style | a ir nos avremos: did not say what nos goes with | nos belongs with ir (irnos 'to go away'); `i` already right |

Checked and found sound (no change):
- Rubrics against the scan: 40 Minaya ve cumplido su voto. — Botín de la batalla. — El Cid dispone un presente para
  el Rey; 41 El Cid cumple su oferta a la catedral de Burgos; 42 Minaya parte para Castilla; 43 Despedida. The
  assonances are right: 40 á-o; 41 í-a; 42 á-o (a separate tirada in Pidal although the vowels are the same,
  which the note says); 43 í.
- Pidal's footnotes are reported correctly: 782 (the vow, 498), 789 (cofia fruncida, almófar, beard; pp.
  105–106, v. 2059), 792 (Grado; 1118, 1267, 2456; gracias 895, 2095), 794 (albergada, v. 656), 798 (fallar menos,
  1260), 801 (moors put out, v. 679), 804 (averes largos), 805 (recuérdese 796b), 816 (p. 99, Alfonso XI, Salado
  1340, Avignon; the quotation is accurate), 818 (sendas), 820 (he aquí, 253), 821 (uesa, pockets), 822 (paguéis,
  225), 823 (romanecer/remanecer), 825 (visquiero, visco, -o, fallaro 1260), 829 (interrogation, 204), 832 ('si
  nos hallareis aquí, bien; si no…', 181), 836 → 827. Pidal's 772 note (alcaz, citing 786) is cited correctly.
- Flags: 796b, 800b, 826b are in Pidal's margin, and the notes say they are his. 835b is wholly italic on the image,
  "d' aquí" included, and has no number. The note says it is Pidal's restoration, printed plain, and that the
  letter b is ours. 785: the overflow "[dexados" set on the next line is described correctly.
- Italics/brackets checked on the image: [arrancado] (whole word), f[o]ron, robad[o], [que y avién fallado],
  arrancad[o], colga[ndo], [fina], visquier[o], [avie], entrad[o], R[o]y (828), acorda[ndo], pode[d]es; the whole
  of 835b. The one discrepancy (Roy, v. 784) is above.
- Specific points: 791 commos = commo + se (allegarse; ir + gerund). This is right, and on the crop the print is
  plainly "commos". 785: the participle agrees with the object, and the subject is now left open. 827: davan çevada
  'were feeding barley', said of nightfall, is consistent with 19-23 (çevada dar). 832–833: the elliptical
  apodosis follows Pidal's own gloss, and `i` "if you find us here — well" renders it. 835b: aver a + infinitive.
- Grammar labels: l'anda, daquestos, tajador (-dor, one form for both genders), a [arrancado], a dexados, yas,
  nasco, cómmo, son llegados, ffallaron, avién, diessen (impf. subj.), Grant a, Dio a partir, oíd, sodes, prended,
  quiérol, me a ayrado, quitedes (pres. subj. as a command), romaneçiere (fut. subj.), daldo (dadlo), rueguen,
  visquiero (fut. subj. 1st sg.), ides, podedes, vençiemos, falláredes/sopiéredes (fut. subj.), indos, avemos de,
  podriemos (conditional), cuedo, avremos. All right.
- House renderings: "who was born in a good hour" (787, 808); "my Çid", "Çid", "Ruy Díaz" in `i`; Minaya Álvar
  Fáñez in `i`, Mynaya/Álbar as printed in `l`; Castile in `i`, Castiella in `l`; King Alfonso. Nothing
  bowdlerized.
- Uncertain readings are marked as uncertain: the subject of a dexados and the sense of sin dubda. The pode[d]es
  italic is now confirmed and no longer hedged.

Findings refused:
- `i` 834 "we must win our keep" for avemos de guarir: idiomatic, and the note gives the literal 'save ourselves,
  get our living'. Left.
- Note 794 "the encampment of the besiegers spoken of at v. 656": the "besiegers" is the drafter's gloss, not
  Pidal's, but it is true of the camp at v. 656 and is not put in Pidal's mouth. Left.
- `l` 822 "you-pay-for" for the jussive subjunctive quitedes: the note says it is a subjunctive used as a command,
  and the `l` line stays readable. Left.
- 827 "the horses fed at nightfall, ready for an early start": an inference, but Pidal's 836 note supports it. Left.

## Pass 2 — gloss.json

Counts: error 2 · weak 10 · style 12 (24 changes)

| key | sev. | what was wrong | what was done |
|---|---|---|---|
| indos | error | "id + vos … id + vos > indos; = idos": wrong pronoun, and the change cannot happen (vos gives no n). The units note has id + nos | id + nos, d/n transposed (idnos > indos, as dadlo > daldo); nos is the object of the infinitive: indos conseguir 'go and overtake us'; = id a alcanzarnos |
| moriscos | error | "as a noun, the Moors … de los moriscos 'from the Moors'": wrong for this text. The cavallos is understood: 'of the Moorish (horses)' | adjective used without its noun, 'of the Moorish ones', i.e. the Moors' horses |
| daquestos | weak | lemma "aquesto" (that is the neuter) | aqueste, as the existing aquestos entry has it |
| lid | weak | "= lid, now only 'a legal dispute'": false | "now literary, closest batalla, combate" |
| fronzida | weak | "the exact picture is uncertain": Pidal's footnote (789) describes it | Pidal 'fruncida sobre la cara', drawn up about the face |
| tornados | weak | "turned back, driven … 'they have driven the Moors back inside'": the Moors are let back in (Pidal on 801) | 'returned … they have put the Moors back inside' |
| acordando | weak | "'consulting among themselves' … sense uncertain": the Çid takes counsel con los sos, and the sense is not in doubt (cf. tornós a acordar) | 'taking counsel with his men'; hedge dropped |
| sopiéredes | weak | "strong preterite stem sopi-": invented stem | stem sop- of sope, sopo |
| cuedo | weak | lemma cuidar, "= cuido": modern cuido means 'I take care' | lemma cuedar (old cuidar 'to think'); = creo, pienso |
| __broaden__ dio | weak | "dar a + inf. 'to set about' (he set about dividing)": misreads the construction | dar a + inf. 'to give (something) to be …-ed' ('he had this money shared out'); old entry kept whole |
| __broaden__ tornada / recabdo | weak | missing. The known entries give only 'the return charge' and 'care, precaution; business secured', and neither fits a la tornada 'on your return' (832) or non saben recabdo 'past reckoning' (799) | two broadens added, each old entry whole + " · " + the new sense |
| mynaya | style | the parenthesis "(a Minaya Álbar Fáñez; see minaya)" is garbled | spelling of Minaya with y (see minaya) + the title |
| barbado | style | "past-participle adjective": there is no verb; it is formed on barba | adjective from barba |
| commos | style | "how they were gathering" for present van | 'how they come gathering' |
| allegando | style | "= llegar, here 'to assemble'": the wrong modern verb | = allegándose, juntándose |
| albergada | style | Pidal's gloss missing; "= albergada, archaic" | adds Pidal 'campamento'; = campamento |
| ffallaron | style | "ff- is the capital F of the line-opening" stated flatly | ff- a scribal spelling of initial f-, in medieval hands often standing for capital F |
| fallaron | style | Pidal's gloss for fallar menos missing | adds Pidal 'echar de menos' |
| aguisa | style | "= guisar in the old sense" | = dispone, prepara; aguisar obsolete |
| colgando, podedes | style | "restored in brackets by Pidal" ties a general entry to one line | removed |
| guarir | style | example "'we must live by (them)'" | 'we must save ourselves, live'; = guarecerse |
| romaneçiere | style | Pidal's gloss missing; "= remaneciere" | adds Pidal 'quedar, sobrar'; = sobrare |

Checked: the gloss keys (68, excluding __broaden__) equal the novel-forms.json keys exactly. Every __broaden__
value (6) begins with the known-forms.json entry exactly, then " · " (checked by script). The broadens of menos
(fallar menos), si (si non; with the future subjunctive) and guisa (a vuestra guisa) are justified. No other
broaden is missing: the known entries already cover so 'I am', a 'has' with agreement, dubda 'fear', va 'there
is', quando 'since', don 'gift', señas 'one each', partir 'divide', quinta, refechos 'made rich', mandado 'message',
nos reflexive, avemos de, do 'wherever', ayrado. The other entries were checked against the text and found right in
lemma, person, number, tense and mood: mató, tajador, dize, yazen, dexados (agreement with the object), andava,
cuestas, robado, llegados (seer auxiliary), avién, fallado, caen, cient, pagó, encavalgados, quiérol, siellas,
enfrenados, fina, uesa, lleña, mingua, quitedes (pres. subj.), daldo, rueguen, contados, valió, vençiemos,
falláredes (fut. subj., not indicative), conseguir, angosta, bivir, avremos.

Findings refused:
- alegreya "= alegría" with no derivation: nothing is invented, and none is needed. Left.
- quiérol "= le quiero": the modern order lacks the infinitive, but the gloss gives 'I want to send him'. Left.
- avremos "the clitic nos set inside the phrase": loosely put, but not wrong. The units note now says nos goes with
  ir. Left.
- dexados and several others quote the line as an example: this is the house format (cf. fallen, destellando), and
  the meaning given is general to the form. Left.
