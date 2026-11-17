# Review — cid-tiradas-49-55 (tiradas 49–55, lines 899–959 incl. 934b, 935b, 935c)

Adversarial review against the pinned packet, Pidal's rubrics and footnotes on the scan (PDF pp. 189–194, read at
200 dpi, with crops at 500–600 dpi for lâ (v. 914), the mark over que (v. 908), d'Alcañiz (v. 936), the stop after
van (v. 943) and lo so … menguar (v. 948)), conventions.md, the pilot (01-04), the published parts 05-09 … 44-48 and
the drafts 40-43 and 44-48. All edits made by script (json load/dump, ensure_ascii=False, indent=1). No `t` changed:
the 64 `t` lines concatenated equal the packet's 64 lines exactly (checked by script after the edits); one `l` line
per `t` line in all 26 units.

## Pass 1 — units.json

Counts: error 0 · weak 6 · style 9 (15 changes)

| unit (first words) | field | sev. | what was wrong | what was done |
|---|---|---|---|---|
| all units | i, n | style | `i` had "my Cid" / "the Cid" (9 times), following the pilot; every published part from 05-09 to 44-48 has "Çid" in `i` (11 of 12 parts) and in the notes' English | "Çid" in `i`, and "the/my Çid" in the notes' English; Pidal's Spanish ('el Cid', rubrics) and the work title left |
| 899 Quiérovos | l, n | style | `l` "in a-good[-one] girded sword": the brackets suggest a restoration that is not there (only the a of buen[a] is Pidal's), and the house `l` for the formula is "in a-good (hour)" (pilot, 10-14, 15-17, 18-18) | `l` "in a-good (hour) girded sword"; note says so |
| 903 Estando allí | n | weak | "The Martín … flowing north into the Ebro below Zaragoza": drafter's geography, no footnote on 904 on the scan | removed; "Pidal gives no note on the river" |
| 903 Estando allí | n | style | lemma "preár" (accent invented) | prear |
| 908 quando vío | i, n | style | "the worthy one": the house rendering of el caboso (v. 226, 10-14) is "the worthy man" | "the worthy man"; note cites v. 226 |
| 926 ¡Dios, cómmo f[o] | i | weak | "bringing them greetings": Pidal's footnote (928) glosses saludes 'noticias de una persona ausente', and the note itself says "more than mere greetings" | "bringing them news of their cousins and brothers" |
| 926 ¡Dios, cómmo f[o] | n | style | compañas 'households, families' stated as fact; no footnote; the known entry has 'company, band of troops' | "'companies, people': here the households and kin left behind … (the sense is ours)"; broaden added in pass 2 |
| 930 Dios, cómmo es alegre | l, i, n | weak | barba vellida as "the beard full-grown" / "the man of the flowing beard" / 'luxuriant, well grown': unsupported (Pidal's footnote gives only 'el Cid', v. 274), and 15-17 (v. 274) has "the beard handsome" / "He of the handsome beard"; glossary vellido 'fair, beautiful' | `l` "the beard handsome", `i` "he of the handsome beard", note 'handsome, fair' (bello) |
| 930 Dios, cómmo es alegre | i, n | weak | "brought him greetings" (same saludes as 928) | "brought him news"; note adds saludes 'news', as v. 928 |
| 930 Dios, cómmo es alegre | n | style | the thousand masses stated without a reference (drafter's fact) — verified in this repo: vowed at v. 225 (10-14, "faga i cantar mill missas", at Santa María of Burgos) and sent with Minaya at v. 822 (40-43, "en Santa María de Burgos quitedes mill missas") | references added |
| 935 Non lo tardó | n | weak | "935b carries Pidal's own number": on the scan neither italic line has a margin number; 935 b occurs only as the head of his footnote | note says so: label 935b from his footnote, 935c ours |
| 936 tierras d'Alcañiz | n | weak | "the town on the Guadalope in lower Aragon": drafter's geography, not in Pidal (his only note on the line is negras) | removed; "Pidal gives no note on the place" |
| 936 tierras d'Alcañiz | i | style | "black and bare": the note (after Pidal, 'yermas, estériles') says the sense is waste, barren | "waste and barren" |
| 943 Con estas ganançias | n | style | "may be a poorly printed comma": at 600 dpi the mark is a round full stop | hedge replaced by the observation |
| 946 Sonrrisós | i | style | "The worthy one" | "The worthy man" (v. 226) |

Checked and found sound (no change):
- Rubrics against the scan: 49 Correrías del Cid desde el Poyo. — Minaya con doscientos castellanos se reúne al Cid;
  50 Alegría de los desterrados al recibir noticias de Castilla; 51 Alegría del Cid. (Serie gemela.); 52 El Cid corre
  tierras de Alcañiz; 53 Escarmiento de los moros; 54 El Cid abandona el Poyo. — Corre tierras amparadas por el Conde
  de Barcelona; 55 Amenazas del conde de Barcelona. Assonances right: 49 á-a, 50 á-o, 51 í-a, 52 á-o, 53 ó-a, 54 á
  (grandes, Fáñez, partes á-e), 55 ó-a.
- Footnotes reported correctly: 901 (frase adverbial 'mientras el mundo dure, siempre', comp. 145), 902 (por carta
  'por escrito'; the failed prophecy; Fuero de Molina, v. 864), 903 (véase nota a 477), 908 (el caboso 'el Cid',
  226), 912 (véase nota a 971), 926 (fonsado 'ejército', comp. 764), 928 (saludes, comp. 1921), 930 (la barba vellida
  'el Cid', 274), 935 b (escollecho, participio dialectal of the Crónica General for escogido), 936 (negras 'yermas,
  estériles', opposed to tierra blanca o de sembradura), 938 ('donde salió allá se tornó', the Poyo), 940 (Monzón,
  pueblo y castillo al SE de Huesca, between it and Balaguer), 942 (fonta 'ultraje', 'daño' en general), 946
  (endurar 'resistir'; the Çid cannot spare his men the march; Fernán González 333), 951 (Alucat = Olocau del Rey,
  15 km W of Morella; 50 and 65 km from Montalbán and Huesa, Teruel), 955 (salido as 981, 'expatriado, desterrado'),
  958 (lands under his protectorate, comp. 964; Alhagib Monzir of Lérida, Berenguer Ramón el fratricida, ps.
  15-16), 959 (fonta 'ultraje, afrenta'). No footnote on 899, 904, 914, 936 (Alcañiz), 948, and the notes now claim
  none.
- Italics on the image: buen[a], [val], se[d]manas (907, 915), vi[d]o, f[o] (926, 933), dexad[o], Hu[o]sca, R[o]y
  (942, 958; Roy roman at 912), F[o]ron, [las], co[m]de; 934b, 935b, 935c wholly italic. d'Alcañiz is roman (crop at
  600 dpi).
- Flagged points: 914 lâ — circumflex confirmed on the scan; la + a(ha) with the participle agreeing, Zaragoza the
  object, hedged in the note (kept). 943 "van." — full stop confirmed, sense runs on (kept). 946 endurar — Pidal's
  'resistir' and his sense are reported; `l` "endure" kept, as in 32-34 ("non lo pudo endurar" → "not it
  could endure"). 948 lo so — lo + so 'what is his', subject of puede menguar, no footnote (kept; gloss
  example corrected to match, pass 2). 899 buen[a] with ora understood — right; `l` aligned with the house form.
  934b/935b/935c — flagged as restorations; numbering now described exactly.
- Grammar labels checked and right: quiérovos, çinxo, priso, asil, preava/metió (tense-mixing), legavan, firme
  mientre, sovo, se tardava, desenparava, metuda lâ, fecho ovo, venido es, sabet, vi[d]o, valo, besóle, gelo, nol,
  visquiéredes, f[o], era llegado, avien, quel, bivades, valedes, nasco, escollechos, va parando/preando, ixo, es
  tornado, temién, tornando se van, plogo, sonrrisós, dezir vos he, qui, penssemos de, dexat, dent, aquessa, ovieron
  a, F[o]ron, son idos, corrié, tóvoslo.

Findings refused:
- 905 / 945 `l` "not it-pleases the Moors", "it-pleased my Çid" omit the a of the dative: readable and as earlier
  parts render plazer a. Left.
- 919 `i` "without delay" for sin falla (filler 'without fail'): the filler sense is in the note; "went to embrace
  him without fail" is not English. Left.
- 946 `l` endurar → "resist" (Pidal's gloss): 32-34 renders the same phrase "not it could endure"; `l` is the
  cognate, the note gives Pidal. Left.
- 955 `l` "treats" for trae: a literal "brings" would mislead; the note explains traer 'to handle'. Left.
- 958 note "(his introduction, pp. 15–16)": Pidal writes "ps. 15-16"; these pages are in his introduction. Left.
- 899 note "the hill above Monreal … (v. 864)": the hill is named at v. 863, Pidal's note is on 864. Left.

## Pass 2 — gloss.json

Counts: error 2 · weak 8 · style 9 (19 changes)

| key | sev. | what was wrong | what was done |
|---|---|---|---|
| preava | error | lemma "preár": invented accent; the Old Spanish lemma (and the glossary's preavan) is prear | prear |
| preando | error | same | prear |
| saludes | weak | 'greeting, regards' only; Pidal (928) 'noticias de una persona ausente' | 'greeting; news of an absent person', Pidal cited; example "bringing them news" |
| fonta | weak | 'shame, disgrace … closest vergüenza': not Pidal's sense ('ultraje, afrenta', 'daño' en general) | 'outrage, affront; harm', both lines as examples; = afrenta, ultraje |
| temién | weak | example 'they feared no shame' | 'they feared no harm' |
| ninguna | weak | example 'no disgrace at all' | 'no harm at all' |
| negras | weak | "i.e. burnt and ravaged": not Pidal's 'yermas, estériles' | 'waste, barren', Pidal cited; = yermas |
| menguar | weak | example "'can diminish what is his'" makes lo so the object; units.json (and the grammar) read it as the subject | "'what is his may dwindle'" |
| __broaden__ so | weak | same | same |
| __broaden__ dent | weak | missing: known dent 'of it, thereof' does not cover 'from there' (v. 952) | broaden added (old entry whole + " · ") |
| sovo | style | "Latin sedui": unverified etymology | removed |
| saragoça | style | "the Moorish kingdom the Cid shields and taxes": interpretive, not general to the form | "seat of a Moorish kingdom" |
| desenparava | style | lemma desemparar; the text and the glossary (desenparada) have desenparar | desenparar |
| metuda | style | example misquoted ("metuda la"), 'having put it' | "metuda lâ en paria 'he has put it under tribute'", agreement with the object |
| assi | style | example "assí era llegado" misquotes the line (printed assi) | example as printed; "printed assi, unaccented" |
| alucat, huesa | style | "name of a mountain pass", "place name in the Cid's raiding area": vague; Pidal identifies both (951) | Olocau del Rey (Castellón); Huesa, Teruel province, not Huesca |
| __broaden__ martín | style | "in Teruel province": not in Pidal | "in Aragon" |
| __broaden__ foron, compañas | style | missing: known foron 'they were' (seer) does not cover 'went' (v. 954); known compañas 'band of troops' does not cover the people left behind (v. 929) | broadens added |
| __broaden__ aquellas, pesando | style | missing: known aquellas ends "here referring back to the chests"; pesando 'grieving' with pesando va 'goes on grieving' does not cover the transitive 'grieves (the men of Monzón)' (v. 940) | broadens added |

Checked: the gloss keys (77, excluding __broaden__) equal the novel-forms.json keys exactly. Every __broaden__ value
(14) begins with the known-forms.json entry exactly, then " · " (checked by script). All 265 tokens of the 64 lines
(brackets stripped, lowercased, split at the apostrophe: d'Alcañiz → d, alcañiz) are covered by known + gloss.
Other entries checked and right in lemma and grammar: quiérovos, pueblo, yente, cristiana, asil, dirán, mucha, río,
nuevas, legavan, conplidas, tardava, trasnochada, allén, pinar, tévar, lâ (hedged), çiñen, asomar, corriendo, valo,
boca, encubre, álvar, llegado, diziéndoles, primos, hermanos, alegría, bivades, valedes, mandadería, tardó,
escollechos, corrida, trasnochando, alcañiz, parando, terçer, ixo, hya, monçon, huosca, alegres, verdad, mora,
dexat, iremos, estonçes, mudó, puerto, alván, aquessa, dias, morar, salido, idos, llegaron, comde, barçilona,
corrié, tóvoslo; broadens val, era, a, mano, corre, mont, trae. No other broaden missing: vellida 'fair', endurar,
cuenta, posada, falla, derredor, ovieron (a + inf. under a), mal (adverb) are covered by the known entries.

Findings refused:
- alcañiz "town in Teruel province": not from Pidal but a plain, true identification of the form. Left.
- escollechos under the lemma escoger: Pidal calls it a dialectal participle used instead of escogido. Left.
- Known sonrrisós is lemmatized sonrreír while sonrrisava is sonrrisar: an old entry, outside this part's brief.
  Left (for the owner).

## Readings left uncertain

- v. 914 lâ: read la + a (= la ha), metuda agreeing with Zaragoza as object; no footnote; whether la is Zaragoza or
  the lands is open. The note and the gloss say so.
- v. 946 non lo pudo endurar: Pidal's 'resistir' and his sense ('could not spare his men the march') are followed;
  what lo refers to is not certain.
- v. 948 lo so puede menguar: lo so 'what is his' as subject; no footnote.
- v. 929 compañas 'households, kin left behind': no footnote; hedged as ours.

## For the owner

- v. 908 que: on the scan (500–600 dpi) a small dark mark stands above the u of que ("qûe"), shaped like a blob
  rather than the clean circumflex of lâ in v. 914. Probably a blemish; the pinned "que" is kept and not reported as a
  defect.
- No defect found in the pinned text: every letter, italic and stop checked in the passages above agrees with the
  scan.
