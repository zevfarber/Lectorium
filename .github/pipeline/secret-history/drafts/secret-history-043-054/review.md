# Review, pass 1 — secret-history-043-054 (§§43–54)

Reviewer: adversarial pass 1, on `units.json` only (conventions, runbooks, `../run3/RUNBOOK.md` §2, the packet, `novel-forms.json`, `known-forms.json`, the model `secret-history-01-06.json`, the published parts §§7–23 and §§24–42 with their `review.md`, and `secret-history-glossary.json` read; no modern translation opened or recalled; Naka Michiyo not in the folder, not used). `units.json` was edited in place by script; no `t`, word count, word order, `p` flag, schema key, `titleEn` or `part` was changed. `gloss.json` does not exist yet; pass 2 will check it.

## Totals

| severity | changes |
|---|---|
| major | 1 |
| moderate | 17 |
| minor | 47 |
| trivial | 16 |
| **all** | **81** |

A spelling rule applied across many units (the `bulk` lines at the end) counts as one change.

Method notes: every `t` was re-cut from the packet by script (427 packet rows, all consumed once, in order; unit 46's `Qulan- Baγ̇atur-un` is one packet row with an internal space and stays one word); every bracketed Ming gloss in every morph was checked against the packet's Ming column by script (one real mismatch, #50, where the Han 訥 stood in a Ming bracket; the one remaining non-Ming bracket, `(no Ming gloss)` at #51, is the published parts' own marker for a word the Ming leaves blank, packet row 297); the 12 `p` flags fall on the first unit of each §; every morph lemma was compared by script with the lemma the published parts give for the same token (one difference, #6 Urjaṅqai + -dai; sünid is a different word here, see below); the spelling of names in `i` was checked against the published parts' rules (ž→j, č→ch, j→y, ṅ→ng, γ̇→', γ→q).

## What the drafter's flagged doubts came to

- **§44 (#6, #7, #8).** *Žeġüredei-ji … ger daluγ̇a … aluγ̇a* — 'with' for the Ming's 行 stays a flagged guess; no other reading is better supported (the alternative, 'in Žeġüredei's house', would need a genitive). *Teġün-ü-ġei bi že* — kept: it is the same frame as the published §18 (*teġün-ü-ġei bi-že*, 'must be his'); the note now says 'he' and 'that man' are supplied. *oboγtu bolγažu* — i lost 'of his own' (not in the form) and the note says the object ('him') may be a whole line.
- **§46 (#14–#24).** The Barula reasons: *baruγ … büleġe / Barulas oboγtan boluba* (#16–17) has no *tula*, and the links to Barula are now marked as the drafter's. *teriġüten* (#20) — 'heads' kept; the gloss no longer calls 'chief' a dictionary meaning (the Ming has 項, which is 'neck' or 'item, kind', and perhaps the 頭項 'headman'). *ügeġün* (#21): the note claimed the glossary has a -ġün; it does not — now stated as a guess. Adargin (#24): *adaluγči* stays uncertain; 'spy' is the Ming's 間謀 and i says only that.
- **§47 (#30).** *Ambaγai-tan* — the possessive reading of -tan ('Seṅgün-Bilge, having Ambaγai') had not been considered and fits §52; added to the note; i and the Ming-based reading kept.
- **§48 (#34–#37).** 'Qabul Qaγan, Simsečüle' kept as the drafter has it. *aṅqa jeke in-ü* — 'His eldest' kept, now explained as the reading of 最 大 with in-ü following the pair. The -(n)ü printed after back-vowel words (#36) is noted.
- **§50 (#43–#44).** The Belgütei aside: the grammar (*tere büleġe* closing a relative of participles; genitive on Belgütei) supports 'that was the man who split and hacked Belgütei's shoulder-blade'; the one real doubt, who is subject, stays with Büri-Bökö as the drafter says. 'Shoulder' in i now matches l's 'shoulder-blade'; 'two participles' was wrong (qaṅγas is not analysed).
- **§52 (#49–#52).** *meden aba* — 'ruled' kept (the stem of meden is unknown and said to be); the garbled Tatar remark fixed. *böġetele* 'although' reading kept: it is the published gloss, and the Ming's 旣 'since, already' does not change the force of 'although he had seven sons'.
- **§53 (#53–#68).** *ilerün* / *iležüġü* — 'send' is now supported by the published *ilebe* (Ming 敎去了); the alternative (the envoy goes) is stated in the notes; -ġer is marked as a reading because the Ming puts 敎 'cause' on it. 'Two messages' was not in the text (one quotation after two addressees); about and note corrected. *mama-γ̇ar* for *nama-γ̇ar* (Han 納馬) was already caught by the drafter and is right. *kesedkün / soridqun* — the -d- stays unexplained, as the morph glosses say.
- **§54 (#69–#74).** *qatud* — the plural form behind 'was a lady' is now stated in the note and the gloss no longer says 'of rank'; the reading is kept. *šibaγ̇ulan*, *öngeižü*, *qaγ̇lžu* — stems stay uncertain, as flagged. i gained no 'home' (#70), 'closer' (#71) or 'back' (#74).

## Changes

Format: unit · field · severity · what was wrong · what was done. Word indices (w) count from 0 within the unit; unit numbers (#) count from 0 in `units.json`.

- part · about · **minor** · 'Twelve sections of descent' is wrong for §§52–54 (rule, then narrative) · opening rewritten to say which sections are descent and which are story
- part · about · **moderate** · 'his two messages from the Kitad's custody': the text has the Tatars taking him to the Altan Qaγan, not Kitad custody, and it is one sent word (addressed to two men), not two messages · reworded to what the text says
- part · about · **minor** · 'messages' (see above) · 'message'
- #1 · n · **minor** · appeals to 'the dictionary sense', but no dictionary is among the sources · reworded to what the sources show
- #2 · n · **minor** · states the mother as fact in the same breath as saying the words do not say it; the 'Ming's to her' clause is unintelligible · made a plain hedge
- #4 · i · **moderate** · i 'had earlier been in the jügeli' turns oro- 'enter' + büleġe (pluperfect, 'had entered') into a state of membership that the words do not give · 'had earlier entered' (the force of l)
- #4 · n · **moderate** · note defended the wrong i; membership is an inference, not the grammar · note now separates what the form says from the inference
- #6 · i · **minor** · 'lived on constantly': 'on' (continuing) is not in daluγ̇a/aluγ̇a; l has 'dwelt' · 'lived constantly' (the 'with' remains the flagged guess)
- #6 · n · **minor** · note says the ending is unplaced 'as in the glossary' while the morph treated the word as unanalysed · note matches the new two-morph analysis
- #6 w5 · morph Urjaṅqadai · **moderate** · lemma 'Urjaṅqadai' as one unanalysed morph, but the published parts and glossary (urjaṅqadai = Urjaṅqai + -dai; Urjaṅqai in §7–23) have two morphs · split into Urjaṅqai + -dai, Ming bracket kept
- #7 · n · **minor** · i supplies 'He' and 'that man' without saying so · flagged in the note
- #8 · i · **moderate** · i 'with a clan of his own': 'of his own' is not in oboγtu (just 'having a clan'), and 'a Jegüreid' for a plural group name was not flagged · 'a clan-holder, a Jegüreid'
- #8 · n · **minor** · object 'him' supplied unflagged · flagged
- #8 w2 · morph Žeġüreid · **trivial** · derivation stated as fact · hedged
- #9 · n · **minor** · 'after r': Žered ends in d · 'after a consonant'
- #14 · l · **trivial** · l leaves nojan as an English name-form; i says 'lordly', Ming 官人 · 'Lord-like'
- #16 · n · **minor** · asserts the root as fact; the next note says the Ming does not link them · hedged
- #16 w3 · morph baruγ · **minor** · dictionary gloss asserts an unproven root · 'compare'
- #20 · l · **minor** · l carries a commentary clause, '(Ming: kinds)', that belongs in the note · removed (the note already has it)
- #20 · n · **minor** · doubt tested: 項 has a third possible sense not named · added as a possibility, reading unchanged
- #20 w2 · morph teriġü · **moderate** · gloss of teriġü prejudges the doubtful reading ('chief') as a dictionary meaning; the Ming has 項, not 頭 · gloss states the Ming's 項 and marks 'chief' as a reading
- #21 · i · **minor** · 'stirred porridge' makes the participle qudqulaqu a past finite verb · 'were porridge-stirrers'
- #21 · n · **moderate** · 'as in the glossary' is false: no glossary entry has a -ġün ending · note says it is a guess
- #21 w6 · morph -ġün · **minor** · unsupported precedent · said so
- #25 · n · **minor** · derivation stated as fact · hedged
- #26 · n · **minor** · derivation stated as fact · hedged
- #26 w0 · morph Uruγ̇ud · **trivial** · as above · hedged
- #26 w1 · morph Moṅγud · **trivial** · as above · hedged
- #27 · n · **trivial** · the 'suspicion' is stated as fact in its own clause · hedged
- #30 · l · **minor** · l invents 'and company' where the form is -tan (plural 'having'), as l renders -tan elsewhere · 'Ambaγai-having-ones'
- #30 w3 · morph -tan · **moderate** · gloss gives one reading of -tan as if sure · both readings named
- #30 · n · **moderate** · drafter-flagged doubt tested: the possessive reading of -tan, which fits §52, was not considered · alternative added; i kept
- #31 · i · **major** · i says 'a wife of Charaqai-Linggu, his sister-in-law': it makes the woman Charaqai-Linggu's wife (and so asserts the very thing the note says it will not say); the genitive belongs to berigen, not eme · genitive attached to 'sister-in-law'; whose wife she was left open
- #31 · n · **moderate** · note contradicted the old i and hung an inference on the nouns · note rewritten to match
- #32 · n · **trivial** · as above · hedged
- #32 w0 · morph Besüd · **trivial** · as above · hedged
- #34 · n · **minor** · 'printed with Shiratori's comma' misdescribes the punctuation · corrected
- #36 · n · **minor** · harmony mismatch (-(n)ü after Qabul-Qaγan) unmentioned · noted
- #36 w0 · morph -(n)ü · **minor** · gloss calls the form front-vowel without saying it breaks harmony · said so
- #37 · n · **minor** · 'opens a phrase' contradicts the rule just stated and leaves i's 'eldest' unexplained · clarified
- #39 · n · **minor** · 'beki is a title' rests on nothing in the sources · removed
- #41 · n · **minor** · 'from later in the work' is not a source this pass can cite · marked as outside knowledge
- #44 · i · **minor** · i 'shoulder' against l 'shoulder-blade' and the note · 'shoulder-blade'
- #44 · n · **minor** · calls qaṅγas a participle although the note says it cannot be analysed · corrected
- #47 · l · **minor** · l 'those' for tere (Ming 那箇, singular 'that one'; the plural is tede); 'lords' for singular nojan · 'lord, that'
- #47 · n · **minor** · 'Elsewhere' cites usage that is not in the sources; tere singular unremarked · marked as outside; tere explained
- #47 w3 · morph darqan · **minor** · 'exempt from dues' is not in the sources · removed
- #48 w4 · morph -ġün · **minor** · as above · said so
- #49 · n · **minor** · sentence is unintelligible ('the real Tatar and written Tatar') · rewritten
- #50 w1 · morph -(n)u · **moderate** · Ming bracket holds the Han transcription 訥, not the Ming gloss; the packet's gloss for the word is 皇帝 的 · [的]
- #52 · n · **minor** · garbled sentence ('the chain ... is the Mongol's') · rewritten
- #53 · i · **minor** · colon in i promises a list, but unit 54 is the dative of the same noun phrase (bükün describes the peoples named there) · dash
- #53 · n · **trivial** · link to the next unit unclear · clarified
- #58 w0 · morph Kitad · **minor** · 'the northern peoples under the Jin' is not in the Ming (契丹) · 'a people'
- #59 · n · **moderate** · drafter-flagged doubt (§53): the reasoning 'send from go' was circular; the published ilebe is the evidence · evidence cited, alternative kept
- #59 · n · **moderate** · 'two messages' is not in the text; one quotation follows, after the two addressees · hedged
- #59 w5 · morph -ġer · **moderate** · morph labels -ġer instrumental with the Ming bracket 敎 'cause', which fits no instrumental gloss · reading marked
- #59 w7 · morph ile- · **minor** · no cited support for 'send' · published ilebe cited
- #61 w7 · morph ile- · **minor** · no cited support for 'send' · published ilebe cited
- #63 · n · **minor** · öki is not a 'front-vowel variant' of ökin (both are front-vowel); they differ by the final n · corrected
- #65 · n · **trivial** · supplied 'I' in earlier units not flagged · flagged
- #68 w1 · morph ile- · **minor** · no cited support for 'send' · published ilebe cited
- #68 · n · **moderate** · drafter-flagged doubt (§53): the alternative subject was dismissed in one clause · both readings stated; i unchanged
- #70 · i · **moderate** · 'coming home': 'home' is not in aisuqu-ji; the destination is not given · 'coming with her'
- #71 · i · **minor** · 'peered closer': 'closer' is not in öngeižü (Ming 探著) · 'peered at them'
- #71 · n · **trivial** · evidence for the resemblance not given · Han noted
- #72 · n · **moderate** · drafter-flagged doubt (§54): the plural form behind 'was a lady' was not mentioned · named
- #72 w4 · morph qatun · **minor** · 'woman of rank' is not in the Ming · marked as reading
- #74 · i · **trivial** · 'came back': irežüġü has no 'back' (qarin belongs to the previous unit) · 'he came'
- bulk · name: Sengün → Senggün · **minor** · ṅ is ng (published Tenggis, Uriangqai): Seṅgün · #30 i, #30 w2, #52 i, #52 w0 · respelled
- bulk · name: Müngür → Münggür · **minor** · ṅ is ng: Müṅgür · #37 i, #37 w5, #42 i, #42 w0 · respelled
- bulk · name: Adanqa → Adangqa · **minor** · ṅ is ng: Adaṅqa · #6 w4, #7 n · respelled
- bulk · name: Jürki → Yürki · **minor** · Shiratori's j is y (Han 禹): Jürki; compare published Yeke-Nidün · #38 i, #38 w2, #39 i, #39 w0, #40 i · respelled
- bulk · name: Jochi → Jüchi · **minor** · remembered form: Žüči is Jüchi by the pilot's ž→j, č→ch · #45 i, #45 w3 · respelled
- bulk · name: Jüyin → Jüin · **minor** · remembered form: Žüin is Jüin · #57 i, #57 w1 · respelled
- bulk · name: Jeguredei → Jegüredei · **trivial** · ü dropped: Žeġüredei · #3 i, #3 w0, #4 n, #4 w0, #6 w1, #7 n · respelled
- bulk · name: Tödö'en → Tödögen · **trivial** · apostrophe used for a plain g (Tödögen) but not for ġ elsewhere (Jegüredei); one rule: ġ and g are g · #20 i, #20 n, #37 i, #37 w10, #48 i, #48 w1 · respelled
- bulk · name: Sijiu'udai → Siju'udai · **trivial** · stray i: Sižuγ̇udai · #27 i, #27 w4 · respelled
- bulk · name: Qadaqan → Qada'an · **minor** · published Qara-Qada'an: γ̇ is an apostrophe · #37 i, #37 w9, #48 i, #48 w0, #61 i, #61 w3 · respelled
- bulk · name: Shingqor → Shinqor · **trivial** · Šinqor has a plain n · #28 i, #28 w2, #29 i, #29 w0 · respelled
- bulk · name: (Jürkin) → (Yürki) · **trivial** · stray -n in the English form · #40 w0 · respelled

## Findings refused

- #0 `ablin` (Ming 自娶的, 'own-wedded'): analysis stays uncertain as the drafter says; no better stem found in the sources.
- #1 *tatažu* 'making a concubine': kept; it follows the Ming's 做妾着, and the sense of the sentence (the *inže*, the dowry attendant, then a son) supports it.
- #4/#8 *jügeli* left untranslated in i: the Ming's 以竿懸肉祭天 is a description, not a word, and a bare 'pole-rite' would claim more than the sources say.
- #5 'was no more' for *ügei boluγsan*: kept; it is the plain sense of 'having become without', and the note says the Ming does not say 'died'.
- #6 *Žeġüredei-ji* 'with': kept as a flagged guess (see above).
- #7 *bi* as 'is', not 'I': kept; the Ming 有 and the published *bi-že* (§18) agree.
- #16 'fierce at his food': kept as the literal rendering of the Ming's 猛; 'great eater' is in the note as the drafter's inference, not in i.
- #24 'he … they' (Adarkidai is the spy, the clan is plural): kept; the subject of *bolba* is unwritten and the Ming's 每 on *oboγtan* is plural; the note already says 'he' is the drafter's.
- #33 *Sünid* as a clan name, not 'nights': kept; the Ming's 一種(名) decides, and the morph gloss says it is not the earlier word. Pass 2 should make the glossary key `sünid` cover both uses (broaden).
- #37 'His eldest': kept (最 大 'most big').
- #41 the Jesügei remark: kept in the note, now marked as outside this part.
- #43 *tün* 'forest': kept as the Ming's 林 with the stem flagged unknown.
- #46 the space inside `Qulan- Baγ̇atur-un`: kept in `t` exactly as printed; the builder must treat it as one word (it is one packet row).
- #53 *bükün* 'those who live': kept; it is the published gloss (uncertain) and the Ming's 有的.
- #62–#67 'take warning from me', 'try to repay my enmity': rebuilt from *kese-* (戒) and *sori-* (試) with the 您 imperative ending; neither phrase is a ready-made English formula that needed replacing.
- The orthography of Monγutai → 'Mongqutai' (plain n) beside Moṅγud → 'Mongqud': left; Shiratori's n/ṅ variation is not explained by the sources and neither spelling is more right.
- The ġ in names (Jegüredei, Jegüreid, Sigiratu, Tödögen): all now spelled g; the published parts have no ġ-name to copy, so the rule is the reviewer's and stays open for the owner.

## Remaining doubts (for pass 2 and the owner)

- Who is the subject and what is the object in #8 (*bolγažu*): 'him' or the whole Žeġüreid line.
- #16–#20 and #24: whether the Barula, Budaγ̇ad and Adargin clauses are really 'reasons' as the *tula* suggests, and what *teriġüten* and *adaluγči* mean.
- #30 the sense of *Ambaγai-tan*.
- #49/#52 the stem of *meden*; #59–#68 *ilerün / iležüġü* (send or go) and the unexplained -d- of *kesedkün / soridqun*; #72 *qatud*.
- #6 Žeġüredei-ji 'with'.
- Pass 2: the glossary entries for the new forms must carry the same hedges (teriġü / teriġüten, -ġün, -tan after a name, -ġer, ile- with the published *ilebe*), and `sünid` and `ile-` need broadening checks.


# Review, pass 2 — secret-history-043-054 (§§43–54)

Reviewer: adversarial pass 2, on `units.json` (second look) and `gloss.json` (first check). Read: conventions, runbooks, `../run3/RUNBOOK.md` §2, the packet, novel/known forms, pass 1, the shared glossary, the pilot and published parts as references, and `hooks.py` / `r3lib.py` for the build's token and `__broaden__` handling. No modern translation opened or recalled. Edits by script, in place; no `t`, word order or count, `p`, schema key, `titleEn` or `part` changed. Build and publish not run; no other file touched.

## Totals

| severity | changes |
|---|---|
| major | 0 |
| moderate | 2 |
| minor | 20 |
| trivial | 6 |
| **all** | **28** |

## What was checked

- **Key coverage, by script against the build's own derivation** (`r3lib.tokens` over every `t`, and `hooks.forms`): 269 reader tokens; 194 are not in the shared glossary and all 194 have an entry in `gloss.json`; none is unused. Every `__broaden__` key except `ilebe` is a token of this part and its old entry in the shared glossary is a prefix of the new text (old entry whole + " · " + new reading).
- **How the build treats `__broaden__`** (`hooks.assemble`): `gloss.pop('__broaden__')` is then applied with `G['glossary'].update(broaden)` for any key, with no check that the key is a token of the part and no check that it extends the old entry. A broaden key outside the part's tokens would therefore be written into the shared glossary as an unused entry (the "no unused keys" rule), and would overwrite a published entry. New entries are added only if the key is not already in the glossary (`k not in G['glossary']`), so a new entry can never overwrite an old one: broadening must go under `__broaden__`.
- **Ming brackets**: the bracket of every gloss entry equals the packet's Ming gloss for that token (VS16 and spaces ignored) in at least one occurrence; every morph bracket re-checked against the word's Ming (the split into per-morph pieces is the convention).
- **Names**: the English spelling of every name entry occurs in the `i` of the units that use it (ž→j, č→ch, ṅ→ng, γ̇→', j→y as in pass 1).
- **Lemmas**: every entry's lemma compared with the morph lemmas of the word that uses it (three differences, all fine: `nojansiγ` is a hedged one-piece entry for nojan + -siγ; `qulan` and `baγ̇atur-un` are the two tokens of the one printed word `Qulan- Baγ̇atur-un`, which WORD_RE splits at the space).
- **Known entries against this part's use** (all 75 known tokens): all cover the use except those broadened or added below; `ideġen-e` ('for food' against 'at food', Ming 行 against 處) is covered by 'dative-locative' and left alone.
- Units: every grammatical label in every note and morph re-read against the form and the Ming, `l` against the words, `l` ↔ `i`, remembered English, and consistency of lemmas (bolu- in boluba, bol- in bolba/bolγažu, as the published glossary has them). Pass 1's edits hold; the only things left were over-firm statements and one wrong count.

## Changes

Format: unit or key · field · severity · what was wrong · what was done.

### units.json

- #3 · n · **minor** · 'Žeġüredei is the root of the clan name Žeġüreid' stated as fact; the entry for Žeġüreid (and #8) calls the link a guess · 'seems to be … a likeness only'
- #8 · n · **minor** · 'Žeġüreid is Žeġüredei's name with the plural -d' stated as fact, against the morph ('evidently') and the glossary ('a guess') · 'looks like … (a guess)'
- #11 · n · **minor** · 'Five of the seven names begin Qači-': Qačula begins Qaču-; all five begin Qač- · 'Qač-'
- #30 · n · **minor** · the argument is unsound: that Ambaγai is Seṅgün-Bilge's son (§52) does not 'explain the plural' of -tan; it fits the possessive reading · rewritten: it fits the possessive reading at least as well; the Ming's 每 is the only evidence for the plural
- #30 · n · **trivial** · 'Taičiγ̇ud is formed with the plural -d' stated as fact · 'seems to be formed'
- #52 · n · **minor** · 'whom §47 named as Ambaγai-tan, "and his lot"' takes one of the two readings of -tan (see #30) as settled · both readings named
- #57 · n · **trivial** · 'two labels for one people' stated as fact; it is the drafter's apposition reading · 'two labels that I take for one people'
- #59 · n · **minor** · 'the clan grew from the man' (Besütei) stated as fact; the Ming says only 姓氏(名) here and 兒名 in §47 · 'the clan name seems to come from the man'
- #74 · n · **minor** · uduridču 'with the d of the stem' contradicts the morph (and the shared entry) that say the d is unexplained · 'whose d is unexplained (the same d as in nereidčü)'

### gloss.json: new entries

- `altan` · meaning · **moderate** · entry says only 'a son's name (altan 'gold')', but the same token is the title in Altan Qaγan (#58, Ming 金 'Jin'), which the entry did not cover (the key is shared and the entry is general) · lemma altan 'gold', son's name, and the Jin emperor's title, bracket [(兒)名; 金] (both occurrences' Ming)
- `barim-siġiratu-qabiči` · meaning · **minor** · 'later Qabiči alone' pins the entry to the next line · removed
- `žeġüredei` · meaning · **minor** · 'the root of the clan name Žeġüreid' as fact, while `žeġüreid` says 'a guess' · 'perhaps the root'
- `aṅqa` · meaning · **minor** · 'aṅqa jeke in-ü read as "his eldest"' pins the entry to one line · removed (the note of #37 keeps the reading)
- `budaγ̇ad` · grammar · **minor** · 'with plural -d' asserted; the Ming has no 每, the unit morph does not analyse the word, and 'the drafter's guess' is a process word in a reader-facing file · 'the ending -d is probably the plural; … only a guess'
- `taičiγ̇ud`, `airiγ̇ud`, `biruγ̇ud`, `olqunuγ̇ud` · grammar · **minor** (4 entries) · 'with plural -d' asserted for four clan/people names that the Ming glosses 種姓(名) / 一種(名) with no 每, and whose unit morphs are unanalysed · 'the ending -d is probably the plural, which the Ming does not mark'
- `kesedkün` · meaning · **minor** · stem kese- given as dictionary form with only the ending hedged; the stem is no more certain than the -d- · 'the stem is a guess from the Ming'
- `inže`, `hüdežü`, `eġüsgežü` · wording · **trivial** (3 entries) · 'the drafter's word/sense/reading' is a process phrase; no published entry uses it · 'our word' / 'a reading from the context' / 'a reading'
- `ökini` · wording · **trivial** · 'the (i) is Shiratori's accusative' says the print has an accusative; it is a bracketed vowel read as one · reworded

### gloss.json: `__broaden__`

- `ilebe` · key · **moderate** · not a token of this part (it is the published form; this part has ilerün, iležüġü), so the build would add it to the shared glossary as an unused entry and overwrite the published entry with part-specific text about two other words · dropped. The `ile-` information is carried where it is valid: the entries `ilerün` and `iležüġü` (new, in this part's tokens) both give 'ile- — to send (as in ilebe, Ming 敎去了)' with the 'go' alternative; the published `ilebe` stays as it is.
- `nu` · added · **minor** · the shared entry says 'the n appears after a vowel-final stem', but this part prints (n)u after stems that already end in n (Menen-Tudun, Qačin, Qaγan, Onan: 8 printed forms in all), which that entry does not cover · broadened: old entry whole + ' · also printed after stems that already end in n …'
- `nü` · reading · **minor** · the broadening mentioned only the back-vowel names; Tumbinai-Sečen-(n)ü also follows an n-final stem · added
- `köġün` · reading · **minor** · 'also a collective' stated as the form's meaning; it is the drafter's reading of #11 · 'also read as a collective … the plural köġüd is the usual form'
- `sünid` · grammar · **minor** · 'with plural -d' for the clan name asserted · 'perhaps the same word with the plural -d, but not the "nights"'

(`aba`, `jan`, `jen` checked and kept as the glosser wrote them: each is old entry whole + new reading, the readings match the units, and the Ming brackets are the old entries'.)

## Findings refused

- **`-tan` after a name (`ambaγai-tan`)**: entry keeps both readings (plural / possessive) as the glosser wrote them; nothing in the sources decides.
- **`baruγ` 'fierce, mighty, brave'**: kept; 'fierce' is the Ming's 猛, and the unit note and the entry both mark the link to Barula as unproved.
- **`tatažu`, 'no other source known here for tata- with this sense'**: kept; it is a hedge, not a line-pin.
- **`qulan`, `baγ̇atur-un`**: the parenthesis about the printed space after the hyphen is specific to one line, but the two tokens exist only because of it, and the readers' split would otherwise be unexplained; kept.
- **`žeġüredei-ji` 'with is a guess'**, **`ġer` 'have the envoy go' possible**, **`ilerün` / `iležüġü` 'go' alternative**, **`qatud`**, **`teriġüten`**, **`adaluγči`**, **`qaṅγas`**, **`šibaγ̇ulan`**, **`öngeižü`**, **`qaγ̇lžu`**, **`tün-dür`**: all hedges as in pass 1 are preserved and consistent with the units; left.
- **`ġer` bracket [使臣行 敎]** is the Ming of the whole word elčin(i)-ġer, as `jan`/`jen` use the whole-word bracket; left.
- **`ideġen-e` broaden** ('for food' / 'at food'; 處 / 行): declined, see above.
- **No `l` or `i` change in pass 2.** Nothing in `l`/`i` was wrong after pass 1; the over-firm places were all in notes.

## Remaining doubts (for the owner)

- The sense of **Ambaγai-tan** (#30): plural 'and his company' (kept in i) or possessive 'Seṅgün-Bilge, having Ambaγai'; the second suits §52 as well or better.
- **Who** drives out and enrols Jegüredei and what the object is (#8); **teriġüten**, **adaluγči** and the 'reason' readings in §46; the stem of **meden**; **ilerün / iležüġü** (send or go); the **-d-** of kesedkün / soridqun / nereidčü / uduridču.
- **qatud** (#72): 'was a lady' reads a plural form as a single woman.
- The **ġ-in-names rule** (all spelled g) is still the reviewer's, not the owner's.
- The pilot-style glossary does not mark which brackets are whole-word Ming glosses and which are per-morph pieces; nothing here depends on it.
