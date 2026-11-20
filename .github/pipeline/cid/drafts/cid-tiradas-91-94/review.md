# Review — cid-tiradas-91-94 (tiradas 91–94, lines 1657–1710 with 1666b and 1690b; 1689 printed before 1688)

Adversarial review against the pinned packet, the scan (PDF pp. 239–242 at 150 dpi; lines 1689 and 1701–1702
cropped at 300 dpi), conventions.md, the pilot (01-04), the published parts (01-04, 10-14, 84-86 for the en buen
ora formula and its `l`; 18-18 for v. 324; 19-23 and 35-39 for Álbar Salvadórez; 32-34 for v. 710; 64-68 for
vv. 1137–39; 78-82 to 87-90 for Don Jerome, Ruy Díaz, Ximena, the tents of vv. 1630/1644) and known-forms.json.
All edits by script (json load/dump, ensure_ascii=False, indent=1). No `t` changed: the 56 `t` lines joined with
"\n" equal the packet's 56 verses in print order (1689 before 1688), checked by script before and after the
edits; one `l` line per `t` line in all 20 units; every one of the 59 novel forms has a non-empty gloss, and all
252 reader tokens are covered by known-forms or novel-forms.

## Pass 1 — units.json

Counts: error 4 · weak 6 · style 5 (15 changes)

| unit (index / first line) | field | sev. | what was wrong | what was done |
|---|---|---|---|---|
| 2 / 1663 Prisos | n | error | "pro … (masculine here, vuestra pro)": vuestra is feminine | "feminine here" |
| 7 / 1676 Dos fallan | n, l | error | "cometiénlos = acométenlos, 'they attack them', imperfect in -ién": equates the imperfect with a present; l "attack-them" present | note "= los acometían, 'they were attacking them', imperfect in -ién of cometer (= acometer)"; l "they-were-attacking-them" |
| 11 / 1689 el obispo | i | error | "he will say mass for us, and then set about riding out": makes the bishop the subject of penssad, a 2nd-pl. imperative to the knights | "and then you are to make ready to ride" |
| 0 / 1657 Fincadas | n | error | "the Moroccan camp of v. 1642": v. 1642 is about moradas; the tents are pitched at v. 1630 and seen at v. 1644 | "vv. 1630 and 1644" |
| 1 / 1660 Miedo | n | weak | (flagged) Miedo a su mugier read as 'fear has his wife', fear the subject: aver miedo is the idiom (non ayades miedo, v. 1664, four lines on); quiérel's subject (el coraçón) not stated | reading 'his wife has fear', object first; the prepositional reading (parallel a las dueñas) kept as alternative, no Pidal note; quiérel: el coraçón subject, le dative 'her' |
| 4 / 1668 colgar | n | weak | (flagged) Vocaçión "Latin vocatio in its church sense of a promise made to a saint": no such Latin sense | "most likely 'a vow, a votive offering' (from Latin vocatio, 'a calling')"; rare, no Pidal note, not certain — hedge kept |
| 7 / 1676 | l, i, n | weak | (flagged) Pidal's footnote: Dos fallan 'cuando se encuentran' — 'when'; the unit rendered 'Where' | l "When-they find-themselves", i "When they come upon the Moors", note: do 'where', here 'when' as Pidal glosses |
| 10 / 1685 Oídme | n | weak | prieta stated flat as 'dark'; the adjective's own sense is not given by Pidal (only the phrase 'cerca del amanecer') | 'dark' as the likelier, 'close, tight' possible, the phrase's sense settled by Pidal |
| — | titleEn, part | weak | "Jimena reassured": house form in `i` and titles of published parts is Ximena (83a, 84-86, 87-90; LOG) | "Ximena reassured" in both (parts.json "name" still has Jimena — left for the publisher) |
| 18 / 1706 A vos Çid | i | weak | (flagged) "who in a good hour girded on your sword": relative clause not in the text; house rendering is "in a good hour you girded on your sword" (pilot v. 41, 10-14 v. 175) | "To you, Çid Don Rodrigo — in a good hour you girded on your sword — I have sung the mass this morning" |
| 18 / 1706 | l | style | "in good[-one] you-girded sword" | "in good[-hour] you-girded sword" (84-86 v. 1560) |
| 18 / 1708 | n | style | "dona, 'gift' (Latin dona)": dona is the Latin plural | "Latin dona, plural of donum, taken as a feminine singular" |
| 5 / 1671 | l | style | e[ntr]an as "th[ey-ent]er": the bracket swallows the pronoun | "they-[ent]er" |
| 6 / 1673 | l | style | Vi[d]olo as "Saw-it", Pidal's d unmarked (vi[di]eran in u1 is marked "s[e]en") | "Sa[w]-it" |
| 14 / 1696 | n | style | quoted "del otra parte"; the text has part | "del otra part" |

Checked and found sound (no change):
- Scan: rubrics of 91 ("El Cid esfuerza a su mujer y a sus hijas. — Los moros invaden la huerta de Valencia"),
  92 ("Espolonada de los cristianos"), 93 ("Plan de batalla"), 94 ("El Cid concede al obispo las primeras
  heridas") as the notes give them. Margin labels 1660, 1665, 1666b, 1670, 1675, 1680, 1685, 1689, 1688, 1690,
  1690b, 1695, 1700, 1705, 1710.
- Footnotes, wording and numbers right: 1666b (tambores desconocidos de los cristianos, p. 107; comp. p. 85),
  1671 (a vigor 'con presteza', 2589, 3583), 1673 (tocó la campana para avisar a la ciudad), 1676, 1681 (p. 83),
  1685 (véase 710), 1687, 1689 (soltura 'absolución' de pecados, v. 1703), 1695 (v. 1461), 1701 (v. 324),
  1705 (Turpin, Roland 1132, Girard de Vienne, Bello II p. 266), 1709 (p. 98). No false "no note" claim.
- Italics on the scan match `t` and notes: [cr]ebar, vi[di]eran, a[l], [abremos a ganar], sse[e]r, Jero[me]
  ×3, e[ntr]an, Vi[d]olo, [Roy Díaz] (whole name italic), piénssan[se de tornar], [non passará por al],
  f[ór]edes, buen[a], un[a] don[a], presentad[a].
- 1689 "do Jero[me]": "do" printed (300 dpi), not "don"; l "do(n)" and the note's "do = don, so printed" are right.
- 1701: the full stop after mañana is printed (300 dpi); the note says so and the i runs on. Right.
- 1702 cantava, 1703 dava: imperfects, tense-mixing — labels right.
- 1694 "a mí mandedes al": no Pidal note; 'give me another charge' kept as the likelier reading, hedge kept.
- Assonances: 91 ó (with ó-e), 92 í-a, 93 á (with á-e: seades, Yague), 94 á-a; word lists right.
- Cross-references: vv. 443, 710, 1138, 1139, 1460, 1461, 1615, 1647, 1703, 324 checked.
- House renderings: my Çid; Ruy Díaz for [Roy Díaz]; the bishop Don Jerome; Álvar Salvadórez (Álbar in `l`);
  Minaya; Morocco for Marruecos; Saint James; "It cannot be otherwise" for non rastará por al (as 32-34 v. 709).

Findings refused:
- 1660 l "Fear has his wife": word order kept literally; ambiguous in English as the Old Spanish is, and the
  note now says which is the subject. Kept.
- 1669 i "It was a vow" for es (present): epic tense-mixing; kept.
- 1670 i "glad again": a light addition within the force of perdiendo van el pavor; kept.
- 1691 i "our harvest" for el pan: the Çid's huerta is meant (the note says so); kept.
- 1689 do: whether a slip or a reduced form is not for us to decide; "so printed" is enough.

## Pass 2 — gloss.json

Counts: error 3 · weak 9 · style 5 (17 changes, 1 of them a new broaden)

| entry | sev. | what was wrong | what was done |
|---|---|---|---|
| tanxo | error | lemma "tanxer": invented; tanxo is the strong preterite of tañer | "tañer — … (strong preterite …; = tañó)" |
| vigor | error | a vigor 'vigorously, with force' against Pidal's 'con presteza' and the unit | 'swiftly', Pidal's gloss quoted |
| __broaden__ salido | error | el día es salido 'the day has come up': the unit (and the line: night has come in) reads 'the day has gone' | 'gone out, ended'; = ha salido, ha pasado |
| cometiénlos | weak | (flagged) false hedge "tense somewhat uncertain, possibly a present": -ién is the imperfect | hedge removed; = los acometían |
| prieta | weak | (flagged) 'tight, close, pressing' as the sense, against the unit's 'dark' | 'dark' first, 'close, tight' possible, Pidal's 'cerca del amanecer' |
| vocaçión | weak | (flagged) aligned with the revised note | 'vow, votive offering', from vocatio 'a calling', not certain |
| ffazie | weak | (flagged) false hedge on the construction; doubled ff not explained | 'so it did to the ladies', ff a spelling only |
| préndol | weak | gloss 'I take his sins upon me' against its own 'I take from him' and the unit; "= le prendo" not modern | 'I take his sins from him', I absolve him; = le quito |
| quiérel | weak | "= le quiere reventar"; 'for/in her' | dative 'her'; querer + inf. 'about to'; = se le quiere quebrar |
| __broaden__ santa, maría | weak | (flagged) "probably … somewhat uncertain": the drums are to go to Don Jerome, bishop of Valencia; unit states it | hedge removed, Valencia's cathedral, Jerome's see |
| __broaden__ al | weak | mandedes al "i.e. as you will": not the unit's reading | 'order me something else', give me another charge (likelier reading) |
| __broaden__ dos (new) | weak | known dos is only 'two'; Dos fallan (= do se, Pidal 'cuando se encuentran') uncovered | old entry whole + do + se 'when/where … (they)' |
| sultura | style | (flagged) "perhaps a scribal slip": speculation; Pidal prints it and cross-refers 1689↔1703 without comment. The key does occur (v. 1703) and stays; soltura (v. 1689) has its own entry | "variant spelling of soltura, as printed" |
| soltura | style | Pidal's gloss absent; "Latin solutio" | from soltar; Pidal 'absolución de pecados' |
| sseer | style | quoted "an a sser" | "an a sse[e]r" |
| adobasse | style | r → s assimilation not said | added |
| dona, seam | style | Latin dona unexplained; "= séame" alone | plural of donum; "= séame, me sea" |

Checked and found sound (no change): the remaining 45 novel entries and 12 of the 16 broadens (coraçón,
guisa, abremos, se, mejor, do, ir, vale, valdrá, cara, fóredes, voluntad), each starting with the known
entry whole. Every modern equivalent is real Spanish.

Findings refused:
- sultura: the brief suggested it might not occur; it does (v. 1703, "grant sultura les dava"), so the key is kept.
- nasquieran, vidieran "= habían nacido / habían visto": right for the -ra pluperfect; kept.
