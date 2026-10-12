# The Azatiwada inscription (KARATEPE 1, Hieroglyphic Luwian) — conventions (Run 3)

Distilled from the project's `hieroglyphic-luwian-conventions.md` (2026-07-11/12) and the published pilot
`azatiwada-luwian.json` (§1–§21), the model of shape and register.

## Why the pre-1930 rule cannot apply — the Luwian amendment (agreed 2026-07-11)
Karatepe was found in 1946 and the script's decipherment is post-1930 (revised again in 1973). So:
- the sign sequence is taken from the monument as documented — facts;
- facts from modern scholarship are allowed: sign values, transliteration conventions, lemma meanings,
  morphology (the Annotated Corpus of Luwian Texts, ACLT 2; eDiAna; Payne; sign lists; the Unicode proposal);
- expression from no one: no modern running English translation (Hawkins CHLI, Çambel, Payne, Bron for the
  Phoenician …) is ever open, consulted or paraphrased while drafting `l`/`i`.

## Source
`source/source.json` — ACLT 2 docs/96 (copy Hu., the base) parsed word by word, 2026-10-12: per clause the
transcription, the transliteration, each written word with register breaks (`lb_before` → word `nl`; inside a
word → glyph `nl`), its glyph-units and their signs (Laroche keys), damage, supplied/erased marks, and ACLT's
clitic-level lemmas, parts of speech, glosses and grammar; Ho. (docs/176) for reference. Raw pages in
`source/raw/`. Coverage: §17, §42, §43 and §46 are in neither copy as ACLT gives them; Ho. never preserves
more than Hu. from §22 on.

Sign keys verified 2026-10-12 against the Unicode proposal N4282 and the Unicode names list
(`source/sign-verification.json`, `source/ref/`): 113 of 117 labels verified. Treated with care (marked in the
packet): `ha` is keyed A215 as in the pilot (N4282 pairs A215/A215A as monumental/cursive forms; open
question); `rú` → A102 and `ara/i` → A134 (several signs carry these values; the base forms chosen); ANIMA and
COR have no verifiable sign → the ▢ placeholder (DAMAGED) with a note; `x` and `pa/ha` are damage notations.

## Script model (as the pilot)
Roles: `phon` syllabogram; `log` logogram (Latin caps); `det` determinative (in parentheses in ACLT; ^I = the
personal-name marker A383A; LITUUS A378 before Azatiwada's name); `comp` phonetic complement (ACLT does not
mark it — the drafter decides, as the pilot did: logogram + syllabic ending). Every logogram whose Luwian value is
known carries `val` (as in the pilot: CAPUT → ziti, TONITRUS → Tarhu): it drives the reader's signs | sounds |
words toggle. A ligature or compound (wa/i+ra/i,
OMNIS.MI, PES₂.PES₂) is ONE glyph with several keys. Word dividers and sign reversals are not reproduced;
ACLT's logogram quotation marks “ ” are dropped, as in the pilot. Lost signs: the DAMAGED placeholder ▢ (sign key
`DAMAGED`), tr "[…]" or the corpus's restored value with "?"; partly damaged signs keep their key and the note
says what is damaged. Supplied <…> signs are editorial: shown, and the note says so.
`reading` = the interpreted phonological word (Azzattiwadas, kwin); `say` = the readable word; `morph` splits
clitic chains (=wa, =mu, =ada) and case endings with their own lemmas and glosses (from ACLT's facts).

## Transliteration and pronunciation
Hawkins-style values as adopted by ACLT (Hiyawa in §2, with the note). Pronunciation: conventional scholarly
Iron Age Luwian values (z = ts, h = a rasped kh). `langCode: null`. No voice chosen; parts publish without audio.

## Translation and notes
- One unit per clause; `ln` = the clause number (§ chips). `l` follows the Luwian syntax; `i` real English from
  the `l`. Divine names as names (Tarhunzas, not "the Storm-God"); persons and places untranslated (Azatiwada,
  Awariku, Adanawa/Hiyawa, Muksas).
- Recurring patterns, flagged then nudged: the quotative/demarcational =wa in every clause; clause-initial clitic
  chains; logogram + complement spellings; REL kwi-; nominative -s / accusative -n; TONITRUS-hu-za-sa = Tarhunzas.
- The spindle clause (§35, FEMINA … (“FUSUS”)…): rendered fresh from the grammar, the literal following the
  Luwian; the idiomatic must not echo any published phrasing; record the wording as a house rendering.
- Honesty: readings are the most secure in the corpus thanks to the Phoenician parallel, but individual words and
  sign values remain debated — the notes say so.

## Decisions taken while setting up Run 3 (2026-10-12; in QUESTIONS.md)
- Parts: §22–§37 (the conquests and the safe roads, with the spindle clause), §38–§58 (the city and its god;
  the damaged and missing clauses), §59–§75 (the curses).
- §42, §43, §46 (absent in both copies) are gap units with `"absent": true`, like the pilot's §17.
- New parts use the verified keys; the 38 new signs they need were added to signs-anatolian.json (and the
  reader's embedded copy) at setup. The pilot uses keys N4282 does not support for SUPER (A270 → A070, §8–10),
  tu (A088 → A089, §20) and INFRA (A056 → A057, §21); the first Azatiwada firing corrects those five glyphs in
  `azatiwada-luwian.json` (keys and characters) and logs it. The pilot's
  §17 note ("survives only in the other copy") is not supported by ACLT; the same firing rewords it to say the
  clause is not preserved in either copy as the corpus gives them.
