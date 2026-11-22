# Review: cid-tiradas-103-104a (tiradas 103–104a, vv. 1959–2012)

Checked against the pinned packet; Pidal 1923, PDF pp. 256–259 (printed 252–255: text, rubrics, footnotes 1965,
1968, 1970, 1971, 1972, 1980, 1982, 1984, 1987, 1993, 2001, 2007, 2010, 2012; enlarged crops of vv. 1971, 1975,
2008 and 2011); the published parts (102-102 and the pilot, plus 19-23, 35-39, 49-55, 78-82 and 84-86 for names
and formulas); `conventions.md`; and `cid-glossary.json`. Pidal's *vocabulario* is not under `source/`.
`t` integrity: all `t` joined by "\n" equal the 57 packet verses in order (1992b, 2000b and 2004b included), both
before and after the edits. No `t` was touched, and every `l` has one line per verse. Both files were edited by
script (json load/replace/dump, indent 1, ensure_ascii=False).

## Pass 1: units.json

1. Header · titleEn, part · **style** · "the meeting on the Tagus" clashed with the `i` ("Tajo") and with 102-102
   (`i` "On the Tajo"). Done: "on the Tajo" in both. parts.json (line 1120, `name`) still says "Tagus" and is
   left to the orchestrator.
2. 1993 (vv. 1993–96) · i + n · **error** · "Galind Garçiaz, the man from Aragon": the house rendering of this
   knight is "Galín García" (vv. 443, 740, from 19-23 and 35-39), and the note did not link him to that name.
   Done: `i` "and Galín García, who was from Aragon" (this also renders f[o] 'was'). The note now says "Galind
   Garçiaz is the Galín Garcia[z] of vv. 443 and 740 … Galín García in the translation as there; Pidal prints
   Galind here." `l` keeps Galind Garçiaz.
3. 1999 (vv. 1999–2001) · i · **error** · (a) "Galind Garçiaz", changed to "Galín García" as in item 2.
   (b) "together with all the others under their command" makes the others fellow guards. Pidal's footnote
   says en poder dessos is 'bajo la custodia de esos', so the others are in the two men's keeping. Done: "and
   all the others who were in their keeping". The note adds: "the others are those left in their charge, not
   further guards".
4. 1966 (vv. 1966–68) · i · **weak** · "stout and swift beyond fault" changed the filler sin falla ('without
   fail', Pidal's ripio) into a claim that the horses were faultless. Done: "stout and swift, without fail,".
5. 1975 (vv. 1975–78) · n · **weak** · (a) "the ó may be his too (uncertain on the scan)". At 3x on an enlarged
   crop, only the n of Carrión is clearly italic. The ó looks roman, as the pinned text has it, but the print is
   soft. Done: the note says this and keeps a small hedge. (b) **style** · "creçeríe" is a misspelt Old
   Spanish conditional. Done: "creçerié".
6. 1969 (vv. 1969–71) · n · **weak** · "So Pidal adds an n (in italics) to the manuscript's Adria" put an
   inference in Pidal's mouth, and the print has two italic n's. Done: "Pidal's italic n's mark the letters he
   adds to the manuscript's Adria". The note now also says that both italic n's are plain on the scan, and the
   doubled form stays flagged as uncertain.
7. 1982 (vv. 1982–84) · n · **weak** · non son en cuenta is the formula of v. 915 (published as "are not
   counted" / "not in the reckoning"), and the note did not mention it. Also, "the reading is uncertain" was
   wrong: the reading is certain and only the sense is doubtful. Done: the note cross-refers to v. 915 and says
   "Pidal has no note, and the sense is uncertain". The `i` "past counting" is kept.
8. 2006 (vv. 2006–08) · n · **weak** · puode: the drafter asked whether it is present or preterite. Pidal's
   footnote to 2007 paraphrases it with 'que ninguna puede salir', which makes it a present. Done: the note adds
   "a present, 'can', as Pidal's paraphrase puede shows, not the preterite pudo". `l` "not can" and `i` "may
   leave" are kept.
9. 1991 (vv. 1991–92b) · n · **style** · Mont Mayor was not linked to v. 738, where Pidal identifies the town
   and where the same half-line is the manuscript's own text (and the source of his restoration here). Done:
   that cross-reference is added. The `i` "who held command at Montemayor" matches 35-39 word for word.
10. 2004 (vv. 2004–05) · i · **style** · "who serve them as they please" did not say whose pleasure is meant,
    and it differed from the `l` and the note ('to their liking'). Done: "who serve them to their liking".
11. 1987 · n · **style** · "pelliçones … (from pelliza)": the derivation is not established. Done: "(compare
    pelliza)".

Drafter's points, judged:
- 1971 A[n]dria[n]dria: the footnote (p. 253) is quoted accurately: earlier A[lexán]dria, "soie Alexandrine",
  Schultz-Gorra (ZRPh XXVI 718) and Bertoni keep d'Adria as a mistranslation of "cendal d'Andre", and Crescini
  (Atti R. Ist. Veneto LXXVI, 1917) shows that Andros was also called Andra, Andre and Andria. "Andros" in the
  `i` follows Pidal's final view and is kept. The doubled form is left flagged as uncertain (a probable
  misprint), and the `t` is untouched.
- 1983 non son en cuenta: "past counting" is kept, and the uncertainty is now attributed to the sense (item 7).
- 2012 Hyas: Hya = ya with h- is the house reading (vv. 939, 1378); Hyas = hya + se is sound, and the note
  marks it as ours. Kept.
- 1961 buen[a] without ora: only the a is italic, as confirmed on the scan. The `l` "in good (hour)" and the
  house formula in the `i` are right, and so is the note. Kept. (Compare v. 1603 en buena, from 84-86.)
- 1985/1990 margin: Pidal does print 1990 beside the Minaya line. The count from 1985 and the footnotes to 1987
  and 1993 confirm the drafter's 1991. Kept.
- 2011 dieran: this is the -ra pluperfect indicative 'they had (not) given', parallel to gañara. The `l`, `i`
  and note are right. Kept. (The glossary's conditional reading was corrected in Pass 2.)
- 2004b: there is one line too many between 2000b and 2005 on p. 255. The note's "the letter b is provisional"
  is right. Kept.

Confirmed and unchanged: the rubrics of 103 and 104 (quoted exactly); the assonances (á-a, ó); Pidal's
footnotes 1965 (2079, 3139), 1968 (p. 44, n. 2), 1970 (p. 104), 1972 (804), 1980 (conde and podestades),
1982, 1984, 1987 (v. 1548; 2572, 3242), 1993 (v. 1501), 2001 (486), 2007, 2010 (v. 1548), 2012 (33); every
bracketed italic (buen[a], se[d]manas, vi[d]o, A[n]dria[n]dria, Carrió[n], gana[n]çia, cue[mdes], Vermu[doz],
the half-lines of 1992 and 2002, Jero[me], Alvar[oz], Sa[l]vadórez, f[o], [quantos], [otros], alcáç[er],
s[o], alcáç[e]r, pu[o]de, [a]); the uncedillaed Garciaz, Valencia and corazón of 1999–2000b; naçió at 2008 is
roman; and the forward reference in the 2012 note (the king arrives a day early) is on p. 255 (De un día es
llegado antes el rey don Alfons).

Refused / left as drafted:
- 1964 `l` "themselves they-were-returning" for se tornavan: literal and house-like. Left.
- 2010 note: diestro as 'the hand on which a charger is led' is not in Pidal's footnote. It is standard and
  harmless, and it matches "led at his right hand" in 84-86 (v. 1546). Left.
- 1979 `i` "governors" for podestades: this fits Pidal's footnote (government or tenure of a fortress, city or
  territory). Left.
- 1959 `l` "himself he-pays" for se paga: transparent, with the sense given in the note. Left.
- 2006 `i` "may leave": in context it covers 'can' and is not a mistranslation. Left.

## Pass 2: gloss.json

1. andriandria · **error** · glossed as "Alexandria (Alejandría)", the reading Pidal abandons in his footnote,
   and contradicted the unit. Done: Andros, following Crescini's Andria. The note now says that the two n's are
   Pidal's and that the doubled form is unexplained.
2. curien · **error** · "the ending -ien stands where -en is expected" is false: curiar → present subjunctive
   curie-n is regular. Removed.
3. ge · **error** · the example gave "'they would not have given them to him'" (conditional), against the unit's
   pluperfect. Done: "'they had not given them to him as a gift'". The entry now also covers to her / to them
   before lo, la, los, las.
4. __broaden__ dieran · **error** · the added sense "with the sense of a past conditional; = no se los habrían
   dado" contradicted the unit. Done: "'they had not given them to him as a gift' (= no se los habían dado)".
5. hyas · **error** · "Pidal reads 'ya se va'" is an invented attribution: Pidal has no note on v. 2012 except
   paró. Done: hya (= ya with h-, as in the glossary's hya) + se; "= ya se".
6. gañara · **error** · the lemma was given as ganar, but the glossary has gañar (gañó). Done: "gañar … (= ganar;
   se los había ganado)".
7. puode · **weak** · the entry hedged "could also be read as the preterite pudo". Pidal's footnote paraphrases
   it with puede. Done: present, with Pidal's 'que ninguna puede salir'.
8. podestades · **weak** · "power; … persons of power … probably" is a false hedge, because Pidal's footnote to
   1980 is explicit. Done: magnates holding an office below count, with the footnote paraphrased.
9. paró · **weak** · "probably": Pidal glosses 'convino, concertó'. Done: the hedge is dropped, Pidal is cited,
   and the modern form is "= acordó, concertó".
10. boclados · **weak** · "probably from bocla" ignored Pidal's footnote ('con bloca de oro'). Done: Pidal is
    cited, and the modern form is "= blocados, guarnecidos con bloca".
11. adebdan · **weak** · "they owe" differed from the unit ('run into debt', 'buy on credit'). Done: matched to
    the unit, "= adeudan, se endeudan".
12. __broaden__ tenien · **weak** · "'as they stood, as they had it set up' (probably …)" differed from the unit
    ('as they reckoned'). Done: "tener 'hold, reckon' (commo ellos tenien 'as they reckoned it' …; = tenían,
    pensaban)".
13. palafré · **style** · "final -n dropped" is an invented derivation (the word comes through Old French
    palefrei). Removed.
14. cuemdes · **style** · "cue[mdes] restored by Pidal" was inexact, because only the letters mdes are italic.
    Done: "in cue[mdes] the mdes is Pidal's".
15. galind · **style** · added the link to Galín Garciaz elsewhere.
16. __broaden__ cuenta · **style** · "are beyond counting" was stated as certain. Done: "past counting, or not
    reckoned in", matching the unit's hedge.

Checked and kept: echaron, paga, saludadme, mula, preçiada, pendón, astas, conduchos, aparejadas, atantas, creçer,
quisiessen, leoneses, gallizianas (Pidal 'gallegas'), castellanas, adeliñadas (Pidal 'encaminadas'), detarda,
adobó, gruessa, sazón, arma, capa, colores, á, garçiaz, adoban, corazón, dessos, recabdado, torne, salien,
aguijan; and the __broaden__ entries s, ques, tanto, uno, corredor and mejor. All 45 novel forms are covered, and
no entry is pinned to a line number.
