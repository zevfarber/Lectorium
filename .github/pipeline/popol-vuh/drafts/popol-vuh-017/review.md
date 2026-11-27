# popol-vuh-017 — review

## Pass 1

I checked all 60 units against conventions.md (the house renderings table included), the packet and establishment log, the
drafter's notes, QUESTIONS.md (with the 017 establish entry and its two README-5b corrections), the published parts
001–016, the glossary and 016's review. A script compared every token's mt with the mt of the same form in 001–016; every
new form's mt was read against its manuscript word under the toggle rules. Every grammatical label in the notes was read
against the form (person markers, ergative/absolutive, completive/incompletive, active/passive, agent focus), `l` against the
original word by word and `i` against `l`. Every claim the notes credit to Brasseur was checked in the OCR (lines
24555–25070, K'iche' text, French and footnotes). Every doubtful reading in the establishment log was traced to its unit's
note. Edits were made by script (load, change named fields, dump with ensure_ascii=False, indent=1); gloss.json was not
touched. After the edits, a script check confirms: no t changed; the 60 units tile the 19 pinned paragraphs exactly; each
paragraph starts a unit (U1, 2, 4, 6, 8, 11, 13, 16, 21, 26, 29, 32, 36, 39, 42, 45, 48, 54, 59); and every mt has one
entry per WORD_RE token.

Counts: 0 major, 12 minor, 5 style.

### Changes

- U30, U31, U51, U58 · mt/n · minor · The cry word oꜫ, written with plain c (xoc, v oquibal, choquic, coquic, mix oquic), was left ok- by the letters, while bico / xbic, in exactly the same position (plain c, Brasseur's g, a certain modern word), was restored to b'iq'. The 007/010 rule (QUESTIONS 010 point 1) restores the mark where the word is certain and Brasseur's letter agrees. Here the word is certain: the bird's call, the grandmother weeping, "do not weep". 015's choc was left chok only because its reading was inferred. · mt xoq', oq'ib'al, choq'ik, koq'ik, oq'ik. The notes say so and keep the distinction from oc 'enter' (xok, okik). 015's chok goes to the owner.
- U2, U5, U50 · mt/n · minor · The 'play' root was split inside the part: quetzabal → ketz'ab'al (the published queꜩabal), but etzanem / etzanic → etz-. The word is certain (modern etz'anem). Supplying tz' on the plain ligature is the practice of 009, 015 and 016 (ketz'ab'al, tz'iloj, tz'onoj, tz'apij). · mt etz'anem, etz'anik. The notes say so, and say that 006's etzeyaj stays as published and should be brought together with them.
- U4 · n · minor · "xe may be the 'they' of the lords … or the object" did not say what xe is. xe is the absolutive, and no ergative is written. · The note now says that xe is the absolutive, that with Brasseur's reading the lords' qui- is unwritten, and that as written xe is the one sent or sent for.
- U14, U19 · n · minor · chavah was analysed "ch- + a- 'you' + v-? + ah", "the v is not explained", and Chavila "ch- + a- 'you' + vila". The v is the 2sg ergative before a vowel, av-, just as v- 'I' in vilo in the same unit. · Both notes now say this. chavah is ch- + av- + ah 'want'; Chavila is ch- + av- + il 'see' + -a.
- U7 · i/n · minor · "She and the boys were eating (?)": que is 'they', with no subject named, and the boys are away at the ball court (¶1, ¶4). "and straight down it (?)" was not English. · i: "and the messengers came straight (?) to the grandmother. They were eating (?) when …". The note says that 'they' is unnamed and the boys are away.
- U12 · n · minor · Brasseur runs Mavi quitzih ri Xibalba (end of U11) into this sentence as one question ('N'est-ce pas véritablement de la même manière que vinrent autrefois les envoyés'). The note did not say so. · Added. The established punctuation is kept.
- U21 · l/n · minor · l had "it-was-swallowed(?)", but i and the note have 'taken in'. The stem ric was not considered as the riq 'find, come upon' of 003's chu rico. · l "it-was-taken-in(?)". The note gives the ric alternative (guess either way). mt left by the letters (k), as the link is a guess.
- U41 · n · minor · Brasseur prints Nakipa qo takikil, with qo where the text has a. The establishment log is silent and the note did not say so. · Added to the note. The text is kept as established, and the difference is flagged for the establisher.
- U43 · n · minor · xrah chaiic was labelled "'it was wanted, the beating'", a passive. xrah has the ergative r-, so it is active, 'it wanted' (the fixed construction; cf. 016 review, ca rah). l already had "it-wanted". · The note now gives x- + r- 'it' + ah 'want', active, with cumal ꜭaholab naming the boys.
- U46 · n · minor · "The toad's offer to carry the louse in ¶8 was a trick" said the opposite of the text: the toad is the one fooled (U47 xchacatah; Brasseur 'C'est ainsi que fut joué le Crapaud'). · The note now says that the toad never had the louse inside and was the one fooled.
- U59 · n · minor · xticou was called "the form that puts the doer first", but Xbalanque follows the verb here. · The note now calls it the agent-focus form of 014's xe chacouic (inferred) and says that the doer here follows the verb, where in 015 it stood before it.
- U60 · n · minor · Singular xu tic vi ('he planted') stands beside plural xqui tic for the same act, and i gives 'they' for both. The drafter's notes mention this, but the unit's note did not. · Added.
- U14, U19 · i · style · "will you let me send / swallow you" for chavah 'do you want'. · "would you like me to send you …", "Would you like me to swallow you?".
- U15 · i · style · The inner quotation closed after "says your grandmother", so the grandmother's tag was inside the messengers' words. · "‘You are to go there; in seven days they are to go there,’ say the messengers of Xibalba, says your grandmother.”"
- U29 · i · style · The pair que quicot … que chaahic was collapsed to "happily playing". · "were rejoicing, playing ball".
- U33 · i · style · "they ran to catch it" for xbe qui chapa 'they went to catch it'. · "they went to catch it".
- about · style · "Do not weep" came after the planting, but the text has the speech first and then the planting. · Reordered.

### mt against the published parts

After the edits, five forms have an mt that differs from the published mt for the same letters. Each is a different word:
- `camoc` k'amoq (007 kamoq 'let him die'): this is the 'take' verb, given k'am in 015 and 016 (Brasseur qam-oc).
- `bic` b'iq' ×2 (016 b'ik 'going', a doubtful reading): this is 'swallow' (Brasseur big).
- `acan` akan ×2 (published aq'an 'climb, up'): this is 'leg', as the published racan rakan (Brasseur akan / r'akan).
- `xoc` xoq' (published xok 'entered') and `oquic` oq'ik (published okik 'entering'): this is the cry word (see Changes).

Forms with several published mt (ca qa/ka, catit qatit/katit, cochoch kochoch/qochoch, he je/je', vi wi/wi', chi
chi/chik/chi', vvb wub'/uub', cam k'am/kam, quih kij/q'ij, cab, xcah, chac, cuꜭ, oc) were each checked against person and
sense. The draft's choices match the published distinctions in every case: ca, catit and cochoch go by person (narrative k-, the twins' and lords' speech q-, as 014–016); vvb after ca is wub' and lone vvb is uub' (008 point 6); chac is 'work', chak.

### Rulings on the drafter's open points

1. bico / xbic / xa bic → b'iq', xpec → xpeq, cazlic → k'aslik: confirmed. The word is certain and Brasseur's letter agrees (007/010 rule). xpeq is only the c-for-/q/ respelling.
2. oꜫ 'cry' with plain c: changed to oq' (above). 015's choc should follow if the owner confirms that reading.
3. etz / etz' 'play': changed to etz' throughout the part (above). 006's etzeyaj stays as published.
4. acan 'leg' akan: kept with the published rakan. raqan is the open question of 008 point 5.
5. ꜫuz: kept 'grieving (?)' here after Brasseur's 'seule et triste' (OCR 24692). 015's 'delight' rests on his 'plaisir' there. Both are guesses; the glossary needs a broadening, not a replacement.
6. ri xic 'the hawk': accepted. Brasseur's footnote (OCR 24800–24801) names the bird, and 009's Xic stays a name as published.
7. qui quih q'ij: kept with 016's tiquil quih (still open there).
8. ca nu taco / ca nu bico with 'you' unwritten, and Apa china 'who': accepted as inferred. Both are Brasseur's readings, and the notes say so.
9. Nested speech in single quotes in `i`: accepted, as the 017 establish entry decided.

### Refused

- U15 `Ta xbec taconel` read in `i` as narrative ("So the messenger went (?) with this word"), although the tag xuꜭhax ri vꜭ shows the speech is still being given to the louse. xbec is completive, not an imperative, so 'Go, messenger' would need another form. The note gives both readings and marks them. Kept.
- U12 `choc` 'entering' (mt chok) beside the cry word: Brasseur's 'en entrant seule et triste dans la maison' (OCR 24690–24692) confirms 'enter'. Kept as chok.
- U32 / U34 "the eye", "my eye" for vbac vvach, where the house row gives "his eyes": one eye is struck (Brasseur 'la prunelle de l'œil'). Kept.
- U43 "This, it seems, is why the toad's back sits so low": the hedge is in the note, and it follows the origin pattern of U26–U28 and U47. Kept.
- U22 Zaquicaz mt Saqikas (c → q): the note ties the name to zaqui 'white' (007 rule). Kept.
- U45 zucah mt sukaj by the letters, against Brasseur's tzukuh: this follows 011's letters rule (tzotz, sima). Kept.
- Inferred senses that are marked in the notes but not (?) in i (Cat oho "Come here", Hupa "Why"): house practice, as 014–016. Kept.
- Establishment log: every doubtful reading, every letter decided against Brasseur and both 5b corrections are in the units' notes. U2 and U59 open with the MS reading. The t-as-h, r-as-v and a/u letter forms are each noted at their word. Nothing to change.
- Brasseur: every quotation in the notes is in the OCR, allowing for OCR noise (e.g. 'Parle done', 'Xtc', 's'abaitit', 'tavale'). This includes the footnotes on Tamazul (24752–24753), ba (24755, 24799–24800), Vac / voc / Xic (24799–24801), Lotzquiq and the cataract (24842–24844, 24894–24895) and xi (24969–24970), and 'il y a ce signe de notre parole qui est resté avec vous' (25015–25016). The K'iche' readings credited to him (tiqiba, He cu y taka, nima 'hoc, togol, qu'echahic, gih, qam-oc, guz, Uq, akan-oc, ch'av'ah, Xpek, bigo/big, Zakicaz, x-og, r'ogibal, x-chakachob, Ca chau-oc, chu qaxah u chi, chayic, qaxtok, x-yicu va r'achak, r'akan, tzukuh, chuva re, ch'anic, xa u bi cumatz, pachgab, tzuum, qaztah, c'ogic, qazlic, m'yx ogic, x-ucou, mana-Ipu) were all confirmed.

### Open decisions for QUESTIONS.md

1. oꜫ 'cry' with plain c is now oq' here (5 tokens). 015's choc (chok) should become choq' if the owner confirms its reading.
2. etz' 'play' is now supplied on plain t + z here (etz'anem, etz'anik, ketz'ab'al). 006's eꜩeyah (etzeyaj) should change with them; this settles 009 point 1 for this part.
3. ꜫuz: 'grieving (?)' here, 'delight (?)' in 015. Both rest on Brasseur. Broaden the entry, or revise one.
4. For the establisher: ¶14 `Naquipa a taquiquil` has Brasseur's `Nakipa qo takikil`, and the log is silent on it. Recheck the image if 017 is revisited.
5. Glosser (gloss.json is being written in parallel): the mt changes above (xoq', oq'ib'al, choq'ik, koq'ik, oq'ik, etz'anem, etz'anik) must be matched by the entries. Pass 2 will check this.

## Pass 2

This pass read all 60 units again as a fresh read: the labels, `l` against the original, `l` against `i`, mt against the published parts (the comparison script was run again) and the Brasseur claims. It also checked every gloss entry: 83 novel keys and 30 broadenings from the Sonnet glosser, written before pass 1's mt changes. Pass 1's changes were checked and found right.

Gloss checks, by script and by reading:
- Every gloss value's modern form was compared with the units' mt for that token.
- Every key is a lowercased WORD_RE token of the text, and every novel form is covered.
- Every broadening starts with its popol-vuh-glossary.json entry, copied whole, + " · ".
- Every known token whose mt this part uses was checked against the forms its glossary entry offers.
- Each existing entry was read against this part's sense of the word.
- Every Brasseur citation in the gloss was found in the OCR. The coh citation 'l'appliquèrent à l'oeil' is at OCR 24872; the gloss itself cites no line number, so there was nothing to remove. One quotation was wrong (vtux, below).

Edits were made by script (load, change named fields, dump with ensure_ascii=False, indent=1). No t changed. After the edits, a script check confirms:
- the 60 units tile the 19 paragraphs exactly;
- each paragraph starts a unit (U1, 2, 4, 6, 8, 11, 13, 16, 21, 26, 29, 32, 36, 39, 42, 45, 48, 54, 59);
- len(mt) equals the number of WORD_RE tokens in every unit;
- gloss.json loads, with 83 novel keys and 34 broadenings;
- every modern form in the gloss now equals the units' mt;
- every broadening begins with its glossary entry + " · ".

Counts. Units: 0 major, 1 minor, 0 style. Gloss: 0 major, 15 minor, 3 style.

### Unit changes

- U44 · l/n · minor · `chu chub vchi` was glossed "its mouth spat", with chub as a verb 'spit'. The published chub is the noun 'spittle' (chub'). The clause has the same frame as chu caxꜩ vchi in U42, which is itself unclear. · l "spittle(?)". The note gives the published noun and calls the frame unclear (inferred), with Brasseur's 'qu'une sorte de bave autour de sa bouche'. i "only its mouth frothed (?)" is kept.

The fresh read found nothing else to change. The labels were checked again after pass 1's edits: ergative/absolutive, x- completive and future, ca/que ongoing, the passives xevꜭhax, xuꜭhax, xbic, xculutah and xchacatah, and the agent-focus reading of xticou. All are right. The mt comparison is unchanged from pass 1: camoc, bic, acan, xoc and oquic differ from the published mt, each because it is a different word.

### Gloss changes

- etzanem, etzanic · minor · The modern form was etzanem / etzanik, not the units' etz'anem / etz'anik (pass 1). · Both are rewritten with etz' and say that the tz' is supplied.
- oquibal, choquic, coquic · minor · The modern forms okib'al / chokik / kokik predate pass 1's oq'. · They are now oq'ib'al, choq'ik and koq'ik, with Brasseur's g and the restoration stated.
- oquic (broadening) · minor · The new reading was okik 'weeping'. The unit's mt is oq'ik. · "oq'ik — weeping, crying; … the tresillo restored; not ok 'enter'".
- xoc (broadening added) · minor · The existing entry has only xok 'entered', but U30's xoc is xoq' 'cried'. No entry covered it. · Added "xoq' — cried (out); …; not the xok 'entered'".
- chavah, chavila · minor · "the w a glide (uncertain)" and "wila, il 'see' with the w of wilo" took the 'you' prefix for something else. In wilo the w is 'I'. The w here is aw-, the 'you' prefix before a vowel (pass 1's U14 and U19 notes). · "ch- + aw- 'you' (a- before a vowel) + aj / il …".
- tio · minor · "perhaps the verb of tij 'try, taste'" invented a link. The unit and the published glossary have ti 'eat (flesh)'. · "ti 'eat (flesh)' + -o …".
- xauah · minor · "x- completive + awaj" misanalysed the form. xauah is the stem xawaj itself (xu xauah = x- + u- + xauah), the published xavah written with u. · Rewritten.
- caꜭhau · minor · "ka- + ch'aw" did not say what ka- is. The command is to one person (Brasseur 'Parle donc, toi'). · "ka- (k- with a 'you', inferred, as kat) …".
- xticou · minor · "the ending of a verb that puts the doer first": here the doer follows the verb (pass 1, U59). · "read as the agent-focus ending (as xe chakowik)", with Brasseur's x-ucou.
- vtux · minor · The entry quoted Brasseur as 'vienne à fleurir'. The OCR (25058) has 'si elle vient à fleurir'. · Corrected.
- ꜭaxtoy · minor · It cited the published form as k'axtok. The published entry ꜭaxtoꜭ is k'axtok'. · Corrected, and the entry now says it is respelled by the letters.
- malmat (broadening added) · minor · The existing entry is 'in haste, eagerly', but U13 and U16 use it of the louse 'wriggling', after Brasseur. · Added "(inferred) wriggling, waddling …".
- caꜩihon (broadening added) · minor · The existing entry is 'it talks' (ka- ongoing), but U48's Caꜩihon oc is the command 'speak now' (l "You-speak"). · Added "(inferred) you speak, speak! …".
- taco · minor · The example "xe taqo 'they sent (them)'" fixed one reading of a form that U4 leaves open (pass 1). · The entry now gives both readings and says it is unclear.
- xrictaxic · minor · The entry gave 'was swallowed', which goes beyond the unit's 'taken in', and lacked the ric alternative. · "(guess) was taken in; … perhaps the ric 'find, come upon' of rico".
- rih (broadening added) · style · The existing entry is 'its back', but U36's rih quic is the surface of the ball's rubber. · Added "rij — surface, outer part …".
- xquin · style · "(ki- + in)" was confusing beside x- + k- + in. · Removed.
- cayac · style · "son ju-pon" kept the OCR's hyphen. · "jupon".

The other novel entries were checked against their units and kept. They are true to the form, marked (inferred) or (guess) where the units mark them, and general to the form. The other 29 broadenings each add a sense not already present and copy the old entry whole: quih, camoc, bic, acan, xic, quecha, chac, rech, ah, re, chi, coh, ꜫuz, ta, china, apa, tah, chaah, tocol, yacal, ruꜭ, canoc, taca, va, cul, chapa, oc, xi, mix. Kept.

### Refusals

- coh (broadening): a citation at "OCR line 313" was queried, but gloss.json has no line number. The quotation 'l'appliquèrent à l'oeil' is in the OCR (24872). Kept.
- ve: a 'yes' broadening was considered and dropped, because the published entry already has "we — yes".
- chub: no broadening is needed. The published noun 'spittle' covers U44 now that the unit reads it as a noun.
- apa 'who' (broadening) duplicates the china broadening, since 'who' is carried by the pair. It is kept, because the reader taps apa alone.
- chi (broadening) repeats chi' 'mouth', which the old entry already has, inside its new reading. It is kept, because the new reading's main point (the conditional particle in we chi chaqi'jik, ta chi pe utux) is new.
- The (guess) / (inferred) labels in the gloss for vmucubal, vac and oho differ slightly from the units' notes. This is within house practice, and the senses agree. Not changed.

### Open decisions for QUESTIONS.md (final, pass 1 and pass 2)

1. oꜫ 'cry' with plain c is now oq' here (xoq', oq'ib'al, choq'ik, koq'ik, oq'ik). 015's choc (chok) should become choq' if the owner confirms its reading.
2. etz' 'play' is now supplied on plain t + z here (etz'anem, etz'anik, ketz'ab'al). 006's eꜩeyah (etzeyaj) should change with them, which closes 009 point 1.
3. ꜫuz: 'grieving (?)' here, after Brasseur's 'triste', and 'delight (?)' in 015, after his 'plaisir'. The entry is broadened. Decide whether one reading should go.
4. acan 'leg' akan, with the published racan rakan; raqan is still open (008 point 5).
5. qui quih q'ij, with 016's tiquil quih (still open).
6. For the establisher: in ¶14, the text has `Naquipa a taquiquil`, where Brasseur has `Nakipa qo takikil`, and the log does not mention it. The image should be rechecked.
7. Proposed house renderings from the drafter (vꜭ louse, xpec / Tamazul, cumatz / Zaquicaz, vac falcon, xic hawk, vvcubix 'in seven days', the louse's formula, loꜩ quic, ah 'cane', rax / chaquih vleu, pixabai, taconel / tacol): none were added meanwhile.
