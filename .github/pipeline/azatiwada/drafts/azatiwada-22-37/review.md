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

## Pass 2

Coordinator decisions, recorded here: (1) CAPUT stays as ACLT has it (no val). The pilot's ziti is left alone, and the question goes to the owner. (2) kwippa gets its own glossary entry, separate from the pilot's kwi=pa. (3) The pilot's BONUS key A320 is not changed this firing and goes to the owner. gloss.json was edited by script (scratchpad review2.py). Dry-run with gloss.json passed into assemble: 0 errors, the same 3 expected no-val warnings (CAPUT, PES₂.PES₂, TERRA+LA+LA). Every morph lemma in units.json now has a glossary entry.

### Changes (gloss.json)

- CAPUT-tt(i)- · new entry · major · The lemma introduced in pass 1 had no entry. · Added: "man, person — written with the head sign CAPUT; the corpus leaves the Luwian word open (§1 and §20 read the sign ziti-)".
- walilid(a)- · new entry · major · The lemma introduced in pass 1 had no entry. · Added: "territory, open land — the corpus's lemma for TERRA+LA+LA (transcribed warranza); reading and meaning uncertain".
- kwippa · entry · minor · The entry did not mention the pilot's kwi=pa for the same spelling. · Now "indeed — adverb that opens a clause (the corpus's kwippa; the same spelling kwa/i-pa is written kwi=pa 'but, however' in §11)".
- tu(wa)-, allant-, hantili-, harwa-, wanatti- · entries · minor · Each called a logogram a "classifier": PONERE, LOCUS, FRONS, VIA and FEMINA are logograms in these words. · Changed to "written with …".
- asa-, warriyamalla, irhi-, hattal(a)i- · entries · minor · "classified by" was wrong or only half right. SOLIUM.MI and BONUS+RA/I (§37), FINES+HI (§32) and L274 (§25) are logograms in some words and classifiers in others. · Changed to "written with (or classified by) …".
- zanta · entry · style · Added that INFRA also writes annan.
- zila · entry · minor · The entry did not mention the form actually written here. · Added "also sounded zira".
- -una · entry · minor · "'to go'" tied the ending to one line. · Changed to "infinitive ending — 'to …'".
- -ri · entry · minor · The entry carried a line-specific remark about the sign tara/i. · Changed to "instrumental ending — 'with, by means of'".
- -nti · entry · style · "the n goes unwritten" was stated as a rule for every occurrence. · Changed to "the n is usually left unwritten".
- asiya- · entry · style · The wording was garbled ("as 'sit, dwell'"). · Rewritten.
- Attanawanni- · entry · style · Brought in line with the house place-name form. · Changed to "Adanawan, of Adanawa (Adana)".
- __broaden__ -nza · major · "accusative ending · dative plural ending; also neuter singular nominative" lumped unrelated endings and mislabelled one of them (the "accusative" -nza is the neuter nom./acc. singular). · Rewritten as two named endings: dative-locative plural, and neuter singular nominative/accusative.
- __broaden__ -i · major · The entry repeated the dative twice and kept "'upon army'". · Rewritten: "two unrelated endings spelled alike: on nouns, the dative-locative singular; on verbs, the 3rd person singular present".
- __broaden__ -ya · minor · The draft's "neuter plural … also dative" ran the homonyms together. · Rewritten as two named endings: dative-locative singular, and neuter nominative/accusative plural.
- __broaden__ -di · minor · The entry joined two line glosses ("'because of'" · "'by which'"). · Rewritten as one case: "ablative-instrumental ending — 'from, because of; by, with'".
- __broaden__ -ta · minor · The pilot's "(there) were" plus "was" read as a list of lines. · Now "3rd person singular past ending …; a neuter plural subject also takes it ('there were')".
- __broaden__ -nzi, -nta · minor · They joined pilot and line glosses. · Rewritten as general entries (common-gender plural nom./acc.; 3rd plural past).
- __broaden__ ibami-, kistami-, harnissa- · minor · Each had a case label ("dative case", "neuter plural accusative") appended to the lemma gloss. Case belongs to the ending, not the lemma. · Removed. Each now reads "written with or classified by …".
- __broaden__ ammu · minor · The entry kept the pilot's "written with EGO", but here ammu is spelled á-mu, and the dative was given only as a line note. · Rewritten as "I; also the dative 'me' … (spelled á-mu, or with EGO)".
- __broaden__ =mu, =pa, allummida-, Azzattiwada- · minor · Each was a "pilot · line" join. · Merged into one general reading each. allummida- now gives both the corpus's adjective reading and the noun reading.
- __broaden__ -n · new · minor · The pilot entry "accusative singular ending — 'whom'" was tied to one line (harwan here). · Changed to "accusative singular ending — marks the object".
- __broaden__ isnuwa- · new · minor · The pilot entry says "most of this word is restored — the stone is broken here", which is true only of §16. §30 and §31 are intact. · Changed to "seat, settle — 'make sit' (written with or classified by SOLIUM)".
- __broaden__ hassa- · new · style · Added ACLT's "luxury(?)" next to "satiety(?)", to match the §36 note.

### Considered and refused (pass 2)

- kwi=pa (the pilot glossary): its "but, however" differs from ACLT's kwippa "indeed". It is not used in this part, so a broaden entry would have no effect, and the pilot is left alone this firing. Recorded for the owner, and the new kwippa entry points to it.
- -ya: the pilot's §19 calls -ya a "dative plural". That was not repeated in the general entry (Luwian's dative plural is -nza), and the pilot itself is left alone.
- =ada, pad(i)-, aba-, parran, =wa=ada, =wa=di, usa-, abadi, a, kwissant(i)-, ruwan, kwissa-, i-, sitta-, (PES₂.PES₂)da-, sannawizz(a/i)-: checked against the packet and ACLT's labels. They are correct and general, so no change.
- The pilot entries used unchanged in this part (-s, -ha, -tta, =wa, =ha, =tta, =ada=tta, kwi-, as-, ami(ya)-, halli-, latra-, zin, tawiyan, anta, annan, na, tama-, kwittan, Ahhiyawa-, Ahhiyawanni-, hantawatti-, suri-) are general and fit their uses here.
- units.json, second full pass: I re-read every unit (l/i, notes, morph glosses, g coverage, roles, vals, nl) and found nothing further to change. The cross-references to §11, §1 and §20 inside two glossary entries were kept deliberately: they explain divergences from the published part.

### Open questions for the owner (carried)

1. CAPUT: the pilot's zitis (§1, §20) differs from ACLT's CAPUT-tt(i)- (§34 here, and §60, §61, §73 later).
2. kwi=pa (pilot) vs kwippa (ACLT) for the same spelling.
3. The pilot's BONUS key A320 is not corrected (sign verification gives A165).

## Orchestrator check (after pass 2)
- §26 · i · style · "had never destroyed" overstated plain NEG₂ na · changed to "had not destroyed".
