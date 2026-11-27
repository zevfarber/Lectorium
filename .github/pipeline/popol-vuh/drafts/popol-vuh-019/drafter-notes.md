# popol-vuh-019: drafter's notes

There are 50 units for 10 paragraphs (705 words). `cut.py` and `make_units.py` are copied unchanged from 018. `cut.py`
cuts the pinned paragraphs of packet.md into 73 pieces (cut.json). It cuts at every semicolon, and at . ? ! (with any
closing ”) unless the next word is lower case, so a speech tag stays with its speech. `groups.py` merges consecutive
pieces within a paragraph. `units_src.py` holds mt / l / i / n. `make_units.py` builds units.json, taking `t` only from
cut.json, and runs the checks. No `t` was retyped.

The longest unit is U22, the ants' summons (34 words, one speech with its narrative lead). The lords' charge to the
guardians (¶5) is split at its question into U25 and U26. U25 holds the lead-in and the first half; the reply
"Vꜩ bala," xeꜭha cut is U27. This is the only speech split across units. I split it because it would otherwise run to
46 words. The reviewer may join U25 and U26 if a speech must never be split.

## Checks run
- make_units.py: the units tile the 10 paragraphs exactly. Each paragraph starts a unit (U1, 6, 12, 17, 24, 28, 34,
  37, 43, 48). No unit straddles two paragraphs. Every mt has one entry per WORD_RE token. The JSON loads.
- hooks.assemble + hooks.validate, run in memory with nothing written. The only error is glossary coverage for the 50
  novel forms, which is the glosser's job. There are no warnings.
- Every mt was compared by script with the mt of the same form in published 001–018. Only two differ: `cana` q'ana
  (U10, 'yellow'; the published kana is 'left behind') and `ꜭux` k'ux (U34, the verb 'gnaw (?)'; the published k'u'x is
  'heart'). Each is a different word.
- Every French quotation in the notes was checked by script against the Brasseur OCR. Ten were not found as exact
  strings. Each was then found by hand, broken only by OCR noise: accents (méme), a hyphen at a line break, or the two
  footnote columns interleaved.

## Doubtful decisions
1. **`“He na qui cut,” xa xeꜭha ꜭaholab.` (U7).** I followed the house tag rule, so the words are the boys'. He is read
   'go' (as 018's He bala 'go on, then'). `i`: "“Go on, then (?),” was all the boys said." Brasseur's reading (one speech
   of Xibalba from He na qui cut to cah ꜩel coꜩih) is quoted in the note.
2. **acab / aꜫab.** I printed plain c as established (acab, acaba, acabil, chacab), with mt aq'ab' etc. as in 015 and
   016. The U15 note says that 018 printed aꜫab and that a house decision is wanted.
3. **cha in ¶1 and ¶3.** `chi cha` (U1) is read 'at the ball court', taking cha as chaa written short. `Ta xcah cut qui
   cha … ꜩaꜩ pu qui cha ri ꜭaholab` (U12) is read as the game ('their game began … the boys played hard (?)'), on the
   parallel of xcah cu chaah. Brasseur reads 'lances' here. In ¶4 cha is the blade (Chaim Ha, rumal cha, chire cha).
   This is a guess, and it is marked.
4. **chacon / chacom / chaco.** All three are taken from chac 'win, defeat', with chacon as the stake won, which the
   lords claim (qui chacon ahauab, ca chacon). In U6 (`xqui choi qui chacon`) Brasseur's 'leurs défaites' is followed in
   `i`, "counted up the defeats (?)", and the note gives both readings. choi 'count' is a guess.
5. **The four flowers (U10).** huticab 'a bunch' (Brasseur 'un bouquet'). The flower names are kept, with the colours
   translated: red muchih, white muchit, yellow muchit, carinimac. `cana` has q'ana in mt, because the colour word is
   certain here (Brasseur gana). I restored it on the same reasoning as acab → aq'ab'. Please confirm. carinimac stays
   karinimak by the letters (not divided).
6. **The 'say/want' line (U8).** `Xa ca cha ca cah cah ꜩel coꜩih`: the division is doubtful. ca cah is read 'we want'
   (mt ka qaj; qaj 'we want' as the glossary), and `i` is "All we want (?) is four bowls of flowers".
7. **acaba (U16).** Brasseur has 'Cette nuit'. The game in fact resumes after dawn (¶10), so the note says the word may
   be 'early, at daybreak' (in modern K'iche' aq'ab' is also used of the early morning). `i` keeps "at night (?)".
8. **catacox (U18).** mt q'atakox: ꜫat 'cut' as 011's xcat, on Brasseur's g and the sense (inferred).
9. **elecaxic / elecai.** mt eleq'axik / eleq'ai: 'steal', on Brasseur's g and the sense. The -ai ending is kept as in
   published xkanai and pixab'ai.
10. **Chai zanic (U22).** mt Chay: chai 'obsidian', after Brasseur's note and his 'Fourmis tranchantes', with -ai → ay
    as published nai → nay. Chequen mt Cheken. Both are kept as names in `i` ("Chai ants, Chequen ants").
11. **oh i cama (U22).** Read 'take (them) for us (?)', with oh 'we'. Brasseur has 'allez chercher'.
12. **¶6–7, the ants and the birds.** chacala 'perched (?)', bolovic 'swarming (?)', tucuvic 'cutting (?)', `e rai
    coꜩih` (not understood, left "(?)"), zicou 'gather (?)' (Brasseur: the flowers' scent), and re 'teeth (?)' (Brasseur
    'les dents'). `ca ꜭux qui he, ca ꜭux qui xic` is read 'gnawing their tails, gnawing their wings' after Brasseur's
    'scier'. mt k'ux is by the letters. All of these are marked guesses or inferred.
13. **U32 `chahal ticon v ticon Huncame`.** The second v ticon is not in Brasseur, and the establishment log is silent.
    It is kept as established, and the note asks for the image to be rechecked.
14. **Qui tique laon (U39).** Not understood. I read 'full and heaped up (?)', linking tique to ¶7's tiquitoh 'full'.
    Brasseur passes over the words. cu caam 'he took' has kaam by the letters (014's ruling).
15. **xqueleh (U49, U50).** 'they left off (?)', after Brasseur 'ayant achevé de jouer'. mt xkelej by the letters. The
    final `xeꜭha Xibalba` is left as narrative ('so Xibalba said'), as established.
16. **chi → chik** where chi stands for chic: Cate chi cut ×2, xe oc chi, e ꜭo chi, acaba chi cut, tiquitoh chi cut,
    and chi cu ×2 in U49. chi is kept where it is a particle before a verb, in Libah chi, and in U21's unclear chi vi.
17. **ca vilo (U43).** Read 'we see it', with mt qa wilo. The v is taken as a glide before the vowel (inferred).
18. **xhix / herebac / tohbal / chahin (U45, U47).** Read 'were split / split / punishment / guarding' after Brasseur,
    all inferred. mt follows the letters (xjix, jereb'ak, tojb'al, chajin).
19. The tz' on the plain ligature is supplied in coꜩih → kotz'i'j and coꜩihal → kotz'i'jal. The word is certain, and
    this follows 015–018's open practice. The glottal stop is supplied too.
20. at ahau 'lord' (U44), as 011's Xca quizo, at ahau.

## Proposed house renderings (not added to conventions.md)
- Chaim Ha: 'the House of Blades (?)' (as 011); "(?)" only at its first mention in a part.
- zanic: 'the ants'. Chai zanic, Chequen zanic: 'Chai ants, Chequen ants' (names kept).
- coꜩih: 'flower(s)', mt kotz'i'j. cah ꜩel coꜩih: 'four bowls of flowers'.
- chahal: 'guardian', chahalib 'guardians'. chahal ticon: 'the guardians of the garden'. ticon: 'garden' (planting).
- Puhuyu (the birds' name and the second call), Xpurpuvec (the first call), Purpuec (the bird): kept as written.
- muchih / muchit / carinimac: kept as the flowers' names, with the colours translated.
- chacon / chacom: 'what (we) have won', the stake.
