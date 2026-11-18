# Reviewer brief — ani-125-address, pass 1 (adversarial)

Lectorium edition of the Book of the Dead; part ani-125-address is a SUPPLEMENT (not on Ani's papyrus): the address to
the gods after the 42 declarations, Budge 1895 pp. 203–213 (his Appendix from Naville). Folder:
/home/user/Lectorium/.github/pipeline/ani/ . Read: conventions.md; drafts/ani-125-address/packet.md (the established
words with Budge's transliteration and English — a check on signs and sense only); drafts/ani-125-address/known-lemmas.json;
/home/user/Lectorium/ani-spell125-opening.json and /home/user/Lectorium/ani-125-introduction.json (published parts:
house renderings, note style). No modern translation is opened or recalled; no web.

Your input file (half of the draft): drafts/ani-125-address/chunks/review-in-<N>.json ({"sentences": [units]}).
Check, unit by unit, word by word:
1. every glyph's role and tr against the word's reading (phon/comp/det/log/suff/num as in conventions.md; det has tr "");
2. every reading against the signs and against Budge's transliteration (disagreeing with Budge is fine when the signs
   support it and the note says why);
3. every grammatical label in every note against the form (verb forms, stative, sḏm·n·f, participles, pronouns,
   particles); 4. `l` word by word against the Egyptian; 5. `i` against `l` in sense and force;
6. Budge-isms or remembered modern-translation phrasing in l / i ("homage", "saith", "thee", "triumphant" ...);
7. names and renderings consistent with the published parts and across this half (same word, same English);
8. `say` per conventions; 9. the notes never call the writer "Ani's scribe" (supplement); doubtful readings are said to
be doubtful; misprint-rule notes open "The text writes X; read Y."
Lemma keys: keep them as they are unless one is plainly wrong; the morph "gloss" per-occurrence overrides are allowed.
DO NOT change any glyph's "sign" or the order or number of glyphs (the established signs are fixed; the build compares
them). You may change role, tr, reading, say, morph (lemma/g), l, i, n, p, ln; you may join/split words only if
glyph order is unchanged and q is re-indexed accordingly (avoid unless necessary).

Edit by script: write the corrected half to drafts/ani-125-address/chunks/review-out-<N>.json (same shape), and
write drafts/ani-125-address/chunks/review-<N>.md: a list of every change — unit index (within your file) · field ·
severity (major = wrong sense/grammar/reading; minor = imprecise label, role/tr, say, consistency; style) · what was
wrong · what you did — and every finding you considered and refused, with the reason. End with counts by severity.
Self-check before finishing: the flattened glyph sign list of review-out equals that of review-in; every morph g-list
covers each word's glyphs once; every q covers its glyphs once.
