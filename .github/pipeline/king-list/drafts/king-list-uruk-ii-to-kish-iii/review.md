## Pass 1

I read Plate III (langdon1923_0044.jpg), Col. V 11–47, and the foot of Plate II (langdon1923_0043.jpg), Col. IV 42–48, line by line at 2–10× zoom. For the comparisons the drafter cites I also read III 15 (URU), III 27 (IR), IV 43–44 (MA, KI, EŠ₂, BA) and V 41–44 (KI, GIŠ, KU, BA, DU, and the Akšak signs). I checked Langdon pp. 14–15 (langdon1923_0019–0020.jpg): transliteration, translation and footnotes. I also checked his Introduction, pp. 5–6, in the OCR text `source/raw/langdon1923_djvu.txt` (the page images for it are not in `source/pages`).

Edits were made by script (scratchpad reviewer/rev1.py). The JSON was loaded and dumped with indent 1, ensure_ascii=False and no trailing newline, as before, and no cuneiform was retyped. Afterwards:
- the JSON parses;
- every glyph sign is a key in signs-cuneiform.json;
- every morph `g` covers its word's glyphs exactly once;
- `r3.py build` and `validate` give PASS (one WARN: the V 32 linecheck line, confirmed below);
- `signs.py check` says "in sync".

After the build, stories.json was restored with git checkout and the generated king-list-uruk-ii-to-kish-iii.json was deleted. No glossary file was touched, and no sign was added.

### Changes

- V 1 · n · **major** · The note said Langdon (Intro. p. 5) puts "the rest of the second dynasty of Uruk, and the beginning of the dynasty that follows" in the break. Langdon says the opposite. In his view the second dynasty of Uruk had only one known king, Enugduanna, and "the kingdom endured 420 years" (IV 45–48; his table: "Second dynasty of Erech 1(?) 420"). The break (his "Col. V 1-11") belongs to a second dynasty of Ur: from P. No. 2's 13 or 14 kings for the three Ur dynasties, less the 9 of the first and third, he gets "4 or 5 names to be supplied in the break", with "a possible total of 108 years". The note is rewritten to say this, and adds that V 15's refrain bears out Ur.
- about · minor · Two fixes:
  - "ten lines, which held, Langdon thinks, four or five more names" followed the drafter's reading of p. 5. It now gives the break to a second dynasty of Ur, as Langdon does.
  - "the most famous entry of the list" was an outside judgement, not drawn from the source, and has been dropped.
- IV 48 · i · minor · "… reigned 480 years." In the house style "…" marks lost text (ur-i-awan IV 12), but nothing is lost here. The line simply names no one. Now "He (?) reigned 480 years.", which matches IV 47's "He (?)" for the same unnamed 3sg ni-ag.
- IV 48 · n · minor · Two fixes:
  - "(the totals have ib-ag)": this part's own totals at V 32 and V 41 have ni-ag. Now "most totals have ib-ag, though two in this part, V 32 and V 41, also have ni-ag".
  - The note left out Langdon's own reading of the line. His Introduction (p. 5) takes it as the length of the whole dynasty, again as 420. That view is now quoted.
- V 17 · n · minor · "Read as a phrase it could be 'the king whom An built (?)'": a relative clause would need -a on the verb (mu-un-du₃-a, as uruk-i III 7), and the name has none. The note now analyses lugal + an-ni (perhaps An + ergative -e) + mu-un-du₃ 'he built', says it is not a relative clause, and leaves the sense open.
- V 23 · l · minor · "to(?)-Mari": the "(?)" suggested a doubtful reading, but EŠ₂ is clear on the copy (at the edge of the break). The oddity is the case, not the sign. Now "to-Mari (sic),". The `i` keeps the formula "In Mari", and the note explains why.
- V 33 · l · minor · "[its]-kingship": the brackets were on the wrong word. BI (-bi 'its') is clear on the copy, and nam-lugal is restored. Now "its-[kingship]".
- V 36 · l · minor · "[was]-king" for [lugal]-am₃ had the same problem. A (with AN) is at the edge of the break and visible, and lugal is restored. Now "was-[king]".
- V 25 · n · style · "His 25 does not in fact come from that total" accused Langdon where a statement of the numbers is enough. Now "does not agree with that total as the copy gives it". The arithmetic is unchanged and correct.

Counts: 1 major, 7 minor, 1 style.

### Drafter's questions settled

1. **Mari's second sign (V 22): URU, read ri₂, confirmed.**
   - V 22 on the copy reads: a trace at the hatching's edge, then MA (drawn as in ḫa-ma-zi IV 43), a box with an inner upright near the left and a cross-stroke, KI (the hatched lozenge, as in V 42 and IV 44), EŠ₂, BA, DU. That makes six signs. MA–x–KI–EŠ₂–BA–DU fits Langdon's Ma-er-(ki)-šú ba-gín sign for sign.
   - The second sign matches III 15's URU (eri-ki-ni) closely: the same box, inner upright and top stroke.
   - IR in III 27 (La-ba-še-ir) is a quite different form: a long horizontal with a wedge-head and a boxed cluster.
   - So the plate supports URU, and ri₂ is a value of that sign. Langdon's "er" is kept in the notes and in the glossary text.
2. **V 13 and V 14 unbracketed: confirmed.**
   - V 13: LUGAL is drawn whole, a little right of centre, with hatching on both sides.
   - V 14: MU and BI are clear at the start, then hatching, then two clear signs at the right end.
   - The second of those is AK. The first fits IB: it has the same long horizontals and middle crossing as V 20's IB, though drawn without V 20's inner horizontals. That is acceptable, and the restored context requires ib-ag.
   - Langdon's brackets over the whole lines go too far. The convention "the plate decides" applies, and the note says so.
3. **Akšak's second sign: kept as UD + KUSHU2, uncertain.**
   - V 43 on the copy reads: NAM, LUGAL, BI (as BI in V 41), then two signs, then KI (the hatched lozenge), then BA and DU.
   - So there are two signs before KI, which bears out the drafter's count.
   - The first is a wedge-triangle with a crossing stroke, and the second a horizontal with heads at both ends and an upright. Neither can be confirmed as UD or KUŠU₂ from the copy alone. The note already says so, and the shipped pair is the conventional value.
   - For the next part (V 44, Akšak-šú): its first sign looks like the second sign here, followed by the hatched lozenge and a box. The drafter of V 44 should compare.
4. **V 1–10 as one lost unit: the note is honest.** It says the copy's heading reads "Lines 1–10 defaced", that Langdon prints one row of dots numbered "1-10.", and that the one unit stands for all ten lines by convention. The only error was the account of what Langdon thinks the break held (fixed above, major).
5. **IV 47 wording: kept.**
   - The literal "its-kingship, years 2-sixties he-exercised" departs from the house "he-ruled" for ni-ag. That departure is justified here because nam-lugal-bi is the object: "ruled its kingship" is not English, and "exercised" is close to aĝ₂ 'measure out' (as the morph gloss says).
   - The `i` "He (?) exercised its kingship 120 years" keeps the grammatical 3sg and flags that no one is named. The note gives Langdon's impersonal rendering.
   - IV 48 is aligned with it (above).

### The other points asked

- **V 25, ZI in the break: confirmed.** After the hatching the copy has exactly four signs: TUR (dumu), AN, BU, KID. The name must therefore end inside the hatching, so [lugal-tar-zi] bracketed whole is right, against Langdon's unbracketed zi.
- **IV 48, 480 vs 420: confirmed as 480.** At 10× the numeral is four wedges over four. That is 8, so 8 geš = 480. Langdon's translation (420) and his Introduction (420, "the kingdom endured 420 years") disagree with his transliteration and his copy. 480 is shipped and the discrepancy is noted, as the conventions require.
- **V 26, restored 25(?): correctly not shipped.** It is a doubtful restoration with Langdon's own "?", so the house rule applies. Arithmetic checked:
  - Total in V 32: 2 geš + 1 u + 6 diš = 136 (on the copy: two uprights, then a corner wedge with 3-over-3).
  - Surviving reigns: 30 (V 24) + 30 (V 27) + 20 (V 28) + 30 (V 29) + 9 (V 30) = 119.
  - 136 − 119 = 17. With 25 the reigns make 144.
  - The notes (V 25, V 31) and the about state this correctly.
- **V 37, munus lu₂ kaš-tin-na: grammar accepted.** lu₂ X-na is 'person of X', with -na = the genitive -a(k) after the final n of tin, flagged uncertain. munus is 'woman', in apposition. The restoration is Langdon's, from Legrain No. 1 (fn. 1 p. 15). Only NA and a trace are on the copy.
- **ni-ag in the totals V 32 and V 41: confirmed on the copy.** The sign before AK in both lines is NI (the same form as in the reign lines), not IB. The l keeps "he-ruled" and the i follows the house total formula, as the notes say.
- **ba-gub at V 43: consistent with the pilot.** king-list-antediluvian renders nam-lugal-bi la-ra-ak{ki} ba-gub and šuruppak{ki} ba-gub as "its-kingship, Larak, was-established" / "its kingship was established at Larak". V 43 l and i match that exactly.

### Plate record, line by line

- IV 45: UNUG KI GA, EN, a large sign with a long horizontal tail (UG, after Langdon), DU AN NA.
- IV 46: LUGAL A AN, MU, 1 diš, ŠU IGI, NI AK.
- IV 47: NAM LUGAL BI, MU, 2 diš, ŠU IGI, NI AK.
- IV 48: indented. MU, 8 (4 over 4), NI, then AK drawn inside the hatching. A ruling below.
- V 1–10: "Lines 1–10 defaced".
- V 11: hatched, then a boxed sign with crossing strokes at the right end (LU?).
- V 12: hatched, then an upright with a head at the right end (trace).
- V 13: hatched, LUGAL, hatched.
- V 14: MU BI, hatched, IB AK.
- V 15–18: hatched across.
- V 19: hatched, LUGAL.
- V 20: hatched, a corner-wedge trace, IB AK.
- V 21: hatched, GIŠ KU BA AN SIG₃ (BA is clear, not KA).
- V 22: a trace, MA URU KI EŠ₂ BA DU.
- V 23: hatched, EŠ₂ at the edge, AN BU.
- V 24: hatched, MU, 3 u, NI AK.
- V 25: hatched, TUR AN BU KID.
- V 26: hatched, NI AK.
- V 27: hatched, LUGAL, MU, 3 u, NI AK.
- V 28: a trace, LU₂ GAL, MU, 2 u, NI AK.
- V 29: hatched, BI (at the edge), IM, MU, 3 u, NI AK.
- V 30: hatched, BI (at the edge), MU, 9 (3×3), NI AK.
- V 31: hatched, 6 diš (3 over 3), LUGAL.
- V 32: hatched, 2 geš, u + 6 diš, NI AK.
- V 33: hatched, BA AN SIG₃.
- V 34: hatched, BI.
- V 35: hatched, BA DU.
- V 36: hatched, BA (half in the hatching), U₂.
- V 37: hatched, a trace, NA.
- V 38: hatched, KI (at the edge), MU UN GI NA.
- V 39: hatched, A (at the edge) AN, MU, 1 geš + 4 u, NI AK.
- V 40: 1 diš, LUGAL.
- V 41: MU BI, 1 geš + 4 u, NI AK.
- V 42: KIŠ KI GIŠ KU BA AN SIG₃.
- V 43: NAM LUGAL BI, two signs (Akšak), KI, BA DU.

All signs, roles and values in units.json agree with this record.
- Numerals:
  - The `u` names resolve (EIGHT GESH2, NINE DISH, SIX DISH, TWO GESH2, FOUR U).
  - 2 diš at IV 47 is two DISH glyphs, as the pilot writes 2.
  - Repeated U is used for 20/30/90, as in uruk-i and ur-i-awan.
  - Values: 60, 120, 480, 90, 90, 30, 30, 20, 30, 9, 136, 100, 100.
- Readings by sign follow the conventions: -še₃/-šú, ba-ĝen/ba-gín, sig₃, {ĝeš}tukul, lu₂, -ke₄, du₃, ku₃, suḫuš, urim₂, am₃. Langdon's forms are given in the notes.

### Coverage and structure

- Units: IV 45–46 | 47 | 48 | V 1 (lost, = 1–10) | 11–12 | 13–14 | 15–16 | 17–18 | 19–20 | 21–22 | 23–24 | 25–26 | 27 | 28 | 29 | 30 | 31–32 | 33–35 | 36–39 | 40–41 | 42–43.
- That is 21 units. Every line is present, in order, and no unit crosses a column.
- `nl` falls on the first word of each later prism line, and only there.
- Morph `g` coverage is exact.
- {d} has its own morph in ku₃-{d}ba-u₂, as in ur-{d}nun-gal.
- Lost name-beginnings are a separate "[…]" morph, as uruk-i III 31.
- The house formulas are applied ("In X, Y became king; he reigned N years"; "N kings reigned M years" / "One king reigned N years"; "X was smitten with weapons; its kingship was carried to Y").
- The grammar labels (locative -ga/-a, -še₃, -am₃, -bi, -ke₄ = gen. + erg., ba-an-, mu-un- … gi-n-a, ni-ag / ib-ag) are right for the forms.
- The `l` and `i` agree in sense.

### Findings considered and refused

- **i "a woman tavern-keeper" as remembered English (Langdon: "a female wine seller")** · refused. "tavern-keeper" is the part's name as fixed in parts.json/plan.md at setup. It is also the project's existing English for the woman who sells drink: signs-cuneiform.json DIN cites "ŠAL.GEŠ.TIN.NA, the tavern-keeper" from Hammurabi. The note gives Langdon's rendering. **Flagged for the owner** in case a 1923-only rendering ("a woman wine-seller") is preferred.
- **IV 47 l "he-exercised" → "he-ruled" for house consistency** · refused, for the reason given under question 5.
- **Write IV 47's 2 as one TWO DISH glyph with `u`** · refused: the pilot writes 2 as two DISH glyphs.
- **Bracket the visible -na and "of" in V 37 l more finely** · refused: the whole phrase is restored except one sign, and splitting the English gloss across brackets would mislead more than it helps. The note says what is visible.
- **V 12 [ni-ag] unbracketed because of the trace** · refused: the trace is a single upright and cannot be identified. As in ur-i-awan IV 24, a damaged sign at the edge is noted, not read.
- **V 15 "Legrain, PBS XIII No. 1" when Langdon writes only "L. No. 1"** · refused: the published ur-i-awan part expands it the same way.

### For pass 2 / the owner

- The "tavern-keeper" question (above).
- new-lemmas.json "en-ug-du-an-na" and "ma-ri₂" agree with the notes. "akšak" should stay flagged as an identification. The glosser should not take Langdon's p. 5 view of the break as being about Uruk.
- For the next part: compare V 44's Akšak writing with V 43's (see question 3).

## Pass 2

I checked every gloss.json entry (17 new lemmas plus `__broaden__` -ga, -a, -šú, ba-gub, kiš) against units.json, its notes, the plate record above, Langdon pp. 14–15 and his Introduction p. 5. I also checked the published glossaries of all five king-list-*.json files, by script. Edits were made by script (scratchpad reviewer/rev2.py). gloss.json and units.json are both dumped with indent 1, ensure_ascii=False and no trailing newline; gloss.json's layout is unchanged.

Checks run afterwards:
- Every `__broaden__` value starts with the published entry exactly as published, followed by " · ":
  - -ga: uruk-i.
  - -a: "nominalizer", as in antediluvian and uruk-i.
  - -šú: antediluvian, kish-i, ur-i-awan and uruk-i.
  - kiš: kish-i and ur-i-awan. The old text "Kish — city in northern Babylonia, seat of the first dynasty after the Flood; written with the KIŠ sign plus the place-determinative KI (unread), as kiš{ki}" is kept whole.
- The new-lemmas.json keys equal the gloss.json keys.
- Every morph lemma in units.json is either in a published glossary or new in gloss.json.
- No gloss.json key repeats a published lemma.
- Every glyph sign is a key in signs-cuneiform.json.
- Morph `g` coverage is exact.

### Changes — gloss.json

- `__broaden__` -šú · **major** · The new reading glossed ma-ri₂{ki}-še₃ as "'in Mari'". That gives the terminative a locative meaning it does not have. The form is the terminative -še₃ 'to', written where the formula (and Langdon's fn. 3, L. No. 1 V 10 Ma-er-(ki)-a) has the locative. · Now: "also written where the formula has the locative -a 'in' (ma-ri₂{ki}-še₃ at the head of a dynasty, where another copy has ma-ri₂{ki}-a); why the terminative stands there is uncertain".
- -na · minor · Three problems:
  - "'man of the tavern'?" made kaš-tin mean 'tavern'. That is not in the words, and the kaš-tin entry itself does not say it.
  - The entry was tied to this one word ("after the n of tin").
  - "-(a)k" was fine, but the entry was not general to the form.
  · Now "-a(k) 'of' (genitive) written -na after a final n, as in lu₂ kaš-tin-na 'person of kaš-tin'; the analysis is uncertain".
- `__broaden__` ba-gub · minor · The broadening was unnecessary. The published antediluvian entry already covers exactly this use: Larak and Shuruppak, "its kingship was established at …", with the city carrying no case ending. The added text was also tied to this line ("where earlier …", "the city here"). · Removed. ba-gub keeps its published entry.
- `__broaden__` kiš · minor · The added text was tied to these lines ("from Mari", "Ku-Bau") and ended with "the earlier phrase 'first dynasty' does not apply here". That disowns the old text inside the same entry. · Now "· the kingship returns to it more than once, so it is also the seat of later dynasties of Kish", with the old text kept whole in front.
- ma-ri₂ · minor · "the reading of the second sign is uncertain" contradicted the plate. Pass 1 confirmed URU against III 15 and IR (III 27). · Now "the second sign is identified from the copy". Langdon's "er" stays in the entry.
- `__broaden__` -ga · style · "here at the head of a dynasty" tied the entry to a line. · Now "(unug{ki}-ga 'in Uruk', at the head of a dynasty)".

### Changes — units.json

- 22 morph glosses for new lemmas · minor · They still held the drafter's wording and did not match gloss.json. · Each is now set to its gloss.json text (as in ur-i-awan pass 2).
- V 23 · morph gloss -šú · minor · It carried the general published 'to, towards', with no word on the odd use. · Now the line-level gloss "terminative -še₃ 'to' (the EŠ₂ sign; Langdon -šú) — written here where the formula has the locative 'in'". It matches the note and the broadening.

Counts (pass 2): 1 major, 7 minor, 1 style.

### Checked and kept

- en-ug-du-an-na:
  - UG is flagged as Langdon's identification.
  - The En-šag-kuš-an-na remark is his (fn. 9 p. 14).
  - "first king of the second dynasty of Uruk" fits his p. 5 view (the only known king).
- lugal-an-ni-mu-un-du₃: "the sense of the name is uncertain" fits the pass-1 V 17 note. No relative-clause reading is claimed.
- an-sir₂, lugal-tar-zi, the four "[…]-" Mari names, […]-lu, adab, akšak (identification flagged), ku₃-{d}ba-u₂, munus, suḫuš: no invented modern forms, and they are general to the form.
- kaš-tin: Langdon's 'wine seller' is credited, and "tavern-keeper" stays as decided by the owner.
- `__broaden__` -a: the locative on a city name is right for adab{ki}-a.
- `__broaden__` -ga: the locative reading is right for unug{ki}-ga at a dynasty's head (as urim₂{ki}-ma in ur-i-awan).
- Published lemmas whose morph glosses differ from the glossary (unug, urim₂, lu₂, gi-n, mu-un- 'he/she', u/geš/diš with "N here = …", šu-ši, lugal 'here plural'): kept as line-level glosses, as ur-i-awan pass 2 and uruk-i do. None contradicts its published entry.
- Second read of units.json:
  - Every reading rebuilds from its glyph tr values.
  - `say` agrees with the reading.
  - l, i and n agree after the pass-1 edits.
  - Nothing further found.

### Findings considered and refused

- Broaden ba-an- for this part · refused. sig₃ is transitive, and the published entry (as uruk-i broadened it) already covers ba-an-sig₃, as ur-i-awan pass 2 found.
- Broaden lu₂ for lu₂ kaš-tin-na ('person of …', not a relative 'who') · refused. The published "man; 'the one who …'" begins with 'man', which covers the use, and the line-level morph gloss says "man, person".

### Build and validate

`r3.py build` produced 21 units, and `validate` printed **PASS**. Its one WARN is the V 32 linecheck line ('120 + 16' written 2 geš + u + 6 diš), which was confirmed on the plate in pass 1. In the built glossary the broadened entries read as above, and ba-gub keeps its published text.

Restored afterwards: stories.json was checked out and the generated king-list-uruk-ii-to-kish-iii.json deleted. git status shows only the drafts files modified (gloss.json, units.json, review.md). signs.py made no changes in this pass.
