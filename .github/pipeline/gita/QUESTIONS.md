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
