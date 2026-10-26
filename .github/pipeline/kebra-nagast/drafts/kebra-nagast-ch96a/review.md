# Review, pass 1 (units only) — kebra-nagast-ch96a

`t` untouched: the t-join equals the packet text exactly (17 units; `p` flags unchanged: unit 0 heading and unit 1 are the only paragraph starts, as in the packet). Edits were made by script with exact-match assertions. `gloss.json` not touched. Units numbered from 0 (0 = heading).

Severity: major = wrong sense or a wrong claim a reader would act on; moderate = wrong grammatical label/lemma, an `l`/`i` mismatch in sense or force, or a break with a published part; minor = polish, hedging, house form.

## Changes

| # | Unit · field | Sev. | What was wrong | What was done |
|---|---|---|---|---|
| 1 | 6 · n, l, i | moderate | አምኑኒ was glossed "if they have believed ... -ኒ 'indeed'", leaving the -ኒ unexplained and weak. With God speaking, -ኒ may well be "me" (አምነ takes a direct object). | Note gives both readings (-ኒ "me" or enclitic "also"), prefers "me" with (?); `l` "if they-believed-me(?)", `i` "if they believe me (?)". |
| 2 | 11 · i, n | moderate | ኢነአምኖ is the indicative (ነአምን) but `i` had the jussive "Let us not believe in Christ" (force of the preceding ኢንስምዖ carried over); note named the form ንእምን; also it takes the object with ለ-, not "in". | `i` "We do not believe Christ."; note names ነአምን, 1cp imperfect indicative, distinct from the subjunctive ንእመን of unit 5. |
| 3 | 15 · l, i, n | moderate | ወርእየ is an active 3ms perfect; `l` "it-was-seen" and `i` "it was seen" supplied a passive the form does not have. | `l` "and-he-saw(?)", `i` "Moses saw (?)", note says the form is active, Moses likeliest, impersonal possible. |
| 4 | 6 · i; 8 · i | moderate | ዐበይተ was "nobles" in `l` but "elders" in `i`; "elders" belongs to አእሩገ (unit 7), and published parts (ch. 36, 76a, 88) render ዐበይተ as nobles / notables / great ones. | `i` "nobles of Israel" in both units. |
| 5 | 10 · i | moderate | "For the Word of God is Christ" gives a causal force the text lacks (ወ-…ሰ, "and the Word indeed"). | "Now the Word of God is Christ." |
| 6 | 2 · n | minor | Said ዘነሰኮ's -ኮ was "written" for -ዎ; it is ከ + ዎ fused. | Reworded. |
| 7 | 2 · n | minor | አመንደበ left rootless; ምንዳቤ "distress" (a known noun) is a plausible relative. | Added as a from-memory, unchecked comparison; sense stays (?). |
| 8 | 2 · i | minor | `i` "in bronze" against `l` "of-bronze(?)"; `i` dropped the (?) on ይትኤመርዎ that `l` and the note carry. | "a serpent of bronze (?)"; "see (?) it". |
| 9 | 4 · n | minor | Cross-reference "same phrase in unit 10" is wrong (unit 10 has ዘእግዚኣብሔር, not ቃለ እግዚኣብሔር). | "units 8 and 9". |
| 10 | 5 · l | minor | "to-him-alone-indeed(?)" glossed the question particle -ኑ as "indeed", contradicting the note and `i`. | "to-him-alone-(question)". |
| 11 | 5 · l, i | minor | ሐመይዎ: note says the root is inferred (?), but `l`/`i` unmarked. | (?) added at first use ("slandered(?)", "spoke against (?)"). |
| 12 | 7 · l | minor | `l` "lyre(?)" against `i` "harp (?)"; published ch. 55–56 renders ዕንዚራ "harps". | `l` "harp(?)". |
| 13 | 9 · i | minor | "We know now" drops ናሁ "behold", which `l` has. | "Behold, we know that God has spoken to you." |
| 14 | 11 · l, n | minor | `l` inserted "means", which is not in the Geʿez; note said ፨ "ends the paragraph" but the packet has no break there. | "means" removed (ብሂል "that-is" stays); note: "closes the section". |
| 15 | 12 · n | minor | "accusative" for ገጽከ; a noun with a suffix shows no accusative ending. | "the object of the imperative". |
| 16 | 13 · l, i | minor | Second መጽሔት ("mirror of my face") carried no (?) though the lexical call is uncertain. | (?) added in `l` and `i`. |
| 17 | 14 · i | minor | ምስብዒተ "sevenfold" is (?) in `l` and note, not in `i`. | "sevenfold (?)". |

Totals: major 0, moderate 5 (rows 1-5; row 4 touches two units), minor 12.

## Findings refused or left

- Units 2 (51 words) and 7 (57 words) exceed ~45 words, but neither has an inner ፤ to cut at; the cut rule needs a ፤, so left whole.
- Unit 9 `i` capital "Word" in the quoted "that Word": it is the author's Christological reading, matches unit 11, and l keeps "word". Left.
- Unit 13 `i` "as at a mirror": the "at" is interpretive, but the reading is marked (?) and the note says so. Left.
- Unit 1 ለትሠሮ: `l`/`i` passive "be rooted out / cut off" is not shown by the form; the note already states this and both fields carry (?). Left.
- Unit 5 `i` "spoke against" vs `l` "slandered": a looser English for the same word, consistent in both occurrences; left (marked (?) now).
- Unit 0 note "ዘ- 'of, that is'": loose but not wrong. Left.
- Words glossed with (?) in the note only (ትዕይንት, ሰገዲ/ወርዕዲ spelling): ትዕይንት "camp" agrees with published ch. 61; the spelling queries are orthographic and not translation cruxes. Left.
- Observation for the glosser, not changed here: known-forms.json glosses ወትሬኢ as "and she sees (3fs)"; in unit 13 it is 2ms ("you will see").

# Pass 2 (units re-check and full gloss check) — kebra-nagast-ch96a

Edits by script with exact-match assertions; `t` unchanged (checked before and after). Coverage re-run: every form of the 376 words is in known-forms.json, gloss.json or `__broaden__`; every novel form has a gloss entry; every `__broaden__` entry starts with the known entry verbatim + ' · '. All entries checked against the text and known-forms.json. No modern translations used; Dillmann not available, so lexical calls are from memory and are hedged where unsure.

## Changes

| # | Unit / form · field | Sev. | What was wrong | What was done |
|---|---|---|---|---|
| 1 | ይነጽሮ (unit 2) · gloss, l, i, n | moderate | Called a 3ms jussive. The spelling (ይነጽሮ, first-order ነ then ጽ) is the imperfect (jussive would be ይንጸሮ). Unit had "let-him-look-at" / "let him look". | Gloss: 3ms imperfect, volitive in force. l "he-looks-at"; i "shall look at"; n "imperfect (volitive in force)". |
| 2 | ኢንሰምዓ, ኢንሰምዖ · gloss; unit 9 n | moderate | Labelled 1cp jussive; ን-ሰ-ም spelling is the imperfect (ንሰምዕ). | Gloss: negated 1cp imperfect used as a refusal ("we do not hear / let us not hear"); unit 9 note fixed. i kept ("Let us not hear"), as force and for matching unit 11. |
| 3 | ኢንስምዖ · gloss; unit 11 n | moderate | Said to be a "variant spelling" of ኢንሰምዖ; it is the true jussive (ንስምዕ). | Gloss and note now say jussive spelling of the same words. |
| 4 | ኢነአምኖ · gloss | moderate | Gloss still had the pass-1-corrected error: "let us not believe in him", subjunctive. | "we do not believe him", 1cp imperfect indicative, not ንእመን. |
| 5 | አምኑኒ · gloss | moderate | Gloss "they have believed ... enclitic -ኒ" contradicted unit 6 (pass 1: -ኒ "me"?). | Gloss: "they believed me (?)", -ኒ as 1cs or enclitic, (?). |
| 6 | ተህየይዎ · gloss | moderate | Lemma ተሀከየ with "perhaps a corrupt spelling of ተህከይዎ"; the form is a regular 3mp + -ዎ of ተሀየየ (ተሀየዩ + ዎ), as unit 4's note and the known ch. 55-56 ተሀየይዎ say. | Lemma ተሀየየ, (?) kept, corruption claim removed. |
| 7 | በሲኦል · broaden | moderate | Known entry reads "as Sheol, by Sheol"; here it is "in Sheol" (place). | `__broaden__` added: 'in Sheol'. |
| 8 | ነገሮሙ · broaden | moderate | Known entry is the noun "their words"; here it is the verb "he told them". | `__broaden__` added: verb ነገረ + -ሙ. |
| 9 | ወትሬኢ · broaden | moderate | Task point: known 3fs; here 2ms. Existing broaden was close but lacked ወ-/G and the stem label form. | Rewritten: old entry whole + ' · ' + "'and you will see' (ወ- + 2ms imperfect, G: ...)". |
| 10 | ለዛቲ, ለደቂቀ, ለሙሴ · broaden | minor | Known entries give only "to/of" readings; here ለ- also marks the object (ኢንሰምዓ ለዛቲ ቃለ; ሐመይዎ ለሙሴ; አመንደብዎሙ ... ለደቂቀ) or names the owner (ሐሜቶሙ ለደቂቀ). | `__broaden__` added for each. |
| 11 | ይስምዑ · broaden | minor | Known "3mp imperfect"; the form is the subjunctive after ከመ. | `__broaden__` added. |
| 12 | የሐይዉ, ኢፈተዉ · gloss | minor | "spelled -ዉ" implied an irregular spelling; -ዉ is the regular 3mp ending after ወ. | Phrase removed. |
| 13 | ዘነሰኮ · gloss | minor | "written -ኮ" (pass 1 fixed the note, not the gloss). | "ከ + ዎ fuse as -ኮ". |
| 14 | ለትሠሮ · gloss | minor | A regular 3fs jussive of ሠረወ would be ትሥረው, not ትሠሮ; entry did not say so. | Added that the form does not match and the lemma is tentative. |
| 15 | Unit 2 · l | minor | l "vexed(?)" against i "tormented (?)". | l "tormented(?)". |
| 16 | Unit 2 · n | minor | Note said "root ተህከየ"; gloss lemma is ተሀከየ. | Note aligned to ተሀከየ. |

Totals: major 0, moderate 9 (rows 1-9), minor 7 (rows 10-16; row 10 is three entries).

## Checked and left

- ፺፮: follows the convention (፸ pattern, spoken ተስዓ ወስድስቱ with transliteration and English). Left.
- ሐጽ "arrow", ትዕይንት, ምንዳፍ, አመንደበ, ተአመረ, ተሀከየ, ደፈነ, ሐመየ, ቆባር, ግላ, መጽሔት: lemmata plausible but not checkable without Dillmann; all already carry (?), kept.
- Lemmata checked as real dictionary forms: ሰበከ, ኦሪት, አንሥአ, አኀው, ሰምዐ, ሕዝብ, ስቅለት, ከይሲ, አውየወ, አድኅነ, አርዌ, ሥዕል, ሰቀለ, ነሰከ, ነጸረ, ሐይወ, ሞተ, ኀልቀ, ወረሰ, ባሕቲት, ተናገረ, ሰአለ, ስርየት, አንጽሐ, ኀጸበ, ዐርገ, አዘዘ, ተአዘዘ, ፈተነ, ከሀለ, አኀዘ, ረዓድ, ጽላሎት, ፈርሀ, ርዕደ, ቆመ, ድንጋፄ, ነገረ, ኮነ, ርእየ, ክሕደ, ብህለ, አርአየ, ሜጠ, ምዕራብ, በርሀ, ነጽሮት, ፈተወ, ጸልአ.
- Left: ሰገዲ/ወርዕዲ -ዲ for -ዱ queries (orthographic, already (?)); ዛቲ with masculine ቃል (already (?) in note); ትስእል label (imperfect, fine for a 2ms asking).

## Unresolved (?) items

ለትሠሮ (lemma, passive sense), አመንደብዎሙ, ይትኤመርዎ, ተህከዩ, ተህየይዎ, ሐመይዎ/ሐመዩከ, አምኑኒ (me or enclitic), እምትዕይንት, ይትራሐቁ, ምንዳፈ, ፈተኑ, ቆባር, ወደፈኖሙ, ወርዕዲ, መጽሔት/መጽሔተ, በግላ/ግላ, ወርእየ subject (Moses or impersonal), ሰገዲ, ወየሐዩ (number), ዕንዚራ, ምስብዒተ, አውየወ, ዘብርት/ብርት.
