# Bhagavadgītā pipeline — run log

2026-09-15 · chapter 1 · pilot, drafted in an attended session · 47 verses, 349 glossary keys · sources
collected for all 18 chapters (Wikisource through the owner's browser, BORI text from GRETIL), collated,
four misprints corrected, 28 vulgate/BORI variants listed; tooling (gita_lib, build_gita, validate_gita)
written and proved on chapter 1 (PASS).

2026-09-18 · chapter 2 (Sāṅkhyayoga) · unattended run · 72 verses, 549 glossary keys · source verified
(sha256 and collation both matched parts.json before drafting); drafted, reviewed in two passes (pass 1:
one overstated Kaṭha Upaniṣad note, one L-line mistranslation at 2.22; pass 2: one stale cross-reference
note at 2.39, one redundant speaker tag at 2.10), glossed on Sonnet (five epithet-identification/gloss-
consistency fixes); conventions.md amended to add sāṃkhya to the untranslated-term list. build_gita.py
and validate_gita.py both PASS (29 benign sandhi-boundary warnings, same class as chapter 1's). Housekeeping:
removed the chapter-1 pilot's superseded ad-hoc files (build.py, words-*.txt, trans.txt, wikisource-ch1.txt,
gretil-ch1.txt, wiki-parsed.json), now superseded by drafts/ch01/, source/ and build_gita.py.

2026-09-18 · chapter 3 (Karmayoga) · unattended run · 43 verses, 322 glossary keys · source verified
(sha256 and collation both matched parts.json before drafting; collate found VAR only at 3.2 and 3.8, as
listed, plus benign orth differences at 3.14 and 3.17); drafted, reviewed in two passes (pass 1: one real
gap — both occurrences of एष in 3.37 under-explained the sa-/etad-pronoun's irregular visarga-drop before
a consonant — plus wording/completeness nits at 3.12, 3.15, 3.40 and a synopsis gap in about.txt; pass 2:
found the same unflagged sa-/etad-visarga irregularity recurring at 3.10 and 3.40, plus unflagged -n+t-→-ṃs
t- at 3.25 and -n+a- written -nn- at 3.36, all fixed), glossed on Sonnet (three fixes: two tautological
guṇa glosses at 3.20 lacking the untranslated-term convention wording, one puruṣa gloss at 3.36 dropping
"a person" present at its other two occurrences). build_gita.py and validate_gita.py both PASS (16 benign
sandhi-boundary warnings, same class as chapters 1 and 2). No corrections.json entries and no house
renderings apply to this chapter. Added to stories.json after gita-ch02.

2026-09-18 · chapter 4 (Jñānakarmasaṃnyāsayoga) · unattended run · 42 verses, 317 glossary keys · source
verified (sha256 matched parts.json; collate found only benign orth differences, no VAR — no
variantsVsBORI and no corrections.json entries for this chapter). Drafted in three parallel batches
(verses 1-14, 15-28, 29-42) after a first single-batch attempt hit the drafter's own output-token limit;
house renderings for 4.7-8 used verbatim. Reviewed in two passes (pass 1: a wrong root for vīta at 4.10
(vī → vi-i), an untranslated "māyā" at 4.6 that should have been Englished, and six stale bare
verse-number cross-references that actually meant an earlier chapter — "verse 20/3/32/15" corrected to
"3.20/3.3/3.32/3.15", one instance of the last caught only on a re-check of the same note; pass 2: a
second leftover untranslated "māyā" in words.txt's morph gloss at 4.6, a siddhi/phala conflation at 4.12
mistranslating "success" as "fruit", and a false claim that moha opened the ch.1 dialogue at 2.1, when
that verse actually names kṛpā and viṣāda — corrected to cite 2.63's krodha-chain instead). Glossed on
Sonnet (five real fixes: karman/pra-vac/sam-bhū/budh gloss-wording drift against their other occurrences,
and prāṇa glossed four different ways across verses 27/29/30 including a self-contradiction within one
line at 4.29 — all standardized to "the outward, upward breath"; a suggestion to add parenthetical form
tags to ~45 bare-particle glosses was not applied, since ch01 already glosses particles like ca/tu/hi
bare throughout and validate_gita.py does not require it — declining rather than inventing a stricter
convention). build_gita.py and validate_gita.py both PASS (10 benign sandhi-boundary warnings, same class
as chapters 1-3). Added to stories.json after gita-ch03.
