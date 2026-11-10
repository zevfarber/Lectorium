# Review — secret-history-281-282 (§§281–282)

## Pass 1

Reviewer pass 1 on units.json. I made the edits by script (json load/modify/dump, ensure_ascii=False, indent=1 as before) and did not touch `t`.
Units are numbered U0–U26 in order (U0 = "Ögödei Qaγan ügülerün:", U25 = first unit of §282).
Checks run after editing:
- JSON parses.
- Joining every `t` gives the packet's 222 words in order.
- Every unit's `t` word count equals its `words` count.
- `p: true` is set on U0 (§281) and U25 (§282) only.
- Every Ming character of the packet appears in the brackets of each word's morphs. The order differs only where a gloss is split across morphs, e.g. 敎 sits on the causative morph.

### Changes

- U18 · i · major · Wrong reading of the genitives. The `i` tied "the Qahan my father" to töre ("the law of the Qahan my father") and made bürin-ü "us all". The words run Qaγan ečige-jin min-u bürin-ü emüne töre kičijekü küġün-i. Both genitives go with emüne "before", just as qān ečige-jin min-u … emüne does in U16. bürin-ü is "of all", not "of us all". · `i` now reads "The man who was diligent in the right way before the Qahan my father, before all — him I harmed in secret, …".
- U18 · n · moderate · The note did not say what the genitives depend on. · Added a sentence: both genitives go with emüne, as in U16, and not with töre.
- U9 · i · moderate · The English had a finite "I was carried away," followed by U10's "and then to be overcome … — this was my fault". That broke the syntax. It also hid the structure: a verbal-noun clause ending in ilaγdaqu, with min-u buruγ̇u bolba "became my fault". · `i` now reads "Again: that, set on the great throne of the Qahan my father and bearing my many people upon me, I was carried away".
- U10 · i · moderate · Same issue as U9. · `i` now reads "and then overcome by grape wine — this was my fault."
- U9 · n · minor · `i` gives the dative-locative ečige-deġen as "of the Qahan my father", and the note did not say so. · Added a sentence saying so; the Ming 父 自的行 does not decide it.
- U3 · i · moderate · "that envoys should run swiftly" added a modal "should". qaγ̇ulqui is a plain verbal noun, "the running", as the note itself says. · `i` now reads "My second deed: the swift running of envoys along our ways."
- U3 · morph (öterlen) + n · minor · The draft had öterle- + modal converb -n. The glossary and published parts (093-099, 100-104, 131-135) use öter + adverbial -len. · Morph changed to öter [快] + -len. The note now says "öter 'quick' with the adverbial -len".
- U3, U26 · morph (žaγ̇ura) · minor · This was one morph. The glossary and nearly all published parts split it as žaγ̇ur + dative-locative -a. · Split it into žaγ̇ur [路間/間] + -a.
- U4 · morph (tabiγ̇ulba) · minor · The lemma was talbi-. The glossary key tabiγ̇ulba and published parts (140-143, 151-153, 172-176) use tabi- "a spelling of talbi-". · Lemma changed to tabi-, gloss "(a spelling of talbi-; the Han 塔勒必 writes the l)". The note's point about the Han is kept.
- U5 · morph (usu) · minor · The lemma was usu. The glossary has usun, and 279-280 pass 1 made the same fix. · Lemma changed to usun, "printed usu, without the final n".
- U6 · n · minor · The note said talbižu "keeps back-vowel -žu after the stem's final i". In fact the a of the stem decides the harmony, and i is neutral. · Reworded.
- U10 · morph (ilaγdaqu, -qu) · minor · The Ming 了 of 被勝了 was missing from the brackets. · -qu gloss: "verbal noun … (the Ming writes 了, as of a past) [了]".
- U12 · i · minor · "The second fault: giving way …, I had the girls … brought" was a dangling modifier. · `i` now reads "The second fault: that, without right, giving way to a woman's words,". In U13 the colon became a dash: "… brought — these were errors."
- U14 · morph (böġetele) · minor · The lemma was böġe-. The glossary and published parts use bü- "(böġe- before an ending)". · Lemma changed to bü-.
- U19 · n · minor · The note was over-confident. It said göreġesün-i is accusative *because* it is the object of qaramlažu. It may instead be the subject of the thought that keġen reports. · The note now gives both readings and calls the choice uncertain.
- All units · morph (buruγ̇u, 10×) · minor · The lemma was buruγ̇u. The glossary lemma is buruγu (also used at 194-194), and the house rule keeps plain γ where the glossary spells it so. · Lemma changed to buruγu. The `l`/`n` spelling of the printed word is unchanged.
- U13, U14, U16 · morph (alžiγ̇as, 3×) · minor · The draft split it as alžiγ̇a + -s. The glossary and published parts (201, 202-203) treat alžiγ̇as as one lemma. · Changed to a single morph alžiγ̇as, "(here with the Ming plural 每, 'errors') [差每]".
- U8, U11, U13, U14, U23, U24 · morph (-že) · minor · The bracket [也者] dropped the packet's U+FE00 (者︀). · Restored it to [也者︀].
- U1 · l · minor · `t` prints lower-case qaγan, but `l` had "Qaγan". · `l` now reads "qaγan".
- All fields except `t` · minor · Apostrophes were curly (’). Recent parts (275-277, 279-280) and the house spellings (Köde'ü-Aral, Cha'adai) use straight '. · Normalised to straight ' (48 occurrences, including titleEn/part/about). The curly double quotes in `i` are kept.

### Findings considered and refused

- **U1 i "Since I sat"** for the converb saγ̇užu: the temporal reading is fair, and "these are the things" is supplied and the note says so. Left.
- **U9 i drops ba "also"** (Ming 也): it adds nothing in English, and `l` keeps it. Left.
- **U9 "carried away"** for odtažu (被去着): this is a guess, and the note says so. "Carried off" is no better supported. Left.
- **U6 balaγad as one lemma** (glossary: balaγasun): the published 151-153 uses balaγad. Left.
- **U4 žamud = žam + -ud** (glossary: "-d"): -ud after a consonant is the correct analysis. Left.
- **U7 aγ̇ulba as a- + causative -γ̇ul-** with no 敎 in the Ming: it is flagged as doubtful in the morph and the note, and "in rest" is flagged as interpretation. Left.
- **"my" in "my elder and younger brothers" (U19, U21)** and **"of my deeds" (U24)**: these are not in the words, but house practice supplies "my" for kin in speech (279-280 refusals). Left.
- **U15/U16 Doqolqu without "the cherbi"**: the text gives no title here. The note says "probably" the cherbi of §§227–229, which is properly hedged. Left.
- **U25 huran "seventh"**: the Ming has 七. The note is honest that it is not doloγ̇an and that the "month-name" idea is only a possibility. Left.
- **U26 "the Seven Lone Hills" capitalised** while the note says the Ming phrase is translated: a translated toponym can take capitals, and the note admits it may be a name. Left.
- **U16 tus-u-γ̇an, U18 buruγ̇ušijaba (-šija-), U20 noduγ̇lžu, U14 dölesgekü, U2 muqudγaba**: each analysis is marked uncertain in the morph and/or the note, and each matches the Ming. Left.
- **Morph Ming brackets reordered across morphs** (e.g. 敎 on the causative): this follows the pilot's practice of splitting the gloss. No character is lost. Left.
- **U18 öisüledügse- / n(i)-jen as two words entries**: Shiratori splits the word over a line, and the packet has two tokens. Left.

### Count

critical 0 · major 1 · moderate 4 · minor 15 (20 changes)
