# Review — cid-tiradas-32-34 (tiradas 32–34, lines 623–714)

Adversarial review against the pinned packet, Pidal's rubrics and footnotes on the scan (PDF pp. 171–176, read on
the image), conventions.md, the pilot (01-04) and the preceding part (27-31). All edits made by script
(json load/dump, ensure_ascii=False, indent=1). No `t` changed: the 92 `t` lines concatenated equal the
packet's 92 lines exactly (checked by script after the edits); one `l` line per `t` line in every unit.

## Pass 1 — units.json

Counts: error 0 · weak 4 · style 6 (10 changes)

| unit (first words) | field | sev. | what was wrong | what was done |
|---|---|---|---|---|
| 636 Quando lo o[d]ió | n | weak | Pidal's footnote hedges ("no creo perteneciesen nunca a Valencia, sino al rey Al-Mostain de Zaragoza, como dice la Historia latina"); the note stated as fact "in any case the lands of Calatayud belonged to the king of Zaragoza" | "he adds that he does not believe the lands of Calatayud ever belonged to Valencia, but to the king of Zaragoza, Al-Mostain, as the Latin Historia Roderici has it" |
| 652 Por todas essas tierras | l, n | weak | `l` "the proclamations they-give": Pidal's footnote takes pregones as the criers ('despachan pregoneros', "en el sentido del lat. praeconem"); `l` and the note's own gloss pulled two ways | `l` "the criers they-give"; note says pregones are the criers themselves, per Pidal |
| 679 Todos los moros | n | weak | "poridad … (from puridad)" — backwards: poridad is the old form of puridad | "the old form of puridad, from Latin puritatem" |
| 711 Espolonó el cavallo | n | weak | "metiól = metiólo (metió + le …)" contradicts itself (lo or le?) | "metiól = metió + l, the pronoun le (or lo) cut to l: 'put him', the horse" |
| 658 Las arrobdas | n | style | "mounted pickets (an Arabic word)" attached to Pidal's gloss: "mounted" is not in Pidal and the etymology is not his | "the pickets (the word is of Arabic origin; Pidal's note gives only the sense)" |
| 665 A cabo de tres se[d]manas | n | style | note cites "querie entrar"; the text (and Pidal) has queríe here (querie unaccented is v. 682) | "queríe entrar" |
| 675, 686, 699, 700 | l | style | letter-level brackets with no English counterpart ("na[m]e", "foot[-soldiers]", "pe[n]nons", "The[s]"); 27-31 brackets in `l` only restored words or stems and drops restored letters (se[d]manas "weeks", la[s] "the") — "foot[-soldiers]" even suggests the whole word is restored | "name", "foot-soldiers", "pennons", "The"; [the] (restored word) kept |
| 625 Mucho pesa | i | style | "it was a heavy grief" for present pesando va, in a sentence otherwise in the present | "it is a heavy grief" |
| 667 el agua nos an vedada | n | style | "que nos queramos ir, 'if we wanted to go'" — queramos is present subjunctive | "'if we should want to go'" |
| 685 fablava mio Çid | n | style | "Pidal glosses the half-line" — his gloss ('todos salgamos fuera, que nadie quede') covers the whole line | "glosses the line" |

Checked and found sound (no change):
- Rubrics and assonance in each tirada's first note, checked against the scan: 32 á (El rey de Valencia quiere
  recobrar a Alcocer. — Envía un ejército contra el Cid), 33 á-a (Fáriz y Galve cercan al Cid en Alcocer), 34 á
  (Consejo del Cid con los suyos. — Preparativos secretos. — El Cid sale a batalla campal contra Fáriz y Galve. —
  Pedro Vermúdez hiere los primeros golpes). The á-e line-ends in the á tiradas (plaze, mensaje, partes, grandes,
  Galve, fablastes, raste, cabdales, mande) are each noted. The closing pointer to tirada 35 matches its rubric
  (Los del Cid acometen para socorrer a Pedro Vermúdez).
- Pidal's footnotes reported correctly: 632 ('si no nos das ayuda'), 636 (no king Tamín; Abu Béquer; "el poeta
  fantasea"; Fáriz and Galve fabulous — hedge now restored), 637 (reyes de moros = emirs/caudillos), 644 (the
  route Segorbe–Cella–Calatayud and the Roman road Sagunto–Bilbilis; Cella "antes Celha … con importantes ruinas
  romanas"), 652, 653 ('excesivas de numerosas'), 658, 660 (almofalla, almohalla, almafalla, almahala, mehalla),
  661 (toller el agua, cf. 555), 667 (Primera Crónica prose), 672 (Bello), 675 (non passar por al, cf. 3367, 710),
  678 (far vicarious for ondrar; vos not the subject; Primera Crónica's reading), 684, 685, 688 (rictad), 690
  (arth 'mal arte, engaño'; sin art 'lealmente'), 692 (kissing the hand), 694, 696 (ante = Latin prae), 698
  (two chief banners of Fáriz and Galve; Primera Crónica on the pendones), 704, 710, 713 (falssar).
- Restorations: Ter[rer] ×2, [sabet, pesando va.], R[o]y, o[d]ió, Calatayu[t]h, se[d]manas ×2, no[m]bre,
  pe[d]ones, Vermu[doz] ×3, ar[t]h, [los] pe[n]dones, La[s], se[e]d, me[s]nadas, acorr[a]des all match the
  italics on the image and are said to be Pidal's; the wholly supplied half-line of 626 is called his conjecture.
  Kept as printed and noted: prendend (657), "leal!" without ¡ (706), the damaged n of "non" (685).
- Grammar labels checked one by one: dexara (-ra pluperfect), dizien, ayrólo, ganado a, ferá, levedes and
  detardedes (subjunctive as command), prendétmelo, aduzidmelo, nasco, gelo, toviérongela, tornós, exir nos ha
  (split future), consintrán, creçremos (syncopated futures), lidiáremos / muriéremos / vençiéremos (future
  subjunctive), aver vos lo iedes de far (split conditional), tener la edes (split future), mandar (= mandare),
  sopiesse, iscamos, raste, veriedes, derranche, acorrades, valelde (metathesis): all right.
- House renderings: "born in a good hour" (663); "my Çid" in `i`; Per Vermudoz in `i` (as 27-31); Ruy Díaz of
  Vivar (as the pilot); Ateca, Terrer, Calatayud, Jalón, Alcocer as in 24-31; Minaya kept as Minaya (it is in
  the text) and identified as Álvar Fáñez in the note.
- Nothing bowdlerized; uncertain things said to be uncertain: the half-line 626, Canal (649), virtos (657),
  the referent of la in toviérongela (664).

Findings refused:
- i 701 "with their bare hands" for a manos tomar: idiomatic English for 'capture outright', and the note gives
  the literal sense; left.
- Note 666 "(Pero Vermúdez)" beside Pidal's "Pedro Vermúdez": Pero is the old short form, not wrong; left.
- virtos "from Latin virtus in its late sense 'troops'": hedged in the note ("not certain"), and the Latin
  plural virtutes 'hosts' supports it; left.
- Note 685 on the damaged n of non: a print blemish, but recorded in LOG.md and the reading is argued; left.

## Pass 2 — gloss.json

Counts: error 6 · weak 13 · style 6 (25 changes)

| key | sev. | what was wrong | what was done |
|---|---|---|---|
| canal | error | "the Canal de Navarrés (Valencia) region … the identification is traditional" — invented, and impossible (Cella is in Teruel); Pidal does not explain the name | part of the name of Çelfa (Cella); what Canal refers to is uncertain |
| tamín | error | "the Moorish king of Valencia (an Almoravid-era name …)" presents him as historical; Pidal: no such king existed | "invented by the poet (Pidal …); the name is perhaps Arabic Tamīm" |
| lidiáremos | error | "we shall fight … = lidiaremos": the modern form given is the future indicative, not the subjunctive | "(if) we fight … = lidiemos, archaic lidiáremos" |
| atamores | error | "Arabic atambor" — atambor is the Spanish form, not Arabic | "also atambor, from Arabic, with the article al- assimilated" |
| __broaden__ señas (new) | error | existing entry gives only distributive señas 'one each' (= sendas); in v. 698 dos señas … cabdales are banners — the reader would see the wrong gloss | broadened: "also seña — banner, standard (pl.; …)" |
| __broaden__ l (new) | error | existing entry is only le 'to him'; in v. 650 todo 'l día the l is the article el | broadened: "also 'l = el, the article cut after a vowel" |
| toviérongela | weak | "they held it against them … ge = les … the -n- before the clitics is a spelling of the -ron ending" (the n simply is the ending); disagreed with the units note (ge = le, the Çid) | ge = le, the Çid; la's referent loose — matches the note |
| queramos | weak | "'even if we wish to go'" — que + subjunctive here is a plain condition (units note) | "'if we should want to go'" |
| ondrástesvos | weak | "you have honoured yourselves" — addressed to Minaya alone (polite vos) | "yourself … the polite vos to Minaya alone" |
| iedes | weak | muddled: "'you must do it'", "second element of a split conditional/future of aver"; Pidal's reading absent | conditional ending -iedes split from aver; = os lo habríais de hacer; Pidal's far = ondrar |
| rastará | weak | "'it will not stay back for anything else'" misreads non … por al | "'it shall not be otherwise', Pidal 'no quedará de otro modo'" |
| muriéremos | weak | "we shall die" for a future subjunctive in a si-clause | "(if) we die … = muramos" |
| vençiéremos | weak | "we shall conquer", same fault | "(if) we win … = venzamos" |
| __broaden__ consejo (new) | weak | existing "counsel, advice"; v. 632 is 'help' (Pidal 'si no nos das ayuda') | broadened |
| __broaden__ pregones (new) | weak | existing "proclamation"; Pidal takes pregones in v. 652 as the criers (praeconem) | broadened, matching the corrected `l` |
| __broaden__ ante (new) | weak | existing "before"; v. 696 is causal (Pidal: like Latin prae) | broadened |
| __broaden__ qui (new) | weak | existing only relative 'he who'; v. 699 is interrogative | broadened |
| __broaden__ çerca (new) | weak | existing "near"; v. 664 en çerca is the noun 'siege' | broadened |
| __broaden__ aver (new) | weak | existing entry is only the noun 'wealth'; v. 678 is the infinitive in a split conditional | broadened |
| pedones | style | lemma given as modern peón | lemma pedón (Latin pedonem), = peones |
| arth | style | key-form as lemma, "probably = arte"; Pidal's gloss absent | lemma art; Pidal 'mal arte, engaño' |
| rictad | style | "power" added to Pidal's 'riqueza' | "wealth, riches (Pidal 'riqueza')" |
| yas | style | "probably so" — the analysis is not doubtful | "= ya se" |
| fáriz, galve | style | "a Moorish king" with no word that Pidal calls them fictional (the units note does) | "fictional, says Pidal" (one row for two entries) |
| __broaden__ part, ha, aquel (new) | style | existing entries lack 'side' (v. 635), impersonal 'there are' (v. 698), and the demonstrative adjective (vv. 676, 704, 707) | broadened (one row for three entries) |

Checked: every token in novel-forms.json (137) has an entry; every __broaden__ value (4 drafted, 11 added) begins
with the existing glossary entry exactly, then " · ". The drafted broadens (van, va, mal, la) are right. Other
entries checked against the text and found right in person, number, tense, mood and modern equivalent
(dexara, dizien, ayrólo, ferá, odió, detardedes, levedes, prendétmelo, aduzidmelo, avrá, ixieron, iscamos, raste,
edes, aguijedes, mandar, podrié, derranche, acorrades, valelde, metiól, among the rest). Glossary and notes now
agree on pregones, consejo, toviérongela, Canal, Tamín, Fáriz/Galve, queramos.

Findings refused:
- odió under lemma oír (not odir): consistent with the existing odredes entry; the units note gives odir; left.
- almofalla "encampment, host, army camp (Arabic al-maḥalla)": Pidal gives 'hueste, ejército'; 'camp' is the
  Arabic word's sense and does no harm; left.
- prendétmelo "d assimilated to t": loose (devoicing rather than assimilation), not misleading; left.
- siloca "the river Jiloca (tributary of the Jalón)": a safe identification, Pidal's Salón/Siloca; left.
- dexara "Latin-type -ra form": loose but right (the -ra pluperfect from Latin -(ave)rat); left.
