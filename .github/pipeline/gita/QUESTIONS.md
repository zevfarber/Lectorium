# Bhagavadgītā pipeline — open questions

## bhakti — translate or leave untranslated? (raised drafting chapter 11, 2026-09-20)
conventions.md's untranslated-terms list is dharma, yoga, brahman, the three guṇas, sāṃkhya. bhakti is
not on it. Chapter 11 verses 54-55 use it twice (bhaktyā tv ananyayā, mad-bhaktaḥ) at the chapter's own
thematic hinge into chapter 12, Bhaktiyoga — "The Yoga of Devotion". Decided meanwhile: translated as
"devotion" in both places, consistent with how chapter 9's trans.txt already handles bhaktyā throughout
(always "devotion", never left untranslated) — so ch.11 does not deviate from existing practice. Worth
a deliberate call, one way or the other, when chapter 12 is drafted and the term becomes central and
recurs many times: if it stays translated, unify the chapter's own title-word treatment with that
choice (as jñāna, karma, etc. are handled in other chapter titles); if the pipeline decides bhakti
should join the untranslated list instead, chapters 9 and 11's existing "devotion" renderings would
need a follow-up pass to conform. Update, chapter 13 (2026-09-20): bhakti recurs once more (v.10,
mayi cānanyayogena bhaktir avyabhicāriṇī) and is again translated "devotion", still consistent with
chapters 9, 11 and 12 — practice has settled on "translated" through five occurrences across four
chapters with no dissent, so this can likely be treated as decided rather than open, but the formal
convention.md untranslated-list line has not been explicitly amended to note the exclusion.

## word-division-only vulgate/BORI differences — do they belong in variantsVsBORI? (raised drafting
## chapter 13, 2026-09-20)
Chapter 13 verse 12's two witnesses read identical letters (anādimatparaṃbrahma) but divide them
differently — Wikisource's spacing gives anādi mat-paraṃ brahma ("beginningless, having me as its
highest, brahman", naming Kṛṣṇa explicitly), BORI's gives anādimat paraṃ brahma ("possessing no
beginning, supreme brahman", no personal reference) — a real difference in traditional sense despite
being letter-identical. conventions.md's collate() classifies anything letter-identical as `orth`
("is nothing," not logged), reserving `VAR` (logged in parts.json's variantsVsBORI and stated in the
verse's note) for letter-level differences — which is what gita_lib.collate(13) actually reported:
only 13.20 as VAR, not 13.12. The chapter 13 drafter and reviewers judged 13.12's difference worth
explaining in the verse's own note anyway (drafted, then sharpened on review to state the sense
actually differs, not just the spacing) without adding "13.12" to parts.json's variantsVsBORI, since
strictly it is `orth` by the letter of the rule. Left as a note-only treatment for now; worth a
deliberate call on whether the collation convention should be extended to flag word-division
differences that change traditional sense even when no letters differ, the next time such a case
turns up (a search across chapters 1-12's existing variantsVsBORI entries for any similar
word-division-only case was not attempted this run).

## puruṣottama — "supreme Person" or "the Supreme Person"? (raised drafting chapter 15, 2026-09-21)
**RESOLVED 2026-09-21 (owner's decision, applied in an attended Cowork session).** House rendering:
"Supreme Person", capitalized, in `l` and `i` at every occurrence; chapters 8 (v.1), 10 (v.15) and
11 (v.3) conformed in their drafts and rebuilt (all PASS); the two possible senses of Arjuna's
vocative are stated in the word's gloss at 8.1, 10.15, 11.3 and 15.18. See `conventions.md`,
"House renderings of recurring terms". The general rule the owner gave with it: normalize a
recurring term, and where one rendering hides a real ambiguity, put the ambiguity in the glossary
entry. The original note follows for the record.

Chapters 8 (v.1) and 10 (v.15) render puruṣottama, addressed to Kṛṣṇa as a vocative epithet, as
lowercase "supreme Person" in their idiomatic lines. Chapter 15 (v.18, v.19), where puruṣottama
becomes Kṛṣṇa's own declared identity and gives the chapter its name, was drafted and reviewed as
capitalized "the Supreme Person", to match this pipeline's existing capitalization of the chapter's
other technical terms — "the Person" (puruṣa), "the Perishable" (kṣara), "the Imperishable" (akṣara)
— all proper-noun-like renderings of a fixed philosophical term. Decided meanwhile: left chapter 15 as
capitalized and did not touch chapters 8 or 10, since reconciling three chapters' wording is outside
one chapter's own run and chapters 8/10's lowercase form was each individually reviewed and passed at
the time. Worth a deliberate call on which capitalization is the house style, with a follow-up pass to
conform chapters 8 and 10 if "the Supreme Person" (capitalized) is chosen — noting chapter 11 already
renders the same term differently again ("highest of beings"), a third variant also outside this
chapter's scope to fix.

## brahma-karma (18.42) — brāhmaṇa's duty, or the untranslated metaphysical brahman? (raised
## drafting chapter 18, 2026-09-22)
**RESOLVED 2026-09-22 (owner's decision).** "The brahmin's duty", matching the other three varṇa
verses; the published 18.42 already reads so and stands. Recorded in `conventions.md` ("Untranslated
terms" and "House renderings of recurring terms") so no later drafter has to rediscover it. The
original note follows for the record.

conventions.md keeps brahman untranslated wherever it names the cosmic absolute (its usual sense
at every prior occurrence, e.g. chapters 2-3, 8, 13, 17). 18.42's brahma-karma is different: in
context it stands beside 18.43's kṣatra-karma and 18.44's vaiśya-karma/śūdra-karma, naming the
brahmin's own caste-duty (short for brāhmaṇa-karma), not a claim about brahman-the-absolute.
Decided meanwhile: rendered "the brahmin's duty" to match the parallel construction, with the
departure from the blanket untranslated-brahman rule flagged explicitly in both the word's gloss
and the verse's note, rather than left implicit or silently generalized into a new exception.
Worth the owner's eyes since it is the one case in 18 chapters where "brahma-" as a compound
member does not mean brahman itself; if this reading is endorsed, it may be worth a one-line
addition to conventions.md's untranslated-terms section noting brahma- as a bound member can name
brāhmaṇa, so a future chapter's drafter does not have to independently rediscover it.

## 18.78 dhruvā — modifying nītiḥ alone, or the whole preceding list? (raised drafting chapter 18,
## 2026-09-22)
**RESOLVED 2026-09-22 (owner's decision).** Leave dhruvā ambiguous, as drafted: the translation does
not pick a reading and the note states both. Recorded in `conventions.md`, "House renderings of
recurring terms". The original note follows for the record.

The Gītā's closing verse names śrīḥ, vijayaḥ, bhūtiḥ and nītiḥ (mama, "mine") wherever Kṛṣṇa and
Arjuna are, and adds dhruvā, "certain, firm" — grammatically feminine singular, which agrees with
the nearest noun nītiḥ but could as plausibly be read (per the verse's own rhetorical shape) as
applying to the whole quartet. Decided meanwhile: left the ambiguity open in the note rather than
silently picking a reading, per the pipeline's standing practice of surfacing real ambiguities in
the note instead of resolving them in the translation (cf. the puruṣottama vocative question at
8.1/10.15/11.3 before it was settled). No action needed unless the owner wants a firm reading
recorded as house style for this, the poem's final verse.
