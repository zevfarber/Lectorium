## Pass 1

Reviewer pass 1, 2026-11-15. All edits were made by script (scratchpad review1.py, review1b.py; json.dump with ensure_ascii=False, indent=1). No sign key was changed. Dry-run validation: 0 errors. 3 warnings, all expected: logograms with no val, namely CAPUT §34 (deliberate, see below), PES₂.PES₂ §35 (reading unknown) and TERRA+LA+LA §37 (reading uncertain).

### Changes

- all § · det glyph `tr` · minor · 26 determinatives had their Latin name as `tr` (LITUUS, PES, CASTRUM, BONUS, OCCIDENS, L274, SOLIUM, DEUS, FINES, MANUS, DIES, PES₂, FUSUS, CORNU+RA/I, LINGERE, URBS). The pilot uses "" for every determinative (checked: all 36 det glyphs in §1–§21). · Set every det `tr` to "".
- §22 · n · minor · "the corpus flags the chain's spelling as irregular" overstated ACLT's bare "!!!". That mark is unresolved (lemma None, gloss "?") and is not a stated diagnosis. · Reworded to "the corpus leaves an unresolved query mark at the end of the chain".
- §22 · n · minor · "under the feet classifier": PES (A090) is the single foot sign. The morph already said "foot sign PES". · Changed to "the foot classifier PES".
- §23 · l · minor · "And indeed …": no Luwian word stands behind "And" (kwippa=wa=tta, and kwippa = "indeed"). · Changed to "Indeed in those places I built fortresses within,".
- §24 · i · minor · "so that Hiyawa might live at ease" adds purpose and a modal. asai is a present indicative, and kwadi is a relative instrumental ("by which"). · Changed to "through which Hiyawa lives at ease."
- §25 · i · minor · The sentence began with lowercase "and" after §24's full stop. "in the west" lost tawiyan's "toward". · Changed to "And I tore down mighty(?) fortresses to the west,".
- §25 · n · style · The =ha=wa reading of -há-wa/i was honestly marked as this edition's own, but the support from Ho. was not cited. · Added "(the copy at the other gate writes hattaliha=wa)".
- §28 · i · major · The unit had no `i` (every non-absent pilot unit has one). · Added "But I, Azatiwada, destroyed them."
- §29 · i · minor · It began with lowercase "and" after a full stop and had no closing punctuation. · Changed to "And I brought them down,".
- §29 · n · minor · "The pair of feet (PES)" is wrong: PES is the single foot, and the pair is PES₂. · Changed to "The foot sign (PES)".
- §30 · i · style · "in the east" lost tawiyan's "toward". · Changed to "toward the east".
- §31 · l · minor · "And Hiyawans then …": kwippa was rendered as an unexplained "And", which is inconsistent with §23 and §35. · Changed to "Indeed Hiyawans then I settled down there."
- §31 · n · minor (point 4) · "another case of d, l and r trading places" overclaimed. The data show zi-tà (a d/t sign) read zira, which is the familiar d → r (as in Azzattiwaras). The lemma zila is the corpus's filing. Nothing in this part shows a general l/r or d/l interchange. · Reworded to "spelled zi-tà, the d sounded r as in Azzattiwaras; the corpus files the word under the lemma zila".
- §31 · w0 nl · minor · ACLT records a register break at the end of §30 (line_break_after_clause, with the source's note on pilot convention), but §31's first word had no `nl`. · Set `nl: true` on kwippa=wa.
- §33 · n, w2 morph glosses · minor · The corpus's << >> means "erased/superfluous" (source field guide), but the draft said "written in error". · Changed to "erased or superfluous" in the note and the three morph glosses.
- §34 · reading/say, CAPUT val, morph lemma, n · major (point 7) · The val ziti for CAPUT is not secure here. ACLT reads the word CAPUT-tt(i)-, leaves its Luwian form open, and does the same at §60, §61 and §73. Its double tt also argues against ziti-. · Removed the val. reading/say are now "CAPUT-ttis=wa=di" (the ACLT form). The morph lemma is now CAPUT-tt(i)-, with a gloss saying §1/§20 read ziti-. The note is rewritten to say the logogram is left unvoiced. The validator now gives a no-val warning, which is intended.
- §34 · i · minor · "would be afraid" adds a conditional to a present indicative (kwissai). · Changed to "where a man is afraid to go along the road —".
- §35 · i · minor (point 8) · "go out on foot, spindle in hand" adds "out" and "on foot" (the verb is "walk, pass"). "Spindle in hand" is a ready-made English formula, so it risks echoing a familiar phrasing. Rebuilt from the grammar: kwippa=wa (left unrendered in i), ammiyanza halliyanza dat. pl. "in my days", wanattinzi=ha nom. pl. + =ha "too", sittari instrumental "with spindle(s)" (number not marked), PES₂.PES₂-danti pres. 3 pl. "walk". · New house rendering: l (unchanged) "Indeed in my days women too walk with the spindle." / i "In my days women too walk about with their spindles." The note's last sentence was adjusted to match §34 ("on roads a man feared to travel").
- §36 · n · minor · "Three nominatives in -s are chained by =ha" was wrong. There are four nominatives (suris, hassas, sanawizzas, asiyas) and two =ha. · Changed to "Four nominatives in -s follow, linked by two =ha 'and';".
- §37 · w4 morph lemma, n · minor (point 6) · The morph carried the pilot's warra- "plain", but ACLT's lemma is walilid(a)- "territory". TERRA+LA+LA (two la) fits walilid(a)- better than §5's warra-, which is spelled wa/i+ra/i, so this may be a different word. · Morph lemma set to walilid(a)- ("territory, open land … reading and meaning uncertain; §5's warra- is spelled differently"). Reading warranza kept (ACLT's transcription). l/i keep "plain" for consistency with §5, and the note now says all of this.

### Considered and refused

- Point 2, fused =wa=ada (§28) and =wa=di (§34) on the one ligature glyph wa/i+ra/i: accepted. A single glyph cannot be split, and the pilot does the same (=an=tta §16, =ada=tta §13).
- Point 3, §25 hattaliha=ha=wa: accepted. The note says plainly that the corpus prints only hattaliha and that the =ha=wa reading is this edition's. The spelling -ha-há-wa/i parallels §5 latrahha=ha=wa. Ho.'s =wa is now cited.
- Point 5, keys: no change. sign-verification.json gives A201 = "terra, locus" (LOCUS and TERRA are one sign) and A079 = "femina, mater". MATER in the pilot and FEMINA here are the same key, and the validator passes. The §35 note ("the same woman sign that wrote 'mother' in §3") is correct.
- Point 7, vals kept: L274=hatta (backed by L274 as a classifier before the fully spelled ha-ta-li- in §26 and §28, with ta as complement), LOCUS=al (the same pattern as the pilot's PUGNUS=al), INFRA=zanta, OCCIDENS=iba, ORIENS=kista, FRONS=hanti, PRAE=parra, VIA=harwa, FEMINA=wanatti, SOLIUM=asa / SOLIUM.MI=asi, BONUS+RA/I=warri, FINES+HI=irhi, CASTRUM=harnissa, PONERE=tuwa. Each is ACLT's reading of the word minus its spelled-out signs, as with the pilot's word-specific vals (INFRA=an, PUGNUS=al). For several of them the full syllabic spelling occurs elsewhere in this part or in the pilot. The different vals for SOLIUM (asa/asi) are word-specific, as INFRA=an/zanta is. Only CAPUT was removed.
- kwippa lemma: the pilot (§11) has "kwi=pa — but, however", while the draft uses ACLT's kwippa "indeed". Kept ACLT, because morph lemmas follow ACLT facts. The pilot's mismatch is flagged as an open question below.
- ami(ya)- / isnuwa- / =pa for ACLT ammi(/a)-, isnu(wa)-, ba: kept the pilot's lemma forms for glossary consistency. They are the same lemmas.
- halliyanza morph (ia inside the stem rather than in -yanza): left as is. It is harmless and close to the pilot's halli-.
- §26 i "never" for na "not": kept, to match the pilot's §21 i ("had never submitted").
- §28 l "But" vs §22 "And" for =ba: both fit a topic shifter, and "But" carries the contrast with the earlier kings in §26–27.
- §33 "neuter plural subject with a singular verb": kept. This is standard Anatolian agreement and matches ACLT's 3 sg asta with neuter plural kwaya kwissanta.
- §35 sittari ending gloss "-ri": kept. I considered adding "-adi sounded -ari", but it is not necessary and the gloss is not wrong.
- §36 hassa- "satiety(?)" vs ACLT "luxury": kept the pilot's English, and the note already reports ACLT's gloss.
- I checked every glyph's tr and role against the source (tr identical, roles det/log/phon with comp only where the source has phon), every glyph/word `nl` against lb_before, and every morph g index (no overlaps, no out-of-range indexes, every non-det glyph covered). Apart from §31 w0 nl, no discrepancy was found.

### Open questions for the owner

1. CAPUT: the pilot reads CAPUT-ti-(i)-sá as zitis (§1, §20, and conventions.md cites "CAPUT → ziti" as a model val). ACLT reads CAPUT-tt(i)- with the word left open, here and at §60, §61 and §73. This pass followed ACLT for §34. Should the pilot be brought into line, or should ziti be restored here and in later parts?
2. The kwippa lemma differs between the pilot (kwi=pa "but") and this part (kwippa "indeed"), so the glossary will carry two entries.
3. The pilot still keys BONUS as A320. sign-verification.json lists this among the pilot's wrong identifications (BONUS = A165), but conventions.md corrects only SUPER, tu and INFRA. This part uses A165 correctly.
