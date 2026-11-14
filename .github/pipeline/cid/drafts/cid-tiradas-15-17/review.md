# Review — cid-tiradas-15-17 (lines 242–294)

## Pass 1 — units.json

**Continuity (after edits):** PASS. 23 units; concatenated `t` = the packet's 56 lines exactly, in order (248b,
269b, 282b included); every `l` has as many lines as its `t`; all units 1–4 lines; no unit crosses a tirada break
(tiradas start at units 0, 13, 19). `t` untouched.
Assonance re-derived from the line-endings: 15 á-o (mandado … echado; nasco fits), 16 í-a (complida … servida),
17 ó with ó-e (pregones, onores). All three claims correct. Every cross-reference to vv. 1–241 was checked against
the published parts' line numbers; three were wrong (u0, u5, u17) and one misattributed (u16).
Bracket claims (f[o], lu[m]bres, [el que en buen ora nasco], mi[o]s, visquier[o], se[e]rvos, [las], [en los braços],
f[o]stes, su[e]s, mi[e], ve[e]des, o[d]iendo, Arla[n]çón, buen[a]) say only that Pidal restored the letters. Correct.
v. 262 ilegando: the note says the print has ilegando, read as llegando, most likely a misprint, and the text follows
the print. Correct and honest; kept.

### Changes
| unit | field | severity | what was wrong | what was done |
|---|---|---|---|---|
| 0 | n | error | Called Dios, qué alegre … ! the minstrel's voice "as in v. 20"; v. 20 is the burghers' quoted cry, not the narrator | Now: the narrator's own exclamation; the same opening as the burghers' cry at v. 20, but there it was quoted speech |
| 5 | n | error | far "as at v. 230"; far is at v. 229 (castigar los he commo abrán a far); v. 230 is the m'incal line | v. 229 |
| 16 | n | error | complida "the word he used of his beard at v. 268": it is Ximena who says barba tan complida | "the word Ximena used of his beard at v. 268" |
| 17 | n | error | "y … usually 'there' in this poem, as at v. 236": v. 236 has no y (Y estava is v. 239), and y/i is 'and' at vv. 2, 13, 242 | "taken as 'and' (as at v. 13); it can also mean 'there' (as at v. 239)"; the alternative reading kept |
| 3 | l | weak | "I-am with-you satisfied": vuestro is 'your', not 'with you' | "I-am your satisfied-one"; note now says vuestro has the force 'with you' |
| 3 | i | weak | "I am beholden to you" (indebted) against the note's pagado 'pleased, content, not paid' | "I am well content with you" |
| 10 | i | weak | "a lady to each carries them, bearing them in her arms": a singular subject with a plural verb, and "her" for several ladies | "a lady apiece carries them, bringing them along in their arms" |
| 15 | n | weak | "it has also been taken as a bow of the head and hands": a report of scholarly opinion the sources here do not give | "a gesture of bowing is not ruled out, but the next line favours reaching down for the daughters" |
| 13 | n | weak | "the copyist's doubled ff": a claim about the manuscript the print does not show | "spelt with a doubled ff, kept as printed" |
| 13 | n | weak | iffantes "(later the word meant 'princes')": misleading; the poem itself uses the word of young noblemen | "(the word also names young men of noble birth, as it will later in the poem)" |
| 19 | n | weak | a clamor "the bells swung together": a detail the line does not give | "a loud, full peal" |
| 16 | l | style | "I so-much you was-loving": ungrammatical with I | "I so-much you loved" |
| 22 | l | style | "in good(hour) was-born" against the published form of the ora-less formula | "in a-good (hour) was-born", as pilot and 10-14 |
| 6 | n | style | "çient = ciento": the apocopated form corresponds to modern cien | "çient = cien, ciento cut short before its noun" |
| 9 | n | style | "avie, as at v. 6": v. 6 has accented avié | "as at v. 22" (el rey … tanto avie le grand saña) |
| 11 | n | style | "the words of its first surviving line": v. 1 reads De los sos ojos … llorando, not Llorava de los ojos | "the words that open its first surviving line (De los sos ojos … llorando)" |

### Considered and refused
- Title/part use "Ximena" where the packet header has "Jimena". Refused: the text, the i fields and the previous part all say doña Ximena; the owner may normalize titles at assembly.
- u0 i: "the news was known within" for sopieron el mandado. Refused: it carries the unannounced subject shift the note explains.
- u4 i: "if I live to see the day" for si yo algún día visquiero. Refused: a fair English idiom; the note gives the literal 'if I live (on) some day'.
- u6 n: "The Çid expects his exile to last at least a year" (from est año). Refused: a reasonable inference from the text, plainly put.
- u10 l: "carry" for traen ('bring'). Refused: traer covers carrying, and the note glosses both verbs as 'to bring'.
- u14 i: "we must be parted" for the split future partir nos hemos. Refused: the future here is one of necessity, and v. 280 i matches.
- u20 i takes the "proclamations go about being heard" reading of o[d]iendo van. Refused: the note states both readings and flags the construction as uncertain; i has to choose.
- u22 n: ellos' read as the reflexive se swallowed after the s. Kept: it matches the line as printed (con ellos' cojó) and Pidal's use of the apostrophe for a lost letter.

## Pass 2 — gloss.json

Keys = the 114 novel-forms.json keys exactly, plus `__broaden__`. Every entry checked against the line(s) where the
form occurs and against the notes. No units.json change was needed; continuity re-run: PASS (56/56).

### Changes
| key | severity | what was wrong | what was done |
|---|---|---|---|
| cojó | error | Quoted the line as "con ellos cojó", dropping the apostrophe and the reflexive the line has (con ellos' cojó) | "coger — he gathered, took (preterite 3rd sg., spelt with j; = cogió); with se, 'to join': con ellos' cojó = con ellos se cogió" |
| aqués | error | Lemma aqueste 'this', = este; aqués is aquese 'that' (aqués día 'that day'), as the note says | "aquese — that (masc. demonstrative, cut short; = ese)" |
| han | error | "split future auxiliary (= habrán)": seervos han = os serán; han itself = han | Rewritten: present 3rd pl. = han; after an infinitive, the split-future auxiliary (seervos han = os serán) |
| odiendo | error | Gloss "being heard … 'go sounding'": a gerund of oír is 'hearing'; the passive reading is one of two the note leaves open | "oír — hearing (gerund, with the old intervocalic d; = oyendo)" |
| señas | error | Lemma "seña" (= sign); the distributive is señas (= sendas) | "señas — one each, one apiece (distributive adjective, fem. pl., Latin singulas; = sendas)" |
| sirvádeslas | error | Invented modern form "sirváis las" | "= que las sirváis" |
| remanida | error | Invented modern form "= remanida"; lemma remanir against the note's remaner | "remaner — left behind, remaining (past part. fem.; = quedada)" |
| mie | weak | "diphthongized variant" of mi: mie is the feminine of mio | "mie — my (fem. sg. of mio, before a noun; = mi)" |
| emos | weak | "short form of hemos": it is hemos without the h | Rewritten in format, split-future use stated |
| visquiero | weak | "(if) I shall live" for a future subjunctive; lemma bivir against the note's vivir; pinned "restored visquier[o]" | "vivir — (if) I live, should live (future subjunctive 1st sg., strong stem visqu-; = viviere)" |
| quísol | weak | "= quiso" drops the le | "= le quiso", meaning made explicit |
| braço | weak | Gloss "arm (sg.)" but the token occurs as braço' = braços, plural | Plural with lost s stated |
| enclinó | weak | "he bowed" against the note's reading (lowered/stretched the hands) | "he lowered, bent, inclined" |
| iffantes | weak | "a noble prince" | "child, young child …; also a young man of noble birth" (as the note) |
| quien | weak | Did not cover the plural antecedent (dueñas de quien) | "also with a plural antecedent; = quien, quienes" |
| evades | weak | Presented as a settled formula; the note says its make-up is uncertain | "the make-up of the form is uncertain" added |
| ilegando | style | Not in the house format; "is a misprint" stated as certain | "llegar — arriving, coming up (gerund; = llegando; Pidal's print has ilegando, read as llegando)" |
| seervos | style | No meaning/modern form in the house format | "seer + vos — to be … to you (…: seervos han = os serán)" |
| adúzenlas | style | Lemma aducir against the note's aduzir | "aduzir + las … (= aducir; = las traen)" |
| lumbres | style | "(pl.; = lumbre)" | "= lumbres" |
| dues | style | Lemma "dos", not the form's own | "dues — two (old fem. form; = dos)" |
| va | style | Modern form missing | "= va" added |
| __broaden__ complida | weak | New reading pinned to two lines and not in the entry format | "· also complido — full, perfect, accomplished (adjective, fem.; = cumplida)" |
| __broaden__ que | style | New reading pinned to the line | "· also por que — because, since (= porque)" |
| __broaden__ de | weak | Missing: known entry "de — of, from" does not cover the agent 'by' of vv. 270, 284 (de quien so yo servida, de mí seades servida) | Added: "de — of, from · also de — by (the agent with a passive participle; = por)" |

### Considered and refused
- fem: "fe + me, = heme aquí". Kept: matches the note.
- afevos "a + fe + vos" vs the note's "afé + vos". Refused: the same analysis.
- reçiben lemma "recebir", gradéscolo "gradecer", falleçiere "fallecer", naçió "nacer" (notes write nasçer, falleçer). Refused: spelling of the lemma, not a contradiction (as in the 10-14 review).
- quería "(imperfect 1st/3rd sg.)": correct; it is 3rd sg. at v. 276 and 1st sg. at v. 279.
- Known entry fostes "= fuestes" (modern fuisteis). Not this part's novel form; left for the glossary owner.
