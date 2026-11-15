## Pass 1

### Changes
- §44 w3 g2–g3, w4 g3; §45 w0 g2; §58 w5 g4 · glyphs · major · signs that are lost but restored by the corpus ([ia-za], [ia], [wa/i], [ti]) were keyed DAMAGED. source.json gives their real keys (A210, A377, A439, A090), and the validator compares every word's keys with the source, so the build would have been refused. The pilot's FUGARE? (DAMAGED) predates source.json and is no precedent for this; 22-37 has no damage · keyed as the source gives them, tr kept as the restored value with "?" (conventions), `"damaged": true` added (hooks.assemble carries it through), and the §44/§45/§58 notes now say the signs are shown with a query and are not on the stone.
- §41 w0, w2; §44 w0, w2; §47 w0, w1 · glyphs/morph · major · the lacunae inside words were drafted as separate glyphs. hooks.src_units puts a lacuna sign that has no `unit` into unit 0, so the source has ONE glyph-unit ([DAMAGED, A041], [DAMAGED, A100], [DAMAGED, DAMAGED], [A209, DAMAGED], [A439, DAMAGED], [A112, DAMAGED]), and the draft would have failed validation · merged to the source's units, tr written "[…]-tà", "[…]-ta", "[…] x", "i […]", "wa/i […]", "za₄ […]", morph g re-indexed (0-based) to match. See "For the orchestrator" for the two words this misplaces.
- §44, §45, §47, §58 · n · minor · the damage wording was out of step with the glyphs, or overstated · §44 now says the restored signs are shown with a query; §45 "za … damaged at its start" (z[a: the sign is partly lost) changed to "partly damaged"; §47 "the first half of the thunder sign" (TONI[TRUS is a damaged sign, not a measured half) changed to "partly damaged", and the separate gap explained as the corpus's bracket token (ACLT: "damage-bracket boundary only (no word)"), not a lost word; §58 adds "shown with a query".
- §49 · n · minor · "the usnu- of §15": usnu- is in §14 (usnuHa), and §15 has no usnu- · changed to §14.
- §48 · l, i · minor · ussi mari is 'during the year' (mari, indecl., "during"). l "in the year" dropped mari, and i "a bull each year" adds a recurrence the grammar does not state · l "during the year a bull", i "a bull in the course of the year".
- §51 · l · major · ahha (ARHA) was missing from the literal line, which has to follow the Luwian word by word (the pilot renders ARHA in l: "forth", "utterly") · "Tarhunzas, fully(?) pleased", queried because its force is unclear (as the note says). i "well pleased" kept.
- §51, §55 · n, morph · minor · "genitival ending/forms": ACLT tags zassi, harnassassi, hawassi, wawassi, Kumarmassi and TiPariyassi as gen and keeps poss_adj for -ssan (§58), so "genitival" (the adjective) goes against its analysis · now "genitive".
- §55 · i, n · major · i "may it all, sheep and bull, belong to Kumarma and Tipariya" turned hawassi wawassi into an apposition to the subject, but they are genitives exactly like Kumarmassi and TiPariyassi. The note built this reading as the edition's own · i rebuilt from the grammar: "may it all become the sheep's and the bull's, Kumarma's and Tipariya's."; the note now says that all four genitives stand alike and that their sense is uncertain.
- §55 · l · style · "they may be made" read as possibility, but izziyaru is imperative · "may they be made".
- §56 · n · style · "the sheep and cattle of §55" did not fit the reworded §55 · "the sheep and bulls named in §55".
- §57 · i · minor · man 'much' was lost in the idiomatic line ("make them grow great") · "And may they make them grow very great."

### Checked and confirmed (no change)
- Glyph nl at §39 (inside á-la/i||ma-za, before ma) and §53 (before the last za of harnissanza): source.json has `lb_before` on those signs (sign level, so the packet's word-level [lb] flag does not show it). Correct. The word nl flags at §51 w8, w11, w13, §52 w3 and §54 w1 match the source.
- BOS.ANIMA / OVIS.ANIMA keyed [A105|A110, DAMAGED]: as the source gives them and as conventions require (ANIMA has no verifiable sign → ▢ with a note). The notes at §48 and §55 say that the placeholder is a gap in the repertoire, not damage to the stone.
- New vals, each against ACLT's interpreted word: POST appa (POST-na = appan), CERVUS₃ Runt (Runzas, lemma Runti(ya)-), SUPER+ra/i sar (SUPER+ra/i-li = sarli), BOS.ANIMA wawi (wawis/wawassi, and Ho. spells (BOS.ANIMA)wa/i-wa/i-sa), OVIS.ANIMA hawi (Hu. itself spells (OVIS.ANIMA)há-wa/i-sá), DEUS massani (massaninzi, massanadi), LONGUS arra (arraya, array(a/i)-), FULGUR piha (pihassa, pihass(a)-), REGIO wattani (wattaniya), BONUS Kumarma (Kumarmas(sa), Kumarmassi), VITIS TiPariya (TiPariyas(sa), TiPariyassi). In each case ACLT transcribes the word in Luwian, unlike CAPUT-tt(i)- in §32, where it leaves the logogram unread, so every val stands. Two have caveats the notes already state: TiPariya's capital P is ACLT's mark for a sound left open (§53), and FULGUR is in a word supplied entirely by the corpus (§52).
- Absent §42, §43 and §46 have the runbook's gap shape (absent, l "[This clause is not preserved.]", n, one DAMAGED "[…]" word with the "[missing clause]" morph).
- Supplied signs: <+ra/i> (§51 harnassassi) and <“FULGUR”-há-sá> (§52) are shown and noted as editorial, and the <“> of §45 is noted as dropped.
- Cross-references checked against the published parts: §2 (urannu-), §3 (TONITRUS), §8–§10 (SUPER+ra/i), §14 (usnu-, after the fix), §15 (´ stroke), §19/§23 (AEDIFICARE), §21 (-ssan parni), §22 (PONERE), §26 (FRONS), §30–§31 (isnu-), §32/§36 (a=wa), §33 (neuter plural with a singular verb), §35/§36 (ammiyanza halliyanza), §36 (sá-ta).

### Refused
- §40, §53 · i dropping "Indeed" for kwippa: the published parts do the same (§23 and §31 "And …", §35 without it). Keeping the house practice.
- §40 · i "stood behind me" for asanta 'were': this is ordinary English for support and the l keeps "were". Kept.
- §58 · i "serve … well" for man 'much': "well" is a natural English intensifier with "serve", and the l keeps "much". Kept.
- §50 · i "be made high" for sarli 'highly': an English adverb cannot stand here without awkwardness, and the l keeps "highly". Kept.
- §48 · i "crushing of the grapes": it rests on the VITIS classifier, and the note marks the sense as likely, not certain. Kept.
- §45 · i "And" without the query of l "And(?)": the clause is §38's again, and the l and the note carry the uncertainty. Kept.
- Tarhunt- (§58) beside Tarhunza- (§40, §47, §51) as a lemma: this follows the pilot (Tarhunt- for Tarhuntas §1, Tarhunza- for Tarhunzas §3). Kept.

### For the orchestrator
- hooks.src_units gives a lacuna sign that has no `unit` index the key 0. Where the lacuna ends a word that begins with an intact sign, this files the gap under the wrong glyph: §44 w2 ]i-zi-i-[...] → [A209, DAMAGED], zi, i (the gap really follows the last i), and §47 w0 wa/i-t[a...] → [A439, DAMAGED], ta (the gap really follows ta). The draft now matches the validator, so ▢ shows next to the first sign. Fixing src_units (each lacuna its own unit, in its own position) and splitting these two words back would show the stone correctly. That change is to hooks.py, and the decision is yours.
- Restored lost signs now carry real keys with "?" and `"damaged": true`. Conventions.md reads "lost signs: DAMAGED … or the corpus's restored value with '?'", which the validator cannot satisfy for keyed restorations. Consider rewording it to "restored lost signs keep the source key, tr with '?', damaged: true; unrestored lacunae are DAMAGED '[…]'". The reader does not render `damaged` yet.

## Orchestrator (between passes)
- hooks.src_units · major · a lacuna sign with no unit index was filed under unit 0, putting ▢ beside the wrong sign (§44 w2, §47 w0) and merging separate gaps into neighbouring glyphs · src_units now gives such a lacuna its own glyph in its own position; §41 w0, w2; §44 w0, w2; §47 w0, w1 split back to the stone's order (gap · tà; gap · ta; gap · x; i · zi · i · gap; wa/i · ta · gap; za₄ · gap), morph g re-indexed.
- conventions · restored lost signs keep the source key, tr with "?", `damaged: true`; unrestored gaps stay DAMAGED "[…]" (recorded in conventions.md).

## Pass 2

Edited by script (scratchpad pass2_fix.py). Every morph lemma checked for an exact key in gloss.json or a published glossary (all present, none unused); every morph g is 0-based and in range; the split lacuna glyphs at §41 w0, w2; §44 w0, w2; §47 w0, w1 have morph g on the right glyphs and notes that match.

### Changes — units.json
- §47 w5 · morph lemma · minor · `isnu(wa)-` (ACLT's form) is a second key for the verb published as `isnuwa-` (§16, §30, §31 — §30 is the same form isnuhha), so the reader's glossary would carry two entries for one verb · rekeyed to `isnuwa-`; the note's "isnu(wa)-" now "isnuwa-".
- §49 w1, §51 w3 · morph lemma · minor · `usnu(wa)-` duplicates the pilot's `usnu-` (§14 usnuHa, which the §49 note itself cites) · rekeyed to `usnu-`; notes now "usnu-" and "(the verb of §14)"; the published gloss broadened (below).
- §57 w1 · morph lemma · minor · `urannu(wa)-` duplicates the pilot's `urannuwa-` (§2, which the note cites as "§2's verb") · rekeyed to `urannuwa-`; note matched.
- §44 w0 · morph · minor · the illegible trace x (g1) was folded into the `[lost]` morph, while gloss.json has its own `x` entry, which no word used · split: `[lost]` g[0], `x` 'an illegible trace of a sign' g[1].
- §44 w2 · morph gloss · minor · "the surviving start of a word": the source's ]i-zi-i-[ has the bracket closing w1's gap just before i, so whether i begins the word is not known · "the surviving signs of a broken word the corpus leaves uninterpreted" (gloss.json `i-zi-i-` matched).
- §45 w0 g1 · damaged · style · the lost pa/ha the corpus restores lacked `"damaged": true`, which every other restored lost sign in the part carries (conventions 2026-11-15) · added.
- §47 · n · style · source z[a₄-...]: za₄ is itself partly damaged; the note said only "begins with za₄" · "begins with za₄, itself partly damaged, and breaks off".

### Changes — gloss.json (new entries)
- `isnu(wa)-`, `usnu(wa)-`, `urannu(wa)-` · removed · minor · no longer used (rekeys above).
- `za-` · minor · "genitival zassi": ACLT tags zassi gen (pass 1's §51 decision) · "genitive zassi".
- `-ssi` · minor · "genitival (possessive) adjective ending … (nominative/accusative stem -assa-, here -assi)": goes against ACLT's gen for all six -ssi forms and is pinned to one form · "genitive ending — 'of …'".
- `-s(sa)` · minor · "genitive singular" (ACLT gives no number) and "the -sa part is often left unwritten" (a claim no source here makes) · "genitive ending — 'of …' (the corpus's -s(sa) leaves the ending's full form open)".
- `izzista-` · minor · "honour, to honour (verb; the infinitive honours)" garbled and pinned to §48 · "honour (verb)".
- `-is` · minor · "a variant spelling of -s" misdescribes tanimis (an a/i-stem with i before -s) · "-s, with the i that stems in -a/i- take in this case".
- `kwaruna-` · minor · "harvest of a cutting" is not the corpus's gloss, and L486 is a classifier in §48, not the writing of the word · "cutting (noun, classified by the sign L486; meaning approximate)".
- `-(ra)ru` · minor · "the ra is optional in the spelling" is not in the source (the corpus reads a longer form; Ho. has izziyaru) · "(a longer spelling than -ru, with ra before it; the corpus's reading)".
- `parnawa-` · minor · "written with the CRUX sign, as part of the house sign": Hu. has CRUX as a classifier alone (DOMUS.CRUX is Ho.'s spelling) · "serve (verb; classified by the CRUX sign)".
- `Runti(ya)-` · style · "the stag-god" is a characterisation the corpus does not give; "(Runzas)" pinned · "a god (divine name; written with the stag sign CERVUS₃; sounded Runzas in the nominative)".
- `Azzattiwadaya-` · style · "written with" LITUUS and URBS, both classifiers · "classified by …".
- `Kumarma-`, `TiPariya-` · style · "written with the DEUS and …": DEUS is the classifier · "classified by DEUS and written with …"; Kumarma adds that its sound rests on the corpus's reading, TiPariya the capital-P note (as saPisad(a)-).
- `haw(i)-` · style · §48 has OVIS.ANIMA as classifier too · "written with, or classified by".
- `hadara-` · style · "glossed alike with saPisad(a)-" unclear · "the corpus glosses it 'health', as it does saPisad(a)-".
- `-mmi-`, `-sa` · style · pinned wording ("pleased, blessed", "in these nouns") · made general.

### Changes — gloss.json `__broaden__`
- `hassa-` · minor · the broadening named "ACLT", tied the verb to one form ("3rd plural imperative hassantu"), added "beget" (not the corpus's gloss) and left the licking-mouth classifier reading as if it applied to the verb (§56 spells ha-sá-tu) · "two words spelled alike: a noun, satiety(?), luxury(?) — classified by the licking-mouth sign, the nuance a scholarly guess; and a verb, give birth (to)". Key kept (see Refused).
- `=ada` · style · two glosses joined with "·" · "they, them (clitic pronoun, 3rd person plural, nominative or accusative; leans on an earlier word)". Right on the facts: ACLT has ada nom at §55, acc at §41.
- `usnu-` (pilot, added) · minor · the published "exalt, make prosper" lacks the corpus's 'bless, please', the sense of §49 and §51 · "exalt, make prosper; bless, please".
- `-ari` (pilot, added) · minor · this part's glossary would show "ablative ending — 'out of' (the ending is a modern restoration; the stone is worn)", pinned to §13 and wrong for §49's instrumental saPisarari · "ablative-instrumental ending — 'out of, because of; with, by' (-adi with its d sounded r)", in step with 22-37's `-di`.
- `-za` (pilot, added) · minor · "accusative ending (agreeing with 'plain')" pinned to §5; §39 alamanza is a neuter accusative · "accusative ending (on neuter nouns, the nominative/accusative singular)".
- `[missing clause]` (pilot, added) · minor · this part's glossary would read "clause §17 is not preserved in this copy" for §42, §43 and §46 · "a clause not preserved in either copy of the inscription as the corpus gives them".
- `-tti`, `-ni` (pilot, added) · style · "'upon'", "'to/under the house'" pinned · "'to, for, upon'", "'to, for, in'".
- `kwi-` (22-37, added) · style · "written with the REL sign": §54 kwaya is spelled kwa/i-ia · "written with the REL sign or spelled kwa/i-".
- `sannawi-` (pilot, added) · style · "classified by the BONUS sign": §51 sannawisa is spelled without it · "often classified by the BONUS sign".

### Checked and confirmed (no change)
- All other new entries against ACLT's lemmas, glosses and grammar: `=du`, `alaman-`, `appan`, `[lost]`, `ta`, `x`, `=pa or =ha`, `=an`, `ta-`, `habad(i)-`, `uss(i)-`, `mari`, `waw(i)-`, `harr(a/i)-`, `-ttu`, `saPisad(a)-`, `sarli`, `=as`, `piya-`, `-ntu`, `massan(i)-`, `array(a/i)-`, `miyant(i)-`, `tammihi(d)-`, `pihass(a)-`, `-a` (pihassa: plural accusative with -a, so neuter), `-ru`, `wattani-`, `man`, `=anza`.
- l against the Luwian word by word and l ↔ i for every unit; no i reads as a remembered published rendering. Glyph roles, tr and val match the source and the published vals (CASTRUM harnissa, AEDIFICARE tama, PONERE tuwa, TONITRUS Tarhu, SUPER+ra/i sran (§52) and sar (§50), MAGNUS+ra/i ura, REX hantawatti, FRONS hanti, DOMUS parna, ARHA ahha). The notes' grammar labels match the forms after pass 1.

### Refused
- `hassa-` as two keys: ACLT gives both the noun (§36 hassas, 'luxury') and the verb (§56 hassantu, 'to give birth') the same lemma string `hassa-`, separated only by part of speech. The house handles homonyms with one key and a "two … spelled alike" gloss (`-i`, `-nza`, `-ya`), and a split key ("hassa- (verb)" or similar) would invent a lemma form. Broadened instead; see "For the orchestrator".
- §50 w2: `izzi(ya)-` and `-(ra)ru` both claim g2 (the ligature ia+ra/i carries the stem's ya and the ending's ra). This is a ligature that spans the boundary; the indices are in range. Kept.
- §49 w3: `-ari` takes lá/í, which also carries the stem's r. Syllabic signs cross morph boundaries, and the gloss and note explain it. Kept.
- `=wa` 'quotative particle' (ACLT 'demarcational'), and the keys `tanim(a)-`, `ami(ya)-`, `Tarhunza-`/`Tarhunt-`, `kwi-` against ACLT's tanim(a/i)-, ammi(/a)-, Tarhunt-, kw(a/i)-: these are published keys and house glosses. Kept.
- §56, §57 l "And …" with no connective (man=wa…): the pilot does the same with a clause-initial =wa (§3, §4). Kept.
- §52 i "a radiance" for the plural pihassa: English mass noun; l keeps "auras". Kept.
- OMNIS.MI (here) against OMNIS+MI (pilot §6, §15) in tr: each follows its own source transliteration (Hu. writes OMNIS.{MI} here). Kept.

### For the orchestrator
- `hassa-`: keep one key with the two-word gloss (done), or split the key if the house wants homonyms kept apart. If you split it, the published 22-37/pilot `hassa-` stays as the noun.
- The new broadenings of published entries (`usnu-`, `-ari`, `-za`, `[missing clause]`, `-tti`, `-ni`, `kwi-`, `sannawi-`) change only this part's glossary, but merged_inline_glossary lets later parts inherit them. The pilot's own `[missing clause]` entry still says "§17 … in this copy", in step with its old §17 note; consider rewording it to match the corrected note.
