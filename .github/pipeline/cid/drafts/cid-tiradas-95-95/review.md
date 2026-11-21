# Review — cid-tiradas-95-95 (tirada 95, lines 1711–1798 with 1719-20 and 1782b)

Adversarial review against the pinned packet, the scan (PDF pp. 242–246 at 150 dpi; v. 1794 cropped at 300 dpi),
conventions.md, the pilot (01-04), the published parts (35-39 for Álbar Albar[oz] v. 739; 40-43 for la cofia
fronzida v. 789; 69-74 for Gujera v. 1160; 78-82, 83-83b for coronado; 91-94 for dar salto, rastar, del otra part,
mandadas v. 1710; the en buen ora `l` across 10-14 to 84-86) and known-forms.json / cid-glossary.json.
All edits by script (json load/dump, ensure_ascii=False, indent=1). No `t` changed: the 88 `t` lines joined with
"\n" equal the packet's 88 verses, checked by script before and after the edits; one `l` line per `t` line in all
32 units; every one of the 75 novel forms has a non-empty gloss; all 341 reader tokens are covered by known-forms or
gloss.json; every `__broaden__` value begins with the known entry whole + " · ".

## Pass 1 — units.json

Counts: error 3 · weak 11 · style 18 (32 changes)

| unit (index / first line) | field | sev. | what was wrong | what was done |
|---|---|---|---|---|
| 7 / 1730 Desd' allí | l, n | error | an caçado "they-have hunted", note "the spoil, and the routed Moors, as quarry": Pidal's note on 1731 says caçar is 'coger' in general (captare, captiare), not yet narrowed to hunting | l "they-have taken"; note gives Pidal's gloss (the `i` already had "taken") |
| 12 / 1744 fronzida | i, n | error | i "His face is creased"; note "most likely the marks of the mail hood and helmet … not certain": Pidal's note on 1744 settles it — the coif gathered about the face (as v. 2436, la cofia fronzida v. 789), and desarmado = helmet and almófar taken off to cool the head (cf. 789-90, 2436-37) | i "He comes with his coif gathered about his face, for he had taken off his helmet and mail hood"; note gives Pidal's reading |
| 30 / 1793 El obispo | n | error | "the reading es farto is doubtful": not so — the print reads es farto plainly; the dot between the words (300 dpi) is a blemish, and Pidal has no note | doubt removed; the blemish noted |
| 0 / 1711 Salidos | n | weak | first note gave the part name, not Pidal's printed rubric (there is one, PDF p. 242) | Pidal's rubric in English + Spanish: "Los cristianos salen a batalla.—Derrota de Yúcef. Botín extraordinario.—El Cid saluda a su mujer y sus hijas. Dota a las dueñas de Jimena. Reparto del botín." |
| 0 / 1711 | n | weak | [Quarto] "on the side of Quart (Cuarte) … just which towers is not certain": Pidal's note on 1711 says which — the towers either side of Valencia's gate onto the road to Cuart, Quarto at the fourth milestone | Pidal's note summarized; false hedge removed |
| 3 / 1719-20 Álvar Alvar[oz] | i | weak | "Álvar Álvaroz": the published 35-39 (v. 739) and 19-23 give Álvar Álvarez in `i` | "Álvar Álvarez" |
| 16 / 1754 Rogad | n | weak | besarán vuestras manos "great men will pay you court": Pidal's note: 'tendréis vasallos' (cf. 3450, 2948), they will have more vassals | Pidal's reading given |
| 23 / 1776 Quiérovos | l, i, n | weak | arriados "loose, astray": Pidal's note on 1778 renders 'andan arreados', i.e. with their arreos, harnessed | l "go harnessed"; i "running about in their harness"; note: Pidal's gloss, 'driven' as the other sense, uncertainty kept |
| 24 / 1780 maguer | n | weak | otorgados 'approved, warranted' stated flat: no Pidal note, rare sense | "most likely …; Pidal gives no note; the shade is not certain" |
| 25 / 1783 Tanta tienda | n | weak | obrado 'worked, carved': Pidal's note on 1783 — ornament, inlay, precious stones, silver or gold (cf. 2401, 1786) | 'worked, decorated' + Pidal's note |
| 27 / 1787 mandó | i, n | weak | i "no Christian should take it"; Pidal's note: cristiano 'nadie' (v. 29) | i "no one should take it away"; note gives Pidal (`l` keeps "Christian") |
| 27 / 1787 | n | weak | fita "(fincar, 'to plant')": fita is Latin fictus (figere), not a form of fincar (known entry says fictus); sovisse "of seer" without Pidal's note | fita from fictus; Pidal's note on 1788: 'quedase plantada', dialect form of soviese, from seder (cf. 1820) |
| 28 / 1789 Tal tienda | n | weak | Pidal's note on 1790 ("Olvido posterior del poeta", p. 84) missing: the tent is never sent | added: the gift in the next tirada is two hundred horses (v. 1813), not the tent |
| 31 / 1797 mio Çid | l, i, n | weak | l'a mandado "to-him-has ordered", i "has ordered him the tithe": Pidal's note on 1798 'le ha otorgado el diezmo' (mandar 'grant', as v. 1710 mandadas); i opened with a causal "for" not in the text | l "to-him-has granted"; i "my Çid Don Rodrigo … has granted him the tithe of all his own fifth"; note gives Pidal |
| 0 / 1711 | n | style | acordando without Pidal's note on 1712 | 'previniendo o aleccionando muy bien a sus vasallos' added |
| 3 / 1719-20 | n | style | no cross-reference for Álvar Álvarez | v. 739 added |
| 4 / 1722 | n | style | Pidal's note on 1722 (lance used, broken, then sword; p. 101) not cited | added |
| 4 / 1722 | n | style | destellar "from Latin stilla" | "Latin destillare, from stilla" |
| 5 / 1725 | n | style | Gujera without Pidal's note | 'Cullera', v. 1160 added |
| 7 / 1730 | n | style | preçió "Babieca appraised like a horse at a fair": colour not in the text | removed |
| 7 / 1730 | n | style | a rastado without Pidal's note on 1733 | 'quedar' (ha quedado por suya) added |
| 14 / 1748 | n | style | Pidal's note on 1748 (usual greeting formula, v. 1396) missing | added |
| 15 / 1752 | n | style | Pidal's note on 1753 ('de este modo', 'así') missing | added |
| 16 / 1754 | n | style | diçiendo without Pidal's note on 1756 | 'apeándose', v. 1394 added |
| 19 / 1763 | n | style | Pidal's note on 1765 missing | 'con algunos de aquestos' added |
| 20 / 1766 | n | style | quoted "por espaçio", not the text | "por espacio (so printed, with plain c)" |
| 21 / 1769 | n | style | Pidal's notes on 1769 (thanks for the dowry; 159, 692) and 1771 ('lo han llevado a cabo') missing | both added (2 edits) |
| 22 / 1772 | n | style | Pidal's note on 1773 (Minaya heads the quiñoneros, p. 98) missing | added |
| 24 / 1780 | n | style | maguer de without Pidal | 'a pesar de' added |
| 26 / 1785 | n | style | Pidal's note on 1786 (long tent, elliptical base, two poles) missing | added |
| 30 / 1793 | l, i | style | coronado "crowned-one" / "tonsured cleric": published 78-82, 83-83b have l "tonsured-one", i "churchman" | l "tonsured-one"; i "an accomplished churchman"; note cross-refers vv. 1288, 1460 |

(The two 21 / 1769 edits are counted separately: 18 style.)

Checked and found sound (no change):
- Scan: rubric of tirada 95 as now in the note (PDF p. 242); margin labels 1715, 1719-20, 1725, 1730, 1735, 1740,
  1745, 1750, 1755, 1760, 1765, 1770, 1775, 1780, 1782b, 1785, 1790, 1795. Italics match `t` and notes: [Quarto],
  Alvar[oz], alca[nço], s[o]s ×2, [de], dad[o], Ve[e]des, d[o]ña, f[o] ×2, [ellos], [mucho], [el Campeador contado],
  [h]a, s[u]s, Jero[me], ca[d]ié. Full stop after cabo (1717) and small a (1718) printed, as the note says; gañado's
  broken g; merced (1760), espacio (1768), preciada (1783) with plain c, as the notes say; fuero' with Pidal's apostrophe.
- Footnotes in the range: 1709 (prev. part), 1711, 1712, 1722, 1727, 1731, 1733, 1744, 1748, 1753, 1755, 1756, 1765,
  1769, 1771, 1773, 1778, 1780, 1783, 1786, 1788, 1790, 1798 — all now used. Pidal has NO note on 1717 (a cabo),
  1726 (del sol espada), 1781 (otorgados) or 1794 (farto); the notes claim none.
- Assonance á-o and the line-end list; tense-mixing; split future venir se a; ser + participle of motion; -ie
  imperfects (Reçibienlo, aviedes, avíe, cadié); strong preterites (andido, nasco, plogo, tovo, aduxiestes);
  -sse subjunctives (sovisse, tolliesse, croviesse); enclitics (saliósle, metiósle, muchol, quel, nom, l'a, tomallos).
- House renderings: my Çid; Babieca (Bavieca in `l`); Yúsuf (Yúcef in `l`); Morocco; Álvar Fáñez (Álbar in `l`);
  Don Jerome; en buen ora "he who was born in a good hour" (`l` "he who in good hour was-born", as published).
- Cross-references: dar salto (tirada 92, v. 1673), rastar (v. 1686), alcaz (v. 1680), del otra part (v. 1696),
  v. 1742 ↔ 1772-73, v. 1740 merçed, v. 1774 preçiados, v. 1775 sobejano.

Findings refused:
- 1717 van a cabo: no Pidal note; the hedge ('go along … not certain') is honest and kept.
- 1726 del sol espada: the note already says the construction is uncertain; why del (and not de) precedes sol is
  not explained by Pidal here, and no further claim is added.
- 1714-15 "splendidly fitted with all his gear", 1758 "his wife, a woman of worth": within the force; kept.
- 1725 i "but Yúsuf slipped out": the added "but" only marks the turn of the narrative; kept.
- 1782b "outside the traditional count": a b-number is Pidal's added line; kept.

## Pass 2 — gloss.json

Counts: error 7 · weak 12 · style 7 (26 changes, 4 of them new broadens)

| entry | sev. | what was wrong | what was done |
|---|---|---|---|
| enpleó | error | lemma "empleár": invented form (accent, m) | "enplear … = empleó", Pidal 'usó la lanza' |
| consiguen | error | lemma "consiguir": no such infinitive | "conseguir", old sense 'follow, overtake' (Latin consequi) |
| rastado | error | 'dragged, drawn along … = ha arrastrado … sense inferred': against Pidal's note on 1733 and v. 1686 | rastar 'remained', Pidal 'quedar' (ha quedado por suya) |
| viba | error | "3rd sg. … 'may he keep you'": the unit (and sense) is 'that I may live (for you)' | 1st or 3rd sg.; 'that I may live (for you) some years' |
| atantos | error | "a + tantos … the a marking the direct object": misnamed; atanto is tanto with prefixed a- | "atanto — so many (… not the preposition; = tantos)" |
| diçiendo | error | lemma "diçir": the Old Spanish verb is deçir (descendere); modern equivalent lacked Pidal's | "deçir … Pidal 'apeándose'; = descendiendo, apeándose" |
| __broaden__ sol | error | "sol = Latin solum 'ground, underside', or an error for so 'his'": invented etymology, and not the unit's reading | "so + l, 'under the' (so, Latin sub, + el before a vowel) … likeliest reading; construction uncertain" |
| quarto | weak | "modern Quart de Poblet … identification traditional": not what Pidal says | Pidal's note: fourth milestone on the road toward Castile; towers flanking Valencia's gate onto it |
| saliósle | weak | "it slipped away": the subject is Yúsuf | "he got away from him" |
| caçado | weak | 'hunted down … figurative': against Pidal's 'coger' | 'taken, caught', Pidal's note |
| desarmado | weak | "probably 'bareheaded, coif drawn back', uncertain since he still holds the sword": against Pidal's note | helmet and mail hood off, as Pidal |
| arriados | weak | sense left open between 'harnessed' and 'loose' | aligned with the unit: Pidal's 'arreados', 'in harness' likelier, not certain |
| otorgados | weak | 'allotted to him' against the unit's 'approved' | 'approved, warranted', not certain |
| labrados | weak | 'embroidered': said of tent-poles | 'worked, wrought' |
| __broaden__ cabo | weak | van a cabo (1717) not covered; "sense uncertain" on cabo 'chief' (an established sense) | a cabo with hedge added; false hedge removed |
| __broaden__ acordando (new) | weak | known entry only 'taking counsel' (reflexive); here transitive 'instructing' | old entry + Pidal 'previniendo o aleccionando' |
| __broaden__ fronzida (new) | weak | known entry agrees with cofia; here with cara | old entry + Pidal's reading of fronzida trahe la cara |
| __broaden__ cristiano (new) | weak | known only 'Christian'; here with non 'no one' (Pidal) | old entry + 'nadie' |
| __broaden__ ovieron (new) | weak | known covers ovieron a + inf., not ovieron de arrancarlos | old entry + aver de + inf. |
| alvaroz | style | "restored in brackets by the editor": only -oz is Pidal's | "the -oz restored by Pidal" |
| reçibienlo | style | "read also as 'they welcome him'": an unneeded second reading; -ién stated though printed -ien | removed; "-ien" |
| algunt | style | 'some, a few … algunt año some years': singular | 'some year', a few years |
| quién | style | "the accent here is editorial": all accents are Pidal's; not a fact about the form | removed |
| tendal | style | "modern tendal means 'awning'": beside the point; Pidal's note unused | Pidal's note on tendal obrado |
| sovisse | style | Pidal's note on 1788 unused | dialect form of soviese, from seder; 'quedase plantada' |
| cadié | style | the old form cader not named | "imperfect … of the old form cader" |

Checked and found sound (no change): the remaining 55 novel entries (salidos, guarnizones, adobado, vanlos,
entráronles, arrancarlos, andido, metiósle, palaçiano, alcanço, desd, fuero, notados, escaparon, antellas, omillo,
prez, vençí, sangrienta, sudiento, cum, vençen, entraredes, besarán, descavalgado, buelta, preçiosos, escaños, nom,
aviedes, rogado, aduxiestes, quiérolas, doles, sirvieron, espacio, levantáronse, acabado, escriviendo, contando,
vestidos, preçiados, sobejano, granado, tomallos, cayéronle, preciada, obrado, sufren, tolliesse, croviesse,
riquezas, farto, matados, diezmo) and 8 of the 10 original broadens (preçió, venida, venir, más, ha, qui, tiene,
mata), each starting with the known entry whole. Every modern equivalent is real Spanish.

Findings refused:
- A broaden for mandado ('granted'): the known entry already has "past part. 'granted, assigned'"; not needed.
- guarnizones "armor" vs. "armour": spelling only, the glossary mixes both; left.
- sudiento "no exact modern form": sudoroso is given; left.
- prez "masc./fem.": the gender varies in Old and modern Spanish; left.
