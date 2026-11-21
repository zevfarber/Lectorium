# Review — cid-tiradas-102-102 (tirada 102, vv. 1885–1958)

Checked against the pinned packet, Pidal 1923 PDF pp. 252–256 (printed 248–252: text, footnotes, rubric; vv. 1910,
1939 and 1953 cropped and enlarged), the published parts (house renderings: amor "favour", ondra "honour", Ruy Díaz,
the Infantes of Carrión, the *en buen ora* formula), `conventions.md` and `cid-glossary.json`. Pidal's *vocabulario*
is not under `source/`.
`t` integrity: all `t` joined = the 79 packet verses in order (1899b and 1937b–e included), before and after the
edits; no `t` touched; every `l` has one line per verse. The rubric (fold of Pidal's four sentences) and the assonance
(ó; á-a for 103) agree with Pidal. All edits were made by script (json load/modify/dump, indent 1, ensure_ascii=False).

## Pass 1 — units.json

1. Unit 9 (vv. 1914–15) · l · **weak** · "They-took-leave" rendered espidien (an imperfect in -ie, which the note
   itself says) as a preterite. Done: "They-were-taking-leave of-the king". The `i` keeps "took their leave", the
   epic tense-mixing given in English.
2. Unit 8 (vv. 1910–13) · n · **weak** · the note said the extent of the italics in [naçió] was hard to make out.
   An enlarged crop shows the whole word in italics: italic n and single-storey a, against the roman *ora* beside
   it. Done: the hedge is replaced by that observation, and the bracketing is confirmed.
3. Unit 17 (vv. 1937e–39) · n · **weak** · "çasamiento … the reading is uncertain": the cedilla is plain on the
   enlarged scan, so the print is not in doubt. Only the spelling is odd. Done: "so printed: the cedilla is clear on
   the scan, though the word is casamiento at vv. 1892 and 1937c; kept as Pidal prints it."
4. Unit 22 (vv. 1953–55) · n · **style** · queramos "not quite certain": the final s is broken but visible on the
   crop, and the 1st pl. is needed (nos). Done: "the final s is broken on the scan but there, and the sense needs it."
5. Unit 0 (vv. 1885–88) · l + n · **style** · "as of king and of lord" renders a as 'of'. Done: l "as to king and to
   lord"; the note says "'as (one asks) of king and lord'".
6. Unit 13 (vv. 1926–30) · l · **style** · "that-him he-recognized": le is dative. Done: "that-for-him".
7. Unit 19 (vv. 1943–46) · n · **style** · vernié "the old form without the d" did not explain the form. Done:
   "venir + ie with n and r changing places (venrié > vernié), where modern Spanish puts in a d."

Drafter's points, judged and left as drafted:
- 1929 subject of connosçie: the king is the subject ("the king saw honour in it for him"), and quel = que le
  (dative, the Çid), in parallel with abrá y ondra of v. 1905. creç[r]ié then has the Çid as its subject. The
  reading is sound, and the note correctly marks it as ours. Kept.
- 1934 [h]e: Pidal italicises the h (confirmed). he + tollida agreeing with la onor is the resultative 'I have
  (had) my estate taken'. The note explains it and the alternative e 'and'. Kept.
- onor vs ondra (1905, 1929, 1934): the distinction holds throughout: ondra is "honour" (as in 84-86 and 96-101),
  onor is l "estate" and i "lands and lordship". It is consistent in all three verses. Kept, and proposed as a
  house rendering.
- vistas "meeting": consistent in l and i, with the note's "plural in form, one meeting in sense". Kept.
- conssagrar 1906: Pidal's footnote is quoted exactly (with v. 3356), and "for consagrar" follows his "por". Kept.
- 1899b viniéssem: Pidal's footnote 'venga a vistas conmigo, si gusta' supports viniesse + me, a wish. Kept.
- 1937b–e restoration note: checked against footnote 1937b (pp. 254–255): nephews, Jimena, v. 2188, Hinojosa,
  v. 2606, Primera Crónica General are all correct. "His footnote calls the first 1937b; the letters c–e are ours"
  is right: no margin number is printed on the italic lines. Kept.

Confirmed and unchanged: all Pidal footnotes quoted or paraphrased (1888 p. 91; 1889; 1892; 1893 → v. 1926; 1899b;
1906; 1912 → vv. 1962, 1951; 1913 → v. 1388; 1919 → v. 204; 1921 → v. 928; 1922 → v. 3216; 1937b; 1938 Corominas
1900, charters 1090/1105; 1942; 1944; 1951). The two hundred horses as el don (96-101). Every bracketed italic in
`l`/notes (Vermu[doz], [Roi Díaz], el[le], Di[da]go, Se[e]d, R[o]y, f[o]re, su[e]s, creç[r]ié, [amor], ve[e]r,
ir[i]emos, [e señor], [mayor], se[e]lló) matches the scan.

Refused / left as drafted:
- Unit 15 `i` "the king's favour again": "again" is not in the line, but it is implied by the exile and the pardon.
  It is harmless, so I left it.
- Unit 2 `l` "to-the good Campeador" for al (personal a): this is literal, and earlier parts do the same. Left.
- Bracket placement inside `l` (h[e], hi[s], he-would-gro[w]) approximates the restored letters, which is house
  practice. Left.
- Unit 5 (v. 1900) mandados "messages": this fits, so no change.

## Pass 2 — gloss.json

Rewritten entries:
1. espidiensse · **error** · "preterite 3rd pl. espidieron + se, -onse > -ensse" is not an Old Spanish development.
   It is the imperfect espidien (-ien = -ían) + se, as units.json says. Done: "= se despedían".
2. connosçie · **error** · "imperfect/conditional … = conocería": -ie without r is the imperfect only. Done:
   imperfect 3rd sg., 'recognized, acknowledged', "= conocía, reconocía". The sense now matches the unit.
3. viniéssem · **error** · "the e lost before the clitic": in fact the e of me is lost (viniesse-me > viniéssem), and
   "he might come" missed the wish. The meta-hedge "reading of the enclitic rather than a 1st-pl. form" is dropped,
   and Pidal's 'venga a vistas conmigo' is cited.
4. creçrá · **error** · "grow in honor" contradicted the unit's onor 'estate, lordship'. Done: "grow in estate and
   lordship"; "syncopated" replaced by "with the e dropped".
5. onor · **weak** · led with "honor, dignity", which blurs the ondra/onor distinction the units draw. Done: "estate,
   lordship: the lands and rank held of a lord (fem.)", "distinct from ondra 'honour'".
6. demandedes · **weak** · "'that you ask us for daughters'" reversed the role of nos (dative of interest, 'for us').
   Done; "= demandéis, pidáis".
7. comidió · **weak** · "= comedió" is not a modern form (modern comedir also has comidió). Done: "= meditó", with
   Pidal's 'pensó y meditó'.
8. conssagrar · **weak** · "the sense is the editor's gloss and uncertain" is a false hedge, because Pidal's footnote
   is explicit. Done: Pidal quoted, and "by becoming kin".
9. didago · **weak** · "elder of the two infantes" is not in the text or in Pidal. Dropped.
10. dixiere · **style** · the example "do ell dixiere" misquotes the text (el[le] → elle). Fixed.
11. conpieçan · **style** · "= empiezan" → "= comienzan, empiezan". An example was added.
12. natura · **style** · a needless hedge ("not certain") was dropped.
13. vernié · **style** · "syncopated" → metathesis venrié > vernié.
14. pidimos · **style** · an example was added.

The existing `__broaden__` entry casar (old entry whole + " · " + active 'to marry', casar queremos con ellas) is
correct against known-forms.json. Kept.

Broadens added, each because the current glossary entry does not cover the use here:
15. penssó · **error** · the entry gave only 'set about' (pensar de + inf.), but here it means 'he thought' (penssó e
    comidió).
16. rogar · **error** · the entry gave only 'to pray', but here it means 'to ask, beg' (rogar gelo emos).
17. rogava · **error** · the entry gave only 'he prayed', but here it means 'he was asking' (lo quel rogava).
18. andar · **error** · the entry gave only 'to travel, go on', but here andar a alguien means 'stand by, help' (Pidal
    'quiero ayudar al Cid').
19. amor · **weak** · the entry gave 'love', but here it means a lord's favour (davos su amor; del rey he su amor),
    the house rendering "favour".
20. conssejo · **weak** · the entry gave 'help, remedy' and 'council', but here it means 'counsel, advice'.
21. tornados · **weak** · the entry was transitive only ('put back'), but here it is intransitive (tornados son).
22. agua · **weak** · the entry gave 'water', but here it means 'river' (una agua mayor).
23. ora · **weak** · added una grant ora 'a long while' (Pidal 'un gran rato').
24. sis · **style** · the entry was tied to "if … themselves". Added si 'whether' + se (non sé sis abrá sabor).

Coverage: all 65 tokens in novel-forms.json have an entry. The keys are exactly those of novel-forms.json plus
`__broaden__` (11 entries), and every broaden starts with the known entry copied whole. No invented lemmas remain.

Refused:
- pidimos as present (not preterite): the context needs the present, and the raised i is acceptable. Kept.
- fu under seer, and reçibió under reçebir: these are house lemma practice. Kept.
- varones 'man, male', mandados 'message', queramos (example que nos queramos ir), sobre (hard by): the existing
  entries cover the use well enough. No broaden added.

## Readings left flagged uncertain
- v. 1929 quel connosçie i ondra: the king as subject and le = the Çid is our reading (noted in unit 13).
- (Resolved by this review: [naçió] 1910, çasamiento 1939, and queramos 1953 are now confirmed on the scan.)

## Suggested house renderings to record
- onor "estate" in `l`, "lands and lordship" in `i` (fem., la onor), kept distinct from ondra "honour" (vv. 1905,
  1929, 1934).
- vistas "meeting" in `l` and `i` (a royal interview; plural form, one meeting).
- amor of a lord to a vassal: "favour" in `i` (already used in 78-82; vv. 1924, 1936, 1945).
- Roi Díaz / Roy Díaz: "Ruy Díaz" in `i`.
- una grant (grand) ora: "for a long while" (vv. 1889, 1932; Pidal 'un gran rato').
