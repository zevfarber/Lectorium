## Pass 1

Plate I (langdon1923_0042.jpg) read line by line at 2–5× for I 42–47 and II 1–46; Langdon p. 10 (langdon1923_0015.jpg) footnotes checked. Edits made by script (scratchpad rev1.py), no cuneiform retyped.

### Changes

- II 14 (II 14–15) · i · minor · "son of a mašda" left the key word untranslated in the idiomatic line · now "Arpium, son of a poor man (?), reigned 720 years." (Langdon's sense, marked uncertain; the note already gives the doubt).
- II 14 (II 14–15) · n · minor · on the plate the second sign of maš-dā is drawn exactly like the NI of ni-ag in II 15 (triangle with inner wedges), not like the DA of ma-da in II 36; the note was silent on it · added a sentence: the sign is shown as DA after Langdon's dā, but the identification is uncertain. Sign key not changed (see refused findings).
- II 14 (II 14–15) · n · style · added that 'a poor man' in the English is Langdon's, marked (?).
- II 42 (II 42–44) · n · minor · arithmetic check: the 19 reigns as drawn and as Langdon himself prints them (I 45 1200, I 47 960, II 8 960, 9 840, 11 900, 12 600, 13 840, 15 720, 19 1500, 22 400, 23 660, 25 900, 27 1200, 29 140, 31 306, 32 900, 34 1200, 38 900, 41 625) sum to 15,751, so the drafter's figure is right. The note's wording ("still far short") did not say that Langdon's fn. 8 figure (12,491) disagrees with his own transliteration · reworded: his 12,491 does not match the figures he prints; they add up to 15,751, still far short of 24,510. Neither total is corrected.
- II 42 (II 43) · words (mu-bi, glyph MU) · style · `nl` set on both the word and its first glyph; the glyph flag has no effect in build_t/lines_tr · glyph-level `nl` removed (word-level kept).
- II 45 (II 45–46) · n · minor · the note gave ba-an- as "prefixes" next to a passive English without saying that -n- ordinarily marks a 'he' agent, which pulls against the passive · one sentence added: the house's passive follows the sense of the refrain, not every element of the form.
- II 16 (II 16–19) · n · minor · the note explained e₃ and the Nippur -a but never said what the final de₃ (NE) of ba-e₃-de₃ is doing · added that it is read with the verb, as in I 1 e₃-de₃-a-ba (consistent with the morph, which gives e₃ the glyphs UD, DU, NE).
- I 46 (I 46–47) · i · style · i dropped the final EL that `l` and `reading` keep · now "Gulla-Nidaba-anna[…]el reigned 960 years."

### Checked and confirmed (no change)

- Line breaks: every unit's word-level `nl` matches the prism lines on Plate I (I 42 | 43–45 | 46–47; II 7–8, 10–11, 14–15, 16–19, 20–22, 24–25, 26–27, 28–29, 30–31, 33–34, 35–38, 39–41, 42–44, 45–46; single lines I 42, II 9, 12, 13, 23, 32). II 46 ba-gín drawn below the line, indented, as the note says.
- Numerals on the plate: I 45 two geš'u (1200); I 47 geš'u + 6 geš, 3 over 3 (960); II 8 same (960); II 9 geš'u + 4 (840); II 11 geš'u + 5 (900); II 12 one geš'u; II 13 geš'u + 4; II 15 geš'u + 2; II 19 two geš'u + 5 geš (1500); II 22 6 geš + 4 u (400); II 23 geš'u + one geš (660); II 25 geš'u + 5; II 27 and II 34 two geš'u; II 29 2 geš + 2 u (140); II 31 MU 5 ŠU IGI 6 NI AK (306); II 38 geš'u + 5; II 41 geš'u + 2 u + 5 (625); II 42 2 u + 3 diš (23). `u` names all resolve and match counts; TWO/THREE U and TWO DIŠ have no Unicode numeric character, so repeated U glyphs are right (as the pilot's 𒁹𒁹).
- II 43: the šar₂ cluster reads as three pairs of diamonds = 6; the geš'u are drawn as two upright signs each carrying two corner wedges = 4; then 8 geš (4 over 4), 3 u, ITI, 3. = 24,510, Langdon's figure. The drafter's caution on the šar₂ count stays.
- II 9: confirmed only two MU signs after KA-LU, then the numeral; the drafter's reading ka-lu-mu + mu and its stated uncertainty stand.
- II 32: third sign is a large many-wedged sign, not a single Winkelhaken; U₃ kept as an uncertain identification. The geš'u's upright stands apart from the corner wedge, so the group looks like 1 + 10 + 5, as Langdon fn. 2 says.
- II 45: the verb is one compact sign (upright with two horizontals); PA.GAN₂ = sig₃ kept with the note's uncertainty.
- II 30: third sign is boxed with an inner corner wedge; GAN (Langdon kàr) kept, the note already marks it uncertain.
- I 46: GUL LA AN [NAGA-like] AN NA, a damaged stretch about one sign wide, EL. LACUNA placement right; fn. 6 (ezen) reported.
- I 43: damage hatching before GA₂ visible on the copy, matching fn. 5.
- House formulae: "In Kish, Ĝa-ur became king; he reigned …"; "X reigned N years" for later kings; "became king; he reigned" for lugal-am₃ entries (Etana, Enmenbaragigur); "Twenty-three kings reigned …"; "Kish was smitten with weapons; its kingship was carried to Eanna." All consistent.
- Lemma strings match the pilot (nam-lugal, -la, ni-ag, ib-ag, mu-bi, -bi, -šú, ba-gín, -am₃, {d}, geš'u, geš, u, diš, lugal, mu, an); glosses consistent.
- Sign keys all exist in signs-cuneiform.json; roles checked.

### Findings considered and refused

- II 14 change the DA key to NI · refused: the copy's shape matches NI, but Langdon reads dā and NI has no da value that would give a reading; the plate alone cannot settle the sign, so it is flagged in the note, not changed.
- II 1–4 as one lost unit (conventions: "a lost entry = one lost unit") · refused: the conventions also say "a wholly lost line is a gap unit", and validate counts lost units per line; four line units are accurate.
- II 5 / II 6 show Langdon's restored signs in brackets (conventions keep restorations) · refused: Langdon's restorations here are themselves question-marked guesses ("?e?", "?") with no reign figures; showing only preserved signs + gap with the restoration quoted in the note is the more honest course, and the drafter says so.
- II 28/30 KIŠIB shown with the MES character · refused: Unicode has one character for MES/KIŠIB; the note says so.
- II 30, 39 numeral lemma style ('5'/'6' vs 'diš') and tr "3 diš" vs the pilot's "3" · refused: cosmetic, no reader-facing error.
- II 35 i "made the weapons of the land of Elam bow down" sounds odd · refused: it follows the form (tukul-bi object of gam); the note gives Langdon's alternative.
- II 42 "ib-ag … the plural 'they ruled'" (the -b- is not strictly a plural marker) · refused: identical to the published pilot's gloss; changing it here only would split the glossary.
- II 39 note's mention of the Agga–Gilgamesh story · refused: general background, not a translation.

## Pass 2

Every gloss.json entry checked against units.json, packet.md and Langdon pp. 10–11 (langdon1923_0015/0016.jpg, transliteration, translation and footnotes); Plate I re-read at II 29–31 and II 45–47. Edits by script (scratchpad rev2.py), no cuneiform retyped.

### Changes — gloss.json

- e₃ · __broaden__ · major · the pilot entry 'to descend (verb e₃)' would have been shipped as the glossary sense of e₃ in II 17 ba-e₃-de₃ 'went up (to heaven)', the opposite direction; the glosser did not broaden it · added under "__broaden__": old entry whole + " · to go out, go up (also written UD.DU; Langdon ĕ)".
- ar-pi-u₂-um · gloss · major · said the name's "second sign (Langdon dā) is shown as DA … uncertain" — dā is the second sign of maš-da, not of Arpium (whose second sign is PI) · clause removed; entry now: king of Kish, son of a maš-da (Langdon 'a poor man'), u₂ = Langdon ú, Nippur variants.
- tukul · gloss · major · "no case ending in the list, 'with weapons' being understood in the closing refrain" — false for II 37 {ĝeš}tukul-bi, the object of ib-ta-an-gam, and pinned to one use · now general: weapon, mace — KU with the wood determinative (Langdon ᵍⁱˢku).
- kiš · gloss · major · "it has no case ending … 'in' being understood" is false at II 45, where Kish is the subject of ba-an-sig₃; also garbled ("first dynasty after the Flood, to which the list returns after the Flood") · rewritten general, after the unit's morph gloss: city in northern Babylonia, seat of the first dynasty after the Flood; KIŠ + place-det KI.
- maš-da · gloss · minor · "his dā sign" ambiguous about which sign · now "the second sign (Langdon dā) is drawn on his copy like NI, so its identification as DA is uncertain" (as the II 14 note).
- bu-[…] · gloss · minor · said Langdon "restores 'Bu-Sin (?)'"; he restores Bu-ᵈ[En-zu] and translates 'Bu-Sin (?)' · corrected.
- […] · gloss · minor · pinned to the four lost lines of Col. II, though the lemma is also used in I 46 and II 5 · now general.
- -ke₄ · gloss · minor · pinned ("absent after dumu enmenunna in one line") · generalized ("not always written"); grammar label kept (genitive -ak + ergative -e).
- e-ta-na · gloss · minor · carried his reign (1,500 years) — line data · removed.
- ba-li-iḫ · gloss · minor · carried a Nippur variant reign (410 years) · removed.
- ba- · gloss · minor · pinned to ba-e₃-de₃ and the Nippur spellings · general prefix gloss kept only.
- mu-un-, gi-n, gam, ma-da, -ma, ib-ta-an-, sipa · gloss · minor · each pinned to its line ("in mu-un-gi-na", "Langdon translates 'with his weapon subdued'", "in ma-da elam{ki}-ma", "of the line", "in Etana's entry") · generalized; gam now 'to bend, bow down; (with -n-) to make bow down, subdue'.
- šu-ši, 6, 23, iti, u₄-maš, e₂-an-na · gloss · minor · pinned to II 31 / II 42–44 / II 46 ("5 šu-ši + 6 = 306", "in the dynasty's total", "as in maš-da", "the city whose kings come next") · trimmed to the general sense in the pilot's terse format.
- ba-an- · gloss · minor · justified itself by "the passive English of the refrain" (pinned to the translation of one line) · now ba- (often motion away / middle-passive) + -n-, ordinarily a 'he' who acts.
- dumu · gloss · style · "Langdon reads it as 'son'" added nothing · now "'dumu X' = 'son of X'".

Checked and kept: ĝa₂-ur, gul-la-{d}nidaba-an-na-[…]-el (fourth sign = NAGA after the det., consistent with the I 46 note), ba-[…], ga-li₂-bu-um (fn. 5: three Nippur copies — confirmed), ka-lu-mu, dug₄-ga-gi₄-ib (fn. 7 confirmed on p. 10), a₂-tab, a₂-tab-ba, lu₂, kur-kur, en-me-nun-na, me-lam-kiš (fn. 17), bar-sal-nun-na (fn. 18), tup-za-aḫ (fn. 19), ti-iz-kar₃, il-ku-u₃, il-ta-sa-du-um, en-me-en-bara₂-gi-gur, elam, {ĝeš}, ag-ga, u₄, sig₃. Langdon's translations quoted in the units ('son of a poor man', 'made the foreign lands faithful', 'with his weapon subdued', 'Bu-Sin (?)', 'Baba(?)') verified on pp. 10–11. Pilot entries used here (lugal, mu, mu-bi, ni-ag, ib-ag, -bi, -šú, -la, an, nam-lugal, ba-gín, -am₃, {d}, numerals) cover this part's uses; only e₃ needed broadening.

### Changes — units.json

- II 35 (II 35–38) · l · minor · ib-ta-an-gam rendered "bent-down", which reads as intransitive and drops the -n- 'he' that i ("made … bow down") and the note rely on · now "he-made-bow-down".
- II 42 (II 42–44) · n · minor · "ib-ag … is the plural 'they ruled'" misnames the form: the -b- of ì-b-aĝ₂ is not a plural marker · note now says it is the reign verb of the totals rendered 'they ruled', its -b- the third-person non-personal marker, the plural English following the sense. (Pass 1 refused this to keep the pilot glossary; the glossary entry is left as published — only our note's grammar label is corrected.)
- II 5 · i · style · "Ba[…] …" vs II 6 "Bu-[…] …" · now "Ba-[…] …".

### Re-checked, no change

- Arithmetic: the 19 reigns sum to 15,751; 6 šar₂ + 4 geš'u + 8 geš + 3 u = 24,510 — the II 42 note is right.
- Plate II 45: KIŠ KI GIŠ KU BA AN + one compact final sign; no rule between 45 and 46 on the prism (Langdon's printed rule under 45 is his layout; the prism's rule is below 47), so the II 45–46 unit stands. II 30: third sign boxed with inner wedge, GAN kept with the note's doubt.
- House formulae, l ↔ i, notes ↔ morph glosses: consistent after the changes above.

### Findings considered and refused

- II 16 an-še₃ uses modern še₃ where the pilot prints Langdon's -šú · refused: conventions ask for modern subscript readings; the lemma stays '-šú' so the glossary entry is shared.
- II 45 sig₃ shown as two glyphs PA + GAN₂ while the copy draws one compact sign · refused: no better identification from the plate alone; the note and glossary already say the identification is uncertain.
- II 14 l "son of a-mašda" (odd hyphen) · refused: the hyphen joins the English for one Sumerian word, as house l does; harmless.
- Pilot glossary 'ib-ag … (plural reign verb)' · refused to change here: published entry; the owner can revise it across parts (flag for QUESTIONS.md if desired).
