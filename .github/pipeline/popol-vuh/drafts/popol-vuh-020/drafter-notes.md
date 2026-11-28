# popol-vuh-020: drafter's notes

There are 59 units for 10 paragraphs (1034 words). `cut.py` and `make_units.py` are unchanged from 019. `cut.json` has 124
pieces. `groups.py` merges consecutive pieces within a paragraph, and `units_src.py` holds mt / l / i / n. `make_units.py`
builds units.json and takes `t` only from cut.json, so no `t` was retyped. It prints:
`OK: 59 units, 10 paragraphs, 1034 words, longest 37 (U27); paragraph starts at U1, 7, 12, 15, 25, 33, 39, 44, 51, 55`.

The longest unit is U27, the four ꜭo xa … xbe v cama lines with their lead-in. I kept the litany whole. Two cut pieces
(38 → U17, 67 → U30) each hold the end of one sentence and the start of the next, because the next word begins with a
lower-case ꜭ or ꜩ. They could not be split, so each sits in one unit.

## Checks run
- make_units.py OK (tiling, paragraph starts, one mt per WORD_RE token, the JSON loads).
- I compared every mt by script with the mt of the same manuscript form in published 001–019. None differs from a
  published spelling of that form. Where a form has two published values, I chose one by sense: xcah xkaj 'they wanted'
  (U4), against xqaj 'went down' (U44, U57). xquilo is xqilo 'we saw' (U55). cam is kam 'die' (U4, U59) and k'am 'take'
  (U26). chi is chik where it stands for chic.
- README 5b: U36 and U55 open with "The manuscript has xuhquiba, a misprint for xu tiquiba, corrected here" and
  "The manuscript has xquihquiba, a misprint for xqui tiquiba, corrected here", as in 017.

## Proposed house renderings (not added to conventions.md)
- **Teuh Ha**: 'the Cold House' (description, translated like Balami Ha; mt Tewj Ja). The note says that 011 named the
  second house Xuxulim Ha ('thick with cold'), and that the two are probably the same house, though the text does not say so.
- **Balami Ha**: 'the Jaguar House' (as 011).
- **Zoꜩin Ha / Zoꜩi Ha**: both 'the Bat House' (as 011's Ꜩoꜩi Ha).
- **hun ha chi ꜫaꜫ**: 'a house of fire'. It has no name of its own, so none is proposed.
- **Camazoꜩ**: kept as a name, 'Camazotz' (mt Kamasotz'). The note quotes Brasseur ('qui prend ou commande les
  chauves-souris') and says that cama is not certain.
- **Chaquiꜩam**: kept as a name, 'Chaquitzam' (mt Chakitzam). The note quotes Brasseur ('pointe séchée').
- **coc**: 'the turtle' (mt kok). An earlier part glossed the same letters as 'smell', which is a different word. The
  glosser needs `__broaden__` for coc.
- **vmul**: 'the rabbit'. **vuch** here is 'the opossum', and **mama** 'the old man'.
- **zoꜩ**: 'bat', with mt **sotz'**. *Decision wanted:* 011 gave its ꜩoꜩ (written with the ligature at both ends) mt
  tzotz, by the letters. Here the manuscript has z + ligature, which matches the modern word sotz'. I supplied the tz', as
  015–019 did for coꜩih → kotz'i'j, because the word is certain. The same applies to Kamasotz', Sotz'in Ja and Sotz'i Ja.
  If the house prefers letters only, these four become sotz / Kamasotz / Sotzin / Sotzi.

## Known forms used in a new sense (for the glosser's `__broaden__`)
coc 'turtle'; quel here 'came out (?)' (B. qu'el), not 'hang'; xcupix 'was cut off' (earlier 'was caught'); cul 'meet,
receive' (xu cul); cac 'red (?)' (mt kaq); co = ꜭo 'there is' (co zoz); cama in i cama (U58).

## Main uncertainties (all marked in the notes, most "(?)" in `i`)
1. **ꜩah / cuꜩ mamai na (U3).** Brasseur reads cutz mamai na as 'avec les glands de pin (qu'ils allumèrent)'. I followed
   him, 'through the pine cones (?)', but the words are not understood. The division mamai na (MS mama|ina) is also doubtful.
2. **zacbocom (U2)**: 'hail (?)', after Brasseur's 'glace'.
3. **chopor (U15).** The manuscript is clear, but the meaning is unknown, and Brasseur has chupan. I left it out of `i`
   ("whatever came before them (?)").
4. **U16–U17.** The clauses `xqui ya vi quib hun vi rumal hun chi Camazoꜩ chi cah xpe vi; xavi vcutbal rib ta xqui bano
   rumal` are read with Brasseur ('ils se rendirent à cause d'un autre Camazotz qui vint du ciel pour se manifester'). The
   rendering "one of them gave himself up (?) … only so that it could show itself (?)" is a guess.
5. **ca rah (U20).** The r looks like X. I read mucum as 'peer out' and v nimal as 'his body' (after Brasseur).
6. **zilabic, xa qui chi co zoz chic (U22).** 'He only lay there sprawled (?)', after Brasseur. zoz may be zoꜩ.
7. **Ca vilo (U19).** By the letters it is 'I see it' (as 017). I followed Brasseur in rendering it 'look and see (?)'.
   cahanic / cahanican / labalo are inferred.
8. **ac (U25)**: 'peccary (?)' after Brasseur's 'Sangliers'. mt ak is by the letters; aq 'pig' and ak' 'fowl' are both
   possible.
9. **tiz, cubulcutih, canohoc (U29).** The turtle line is read with Brasseur. tiz is retouched and its meaning is unknown.
10. **xulu culoc / xul coloc (U30)**: 'came hovering (?), came down (?)', after Brasseur's 'vint planer'.
11. **v chuuc hebel (U32)**: 'its hair (?) … fine (?)'.
12. **The dawn (U33–U36).** I read cactarin, xaquinuchic, xuchux and cac raxaꜩinic with Brasseur's notes. I took Ama as a
    question particle (a guess).
13. **Ma vꜩ cha chux cut Hunahpu he (U37)** follows Brasseur. Who speaks is not said.
14. **chayecuh, qui qui banouic (U40); Chacuca (U46); caxou, yecoub (U47); yan, chacoyan (U45).** All are guessed from
    Brasseur.
15. **pix / pixc (U41, U49, U54).** Brasseur has 'les glands de la corniche', and in modern K'iche' pix is the tomato. I
    kept the word in K'iche' in `i` ("among the pix (?)"), and the note gives both readings. The establishment log's
    summary says "the oak", which presumably comes from Brasseur's 'glands' (acorns). *For QUESTIONS.md:* should `i`
    commit to one reading?
16. **camixtah, xtiquixtah, cuba (U51); colem (U54); xcacatah, pucabin, zaquiram (U57).** All are read with Brasseur
    (inferred or guessed).
17. **rahal (U59)** is printed as written. The English follows rahaual 'lords (?)' (Brasseur r'ahaual), and a dropped
    syllable is possible but not certain.
18. **xe quel, tacol que (U5)**: 'came out (?)' and 'to summon them' (doubtful readings).
19. **Huchatic (U21)**: 'again (?)', after Brasseur's 'Puis une autre fois'.

## Other decisions
- **Singular xꜭha with Xibalba / the lords (U6, U58).** I translated it as plural and said so in the note.
- **xavi xare.** I took xare as xa are run together ('just so'), following Brasseur's xavixare, and gave it mt xare by
  the letters.
- **chi → chik.** I gave chik where chi stands for chic: U1, U5, U6, U7, U44 ×2, U51, U52 ×2, U54 ×2, U55, U56. chi stays
  where it is a preposition, comes before a verb, or forms part of libah chi or ꜩaꜩ chi.
- **The struck words `carah cu mucum vloc chuꜩam vvb`.** These are not printed, and the U20 note says so.
- **Nothing was left untranslated.** Every piece has an English rendering, and the doubtful ones are marked.
