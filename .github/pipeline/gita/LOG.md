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

2026-09-18 · chapter 5 (Karmasaṃnyāsayoga) · unattended run · 29 verses, 217 glossary keys · source
verified (sha256 matched parts.json; collate found only one benign orth difference at 5.3, no VAR — no
variantsVsBORI for this chapter). Two adjudicated corrections applied and named in their verses' notes:
5.5 (stray ASCII colon: स: पश्यति → स पश्यति) and 5.8 (misprint श्रृण्वन् → शृण्वन्). Drafted, reviewed in
two passes (pass 1: wrong root for अश्नन् at 5.8 (ad → aś, distinct from the other aś at 5.21), an
unhyphenated compound reading at 5.18 (śvapāke → śva-pāke), an inconsistent su- hyphenation at 5.1
(su-niścitam → suniścitam, matching the chapter's own nir-/a- prefix practice), a duplicated relative
pronoun in 5.10's literal, a stray capitalized "the Lord" at 5.14 that should read the self per the
note's own gloss of prabhuḥ, and an incomplete note at 5.26 missing Śaṅkara's "on both sides (living or
dead)" sense of abhitaḥ; pass 2: a wrong participle count at 5.9 (twelve → thirteen), a swapped
cross-reference at 5.9 (3.28/4.12 citations reversed), a false verbatim-echo claim at 5.10 (3.30 does not
actually read "brahmaṇi ādhāya karmāṇi"), a miscited intra-chapter reference at 5.11 that was actually
4.21, an overclaimed recurrence of the compound apunarāvṛtti at 5.17 (the idea recurs, the compound does
not), an agent/action-noun mix-up for पाक at 5.18 (cooker → cooking), and an about.txt gap skipping the
brahmanirvāṇa sequence at 5.24-26). Glossed on Sonnet (five real fixes: ātman's "self, mind" vs "self"
and indriya's "sense-organ" vs "sense" — the latter inconsistent even within one token at 5.9 — both
unified; buddhi's "intellect" vs "intellect, understanding" unified to the fuller form; sukha's lemma
wrongly cited as the inflected "sukham" at 5.3 and 5.13, corrected to the stem "sukha", and duḥkha's
gloss wording unified; Kṛṣṇa's only appearance, at 5.1, given no identifying gloss, fixed. A suggestion to
add real dictionary content to the bare "yoga — yoga" / "brahman — brahman (kept untranslated)" /
"sāṃkhya — sāṃkhya" glosses was not applied: checked against chapters 1-4 and found to be the chapter-1
practice already carried through every published chapter, not a chapter-5 defect — declining rather than
inventing a stricter convention). build_gita.py and validate_gita.py both PASS (5 benign sandhi-boundary
warnings, same class as chapters 1-4). Added to stories.json after gita-ch04.

2026-09-19 · chapter 6 (Ātmasaṃyamayoga) · unattended run · 47 verses, 338 glossary keys · source
verified (sha256 matched parts.json; collate found the two variantsVsBORI already listed — 6.7
mānāpamānayoḥ/BORI mānāvamānayoḥ, 6.41 lokān/BORI llokān — plus one benign orth difference at 6.13, no
unlisted VAR). No corrections.json entries apply to this chapter. Drafted, reviewed in two passes (pass
1: a lengthened-vowel sandhi error at 6.1, niragniḥ mis-derived as nirāgniḥ; a matching visarga-vs-r
sandhi error at 6.47, antarātmanā mis-derived with antaḥ- instead of antar-; a stray an-/a- prefix typo
on the lemma for anirviṇṇa at 6.23; an untranslated-term slip at 6.27 where rajas was Englished as
"passion" in L and I against convention; an unflagged "the mind's" added to 6.33's literal where the
Sanskrit names only "fickleness" without indriya/manas; pass 2: one leftover instance of the same
6.1 nirāgniḥ/niragniḥ error, left uncorrected in the note's own trailing sandhi gloss after the main fix).
Glossed on Sonnet (name identification: kuru-nandana at 6.43, the chapter's only vocative epithet without
an "addressed to Arjuna" gloss, fixed; the yuj root standardized to one core gloss, "to yoke, join,
discipline (oneself)", across nine occurrences that had each been worded differently; three minor
wording-consistency polishes — vi-naś given its verb sense to match the file's noun-in-parens pattern,
sukha's "ease" occurrence restored to "happiness, ease", ātman's two "self, mind" occurrences unified to
"self"). Two harmless lemma-citation quirks (kim vs. kim-cit for the distinct -cana/-cit indefinite
particles; the homophonous but etymologically distinct aś "eat" and aś "obtain", and vid "know" and vid
"exist", cited under one lemma spelling) were left as is — correct as written, not chapter defects.
build_gita.py and validate_gita.py both PASS (24 benign sandhi-boundary warnings, same class as chapters
1-5). Added to stories.json after gita-ch05.

2026-09-19 · chapter 7 (Jñānavijñānayoga) · unattended run · 30 verses, 243 glossary keys · source verified
(sha256 matched parts.json; collate found only two benign orth differences at 7.27-28, no VAR — matching
the empty variantsVsBORI list). No corrections.json entries apply to this chapter. Drafted, reviewed in
two passes (pass 1: v.1 युञ्जन्मदाश्रयः and v.23 मद्भक्ता both mis-derived with the compound stem mat-
instead of mad- before a vowel/voiced consonant — cf. ch01's mad-arthe; v.14's गुणमयी reading missing its
compound hyphen against v.13's own guṇa-mayaiḥ; v.27's epithet lemma Parantapa left lowercase against
convention; v.30's adhibhūta/adhidaiva/adhiyajña left untranslated in L/I though none are on the
untranslated-term list, inconsistent with v.29's own adhyātma. Pass 2: a leftover "mat-āśraya" in v.1's
āśraya morph note not updated when its sibling entry was fixed in pass 1; three false "first occurs in
this chapter" epithet-novelty claims at v.7 (Dhanaṃjaya), v.11 (Bharatarṣabha) and v.27 (Bhārata,
Parantapa) — all three epithets already used in earlier chapters; v.8's claim that the self-manifestation
catalogue's "I am" is "made explicit only once, in prabhāsmi" — false, asmi recurs explicitly through
vv.9-11 too). Glossed on Sonnet (a name re-identification at v.10's पार्थ, repeating v.1's full etymology
instead of a brief nudge, fixed; a garbled sandhi note and a dropped gloss word at v.20's प्रपद्यन्तेऽन्य-
देवताः, fixed; minor wording-consistency polishes — para's "beyond, higher"/"higher, supreme" split
unified, bhaj's "to worship"/"to worship, revere" split unified, yathā/tathā given the "(adverb)" tag
every other adverb in the chapter carries, and māyā's one-off inline "(Monier-Williams)" citation dropped
to match the plain-gloss style used at its other three occurrences). ā-sthā's two distinct renderings
across v.18 (āsthitaḥ, 'grounded in') and v.20 (āsthāya, 'having adopted [a rule]') were left as is —
genuinely different senses of the same root given their different objects, not a chapter defect. build_
gita.py and validate_gita.py both PASS (16 benign sandhi-boundary warnings, same class as chapters 1-6).
Added to stories.json after gita-ch06.

2026-09-19 · chapter 8 (Akṣarabrahmayoga) · unattended run · 28 verses, 219 glossary keys · source verified
(sha256 matched parts.json; collate found the one variantsVsBORI already listed — 8.7 vulgate asaṃśayam
[adverbial 'without doubt'] vs BORI asaṃśayaḥ [nominative 'there is no doubt'] — no unlisted VAR, no
corrections.json entries for this chapter). Chapter opens with Arjuna's five questions on brahman,
adhyātma, karma, adhibhūta, adhidaiva and adhiyajña (echoing 7.29-30) and Kṛṣṇa's answers at 8.3-4; per
convention only brahman stays untranslated, so adhyātma/adhibhūta/adhidaiva/adhiyajña were given fresh
English renderings ('the individual self' / 'material existence' / 'the divine order' / 'the lord of
sacrifice') matched word-for-word between question and answer, and akṣara ('the imperishable', its
akṣaram-as-syllable sense at 8.13 flagged as distinct) was kept consistent at every later recurrence.
Drafted, reviewed in two passes (pass 1: a wrong sandhi rule at 8.1 tadbrahma [-t+b- stated as unchanged,
actually -d b-]; a wrongly cased यं at 8.6 [nom./acc. given, both tokens are acc. only]; a false 7.21
cross-reference [cited taṃ tam, the chapter actually pairs tasya tasya]; अर्पित at 8.7 lemmatized under its
own inflected form instead of the causative root ā-ṛ; परं/परमं [para vs. parama, distinct headwords]
conflated at 8.8/8.10/8.28; 8.12's प्राणम् wrongly attached to āsthitaḥ instead of ādhāya, against the
verse's own already-correct L/I; an unhyphenated rātry-āgame at 8.18-19 against the chapter's own
ahar-āgame practice; pass 2: Pārtha/Kaunteya left untranslated in L throughout against convention and
ch07's own practice [now 'O son of Pṛthā'/'O son of Kuntī' in L, bare name kept in I]; a duplicated
'ordainer' gloss at 8.9 papering over anuśāsitāram vs dhātāram; an ambiguous 8.3 L letting 'supreme' read
as modifying brahman rather than akṣaram; 'yoga' silently dropped from 8.8's I). Glossed on Sonnet (four
wording-consistency fixes: bhāva's 'state, existence' vs 'state, being' split unified; ā-gam's 'to come,
arrive' vs 'to come' split unified and a truncated 'at the coming of' restored to 'at the coming of
night'; brahma-vidaḥ's brahman member missing its 'kept untranslated' tag, added; a stray un-hyphenated
sandhi note at 8.19 aligned to the file's own -i+ā-→-yā- notation). build_gita.py and validate_gita.py
both PASS (8 benign sandhi-boundary warnings, same class as chapters 1-7). Added to stories.json after
gita-ch07.

2026-09-19 · chapter 9 (Rājavidyārājaguhyayoga) · unattended run · 34 verses, 273 glossary keys · source
verified (sha256 matched parts.json; collate found only one benign orth difference at 9.3, no VAR — no
variantsVsBORI and no corrections.json entries for this chapter). Verse 20's सुरेन्द्रलोक-/मश्नन्ति print-line
word-split (sura-indra-lokam aśnanti) handled on the ch02 v6 jijīviṣāmaḥ/te 'vasthitāḥ precedent. Reviewed
in two passes (pass 1: prakṛti falsely claimed as an untranslated-list term at 9.7; -vat at 9.9 mislabeled
a comparative suffix instead of the adverbial/similative one; sūyate at 9.10 wrongly called passive despite
governing an accusative object; pṛthaktvena at 9.15 mistranslated "as many", the meaning of bahudhā later
in the same line; two spurious vowel-sandhi claims at 9.16 for consonant-final aham; a stale "verse 15"
citation at 9.22 for a yoga occurrence that verse doesn't have; trayī-dharma at 9.21 translated in I but
left untranslated in L, resolved by treating it like kula-dharma (a named body of observance) and
translating both; मां dropped from L at 9.20 despite appearing in both Sanskrit and I; a long-vs-short-a
instrumental-ending confusion at 9.24 tattvena; प्रति जानीहि at 9.31 re-analyzed as the compound verb
prati-jñā rather than adverb+bare-verb; pass 2: dharma silently translated "righteous" at 9.31's
dharma-ātmā, a second undocumented deviation from the untranslated-dharma rule, fixed to keep dharma
visible; brāhmaṇāḥ at 9.33 left as a bare transliteration against the ch02 house rendering "brahmin" and
this verse's own vaiśya/śūdra translations; a false 6.30 cross-reference at 9.14, corrected to 8.14's
nitya-yuktasya yoginaḥ; an overclaimed "verse 14" recurrence of ananya-manasaḥ at 9.13, which only recurs
at 22 and 30; plus polish: fourteen "stem is ā, not a" notes reworded to name the actual -āḥ nom. pl.
ending; V17's dhātā deduplicated from V18's bhartā [both were "sustainer"]; about.txt's catalog-verse count
corrected from two to three; a misattributed 7.23 quotation at 9.25 reworded as this verse's own phrasing).
Glossed on Sonnet (ten consistency fixes: six bare "aham — I" entries missing their nom. sg. case label in
the "I am X" run of verses 16-19 and 24; a mokṣyase gloss at 9.28 restored to match verse 1's format;
teṣu/mat-sthāni/tu/me/bhaj/aś/bhūta/ātman wording drift unified across their repeated occurrences).
build_gita.py and validate_gita.py both PASS (4 benign sandhi-boundary warnings, same class as chapters
1-8). Added to stories.json after gita-ch08.
