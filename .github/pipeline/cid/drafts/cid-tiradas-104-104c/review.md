# Review: cid-tiradas-104-104c (tirada 104, third part, vv. 2068–2126)

Checked against the pinned packet; Pidal 1923, PDF pp. 262–267 (printed 258–263: text, margin labels, the
footnotes 2072, 2073, 2079, 2080, 2083, 2084, 2086, 2087, 2093, 2103, 2104, 2113, 2116, 2121, 2123, 2138, and the
rubrics of tiradas 105, 106 and 107), with 600 dpi crops of v. 2092 (ban), v. 2104 (dó) and v. 2124b
(sírvanvos); PDF p. 96 (printed 92, the introduction's "Valor arqueológico", for the 2086 footnote's "p. 92");
the established texts of earlier parts for every verse cross-reference (253, 255, 269, 371, 1154, 1279, 1360,
1375, 1964, 1965, 1966, 1980, 2029, 2032, 2041, 2055, 2060, 2062); `source/tiradas.json` and the OCR draft of
105–108 for the place of vv. 2127–2130; the published and drafted parts (pilot, 15-17, 40-43, 78-82, 83-83a,
83-83b, 84-86, 91-94, 95-95, 103-104a, 104-104b); `conventions.md`; QUESTIONS.md; and `cid-glossary.json`.
`t` integrity: all `t` joined by "\n" equal the 61 packet verses in print order (2112b and 2124b included, 2116
before 2115), before and after the edits. No `t` was touched, and every `l` has one line per verse. Both files
were edited by script (json load/replace/dump, indent 1, ensure_ascii=False).

## Pass 1: units.json

1. 2125 (vv. 2125–26) · n · **weak** · "Pidal prints vv. 2127–2130 later, inside tirada 107": on the scan (PDF
   p. 267, printed 263) they are the first four lines of tirada 107, straight after its rubric (Muchos del rey se
   van con el Cid a Valencia …), and v. 2156 follows them. Done: "at the head of tirada 107 (after its rubric and
   before v. 2156)". The rest of the closing note is right: v. 2131 opens tirada 105 with the continuation quote
   ”Yo vos pido merçed, assonance á (natural, plaz), and the rubric is quoted exactly.
2. 2097 (vv. 2097–98) · l + n · **weak** · `l` "for veiled-wives" added a word. Done: "for veiled-ones" (the sense
   is in the note and the `i`). The note's account of velar now cites Pidal's own gloss, footnote to v. 2138 (PDF
   p. 266): el velar 'la ceremonia de las velaciones'.
3. 2072 (vv. 2072–74) · n · **weak** · "Pidal's note: escuelas, 'mesnadas' (v. 1360), the household troops, a
   lord's sworn following — not 'schools'" ran our gloss into Pidal's (his note is only 'mesnadas', v. 1360).
   Done: Pidal's words and ours separated; v. 1360 quoted (checked) and the house "my household knights" (78-82)
   named.
4. 2118 · i · **weak** · "Of horses alone my Çid gave away sixty": "alone" is not in the line. Done: "Of the
   horses, my Çid gave sixty as gifts."
5. 2123 (vv. 2123–24b) · n · **weak** · "compare v. 253, where the form is Evades": v. 253 has evades, lower case
   (checked). Done: "(compare evades aquí, v. 253)".
6. 2068 (vv. 2068–69) · i · **style** · "Bishop Jerome": every earlier part has "Don Jerome" (78-82, 83-83b,
   84-86, 91-94, 95-95, 103-104a). Done: "Bishop Don Jerome".
7. 2082 (vv. 2082–85) · n · **style** · "both at the opening of the poem's action, on going to Valencia, and
   now": three moments after "both" (Pidal: tanto al empezar … como al ir a Valencia y ahora al desposarse). Done:
   "at the opening of the poem's action, on the journey to Valencia, and now at their betrothal".
8. 2103 (vv. 2103–04) · n · **style** · "bodas, 'wedding' (always plural)": an unverified universal. Done:
   "(plural, as in modern bodas)".
9. 2099 (vv. 2099–2100) · n · **style** · amor: the drafter's "good will" is kept and the house "favour" refused
   here: the house rendering is for a lord's amor to his vassal (102-102, 104-104b); con vuestro amor is the
   vassal's assent to the king's act, and "with your favour" would turn the relation round. Done: the note says so
   in one clause.

Points the brief asked to weigh, judged:
- dándoslas (2081): dad + nos + las with -dn- > -nd- (dadnos > dandos), the ordinary Old Castilian metathesis of
  the imperative + nos/vos. Right, and stated without hedging. Kept; the gloss is aligned (Pass 2).
- Semejam (2077): semeja + m(e), the pronoun's vowel lost, as quem. The unit is right; the gloss was not (Pass 2).
- por veladas (2098): 'as veiled (wives)', the nuptial veiling; see item 2.
- camearon las espadas (2093): Pidal's footnote (PDF pp. 263–264: in sign of kinship; arms as a pledge of
  friendship; Edmund and Cnut at Olney exchanged clothing and arms) is quoted accurately. Kept.
- escuelas (2072): see item 3; `l` "the retinues", `i` "my household knights", consistent with 78-82.
- 2116/2115: the margin labels 2116, 2115, 2117 stand in that order on PDF p. 265; the note states it. Kept.
- 2112b: the margin label "2112b" is printed (PDF p. 264). The note's "numbered 2112b in the print" is right.
- 2124b: the line is wholly italic, printed with no margin label between 2124 and the labelled 2125 (its last
  syllable, ñor.”, is carried to the right of v. 2125's line with "["). The letter b is ours, and the note says
  so. Kept.
- First note: the rubric fragment matches the tirada 104 rubric (checked at 103-104a) and the assonance claim is
  right. Kept.

Confirmed and unchanged: every Pidal footnote cited (2072 escuelas 'mesnadas', v. 1360; 2073 cometer 'proponer',
acometer 1375; 2079 'De una y otra parte', v. 1965; 2080 rogador, comp. 2088, 2097-99, 2132-37; 2083 de días
pequeñas / chicos 269, niñas 255, 371, 1569, iffantes 1279, comp. nota 2703; 2084 nuevas 'renombre, fama', 1154,
2683; 2086 p. 92 (the page is in the introduction, on the infanzones and the Carrión marriages); 2087 'tanto yo
como ellas estamos a vuestro mandar'; 2093; 2103 ayuda de costa, Ruy Velázquez, Garci Fernández, quoted exactly;
2104 metan 'empleen, gasten'; 2113 'entonces hizo cosa señalada', Bello, Hinard (Adam, Huntington, Bertoni);
2116 d'alfaya 'de valor'; 2121 'los tomó de la mano'; 2123 Evad aquí 'he aquí', comp. 253); no footnote on
[los omenajes dados son], salie[sse] or 2124b, as the notes say; the italics Jero[me], cue[m]des, [los omenajes
dados son], salie[sse], de[vos], and the whole of 2124b; don Elvira (not doña) at 2075, 2088, 2097; Oidme and
otro dia and galardon unaccented; the rubric of tirada 105 quoted in the last note and in the note to 2108. All
other `l` lines checked word for word against `t`; grammar labels (abría conditional, dedes / ayades / vayan /
plega present subjunctive, quisiéredes / fueren / ploguiere future subjunctive, fet imperative, saliesse /
tornasse imperfect subjunctive, criásteslas, gelos/gelas, mándovoslo, afellas/afellos, metiólos, dólas) correct.

Refused / left as drafted:
- 2081 `l` "so you may-help the Creator": ambiguous in isolation, but it is the house `l` for si vos vala el
  Criador (83-83a), and the note and `i` give the sense. Left.
- 2124b `i` "honour you as their lord" for guárdenvos: a fair rendering of guardar 'observe, keep faith with' a
  lord; the note gives the literal sense. Left (the gloss is aligned to the note).
- 2072 `i` "lesser nobles" for ifançones: first occurrence; Pidal's introduction p. 92 sets the ifanzones below
  the ricos omnes, which supports it. Left.
- 2075 `i` "Doña Elvira" for printed don Elvira: the note says the print has don. Left.

Readings left uncertain (each said so in its note):
- 2092 ban: at 600 dpi the first letter has a full ascender as tall as the b of besar, with the bowl broken; at
  200 dpi it can look like t. Read b (van either way).
- 2104 dó: a mark rises between d and o; read as an accent on dó, an apostrophe (d'o) not excluded.
- 2124b sírvanvos: the accent on the italic í is small but present at 600 dpi.

Pass 1 counts: error 0 · weak 5 · style 4 (9 items).

## Pass 2: gloss.json

1. oidme · **error** · "spelt without the d": the d is there (Oidme); what is missing is the accent. Done.
2. camearon · **error** · "the sense of the gesture is uncertain" ignored Pidal's footnote. Done: Pidal
   'cambiaron las espadas', in sign of kinship, arms as a pledge of friendship.
3. __broaden__ ruego · **error** · the glossary has only rogar 'I pray' (verb); here un ruego is a noun, 'a
   request'. Done: broadening added.
4. semejam · **weak** · "the final vowel and m run together": semeja keeps its vowel; me loses its own. Done:
   "semeja + enclitic me reduced to -m, as in quem".
5. aquís · **weak** · "thereupon he set himself to the business" matched neither the unit nor Pidal. Done: Pidal
   'entonces hizo cosa señalada'.
6. dándoslas · **weak** · "probably … uncertain: the transposition is inferred": the metathesis is regular. Done:
   the hedge removed, the analysis as in the unit.
7. aquén · **weak** · "the form is uncertain": it is plainly printed and well attested. Done: hedge removed;
   "the opposite of allén" added, as in the unit.
8. guárdenvos · **weak** · "let them protect you" did not match the unit's note. Done: 'watch over you, keep faith
   with you'.
9. elvira · **weak** · "the Cid's elder daughter": nothing here says which is elder. Done: "one of the Cid's two
   daughters (doña Elvira, also printed don Elvira)".
10. rogadores · **weak** · the generic 'intercessor, pleader' missed the marriage office. Done: Pidal's account of
    the rogador added.
11. __broaden__ prender · **weak** · the entry has only 'seize, arrest'; prender so don is 'take his gift'. Added.
12. __broaden__ si · **weak** · si vos vala el Criador is the optative 'so' (the glossary has it under sí only).
    Added.
13. __broaden__ amor · **weak** · con vuestro amor, a vassal's good will, is covered by neither sense. Added.
14. __broaden__ fijos · **weak** · todos vuestros fijos son covers sons-in-law and daughters: 'children'. Added.
15. __broaden__ manos · **weak** · a las manos les tomó 'took them by the hand' (Pidal) is not covered by a las
    manos 'for the hands'. Added.
16. __broaden__ merçed · **weak** · en vuestra merçed somos nos 'at your command' (Pidal 'a vuestro mandar').
    Added.
17. __broaden__ gelos · **weak** · gelos reçibe 'receives them from him' (dative of separation). Added.
18. __broaden__ gelas · **style** · non gelas do yo 'to them'; the entry had only 'to him'. Added.
19. cometer, metan, alfaya, evad, veladas · **style** · Pidal's glosses added ('proponer'; 'empleen, gasten';
    'de valor'; 'he aquí'; el velar 'la ceremonia de las velaciones').
20. saliesse · **style** · "it should rise, came out" tidied to "(that) it should come out, rise".

Checked and kept: cantó, ifançones, piden, mándovoslo, hedad, pequeñas, perteneçen, hyo, engendré, criásteslas,
afellas, dadlas, levantaron, dades, dólas, caso, ende, afellos, torno, ayuda, bodas, dó, fueren, yernos, fet,
casades, puestas, omenajes, tornasse, metiólos, sírvanvos, devos, galardon; __broaden__ pues, ques. Every
__broaden__ is the glossary entry whole + " · " + the new reading (checked by script). The keys of gloss.json
minus __broaden__ equal novel-forms.json (48). No entry is pinned to a line number, and no invented Pidal
attribution remains. The other 191 known forms were checked against this part's uses and are covered.

Pass 2 counts: error 3 · weak 14 · style 3 (20 items).
