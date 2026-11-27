# popol-vuh-018 — drafter's notes

63 units for 9 paragraphs (985 words). `cut.py` cuts packet.md's pinned paragraphs into 139 pieces (cut.json) at every
semicolon, and at . ? ! (with any closing ”) unless the next word is lower case (a speech tag stays with its speech).
`groups.py` merges consecutive pieces within a paragraph. `units_src.py` holds mt / l / i / n. `make_units.py` builds
units.json, taking `t` only from cut.json, and runs the checks. No `t` was retyped. The longest unit is U32, the greeting
list: 33 words, one speech with its tag. The roll-call of ¶3 is cut one lord at a time (U15–U23): a lord is named, the
next asks "Naquila mi xi tiouic?", and the next is bitten and cries out. Each speech stays with its tag.

Checks (make_units.py, and hooks.assemble + hooks.validate run in memory, with nothing written outside this folder):
- the units' `t` tile the 9 paragraphs of packet.md exactly;
- each paragraph starts a unit (U1, 5, 9, 25, 29, 34, 39, 49, 59), and the assembled story has 9 `p` starts;
- every `mt` has one entry per WORD_RE token;
- no unit straddles two paragraphs;
- the JSON loads.

hooks.validate's only error is glossary coverage for the 62 novel forms, which the glosser supplies. It gives no
warnings. Every French quotation in the notes was checked by script against the Brasseur OCR (lines 24990–25650). All
of them are there, allowing for OCR noise.

## (a) Decisions a reviewer should know

1. **The README 5b corrections.** The note to U32 opens "The manuscript has calata cala xic, a misprint for calata
   Quicxic, corrected here". The note to U38 opens "The manuscript has pa queꜫum maha, a misprint for pa Queꜫuma Ha,
   corrected here". The later-hand marks are in the notes to U12 (the bracket), U32 (the stroke and the blot over
   Quicrixcac), U38 (the underline) and U50 (the struck `taam … xeꜭha`).
2. **Names.**
   - The lords keep the published English: Huncame, Vucub Came, Xiquiripat, Cuchumaquic, Ahalpuh, Chamiabac,
     Chamiaholom, Patan.
   - Ahalcana (plain c) is "Ahalq'ana", mt Ajalq'ana, as 010 decided for the same spelling.
   - New lords: Quicxic, Quicre and Quicrixcac are kept as names, mt by the letters (Kikxik, Kikre, Kikrixkak). The
     notes give Brasseur's derivations (quic 'blood' + xic 'hawk' / re 'teeth' / r-ixcac 'claws'), marked inferred.
   - The Xan is kept as a name ("the Xan"). The note says that in the dictionaries xan is a mosquito (inferred).
   - Molai (birds), Puhia and Quiquia (rivers) are kept. In U3 `i` adds "the rivers of pus and of blood" after the
     names, as an apposition.
   - Queꜫuma Ha is "the Dark House" (house table, 010).
   - Aqui / Ahi, the cries of pain, are kept in K'iche' in `i`.
3. **The roll-call (¶3).**
   - The manuscript's ordinals are followed. At U13 `v cab culel` ('second') stands where the count needs the fourth
     (Brasseur u cah). `i` says "the next one seated" and the note explains.
   - The eleventh lord is not named (U21; Brasseur's note says so).
   - U24 keeps the MS tags: Quicrixcac speaks and Quicre speaks to him. Brasseur reverses the roles.
   - `xi tiouic` is read 'it has bitten you', the -ou agent-focus form beside ¶4's xe tiouic 'that bit them', with
     Brasseur. Whether the i is ix (respectful 'you, pl.') or in 'me' is open, and the note says so.
   - `culel` is taken as 'seated one', in step with cubulel (inferred).
4. **The ball dispute (¶8).** The speakers follow the manuscript's tags, against Brasseur, who gives U53's
   "Re ba chi ca coh…" and U56's "He bala xa hu chil" to the boys. The untagged "Ma bala, xa holom coh." (U57) is not
   assigned in `i`, and the note says it may be either side's. "Ꜭha chic" is rendered "Say that again (?)", a guess
   (Brasseur 'C'est dit!').
5. **mt that differs from the published mt for the same letters.** A script check found these, and they are the only
   ones:
   - `caca` (red) → kaqa. The published `caca` is k'a ka 'still'. The word is certainly 'red' (the modern kaq), so the
     c is read q and no ejective is added. 010's ꜫaꜫa stays q'aq'a by its letters.
   - `quetaam` → qetaam 'we know' (U51). The published form is ketaam 'they know'.
   - `chiquech` → chiqech 'for us' (U62). The published form is chikech 'to them'. Likewise `chique` → chiqe 'to us' in
     U48, which the published form already has.
   - `toc` → tok in `zaqui toc` 'white flint' (U60), as 010's Zaquitoc (Saqitok). The published `toc` toq is a
     different word.
   - `roo` is kept roo by the letters (U14), as 011's Roo. I first wrote ro'o and changed it back.
6. **Restorations and choices of letter in mt.**
   - `ꜩubah` 'suck' → tz'ub'aj, supplying the tz' on the plain ligature, as 016/017 did for ꜩonoh (tz'onoj).
     `ꜩonox` → tz'onox for the same reason. Both depend on the open tz' question.
   - `yicou` → yik'ow, read as the published icou ik'ow with a glide y (inferred).
   - `vvb` (no possessor written) → uub' 'his blowgun', as the glossary's uub'.
   - `catem` → qatem 'our bench'. `cachaco` → qachako 'we beat them'. `chahoc` → chajoq. This is 'play' written with
     one a, which gives the letters of the torch word, and the note says so.
   - `vacac` → waqaq, `vahxac` → wajxaq, `vvc` → wuq, `cablahuh` → kab'lajuj, and so on: the ordinals by the known
     numerals. `hulah` → julaj is by the letters.
   - `zacaric` → saqarik ('dawn'; 010 has zaquiric saqirik). `Halan` → jalan.
   - `chec` stays chek. It may be the modern ch'ek 'knee', which is not restored.
   - `mich` stays mich. It may be the modern mich' 'pluck', which is not restored.
7. **Left by the letters, not restored.** These words are uncertain: cumuc, halha (jalja', ja' as in 010), Molai,
   chacbal, tzakonisaj, hina, quichila, cautalic, culel, holoman, tacchiinel, calata/calainic, xcanai, chohim,
   ticaric, tilovic, varanel, yocouic, alaba, beco, hu, chil, xzac, ꜩininic, chaa.
8. **Doubtful readings in the establishment log, each in its unit's note.**
   - The t-as-h letter forms: tio, ti, tiic in U7, U10 and U11; xi tiouic in U13; xti in U16; xe ti in U27; v ticaric
     in U39; ca tilovic in U40.
   - catem (written like cafem) is in U36.
   - r-as-v: chi roo U14, curi U8. a/u: chua cumuc U2. The h of hix: U37.

   | Reading | Unit |
   |---|---|
   | camol qui ta | U6 |
   | cha ꜩaconizah, xa vech | U7 |
   | xꜭha curi Xan (the x) | U8 |
   | ca chi rox | U11 |
   | the bracket at Ahi xꜭha Huncame | U12 |
   | Xa hina quichila (and who speaks) | U13 |
   | tacchiinel | U30 |
   | the blot in Quicrixcac | U32 |
   | xa ꜫaꜫa hu ꜫex | U43 |
   | Hun aꜫab, chi yocouic | U45 |
   | ca catat | U48 |
   | the struck taam … xeꜭha | U50 |
   | ri que | U55 |
   | Ꜭha chic | U57 |
   | tocob | U63 |
9. **Senses taken from Brasseur, marked (?) in `i`.** These are:
   - cumuc 'steep steps';
   - halha 'rushing water';
   - camol qui ta 'to bring back what they would hear';
   - ꜩaconizah 'finish';
   - xa vech 'your share';
   - tacchiinel 'tempter';
   - yocouic 'watched over';
   - alaba 'who knows';
   - beco 'send into play';
   - hu chil;
   - xzac 'threw';
   - bate 'ring';
   - ꜩininic 'clattering';
   - chaa 'the court'.

   holoman 'head by head' is my own guess from holom.

## (b) Proposed house renderings (not added to conventions)

| K'iche' (MS) | `l` | `i` |
|---|---|---|
| Xan | Xan | the Xan (kept as a name; note: a biting creature, in the dictionaries a mosquito) |
| Quicxic, Quicre, Quicrixcac | names kept | Quicxic, Quicre, Quicrixcac (not translated; Brasseur's derivations in the note) |
| Puhia, Quiquia | names kept | Puhia, Quiquia (the river of pus, the river of blood) |
| Molai | name kept | the Molai birds (kept) |
| calata / cala | hail (ta) | Greetings, … |
| varanel | watchers | the watchers |
| ꜫaꜫa chicop | fire animal | fireflies |
| v he caquix | its-tail macaw | the tail feathers of the macaw |
| zaqui toc | white flint | the white flint (lower case; Zaquitoc as the name in 010/012) |
| xꜭhavic | it-spoke | there was no word / it did not speak |
| Aqui / Ahi | cries | kept in K'iche' in `i` |

## (c) Open questions

1. The tz' on the plain ligature: ꜩubah → tz'ub'aj and ꜩonox → tz'onox, following 016/017's ꜩonoh. Confirm, or
   decide all of them together.
2. caca 'red' → kaqa. The c is read as q where the word is certain. Against that, 010 left ꜫaꜫa as q'aq'a by its
   letters. Should 010's form be brought into line (kaqa), or should this one stay kaka by the letters?
3. xi tiouic: which 'you' is it, ix (pl.) or the asker's in 'me'? The second is grammatically possible but does not
   fit the scene.
4. The speaker of U57's untagged "Ma bala, xa holom coh.", and the sense of "Ꜭha chic".
5. Glosser broadenings are needed for:
   - tio / ti ('bite', against the published 'eat');
   - cut ('show', in xqui cut v vach);
   - cab ('second', the ordinal, against q'ab' 'hand');
   - quetaam (qetaam 'we know');
   - chiquech (chiqech 'for us');
   - xcah (xkaj 'they wanted');
   - he (je 'go', U56 and U60);
   - hu (ju 'one', guess);
   - que (qe 'ours', U54–U55);
   - coh ('put in play');
   - ꜫaꜫa ('fire', in fireflies);
   - he ('tail' of the macaw, je');
   - tacal (in qui cu tacal, of the ball).
