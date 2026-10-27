# Review, pass 1 — kebra-nagast-ch96b (ch. 96, part 2 of 2)

Reviewer pass 1. Units are numbered from 0 (the first unit, ዓዲ ሶበ አዕረጎ…, is unit 0; there are 24).
The joined `t` was checked against the Bezold/HaCohen source before and after every edit: unchanged
(it is the source text from character 2565 of ch. 96 to the end, exactly). gloss.json was not touched.
All edits were made by script (json load/dump, ensure_ascii=False, indent=1).
Counts: 2 major, 6 moderate, 12 minor (20 changes), 6 findings refused.

## Changes

| # | Unit · field | Severity | What was wrong | What was done |
|---|---|---|---|---|
| 1 | 10 · l, i, n | major | ባሕርይ rendered 'nature (?)' and ከርሥ 'body'. The house reading in published parts is 'the pearl' (ch. 25-26, 68a/b, 69, 95; ch. 68a has 'created in the womb of Adam like a pearl-stone', the same figure). The note's reasoning ('Mary was a nature to be taken from Adam') was invented around the wrong sense, and it left units 10-12 (feminine -ኣ resuming the pearl) without an antecedent. | l 'the-pearl', 'womb-his of-Adam'; i 'he created her, the pearl, within the womb of Adam'; n rewritten with the house reading and the chapter references; ከርሥ 'womb' as in ch. 68. |
| 2 | 17 · l, i, n | major | ወአዳም ሥና rendered 'and Adam beauty (?)' / 'the beauty of Adam (?)': an invented genitive (no ለ-, no construct), and against the published readings of አዳም as adjective 'pleasing, comely (?)' (ch. 25-26 ወአዳም ንባብከ, ch. 35 ወአዳም ቃሉ; known-forms ወአዳም 'and pleasing (?)'). | l 'and pleasing(?) beauty(?)'; i 'of pleasing beauty (?)'; n states the house reading and that 'Adam' would need a genitive the text lacks. |
| 3 | 9 · l, i, n | moderate | i 'apart from her man Adam (?)' and 'by listening to a deceiving word': 'her', 'apart', 'deceiving' are not in the Geʿez, and i did not match l ('from-man, of-Adam'). Also ለአዳም was read as owner of ዕድው, whereas the chapter's pattern is ለX doubling the suffix of the verb (ኮነቶ). | i 'having heard a word of snare (?) from the man (?), she became a killer to Adam'; l matched; n explains the ለአዳም reading and keeps the ዕድው crux. |
| 4 | 13 · l, i, n | moderate | Tä-stem ወተወለጥነ ሕይወተ rendered 'we were exchanged for life', which no longer agrees with unit 4-5 (the mortal 'became life', ተውላጠ). A T-stem 'be changed' takes the result in the accusative. | l 'we-were-changed life(?)'; i 'we were changed into life (?) in our mortal flesh'; n gives the reading and 'exchanged for life' as the alternative. |
| 5 | 6 · i, n | moderate | በእንተ 'concerning, on account of' was rendered 'through' (a different force: instrument); 'how great we human beings are' also loosened ዕበይነ ለሰብእ ('our greatness, that of man'). | i 'And openly our greatness, that of mankind, has been made known on account of him who ransomed us'; n notes the sense of በእንተ. |
| 6 | 14 · l, i, n | moderate | ኅቱም rendered 'shut'; it is the participle of ኀተመ 'seal' (cf. ማኅተም, and ተኀትመት 'she was sealed' in unit 20), while 'shut' is ዕጹት (unit 19). The distinction the commentary builds on was erased. | l and i 'sealed'; n explains. |
| 7 | 13 · l, i | moderate | ኢመዋቲት (feminine) beside masculine መንበር: the note says apposition (?), but i gave a smooth attributive 'deathless throne' with no hedge. | (?) added in l and i. |
| 8 | 9, 10, 11 · n (and 10 · i) | moderate | Unit 11's note named 'the divine nature or the Word' as antecedent of -ኣ and ignored ባሕርይ (feminine) in unit 10. | n of unit 11 now lists the pearl first; unit 10 as in #1. |
| 9 | 0 · l, i, n | minor | ቀርሜሌዎስ transliterated 'Qarmeleyos'; the signs are ዎ (wo), so 'Qarmelewos'. | l, i, n corrected. |
| 10 | 0 · l, n | minor | አዕረጎ rendered 'he-brought-up' with the object suffix -ዎ dropped from l (house practice keeps it: 'he-told-them'). | l 'he-brought-him-up'; n adds 'brought him up'. |
| 11 | 2 · l | minor | 'for-saving-of' beside house 'salvation' for መድኀኒት (unit 11 has 'his-salvation'). | l 'for-salvation-of'. |
| 12 | 2 · l, n | minor | l 'she that-earthly' fused ይእቲ ምድራዊት wrongly ('that-earthly' for ምድራዊት); n called the construct ለመድኀኒተ 'accusative form'. | l 'she, earthly(f.)'; n 'construct form -ተ before አዳም', ይእቲ 'she, that (f.)' resuming ሥጋ. |
| 13 | 3 · l | minor | 'Do-you-understand-then': -ኑ is the question particle, not 'then'; the second verb is not marked with it. | l 'Do-you-understand-(question) and-you-examine'. |
| 14 | 3 · i | minor | 'for the sake of his father's will' adds a sense to ለ- not in l ('for-will-of'). | i 'for his father's will'. |
| 15 | 7 · l | minor | 'moreover' for ዘኒ unmarked, although the note hedges it (?). | l 'also(?)'. |
| 16 | 7 · n | minor | 1 Corinthians 15:45 cited for 'the Eve/Mary and Adam/Christ pairing'; it covers only Adam/Christ. | n cites 1 Cor 15:45 and Romans 5:14 for Adam/Christ, and says Eve/Mary is a later Christian reading, not scriptural. |
| 17 | 12 · i | minor | 'free of impurity' for ዘእንበለ ርስሐት, loose against l 'without impurity'. | i 'without impurity'. |
| 18 | 14 · n | minor | 'as in part 1' for ተመንደብነ: part 1 has the Aʾ form አመንደብዎሙ; the tä-form is ch. 91 ተመንደብኪ. Also ተላዐልነ called 'four-letter verb' (it is the tä-stem of ላዐለ, from ላዕል; cf. ch. 90 ተላዐለ). | n corrected on both points. |
| 19 | 14, 22 · i | minor | 'Ezekiel also prophesied', 'Moses also prophesied' for ተነበየ ካዕበ / ወካዕበ ተነበየ ('again'); part 1 renders ካዕበ 'again'. | i 'prophesied again' in both. |
| 20 | 1 · n | minor | አምሳሊሁ analysed as አምሳል + -ሁ; the form is the suffix-stem አምሳሊ-. | n adds the suffix-stem. |

Severity totals: major 2 (#1, #2), moderate 6 (#3-#8), minor 12 (#9-#20).

## Checked and found sound (no change)

- Ezekiel 44:1-2 (unit 14) and Exodus 3:2 (unit 22) are named plainly in the notes; the Ezekiel quotation and the Moses quotation in i are rebuilt from the Geʿez, not KJV-worded ('Lord of the mighty', 'a bush ... that the consuming fire did not burn').
- Genesis 22, Genesis 2:21-22, Genesis 3 are named in their notes. Names follow house forms: Isaac, Abraham, Mary, Ezekiel, Moses, Sinai, Adam, Eve (ሔዋን, as ch. 36, 64-68).
- Grammatical labels in the other notes checked against the forms (tä-stem passives ተጠብሐ/ተቤዘወ/ተፈጥረት/ተወልደ/ተኀትመት; Aʾ causatives አውረደ/አዕረጎ/አኅደራ/አንሥአነ/አዕረገነ/ያርኢ; converbs አንጺሖ/ቀዱሶ/ሰሚዓ; suffix analyses -ዎ -ኣ -ሃ -ሁ -ነ -ኒ -ሰ -ኬ; feminine agreement እንተ ኢትመውት, ዘትነድድ, ኢትውዒ).

## Findings refused

1. Unit 7 · i 'the mother of God' for ወላዲተ አምላክ (suggestion: 'bearer of God'). Refused: the note and l already give 'bearer of God' and name the Theotokos title; 'mother of God' is the standard English of that title and not a remembered-scripture import.
2. Unit 21 · i 'by what was hers (?)' for እንተ ኀቤሃ. Left: it is hedged, l is literal ('which (f.) with-her'), and the house gloss of ኀበ includes 'in the possession of'. No better reading is available without Dillmann.
3. Units 13 and 14 exceed ~45 words (35 and 40 by wordspace count; unit 14 has two sentences run together). Not cut: the source has no ፤ ። ፨ inside them, and units end only at those marks (runbook).
4. Unit 0 has no `p: true`. Correct: the part continues the paragraph begun in part 1 (the source chapter has two paragraphs, a 27-character heading and one body paragraph; this part starts mid-paragraph).
5. Unit 11 · 'he made it (?) dwell upon her' kept as drafted; the antecedent crux is hedged and noted (see #8).
6. Unit 12 · ገብራ 'he made her' (house gloss has 'her servant' beside 'they made'): the reading 'he made her pure' fits ለንጽሕት; kept, and the glosser should list the parse.

## Notes for the glosser (do not affect units.json)

- ባሕርይ in unit 10 should be glossed 'pearl' (as ch. 68), and ለባሕርይ as object; ወአዳም in unit 17 'and pleasing (?)'; ተመንደብነ 'we were afflicted (?)' to match ተመንደበ in ch. 91; ኅቱም 'sealed'; ተወለጥነ 'we were changed'.

---

# Review, pass 2 — kebra-nagast-ch96b (adversarial; gloss.json brought into line with the pass-1 units)

Method: every one of the 98 novel-form entries was checked (lemma, parse against every occurrence in the 24 units,
house consistency against the published kebra-nagast-ch*.json glossaries and known-forms.json); the 8 `__broaden__`
entries were checked against the known text (old entry kept whole, then ' · ' and the new reading); units.json was
re-read once more (grammar labels, l against i, remembered English). Dillmann was not available; hedges (?) mark what
rests on context or the house parallels. Edits by script (json, ensure_ascii=False, indent=1). Verified after the
edit: the joined `t` of units.json is identical to before (and to the source); all 98 novel forms are still covered by
gloss.json (no extra plain keys); every broaden entry starts with the known entry whole + ' · '.
Counts: 2 major, 7 moderate, 28 minor (37 changes); 11 findings refused.

## Changes

| # | Unit / form · field | Severity | What was wrong | What was done |
|---|---|---|---|---|
| 1 | unit 9 · l, i, n; form እምዕድዉ · gloss | major | እምዕድዉ ለአዳም read 'from the man (?)' with ለአዳም doubling the suffix of ኮነቶ. The published ch. 92-93 has the same construction ዕድዉ ለሰብእ ('enemy of man', said of Satan; its entry ዕድው 'enemy, adversary (?)'), and 'a word of snare from the man' makes no sense in Genesis 3, whereas 'from the enemy of Adam' (the serpent) does. The gloss said ዕድው 'man (?)' with a spelling guess. | l 'from-enemy(?) of-Adam, she-became-to-him killer'; i 'from the enemy (?) of Adam, she became his killer'; n rewritten (parallel ch. 92-93, ዕድው 'man' of ch. 35 named as the rejected reading, ለ- as genitive link, ኮነቶ 'to him' = to Adam); gloss entry 'ዕድው — from the enemy, adversary (?)' consistent with ch. 92-93. |
| 2 | ወአዳም · `__broaden__` | major | New part read 'and Adam (ወ- + proper name), in ወአዳም ሥና "and of Adam, beauty (?)"': contradicts the pass-1 unit 17 ('and pleasing (?) beauty (?)') and the known entry's adjective reading. | New part: '· and pleasing (?) (ወ- + adjective, as in ch. 25-26 and 35), in ወአዳም ሥና "and pleasing (?) beauty (?)"'; old entry kept whole. |
| 3 | በአዕልዎ · gloss lemma | moderate | Lemma አዕልዎ is the inflected infinitive, not a dictionary form (an invented headword). | Lemma አዕለወ (causative, from the root of ዕልወት), infinitive named in the parse; hedged (?). በዕልወተ now says 'cf. በአዕልዎ'. |
| 4 | ኢመዋቲት · gloss lemma | moderate | Lemma ኢመዋቲ is not a dictionary form (negative prefix fused to the lemma; house puts the lemma without ኢ-, as ኢተጠብሐ → ጠብሐ). | Lemma መዋቲ ('ኢ- + መዋቲ, fem. መዋቲት'), meaning 'deathless, immortal'. |
| 5 | ኅቱም · gloss | moderate | Meaning 'sealed, shut': 'shut' is ዕጹት (pass 1, unit 14 note; ወዕጹታ in unit 19), so the gloss reintroduced the confusion pass 1 removed. | 'sealed' only, with the note that 'shut' is ዕጹት. |
| 6 | ኢያውዐያ · gloss; unit 22 · l | moderate | Gloss 'ኢ- + 3ms perfect': the prefix ያ- marks the imperfect (a perfect would be ኢአውዐያ), and the unit-22 note already said 'imperfect'; l had 'not-burnt-it'. | Gloss 'which it does not burn (ኢ- + 3ms imperfect … + -ኣ; imperfect with past reference in the vision)'; l 'which not-burns-it fire' (i left as 'did not burn', a fair English for a past vision). |
| 7 | ወተወለጥነ · gloss | moderate | Written before pass 1: 'we were exchanged, changed' (the old unit reading). | 'we were changed' (tä-stem passive of ወለጠ), ሕይወተ 'into life (?)', 'exchanged for life' as the alternative, as in the unit-13 note. |
| 8 | ለምድራዊ · gloss | moderate | Entry covered only unit 3 ('of the earthly'); the form occurs also in unit 4 (ሥጋሁ ለምድራዊ), where ለ- names the owner after the suffix and the parse differs. | Second sense added with ' · '. |
| 9 | ከርሡ · `__broaden__` (new) | moderate | Known entry 'his belly, his body'; pass 1 set unit 10 to 'womb' (house ch. 68; the published ከርሥ entries say 'belly, womb'), but the gloss was not brought into line. | Broaden: known entry whole + ' · his womb (… በውስተ ከርሡ ለአዳም …, the house reading as in ch. 68)'. |
| 10 | ወተውላጠ · gloss | minor | Two stacked '(?)' and an unreferenced 'sense and form uncertain'; no tie to the published ተውላጥ (ch. 9-12). | Rewritten: 'and a change, exchange (?)', accusative predicate of ኮነ, cf. ch. 9-12. |
| 11 | ወበንጽሓ, ወዕጹታ, ወቈጽላ · gloss (3 entries) | minor | Suffix labelled '-ሃ' after a consonant; the house form is -ኣ (-ሃ only after a vowel, as ሥጋሃ). Unit 19/23 notes already say -ኣ. | -ኣ in all three. |
| 12 | ለንጽሕት · gloss | minor | 'ለ- marking the object': the object is the suffix -ኣ of ገብራ; ለንጽሕት is the complement. | 'ለ- introducing the complement "as pure"'. |
| 13 | ቀርሜሌዎስ · gloss; unit 0 · n | minor | Gloss still 'Qarmeleyos' (pass-1 #9 fixed the unit, but the note still read 'mount of Qarmeleyos' once). | 'Qarmelewos (?)' in both. |
| 14 | unit 0 · n | minor | Suffix of አዕረጎ called -ዎ; after the consonant of a perfect it is -ኦ (as known ወቀተሎ -ኦ, gloss -ኦ). | -ኦ. |
| 15 | unit 8 · n; unit 13 · n | minor | Same -ዎ for ኮነቶ and ወቀተሎ. | -ኦ in both. |
| 16 | አምሳሊሁ · gloss | minor | 'written -ሊሁ' left the suffix-stem unexplained (pass-1 #20) and the anticipating ለክርስቶስ unmentioned. | 'suffix-stem አምሳሊ- + -ሁ; ለክርስቶስ ወልድ names the owner'. |
| 17 | ቤዛሁ · gloss | minor | Occurs twice in unit 4; second use (ቤዛሁ ለመለኮት) is the anticipating suffix. | Second sense added. |
| 18 | ዘኒ · gloss | minor | Cited only the unit-7 use; unit 15 is the second. | Both uses cited, still (?). |
| 19 | ኆኅተ · gloss | minor | Cited one accusative use; unit 16 has it twice, the second as apposed predicate. | Predicate/apposition use added. |
| 20 | ሥና · gloss | minor | The suffix reading ሥን + -ኣ 'her beauty' (cf. ቈጽል-ኣ; the published በስንኣ) was not mentioned. | Added as an alternative, hedged. |
| 21 | unit 17 · n | minor | Same alternative missing from the note; also ብሀለ (house spelling ብህለ). | Alternative added; ብህለ. |
| 22 | unit 18 · n | minor | ብሀለ. | ብህለ. |
| 23 | ሕብል · gloss | minor | 'cord, rope (?)' with 'perhaps deceit': not tied to the i ('snare (?)') and double '(?)'. | 'cord, rope, snare (?)', 'word of snare, a deceiving word'. |
| 24 | ወዘይቤሂ · gloss | minor | 'what he says': ይቤ is the perfect, 'said' (unit l has 'said'). | 'and what he said also'. |
| 25 | አዕረጎ · gloss | minor | 'he brought up' dropped the object -ኦ in the English of the entry. | 'he brought him up, offered him up'. |
| 26 | unit 1 · n | minor | 'tä-stem of a four-letter verb': ተርጐመ is itself the four-letter G stem (house lemma ተርጐመ); the form is its passive. | Rephrased accordingly. |
| 27 | unit 4 · l | minor | l 'his-flesh, the-earthly' dropped ለ- of ለምድራዊ (house practice keeps proclitics: 'for-the-divinity' beside it). | 'his-flesh, of-the-earthly'. |
| 28 | unit 4 · n | minor | ሐመ 'suffer'; the verb is ሐመመ (gloss; ch. 61 ሐመምክሙ). | ሐመመ. |
| 29 | unit 16 · l, i | minor | ሙባኦሙ is hedged (?) in n and gloss but not in l/i ('by which the saints enter' was a fuller verbalization). | l 'their-entering(?)'; i 'the entrance (?) of the saints into the kingdom of heaven'. |
| 30 | unit 22 · n; unit 23 · n | minor | 'ወዐየ' for the verb; the house lemma is ውዕየ (ch. 49-50 ወውዕየት, gloss). | ውዕየ (2 places). |
| 31 | unit 23 · i | minor | 'the bush that burns' dropped ዕፀ 'tree/wood of' (l has 'tree-of bush'). | 'the tree of the bush that burns while its foliage is not consumed'. |

Severity totals: major 2 (#1, #2); moderate 7 (#3-#9); minor 28 (rows #10-#31 are 22 rows; counted per entry or place they are 28: #11 three entries, #13 two places, #15 two places, #21 two fields of one note, #30 two places, and #29/#10/#12 etc. one each; the በዕልወተ cross-reference is part of #3). Total 37.

## Checked and found sound (no change)

- Lemmas and parses of the other entries agree with every occurrence: e.g. ወሰሚዓ (gerund 3fs, subject Eve), ኮነቶ (ኮነት + -ኦ, both uses), ተመንደብነ (as ch. 91 ተመንደብኪ), ተላዐልነ, ወተቀበርነ, ተፈወስነ, ናክብራ, ዘይኔጽርዎ (-ዎ after a vowel is right), ወአንሥአነ, ወሐደሳ, አኅደራ, ፈደየት, ዕዳሁ, ዘትነድድ, ኢትውዒ, ኢትመውት, በላዒ, ጳጦስ, ወላዲተ, ያርኢ, ተኀትመት.
- `__broaden__`: ገብራ, ለ, መሥዋዕተ, ንጉሠ, ለሰብእ are old entry whole + ' · ' + a reading that fits the unit.
- Units: Ezekiel 44:1-2 and Exodus 3:2 quotations rebuilt from the Geʿez, not from the English Bible; l and i agree elsewhere after the edits above.

## Findings refused

1. አዕረጎ lemma አዕረገ (dictionary form of the causative). Refused: the published ወአዕረገነ (this chapter, known-forms) has lemma ዐርገ with the causative named in the parse, as does house practice for ናክብራ/ወአንሥአነ; consistency with the published entry wins, and the parse names አዕረገ.
2. ተጠብሐ, ኢተጠብሐ, ተጠብሐት: lemma ጠብሐ rather than a tä-lemma. Kept: the house lists ጠብሐ in ch. 40, 83-86; tä-passives appear under the G root (ተፈጥረት → ተፈጥረ is the exception where the tä-form is itself the headword), and the parse says 'tä-stem passive'.
3. ዕድው lemma against the probable Dillmann spelling ዕዱው 'enemy' (?). Not changed: ch. 92-93 (published) uses ዕድው 'enemy'; the lemma stays so; if ዕዱው is confirmed the published part should be corrected together with this one.
4. ሙባኦሙ lemma ሙባእ: unattested to me (a noun of place from ቦአ would be መባእ/ምባእ). Dillmann unavailable; the entry already says 'stem uncertain (?)'; no better headword can be named without invention.
5. ወትጤይቁ '(?)' after 'investigate': kept (ጠየቀ is the house lemma, 12 published uses); the (?) marks the odd form ጤይቁ and costs nothing.
6. ናክብራ 'jussive/imperfect': form cannot decide; entry says both.
7. Unit 7 · i 'the interpretation concerning the first man': l has 'of'. Left as acceptable English; ዘኒ is hedged.
8. Unit 2 · ይወርድ past sense after አመ ('when he came down') against known 'it will descend': a relative-time use; left, the note says so.
9. Title and `about` 'the Shut Gate': ዕጹት 'shut' is in the text (unit 19) as well as ኅቱም 'sealed'; both words are true of the gate, so the title stays.
10. Unit 21 · i 'by what was hers (?)' and units 13/14 length: as pass 1.
11. ትሌብዉኑ 'understand, grasp (?)' with root ለበወ: matches the published ለበወ entries (ch. 25-26, 60a, 70); kept.
