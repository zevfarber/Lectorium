# Review, kebra-nagast-ch90

## Pass 1

Checked: `t` joined against the packet (identical after whitespace normalisation, 36 units, `t` and every `p` flag untouched; the packet has the heading and one body paragraph, `p: true` on units 0 and 1 only; units 4 (40 words), 27 (41) and 21 (33) stay whole, none has an inner ፤ to cut at and all are under ~45); every grammatical label in every note against the form; original to `l` word by word; `l` to `i`; remembered English in `i` (the scriptural passages, Psalm 125:3 and the Deuteronomy 27 curses, were checked against the Geʿez, not against any English text); consistency with known-forms.json and with the published parts as they appear there and in ch. 88, 89, 40, 38-39, 49-50, 81 (found by searching the published JSON); house renderings from conventions.md and the ch. 89 review. Dillmann and Budge are not available, so lexical calls stay hedged with (?). Edits by script to `l`/`i`/`n`/`about` only (json, ensure_ascii=False, indent 1). Unit numbers are 0-based positions in units.json. gloss.json does not exist yet (first pass).

### Changes

| Unit | Field | Severity | What was wrong | What was done |
|---|---|---|---|---|
| 33 | l, i, n | major | ዳዊት አበ አቡሁ ለእግዚእነ ዳዊት was rendered 'the forefather of our Lord (David)', and the note declared it Christian ('ancestor of Christ'). In this book the party's 'our lord' is Menelik, styled David since ch. 87 (ch. 88 note; known entry for ዳዊት 'your lord David'), and King David is the father of his father (Solomon's father): the phrase says exactly that. The Christ reading has no support in the form and `i` also dropped 'father of the father'. | `i` 'the father of the father of our lord David'; `l` 'lord'; note gives the Menelik reading, marks it (?) against the Christ reading, and says the repeated ዳዊት is kept. |
| 0 | l, n | moderate | ወደሳ read as a bare 3ms perfect; it is ወደሰ + -ኣ 'her' (the queen), the object doubled by ለንግሥት, and the ወ is a root letter. The note called ለንግሥት 'to/of' and gave no function for the second ለ- in ወለሀገራ; `l` lacked 'her'. | `l` 'praised-her'; note rewritten (suffix, doubling as in ch. 89's heading, ለ- marking the object, ሀገራ = ሀገር + -ሃ). |
| 1 | l, i, n | moderate | አእምሮ rendered 'understanding' in `l`/`i`, against the house pair fixed in ch. 89 (አእምሮ 'knowledge', ልቡና 'understanding'). | 'knowledge' in `l` and `i`; note says so. |
| 4 | l, i | moderate | ሕሱመ, ፀዋገ, ንከይድ are all uncertain in the note and ሕሱመ/ፀዋገ carry (?) in the glossary or published parts, but neither `l` nor (for ሕሱመ) `i` showed it. | (?) added after 'defective' and 'affliction' in `i`, and in `l` after those two and 'tread'. |
| 5 | n, l, i | moderate | ኮንክሙ called a verbal noun 'your being'. It is ኮነ, 2mp perfect + -ክሙ (the known entry says so), which is also what makes the clause read: 'you are dark of face'. `l` 'being-your' was a non-form. | Note corrected; `l` 'you-became'; `i` 'that you are dark of face'. |
| 5 | n, l, i | moderate | ዘይነኪየክሙ derived from ነኪር 'strange, foreign', but the form ends in -y, not -r; a derivation from ነኪር is doubtful and `i` presented 'finds you strange' with one flag. | Note says the link is doubtful and another root (perhaps 'harm') is possible (?); `i` 'finds you strange, or does you harm (?)'; `l` (?). |
| 6 | l, i, n | moderate | ተገሐሡ rendered 'keep away' against the house 'turn aside' (chs. 88, 89, 40; the ch. 89 pass 2 settled the verb on 'turn aside'). | `i` 'turn aside from'; note ties it to chs. 88-89 and glosses 'keep away' as the sense of ተገሐሡ እም-. |
| 6 | i, n | moderate | እማውታ 'from the dead' with no flag though the published entry is 'sense here uncertain' and the company (blood, fornication) points to a food or purity rule. | (?) in `l` and `i`; note adds that the list may recall Acts 15:20 (?), which would give 'what has died of itself' (?). |
| 9 | l, i, n | moderate | The same verb ይሰአኖ is 'is hard for him' in `l` and 'is too hard' in the closing clause, but `i` made the first 'what could hinder God', changing the force of the rhetorical question. | `i` 'What is too hard for God, if he loved us and hated them?'; note matches. |
| 11 | l, i, n | moderate | The note says ተሓመየ cannot be fixed, yet `l` 'harm-one-another' and `i` 'injure one another' were unflagged; ኢትሂዲ 'carry off' had (?) in `i` only. | (?) added in `l` and `i` for both; note says 'injure' is only a guess. |
| 13 | i | moderate | 'helped lift it out': neither 'help' nor 'out' is in ወታስተላዕልዎ ('and you lift it'); imported from the Pentateuch law. | 'until you have told him and lifted it up'. |
| 15 | l, i, n | moderate | `i` supplied 'a beast' and 'under him' for ጸዓነ ... ዘወድቆ: no animal is named in the Geʿez (the ass and ox are from Deuteronomy 22:4 / Exodus 23:5), and the note itself marks ዘወድቆ (?). | `i` 'or if someone has loaded up and it has fallen on him (?)'; `l` (?) on the two uncertain words; note says no animal is named. |
| 20 | n | moderate | ኢትጠናቀቁ called 'the Gt' of a quadriradical; Gt is the stem of triradicals. | Called 'a ተ-stem form'; stem label and meaning marked as my reading (?). |
| 29 | n | moderate | አንስት said to be 'the plural of ሴት' (an Amharic word); the lemma is ብእሲት (known entry). | Corrected. |
| 31 | l, i, n | moderate | ይትገሐሡ 'keep away', as in unit 6 (house 'turn aside'). | 'turn aside' in `l`, `i`, note. |
| 32 | l, i | moderate | ተገሐሥ 'keep away' (same). | 'turn aside'. |
| about | about | moderate | 'the dark skin ... a flaw that God can mend': the text says that if God lights up their hearts no one will find them strange (?), and says nothing of mending skin. | Reworded to what unit 5 says. |
| 1 | i | minor | 'there is none except my lord the king' repeated 'there is none', which the Geʿez does not; ዘእንበለ governs the whole claim. | 'resembles you ..., and it was given to you from God, except my lord the king'; note says ዘእንበለ qualifies the whole claim. |
| 1 | n | minor | ተማሰለ called 'reflexive'; it is the ተማ- stem of መሰለ. | Relabelled. |
| 2 | l, i, n | minor | ሰብአ ቤቱ 'men of his house' against ch. 88 'people of his house'; መማክርቲሁ unexplained. | 'people'; note cites ch. 88 and glosses መማክርቲሁ. |
| 3 | n | minor | ኄየሰ for the verb of ትኄይስ; the glossary lemma is ኀየሰ, and the sense is 'better'. | ኀየሰ 'be good, be better'. |
| 4 | l | minor | `l` left ገስስ in Geʿez though the note and `i` read it 'touch'. | 'we-touch'. |
| 4 | n | minor | ፀዋገ glossed in chs. 49-50 'captor (?)' and in ch. 81 'grim (?)': the divergence was not disclosed; 'not smell' for ንከይድ was an unsupported claim. | Note cites the published uses, calls 'affliction' a guess from the pairing with ሕሱመ, links ሕሱመ with ሕሡመ in unit 22; 'not smell' replaced by 'I do not find a verb of smelling in the form'. |
| 5 | n | minor | 'as in the biblical eyes of the heart enlightened' quoted remembered English. | 'cf. Ephesians 1:18 (hearts enlightened) (?)'. |
| 6 | n | minor | ትርዕዲ 'singular-looking': the ending -ዲ is the 2fs ending; sense plural. | Says so (slip or collapsed ending (?)). |
| 6 | n | minor | 'comes in the next paragraph': there is one body paragraph; ኢትትገሐሡ is in unit 8. | 'comes in the next sentence but one'. |
| 7 | n | minor | 'recurs in units 9 and 34': units 9 and 34 contain no በከመ (the cases are units 8 and 33). | Cites the phrases instead of numbers. |
| 7, 33 | i | minor | Quotation marks: unit 7 opened a second ‘ inside Azariah's open ‘ and never closed it; unit 33 closed with ’. | Inner speech in “ ”, closed. |
| 8 | i | minor | 'our own people': 'own' not in the Geʿez. | 'our people'. |
| 11 | n | minor | 'endings -ዩ/-ሁ/-ኡ': there is no -ሁ plural ending; the plural is -u on the last consonant. | Reworded. |
| 12 | l, i | minor | ዘአተወ 'led in / driven' had (?) in the note only; 'that belongs to your neighbour's goods' did not follow እም-. | (?) in `l` and `i`; 'one from your neighbour's goods'. |
| 13 | i, n | minor | ግብ 'ditch' against the house 'pit' (known entry; `l` already 'pit'). | 'pit'; note. |
| 14 | l, i, n | minor | ዐዘቅት rendered 'pit' here and 'well' in unit 13. | 'well' in `l`, `i`; note cross-refers. |
| 17 | l | minor | `l` 'orphan' for እጓለ ማውታ; `l` is meant to be structural. | 'child-of dead (orphan)'. |
| 18 | l, i | minor | ሕልያነ 'bribes' without the (?) of the known entry. | (?) added. |
| 19 | l, i | minor | `l` 'in-midst' for በውስተ ('in, within'); አፍኅርቲሃ 'fledglings' flagged in the note only. | 'in'; (?) on 'fledglings'. |
| 20 | n | minor | ተዐጽዲ called 2mp; the ending -ዲ is 2fs, sense plural; ዐጺደ unexplained. | Corrected; ዐጺደ named as accusative verbal noun. |
| 20 | l, i | minor | ጠናቀቀ, ኢትእርዩ and ክልስስተ are (?) in the note but not in `l`/`i`; `l` 'in-reaping' added a preposition. | (?) in `l` and `i`; `l` 'reaping'. |
| 21 | l | minor | `l` dropped the object -ሁ of ዘያስሕቶ. | 'leads-him-astray'. |
| 21 | n | minor | 'he (Moses) wrote' stated as fact; the subject is unnamed (God is the last subject). | Hedged. |
| 22 | l, i, n | minor | ጽሙም 'deaf' unflagged in `l`/`i`; ሕሡመ in unit 22 and ሕሱመ in unit 4 are probably one word and the renderings did not connect. | (?) added; note cross-refers. |
| 26 | n | minor | 'Like the next-but-one curses, it begins without ወ-': only the killer curse (unit 30) lacks ወ. | Corrected. |
| 27 | l | minor | `l` omitted -ሁ in ዘገብሮ. | 'who-made-him to-Adam'. |
| 28 | n | minor | 'From here the curse takes the form ...': unit 27 already ends with it. | Corrected. |
| 30 | l, i | minor | ይትዔወርዎ 'disregard him' flagged (?) in the note only. | (?) in `l`, `i`. |
| 31 | n | minor | Note quoted remembered English of Luke 11:28. | 'cf. Luke 11:28 (hearing and keeping the word of God)'. |
| 34 | l, i, n | minor | መካልይ 'measures' and ትርብዕተ 'fourfold' unflagged in `l`/`i`; the Gospel parallel was a single guess. | (?) added; note adds that 'he did and taught' resembles Matthew 5:19 (?), Luke 19:8 kept with (?). |
| 35 | l | minor | `l` left ርዴ/ልቃሕ unflagged. | (?) added. |
| about | about | minor | 'He closes with Psalm 125:3': the Psalm is cited in unit 33; the chapter closes with the usury precept. | Reworded. |

### Findings refused

1. Unit 0 `i` 'How' for ኀበ: matches chs. 88 and 89 (house heading form). Refused.
2. Unit 3 `i` 'we have seen that the country of Ethiopia is better': ርኢነ እንተ ትኄይስ ሀገረ ... is an unmarked relative with the country as apposition; the note says so and `l` is literal. Refused.
3. Unit 4 `i` 'the livestock are like the sand' and 'the air is without ...': copulas supplied where Geʿez has none; unavoidable. መረዋሕት, ጸቃውዕ, ጽንጒነ stay in Geʿez with (?) (honest; I cannot improve them without Dillmann). Refused.
4. Unit 5 `i` 'meets the eye' for እምእንተ ትኔጽር: loose, but the note shows the Geʿez and flags 'I read it'. Refused.
5. Unit 9 `n` allusions (Genesis 18:14, Malachi 1:2-3): named as echoes, not quotations, and `i` is built from the Geʿez. Refused.
6. Unit 12 `n` 'do not hide yourself' (Deuteronomy 22:1) quoted in a note: only `i` is bound to the no-remembered-English rule; the quote is marked 'cf.'. Refused.
7. Unit 12 ወእምከመ ረከበ ... who finds whom: left open in the note with (?). Refused.
8. Unit 24 `i` 'in secret' without (?): Deuteronomy 27:24 and unit 30 fix the sense. Refused.
9. Unit 25 and 30 ነፍሰ ደመ ንጹሐ / ደመ ንጹሕ: both hedged in notes; nothing better available. Refused.
10. Unit 26 ዘያስተአኪ 'dishonours' (?) and its stem label: root and stem cannot be confirmed without Dillmann. Refused.
11. Unit 27 ኢአሚኖ 'not believing' as a negated participle, and `i`'s parallel 'that we are all his creatures' (ወኵልነ ተግባሩ ንሕነ): sense-true. Refused.
12. Unit 32 ከመ ኢትዘበጥ: the passive label has a form problem (ትዘበጥ has no ተ- prefix visible) but I cannot say more than the note does. Refused, listed as a crux.
13. Unit 34 ይፈደፍድ 'grows' and መካልይ: kept as hedged above; no better reading.
14. Unit 35 `i` 'interest or demand for repayment (?)': honest guess. Refused.
15. Unit 2 `i` 'used to say' for ንቤ: the note declares the habitual reading as an interpretation. Refused.
16. Unit 33 `i` Psalm 125:3 wording ('rod', 'lot'): these are the plain meanings of በትር and መክፈልት; not remembered English. Refused.

### Outside units.json (for the glosser / second pass)

- known-forms entry ይትገሐሡ ('they hasten, move about (?)') conflicts with the house 'turn aside'; broaden, do not replace. ተገሐሡ, ተገሐሥ, ኢትትገሐሡ to follow ተግሕሠ / ኢትትገሐሥ in chs. 88-89, 40.
- known entry ፀዋገ ('captor (?)') does not cover 'affliction (?)' here; broaden with the guess marked (?).
- ወደሳ must parse ወደሰ + -ኣ 'her' (ወ a root letter); ወለሀገራ = ወ- + ለ- + ሀገር + -ሃ.
- ትርዕዲ and ተዐጽዲ carry the 2fs ending with plural sense; ዘይነኪየክሙ must not be derived from ነኪር; ኮንክሙ is already right in known-forms (ኮነ, 2mp perfect).
- ኢትጠናቀቁ is not a Gt; ሕሱመ and ሕሡመ should be cross-referred; አንስት lemma is ብእሲት; ተማሰለ (ዘይትማሰለኪ) is the ተማ- stem of መሰለ.
- ዘከረየ / ዐዘቅተ 'well' and ግብ 'pit' to be kept distinct.

### Counts (pass 1)

major 1, moderate 16, minor 32 (rows in the table above: 49; refused findings: 16).

### Remaining cruxes

መረዋሕት, ጸቃውዕ, ጽንጒነ, ብትክ, ሕሱመ/ሕሡመ, ፀዋገ, ንከይድ, ኢትሂዲ, ተሓመየ, ተላኰዩ, ዘአተወ, ጸድፍ, ጠናቀቀ/ኢትእርዩ, ክልስስተ, አፍኅርቲሃ, ማኅፈደ, ተድባብ, ዘያስተአኪ, ጽሙም, መካልይ, ትርብዕተ, ርዴ/ልቃሕ (all (?) and unresolved without Dillmann); ዘይነኪየክሙ (root); the ዳዊት phrase in unit 33 (Menelik reading, (?) against the Christ reading); ኢትዘበጥ (form); እማውታ (Acts 15:20 guess).
