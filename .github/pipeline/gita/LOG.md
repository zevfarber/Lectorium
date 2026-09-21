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

2026-09-20 · chapter 10 (Vibhūtiyoga) · unattended run · 42 verses, 347 glossary keys · source verified
(sha256 matched parts.json; collate found only two benign orth differences at 10.33/10.40, no VAR — no
variantsVsBORI and no corrections.json entries for this chapter). This is the vibhūti catalog chapter
(vv.20-39, "of category X, I am Y" identifications across gods, natural phenomena, sages, animals, rivers,
mountains, virtues and abstractions) so drafting was split into three verse-range batches (1-14, 15-28,
29-42), each a separate subagent, after a first whole-chapter drafting attempt failed by exceeding its
output-token budget composing all 42 verses at once — a lesson for any future outsized chapter (18's 78
verses will need the same split). Reviewed in two passes (pass 1: a wrong cross-reference at 10.17 citing
10.9 for an avagraha pattern that verse doesn't have; a subject/object reversal in 10.17's L, translating
Kṛṣṇa as the one meditating rather than the one meditated upon; a wrong lemma at 10.23 [rākṣasa for the
actual s-stem rakṣas]; a false "already named at 10.6" claim at 10.25 [10.6 only gives the sages' number,
names none]; a missed a+a→ā vowel-fusion sandhi at 10.27 narādhipam wrongly called "no change"; a
misattributed rendering at 10.32 [conflating the Sanskrit's own svabhāva gloss with the actually-fixed
ch.8 English rendering "the individual self," and L/I not matching that precedent]; all seven feminine
nouns at 10.34 mislabeled "subject" instead of "predicate"; two false "not yet seen"/"new pattern" sandhi
claims at 10.36 and 10.39 that both recur from 10.6 and 10.14 respectively; a wrong cross-reference at
10.40 [cf. 10.4 instead of 10.3]; five vocative epithets [10.14 Keśava, 10.18 Janārdana, 10.20 Guḍākeśa,
10.24 Pārtha, 10.40 Parantapa] left as bare names in L against the chapter's own established practice and
the ch.8-fixed convention of translating vocatives in L; a wrong lemma at 10.14 [vi-akta for the actual
-i-stem vi-akti]; and inconsistent nom.-subject case tags on catalog "aham" entries, the same lapse ch.9's
review recorded fixing; pass 2, after verifying all pass-1 fixes landed correctly: I mishandling the
chapter's own opening vocative at 10.1 [substituting the real name "Arjuna" plus an added English adjective
for the bare epithet Mahābāho, directly against the pattern pass 1 had just established two lines later];
the vocative Kuruśreṣṭha silently dropped from 10.19's I; "yoga" silently dropped from 10.10's I despite
buddhi-yoga being named as untranslated in its own note — the same bug class ch.8's review caught; two
tokens [10.25 bhṛguḥ+aham, 10.30 mṛgendraḥ+aham] missing a whole "aham" morph entry, not just its case
tag; a stray wrong lemma "idad" for idam at 10.42; plus two convention-compliance fixes beyond the pass-1
list — makara and dvandva at 10.31/10.33 translated into English, since neither is on the chapter's
sanctioned untranslated-terms list — and a register normalization unifying three "among X" catalog lines
[vv.24,27,28] to the chapter's dominant "of X" phrasing, a residual seam from the three-way batch draft).
Glossed on Sonnet (seven consistency fixes, all in the "aham" and "hi" gloss families: a missing ", subject"
tag, two missing "'me'" translations on accusative aham entries, two stray-comma fixes on enclitic "me"
glosses, and two reordering/wording fixes unifying "hi" to the chapter's established "for, indeed"
phrasing). build_gita.py and validate_gita.py both PASS (15 benign sandhi-boundary warnings, same class as
chapters 1-9). Added to stories.json after gita-ch09.

2026-09-20 · chapter 11 (Viśvarūpadarśanayoga) · unattended run · 55 verses, 482 glossary keys ·
source verified (sha256 matched parts.json; collate found the five listed variantsVsBORI as VAR
[11.16, 11.20, 11.21, 11.22, 11.32] plus two benign orth diffs at 11.25/11.29, no corrections.json
entries for this chapter). Longest chapter drafted so far and the first with substantial triṣṭubh
(4-line) content — verses 1-14 and 51-55 are anuṣṭubh, 15-50 triṣṭubh — so drafting was split into
six verse-range batches (1-14, 15-24, 25-34, 35-40, 41-46, 47-55), each a separate subagent, matching
ch10's precedent of splitting outsized chapters. Eight pāda-crossing hyphen-splits (compound/sandhi
words the Wikisource print breaks across a line: 11.15, 17, 19, 29, 30, 38, 46, 48), each drafted per
the ch09 v.20 precedent (leftover consonant opens the continuation token's reading). Verse 11.32 uses
the chapter's mandated house rendering ("Time I am...") verbatim. Reviewed in two passes: pass 1 (14
fixes: three untranslated vocatives in L against the ch08/ch10 convention [Pārtha ×2, Guḍākeśa] and
four more [Keśava, Hṛṣīkeśa, Acyuta, Janārdana] with etymology drift from ch10's settled renderings;
Savyasācin's L/I roles reversed; kirīṭin and jagannivāsa/deveśa worded two ways across their repeated
occurrences; a words.txt reading-field bug at 11.45 [deveśa given fused, not sandhi-undone]; and the
11.48 hyphen-split bug [continuation token's reading wrongly opened with restored visarga ḥ instead of
the literal leftover consonant r — a genuine sandhi error, not just a WARN, since दानैः + न sandhis to
dānair na, visarga-before-voiced-consonant, not a bare restored visarga] — this last one also flagged
directly by validate_gita.py's own opening-letter check); pass 2 confirmed all 14 landed and found four
more: adhyātma (v.1) wrongly left untranslated in I against ch.8's own settled rendering "the individual
self"; v.9 missing its I line entirely; परं at v.18 mislemmatized "parama" instead of "para" [same
headword-conflation bug ch.8's review caught]; and prasīda worded three ways across v.25/31/45. Glossed
on Sonnet: six lemma-citation splits unified (tvam wrongly cited "tvad" at five non-compound forms, tad
wrongly cited "tat" at three, kecit's two occurrences under different lemmas, Brahmā cited once as
"brahman"); a dozen gloss-wording drifts unified across batches (parama, para, viśva, namas, hi, avyaya,
akṣara, Viṣṇu, gadin); a real grammar error (मे at v.18 mislabeled instr. sg., corrected to gen. sg.,
genitive-of-agent); two off-meaning eva glosses ("already", "again" — neither is a sense of eva) fixed to
match the chapter's own dozen correct occurrences; and Kṛṣṇa/Arjuna, cited as bare lemmas nowhere
identified despite every other proper name in the file carrying an identifying gloss, given one each on
first occurrence. build_gita.py and validate_gita.py both PASS (6 benign sandhi-boundary warnings, same
class as chapters 1-10). Added to stories.json after gita-ch10.

2026-09-20 · chapter 12 (Bhaktiyoga) · unattended run · 20 verses, 146 glossary keys · source
verified (sha256 matched parts.json; collate found the one listed variantsVsBORI [12.18, vulgate
mānāpamānayoḥ vs. BORI mānāvamānayoḥ, both meaning "honor and dishonor/disrespect"] as VAR, no
corrections.json entries for this chapter). All 20 verses anuṣṭubh; drafted in one pass (no
verse-range splitting needed, unlike the longer chapters 10-11). Reviewed in two passes: pass 1
(8 fixes: v.2's मे wrongly labeled instrumental instead of genitive-of-agent-with-mataḥ; a wrongly
imported "alone" in v.2's L with no eva in the Sanskrit; v.5's तेषाम् mislabeled gen. sg. instead of
gen. pl.; "yoga" silently translated "discipline" in four spots against the untranslated-terms
convention [v.6 I, v.9 I, v.11 L, v.11 I] — the same bug class LOG.md records for chapters 8 and 10;
v.16's अनपेक्षः lemma wrongly cited the feminine noun apekṣā instead of the adjectival stem
an-apekṣa, which cannot yield a masculine nominative; v.14's note overstating the yaḥ...saḥ refrain
as spanning "every verse through 19" when verses 18-19 do not contain that construction, narrowed to
its true span of 14-17; an unwarranted "instead" imported into v.1's I where the Sanskrit's ye ca api
has no adversative तु, unlike v.3/v.6's genuine ye tu; and a stray apostrophe in v.4's note); pass 2
confirmed all 8 landed cleanly with no collateral damage, did an independent fresh full-chapter pass,
and caught one residual instance of the same "yoga → discipline" bug surviving in v.11's own note
(fixed) plus two non-blocking style notes (the ch.1-6-era "yoga, discipline" gloss style vs. chapters
7-11's "kept untranslated" self-reminder tag — left as-is, matching this chapter's own gloss
precedent; and parts.json's stale words:183 vs. the build's actual 186, a metadata field validate_gita.py
doesn't check). Glossed on Sonnet: three residual gloss-wording drifts for repeated words unified
(sama "equal, even" at v.4 realigned to the chapter's own "equal, the same" used at vv.13,18,19;
ud-vij's two occurrences two lines apart in v.15's own pair worded "to be agitated" vs. "to be
disturbed", unified to the latter; bhaktimat's two occurrences worded in reversed order, "possessing
devotion, devoted" at v.17 vs. "devoted, possessing devotion" at v.19, unified to the latter); no
mislabeled case/number bugs found elsewhere in the file (teṣām/te/tad and yoga/yogin lemma citations,
Pārtha/Dhanaṃjaya epithet identification, and bhakta/bhakti/bhaktimat core translation all checked
clean). build_gita.py and validate_gita.py both PASS (4 benign sandhi-boundary warnings, same class
as chapters 1-11). Added to stories.json after gita-ch11.

2026-09-20 · chapter 13 (Kṣetrakṣetrajñavibhāgayoga, "The Field and the Knower of the Field") ·
unattended run · 34 verses, 235 glossary keys · source verified (sha256 matched parts.json; collate
found the one listed variantsVsBORI [13.20, vulgate kāryakaraṇakartṛtve "instrument" vs. BORI
kāryakāraṇakartṛtve "cause"] as VAR, no corrections.json entries for this chapter). Kṛṣṇa speaks the
whole chapter unprompted (one speaker line only, at v.1); prakṛti, puruṣa, kṣetra, kṣetrajña and
bhakti translated throughout ("nature", "the Person", "the field", "the knower of the field",
"devotion") per established practice from chapters 7-9 and the standing bhakti decision in this
file's QUESTIONS.md, never left untranslated. Drafted in one pass, all 34 verses anuṣṭubh. Reviewed
in two passes: pass 1 (8 fixes — a missing ZWNJ in v.21's भुङ्क्ते token vs. the raw source file;
Kaunteya and Bhārata left untranslated at their v.1/v.2 first occurrences against the
epithets-translated-on-first-use convention; v.12's note overstating the vulgate/BORI word-division
difference [anādi mat-paraṃ vs. anādimat paraṃ] as making "much the same" sense when it in fact drops
or keeps an explicit reference to Kṛṣṇa; two sandhi notes at vv.13/25 mischaracterizing an optional
Pāṇinian visarga-retention-before-ś rule [vā śari, 8.3.36] as if it were the unrelated obligatory
stop-assimilation rule seen at vv.3-4; a spurious compound-hyphen in v.24's L, "by-Sāṃkhya-yoga",
where words.txt itself already keeps sāṃkhyena and yogena as two separate instrumentals; and a real
syntactic misparse in v.30, वित्तारं wrongly read as a second object of line 1's anupaśyati rather
than — correctly — an accusative in apposition with brahma, both governed by line 2's own verb
saṃpadyate, "attains to, becomes" + acc.). Pass 2 independently confirmed all 8 pass-1 fixes landed
(and, checking v.30 from first principles rather than trusting pass 1, confirmed saṃpadyate + acc.
is itself sound dictionary-attested Sanskrit, not merely what pass 1 proposed), then found four more
on a fresh full-chapter read: "yoga" silently translated "discipline" at vv.10/24 against the
untranslated-terms convention — the same recurring bug class this LOG already records for chapters
8, 10 and 12 — now also inconsistent with v.24 L's own pass-1 fix; an arithmetic slip in v.5's note
claiming "twenty-three items so far" when the verse's own list (5+1+1+1+11+5) already completes the
Sāṃkhya 24-tattva tally, contradicting v.6's own correct framing of its items as modifications, not
further tattvas; v.13's note misattributing its Vedic parallel to the puruṣa-sūkta (RV 10.90, which
opens quite differently) when the verse is in fact an almost word-for-word citation of Śvetāśvatara
Upaniṣad 3.16 (the Viśvakarman-hymn/RV 10.81.3 parallel is real but secondary); and v.31's L breaking
the same epithet-nudge convention by translating Kaunteya's second occurrence instead of leaving it
bare as the nudge, exactly as already fixed for Bhārata at v.33. One process-consistency point raised
by pass 2 — v.12's word-division difference is letter-identical between the two witnesses, so by
convention's own "orth is nothing" rule it isn't a parts.json-tracked variantsVsBORI entry the way
v.20 is, even though the note is right to flag its real sense-difference — was left as a note-only
observation rather than added to parts.json, and is recorded in QUESTIONS.md for whoever next reviews
the variant-tracking convention. All pass-1 and pass-2 fixes applied and re-verified (tiling against
gita_lib's ZWNJ/ZWJ-stripped canonical text still exact after every edit — pass 1's ZWNJ insertion
into v.21's token was itself reverted, since gita_lib.read_wikisource strips ZWNJ/ZWJ as
normalization and build_gita.py's own tiling check requires the token without it, a gotcha specific
to this chapter's one ZWNJ-bearing source line). Glossed on Sonnet: 8 high-confidence gloss-wording
fixes (jñeya's gerundive gloss unified to "to be known"; bhūta unified to "being" without the
unexplained "being, creature" variant; vac unified to "to say, call"; bhuj's agent-noun entry
restructured to lead with the infinitive, matching house style; yoga given its dictionary gloss at
its two bare v.24 occurrences instead of standing undefined; sāṃkhya's v.24 entry brought into line
with its established chapters-5 gloss, "sāṃkhya, kept untranslated"; brahman's three occurrences given
the established "brahman, the absolute (kept untranslated per convention)" gloss from chapters 2-3
instead of standing as a bare undefined "brahman — brahman"; sarvataḥ's triple v.13 occurrence
unified) plus 6 moderate consistency fixes (samāsa, vikāra, kṛ, three sthā-compound participle
entries, and four agent-noun/habitual-adjective entries all restructured to lead with the root's
infinitive per house style). build_gita.py and validate_gita.py both PASS (12 benign sandhi-boundary
warnings, same class as chapters 1-12). Added to stories.json after gita-ch12.

2026-09-21 · chapter 14 (Guṇatrayavibhāgayoga, The Three Qualities) · unattended run · 27 verses, 196
glossary keys · source verified (sha256 and collation both matched parts.json's variantsVsBORI list —
14.18 and 14.25 — before drafting; no corrections.json entries for this chapter). Drafted, reviewed in
two passes: pass 1 found five grammar/morph errors (14.4 महद्योनिरहं wrongly analyzed as an adjective
independently agreeing in gender with the feminine yoniḥ rather than as the compound mahad-yoniḥ,
reading and morph corrected to the compound analysis; 14.7 and 14.8's rajaḥ/tamaḥ mislabeled nominative
subjects of viddhi's double-accusative construction instead of accusative objects; 14.10's first-half
rajaḥ/tamaḥ mislabeled nominative instead of accusative objects of abhibhūya, inconsistent with the
verse's own correctly-analyzed second half; 14.24's bahuvrīhi compound tulya-nindā-ātma-saṃstutiḥ
mislabeled feminine instead of masculine, agreeing with dhīraḥ) plus one register polish at 14.25.
Pass 2 re-verified all pass-1 fixes (sound) and found two further errors (14.23's āsīnaḥ given the
wrong root, ā-sad instead of ās; 14.27's śāśvatasya given the wrong gender, neuter instead of masculine
agreeing with dharmasya) plus one minor ellipsis-note tidy at 14.11. Glossed on Sonnet: names correctly
identified on first occurrence throughout; nine gloss-wording consistency fixes (upa-jan, jan, bhū,
dehin, pramāda, sukha, duḥkha, vi-vṛdh unified across their recurring occurrences in the chapter);
para's adjectival ("supreme, highest") vs. substantivized ("the beyond") senses at v.1 and v.19 and
tulya's minor truncation on repeat left as-is, both judged genuine sense-splits or harmless shortening
rather than errors. build_gita.py and validate_gita.py both PASS (7 benign sandhi-boundary warnings,
same class as chapters 1-13). Added to stories.json after gita-ch13.

2026-09-21 · chapter 15 (Puruṣottamayoga, The Supreme Person) · unattended run · 20 verses, 169
glossary keys · source verified (sha256 matched parts.json; collation against BORI showed only one
orth-class difference, no VAR entries, matching parts.json's empty variantsVsBORI list; no
corrections.json entries for this chapter). Drafted (the inverted-aśvattha-tree cosmology of vv.1-5,
the individual jīva of vv.7-11, Kṛṣṇa's identification with nature's powers in vv.12-15, and the
kṣara/akṣara/puruṣottama doctrine of vv.16-20); puruṣa translated "the Person" and puruṣottama "the
Supreme Person" per the precedent already set at chapters 8, 10-11 and 13, kṣara/akṣara translated
"the Perishable"/"the Imperishable" per the precedent at chapters 8 and 11. Two authentic pāda-break
word-splits in the transmitted text (v.3/4's सुविरूढमूल-/मसङ्गशस्त्रेण and v.5's
सुखदुःखसंज्ञै-/र्गच्छन्त्यमूढाः) were reproduced as given and flagged in their notes as not misprints.
Reviewed in two passes: pass 1 found five wrong or self-contradictory cross-references/citations (a
false "exactly as 13.5" parallel at v.7, a vowel/consonant mislabeling of the vimūḍhāḥ elision at
v.10, a false "recurs at verse 18" sandhi claim at v.16, two wrong verse numbers for quoted Sanskrit
at v.20, an overstated 10.10-11 parallel at v.15), an L/I subject-predicate contradiction each at v.1
and v.16, a capitalization mismatch at v.17, an un-hyphenated internal vowel fusion at v.15's
वेदान्तकृद्वेदविदेव, and an unclear L at v.9. Pass 2 re-verified all pass-1 fixes (sound, including
against the actual cited verses' Sanskrit) and found four further errors: v.1's aśvattham wrongly
tagged neuter instead of masculine in two entries (contradicting this same chapter's own correct v.3
tagging), a fabricated quotation misattributed to 13.17 at v.15 (13.17 reads hṛdi sarvasya viṣṭhitam,
not sarvasya ca hṛdi sthitam), a wrong cross-reference at v.15 citing 10.10-11 for smṛti when only
10.34 actually names it, and a lemma-consistency violation at v.12 citing "gata" as its own lemma
instead of the root gam already used for the same participle at v.4 and v.6. All fixes applied and
re-verified (tiling still exact after every edit). Glossed on Sonnet: two occurrences of yat ("to
strive") unified in v.11, and puruṣa's gloss at its two puruṣa-uttama occurrences (v.18, v.19)
corrected from a generic "a person" to the chapter's established technical gloss "the Person",
matching every other occurrence in the chapter; Bhārata (v.19, v.20), na/ca/tad/yad/vid/bhū and
guṇa/kṣara/akṣara all confirmed already consistent. build_gita.py and validate_gita.py both PASS (11
benign sandhi-boundary warnings, same class as chapters 1-14). Added to stories.json after gita-ch14.
A pre-existing cross-chapter inconsistency was noticed but left untouched, out of this chapter's
scope: puruṣottama is capitalized "the Supreme Person" here (matching "the Person"/"the
Perishable"/"the Imperishable"), while chapters 8 and 10 render the same term lowercase, "supreme
Person" — recorded in QUESTIONS.md for whoever next reviews cross-chapter capitalization.

2026-09-21 · chapter 16 (Daivāsurasampadvibhāgayoga, Divine and Demonic Natures) · unattended run ·
24 verses, 173 glossary keys · source verified (sha256 matched parts.json; collation against BORI
showed exactly the two VAR entries parts.json declares — 16.4, 16.13 — plus one orth-class difference
at 16.12; corrections.json's 16.19 krūrān fix already baked into the verified text). Drafted the
divine/demonic catalogs of vv.1-5, the extended description of the demonic nature in vv.6-20
(the godless-cosmos view, the interior monologue of the self-aggrandizing egotist in vv.13-15, and
the "hurled into demonic wombs" close), and the threefold-gate-of-hell teaching of vv.21-24; sampad
translated "endowment, inheritance" throughout (not on the untranslated-terms list), yoga (16.1) kept
untranslated per convention, no house-rendering verses fall in this chapter. Reviewed in two passes:
pass 1 found six factual/completeness corrections (16.5's sampad-vimokṣāya voicing wrongly called
"no visible sandhi change" when -t does audibly voice to -d before v-; 16.5's mā śucaḥ note
misidentifying 2.11's aśocyān anvaśocas tvam, a different indicative construction, as the same
prohibitive used here and at 18.66; two incomplete visarga notes at 16.6 and 16.11 left unstated
where the pattern was already flagged elsewhere in the chapter; 16.13's prāpsye lemmatized as the
bare root āp instead of pra-āp, against the prefix-carrying convention already followed at 16.23's
ava-āp; 16.2's aloluptvam's irregular loss of lolupa's stem-final -a before -tva left unremarked)
plus one translation-consistency fix (16.4's I line rendering darpa "arrogance" against "pride"
everywhere else in the chapter) and one lemma-convention fix (16.2). Pass 2 found two further errors
(16.5's second sampadam wrongly said to be governed by the copula asi rather than by the participle
abhijātaḥ, as verses 3-4 already correctly have it; 16.14's note on the verse's three occurrences of
aham garbling their sequence and wrongly treating the un-elided second aham aham as if it shared the
same -aḥ+a- sandhi as the other two) plus one optional polish (16.3's "point for point" overstating
how closely the 26-item divine catalog and 6-item demonic catalog actually correspond). All fixes
applied and re-verified (tiling still exact after every edit). Glossed on Sonnet: aham's gloss
normalized to "I" at five occurrences that had drifted into case-inflected glosses ("my", "by me");
eva, gati, dambha, darpa, māna and sampad unified across their recurring occurrences; vyavasthiti's
two distinct-looking glosses at vv.1 and 24 cross-referenced; verse 7's noun pravṛtti relemmatized
apart from verse 10's verb pra-vṛt, which had wrongly shared one lemma string with an incompatible
gloss; anya's lemma citation unified (verse 8 had cited "anyat"); as's gloss unified to "to be, to
exist". Para's two legitimate senses ("other" vs. "highest, supreme") and the shared "vid" lemma
covering two distinct dictionary roots were considered and left as intentional, context-disambiguated
polysemy rather than errors. build_gita.py and validate_gita.py both PASS (6 benign sandhi-boundary
warnings, same class as chapters 1-15). Added to stories.json after gita-ch15.

2026-09-21 · chapter 17, Śraddhātrayavibhāgayoga (The Three Kinds of Faith) · 28 verses, 206 glossary
keys. Source verified: sha256 matched parts.json, collate(17) returned only the expected 17.6 VAR (the
sole listed variantsVsBORI entry) plus one benign 17.25 orth diff; no corrections.json entries for this
chapter. Drafted the chapter's threefold-faith framework (v.1-3), the sattva/rajas/tamas catalogs of
worshippers, foods, sacrifices, austerities and gifts (v.4-22), and the closing oṃ-tat-sat passage
(v.23-28) on the threefold name of brahman and the sat/asat distinction; śraddhā translated "faith"
throughout per convention (not on the untranslated-terms list), brahman kept untranslated at its two
occurrences (17.23-24), no house-rendering verses fall in this chapter. Reviewed in two passes: pass 1
found a lemma-naming error (17.13's a-dakṣiṇam mislemmatized as the feminine noun "a-dakṣiṇā" instead of
the adjective "a-dakṣiṇa"), a translation cross-wire (17.9's I line swapped "pungent"/"bitter" against
what L and the morphs assign to kaṭu vs. tīkṣṇa), and a missing participle-root tag (17.26's praśaste
lacking "(past participle of pra-śaṃs)", inconsistent with the chapter's own pattern for participle
lemmas). Pass 2 found three further errors: 17.25's gerund an-abhisaṃdhāya lemmatized as its own
inflected surface form rather than the root abhi-sam-dhā (breaking the pattern already followed by the
same verb's un-negated instance two verses earlier); 17.27's note misidentifying the antecedent of
tad-arthīyaṃ karma as verse 25's mokṣa rather than the verse's own nearer yajña/tapas/dāna triad; and
17.16's manaḥ prasādaḥ mislabeled "gen./nom." when manaḥ (an -as-stem) has no genitive form and is
functioning attributively as a nominative. All fixes applied and re-verified (tiling still exact after
every edit). Glossed on Sonnet: sāttvika/rājasa/tāmasa's guṇa-adjective gloss wording unified to
"belonging to X" (one outlier at v.2 had used "of the nature of X"); dāna's gloss unified to plain
"giving" across 8 occurrences that had drifted between "giving", "a gift" and "giving, a gift"; yajña's
one "a sacrifice" outlier (v.23) unified to "sacrifice"; the quoted-term instances of sat (v.26-27, the
sad-iti/sat-śabda citations) unified to "'sat'", distinct from and left unmerged with v.26's ordinary-
word sense "being, existing, real"; oṃ's second occurrence (v.24) restored the "first of brahman's three
names" identification already carried at its first occurrence and already extended to tat's second
occurrence, for parity. sattva's two special, non-guṇa senses (v.3 "one's own being, disposition", v.8
"vitality, vigor, strength of mind") each occur once and were left as intentional, explicitly-flagged
polysemy distinct from the ordinary guṇa sense, per the reviewer's confirmation. build_gita.py and
validate_gita.py both PASS (5 benign sandhi-boundary warnings, same class as chapters 1-16). Added to
stories.json after gita-ch16.
