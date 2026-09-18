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
