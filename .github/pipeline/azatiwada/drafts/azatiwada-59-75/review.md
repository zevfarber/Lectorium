## Pass 1

Reviewer pass 1, 2026-11-16. Edits were made by script (scratchpad review1.py plus one follow-up fix to the §75 note wording), using json.dump with ensure_ascii=False and indent=1. The file is still written without a trailing newline, as the drafter left it. No sign key, role, tr or nl was changed. I read the scratchpad dry.py first: it only reads files (assemble returns no writes) and does not build. Dry run: 0 errors, and 3 warnings, all expected. The warnings are CAPUT without a val at §60, §61 and §73, which is deliberate and follows 22-37 §34.

Checked by script against source/source.json and found correct: every glyph's keys, tr and order (ligatures are one glyph); every role against ACLT's role_hint (comp only where the source has phon); morph g coverage (0-based, every non-det glyph exactly once, no overlaps); and register breaks. The source has line_break_after_clause for §59, §65, §71 and §72a, which gives word nl on the first word of §60, §66, §72a and §72b. This is the same treatment as 22-37 §31. The source's lb_before gives §63 w2, §64 w1 and §73 w1. No sign-level breaks fall in this part. The dets follow ACLT's parentheses: OCULUS (§74), CRUS (§74), COR (▢, §65, §71), L69, MANUS and MALUS₂.

### Changes

- §73, §75 · l, i, n, morph glosses · minor · The Sun-god was called "Tiwadas" in English. That form is not on the stone. §73 writes SOL-za-sá = Tiwazas (the nominative), and §75's "Tiwadas(sa)" is the corpus's transcription of a genitive. House practice names gods by the sounded nominative (Tarhunzas, Runzas, and Armas here). · Changed to "Tiwazas" in l and i of §73 and §75 and in the Tiwad- and tippas- morph glosses. The §73 note now says Tiwazas is Tiwad- with d sounded z before -s, "as Tarhunt- gives Tarhunzas". The §75 note marks Tiwadas(sa) as the corpus's transcription.
- §73 w6 · SOL val · minor · val "Tiwad" before phonetic za-sá makes the sounds view read Tiwad-za-sá, not ACLT's Tiwazas. The house rule (22-37 pass 1) is ACLT's word minus its spelled-out signs, and TONITRUS = Tarhu before hu/za follows it. · val set to "Tiwa". §75 SOL-ha keeps "Tiwad", because there the genitive ending is unwritten and the stem is the safe value. Both are word-specific vals, like INFRA an/zanta. The pilot's "tiwada" (§1, before mi) is the same stem.
- §73 w3, w5 · morph lemma · minor · "tippasassi-" was an invented lemma key. ACLT's lemma is tippas- (N, poss_adj). The house keeps ACLT lemma forms where no published key exists (Runti(ya)-, array(a/i)-). · Lemma set to tippas-. The gloss now reads "sky, heaven — here its possessive adjective tippasassis 'of heaven' (CAELUM alone) — nominative singular, with …". The val stays "tippasassis", because the one glyph writes the whole word, as ARHA = ahha does.
- §73 w7 · morph lemma · style · "Iya-" was not ACLT's form, which is I(ya)-. No published key exists. · Set to I(ya)-, in line with i(ya)Ti- in the same part.
- §71 w1, §72b w1 · morph lemma · minor · "-adi" made a third glossary key for the instrumental. The published parts file the same ending under "-di" (38-58 massanadi, hadaradi; 22-37 kwadi) and "-ari". · Both rekeyed to "-di". The glosses are unchanged.
- §75 · n, w2 morph gloss · minor · The uncertainty of kwari was understated ("reads best as 'when'"). ACLT glosses kwari as "if" only, so 'when, as long as' is this edition's reading. · The note now says that 'if' gives an odd sense here, and that the reading 'when', shading into 'as long as', is an interpretation and not the corpus's gloss. The morph gloss now reads "if (so the corpus) — here read 'when, as long as'". The sentence was also re-punctuated (the parenthesis around the tai clause).
- §74 · l, n · style · The literal line rendered ahha as a plain "away", although the corpus flags it ?! (uncertain, sic) and the note calls its force unclear. 38-58 §51 queried an unclear ahha in l ("fully(?)"). · l is now "Afterwards away(?) may stay, …". The note adds "the literal line queries it, and the English leaves it out".
- §59 · n · minor · The note said "its penalty (§73–§75)". §74–§75 are not a penalty: they are the wish that Azatiwada's name endure. · The note now reads "then the curse (§73) and the wish that the name endure (§74–§75)".
- §73 · n · style · "the change of verb" was vague. What marks the apodosis is the imperative mood (iyaTintu). · Changed to "the change of mood, to the imperative".
- §71 · n · style · "(so the corpus; it pairs with niba)" claimed a relation the packet does not state. ACLT only glosses both words "or". · Changed to "(so the corpus glosses it, as it does niba)".

### Considered and refused

- New vals kept. All of them are ACLT's word minus its spelled signs, and ACLT transcribes each word in Luwian, so they are not like CAPUT-tt(i)-. The vals are MALUS = attuwal (la/i as comp, the same pattern as REX hantawatta + ta), CAELUM = tippasassis (the whole word in one glyph), LUNA+MI = Arma (Armas(sa), sa spelled), CRUS = ta (tai, i spelled), REX = hantawatta for the verb and the abstract noun (word-specific, as REX hantawatti for 'king'), and PORTA = hilana (la, na comp, as DEUS massani + ní). I found none to be insecure on the packet's facts.
- Roles kept. OCULUS (§74) and CRUS (§74) are dets, because ACLT has them in parentheses, and the §74 note already contrasts OCULUS with LITUUS. COR is a det shown as ▢ DAMAGED with tr "", as conventions require for a sign with no verifiable key. The §65 and §71 notes say it is a gap in the repertoire, not damage, in the same wording as 38-58 for ANIMA.
- §66, §71, §72b "walls up" for anta tama-: kept. §66 states that this is a reading, not a certainty, and §71 and §72b refer back to §66.
- §72a/§72b sharing ln 72: kept. The §72a note says the corpus divides the clause into 72a and 72b and that both carry 72. The validator expects [..., 72, 72, ...].
- §63 note: "The case means 'with, by'; 'from' is how it reads with 'erase'." The house -ari entry is "ablative-instrumental … 'out of …; with, by'", so 'from' is within the case's range. The note is cautious but not wrong, so I kept it.
- §72a note "attuwal- 'bad'": kept. MALUS is the 'bad' sign, and the pilot's attuwari- (§20, under MALUS) is glossed "evil, bad".
- Supplying "and" in i (§62, §74) and in l (§64, wa only): kept, in line with the refusal for 38-58 §56/§57 (the pilot does the same with a clause-initial =wa).
- §64/§70 i "my own name" for ammanza + ethic dative =mu: kept. l carries "for myself", and the note explains it.
- §73 i begins with lowercase "then" in a p unit: kept. The sentence runs on from §72b's dash, and the condition and the curse are one sentence.
- I flag no i as remembered phrasing. "of heaven" comes from the -assi- possessive adjective, "for all times" from the plural arinzi, and "as long as" is now marked as interpretation. Each rests on the grammar given in its note.
- Editorial marks: {ARHA}, {MI} braces, <”> (dropped, noted §65 and §74), z<a> (§70, noted), ^! (§72b, noted as sic, regular form shown) and ?! (§74, noted). All are handled as in the earlier parts.
- Grammar labels in notes and morph glosses checked against ACLT for every word: tenses, persons, numbers, moods (imperatives §73 3 pl, §74 3 sg), cases (instrumentals §63, §71, §72; datives §65; genitives §63, §74, §75; nominative alamanza §61, §74, §75; accusative §63, §64, §70; neuter plural §66, §67, §69, §72b) and pronouns (=as nom, =du/=mu dat). No mismatch found.

### For the glosser / orchestrator

- Homonym collisions with published glossary keys. The morph glosses on the words are right, but the part glossary would show the published sense unless gloss.json broadens these entries ("two endings spelled alike", as already done for -i, -ya and -nza):
  - `-ha`: published as 1 sg past. Here it is the indefinite suffix of kwis-ha (§59).
  - `-wi`: published as "dative ending — 'upon horse'" (pilot §8). Here it is 1 sg present (§63, §64, §69, §70).
  - `-tti`: published as dative-locative. In §59 it is 3 sg present (§65 zatti is the dative, which is correct).
  - `-ri`: published as instrumental. In §66, §71 and §72b it is 3 sg present, tamari.
- New keys needing entries: kwari, niba, ni, hantawatta-, hantawattahi(d)-, CAPUT-tti(ya/i)-, assazza-, i(ya)Ti-, hilan(a)-, alunnazza-, alunnamm(a)-, attuwalastr(i)-, haniyattastr(a/i)-, warall(a/i)-, tub(a)i-, zadi, tazza-, ar(i)-, tippas-, Tiwad-, I(ya)-, Arma-, -in, -ra. The Tiwad- entry should name the god Tiwazas, in line with this pass.


## Pass 2

Reviewer pass 2, 2026-11-16. Edits were made by script (scratchpad pass2_5975.py), using json.dump with ensure_ascii=False and indent=1. Both files are still written without a trailing newline. I checked by script that every morph lemma in units.json has a key in gloss.json or in a published glossary (67 keys, none missing, no gloss.json key unused, and no new key duplicating a published one). I also checked that every `__broaden__` value begins with the merged published entry, copied exactly and whole, followed by " · " (asserted in the script, and all 9 pass). An assemble with gloss.json writes nothing and leaves no lemma uncovered. Dry run (dry.py, which writes nothing; writes = []): 0 errors, and the same 3 expected warnings (CAPUT without a val at §60, §61, §73).

### Changes — units.json
- §59 w1 · morph gloss (kwari) · minor · "if, when" gave 'when' as if it were a gloss. ACLT glosses kwari as 'if' only, §59 is a plain condition, and pass 1 had already marked 'when' as interpretation at §75 · "if (one ligature, kwa/i+ra/i)".
- §75 · n · minor · "kwari is the 'if, when' of §59" went against the same note's statement that the corpus's gloss is 'if' only · "kwari is the 'if' of §59".

### Changes — gloss.json (new entries)
- `-in` · major · "on hilan(a)-, in the word hilanari zin" put the ending on the wrong word. It is the pronoun's ending (zin = za-, ACLT PRO ins); hilanari has -ari · "instrumental ending of a pronoun — 'with, by; from' (za- 'this': zin)".
- `kwari` · minor · "if, when" presented 'when' as the word's meaning, which ACLT does not give. The entry also called kwari a "conjunction/particle" and listed the spellings of single lines · "if (conjunction; the corpus's gloss — where 'if' reads oddly, 'when' is a possible reading)".
- `ni` · minor · "a shorter spelling of niba" claims a relation the packet does not state (pass 1 removed the same claim from the §71 note) · "or (conjunction)".
- `niba` · style · "the i of the spelling may spell out the vowel" was pinned to one spelling (§72b ní-i-pa) · "or (conjunction)".
- `hilan(a)-` · minor · "gate(s)" was number-pinned, and the entry left out ACLT's second gloss, 'palace' · "gate, gateway (noun; written with the gate sign PORTA) — the corpus also glosses it 'palace'".
- `-ra` · minor · "'…ed'" had no subject, unlike the published -ta. "written with the l-sign lá/í" pinned the entry to one spelling · "3rd person singular past ending, active — '(he, she, it) …-ed' (-ta with its t sounded r)".
- `hantawatta-` · style · "with ta for the stem" was pinned to one spelling · "(verb; written with the king sign REX)".
- `CAPUT-tti(ya/i)-` · style · "(the head sign; …)" was garbled · "…, written with the head sign CAPUT; the corpus leaves the Luwian word open".
- `Tiwad-`, `I(ya)-`, `Arma-` · style · These did not follow the published shape for divine names ("Kumarma — a god (divine name; classified by DEUS and written with …)"). Arma- also carried a line-level note on editorial braces ("its MI set in braces by the corpus") · "Tiwazas — the Sun-god (…classified by DEUS and written with the sun sign SOL; the d sounded z before the nominative -s)", "Iyas — a god (…classified by DEUS; the corpus identifies him with Ea)", "Armas — the Moon-god (…classified by DEUS and written with the moon sign LUNA)".
- `alunnazza-` · style · "shown as ▢" matched to the morph gloss and the house wording ("shown ▢").

### Changes — gloss.json `__broaden__`
- `-sa` · minor · Removed. The broadening called hantawattahisa "the accusative singular ending of a noun in -d-", which loses the gender: aba agrees with it as a neuter accusative, and ACLT, the morph gloss and the §73 note all have it neuter. The published "neuter nominative/accusative singular ending" already covers the form. The broadening also cited a non-key form "hantawattahid-".
- `-ha` · minor · "whoever" is not ACLT's gloss ('some-/any(one)'). "two endings spelled alike:" introduced only one ending · "· also the generalizing suffix of an indefinite pronoun — 'any-, some-' (kwis-ha 'anyone, someone')".
- `-tti`, `-ri` · style · "two endings spelled alike: …; and on nouns … the dative-locative / the instrumental" repeated the published entry. They also pinned single forms (hantawattatti, tamari) · "· also, on verbs, the 3rd person singular present ending, active — '(he, she, it) …s'" (for -ri, with "(-di with its d sounded r)").
- `-wi` · style · The broadening began "two endings spelled alike:" but then gave only one ending, and it listed this part's forms · "· also, on verbs, the 1st person singular present ending, active — 'I …'".
- `ahha` · style · "also 'back' (ARHA), with a verb of deleting or erasing, 'delete away, erase'" ran two readings together · "· also 'back' (the corpus glosses it 'away, back'); with a verb of deleting, 'erase'".
- `CAPUT-tt(i)-` (pilot, added) · minor · The published "man, person" does not cover the '(noble)man' that ACLT glosses and that the i of §60, §61 and §73 uses ("nobleman") · broadened "· also '(noble)man' (so the corpus glosses it), a man of rank".
- `anta` (pilot, added) · style · The published "in, inside" lacks the 'into' of ACLT's "in(to)", which is the preverb sense with tub(a)i- and tama- here · broadened "· also 'into', with a verb (as a preverb)".

### Checked and confirmed (no change)
- New entries against ACLT's lemma, word class and gloss: `assazza-`, `i(ya)Ti-` (the capital-T wording follows the published makkissa-, saPisad(a)- and TiPariya-), `alunnamm(a)-`, `attuwalastr(i)-`, `haniyattastr(a/i)-`, `warall(a/i)-`, `tub(a)i-`, `zadi` (wording as the published zila), `tazza-`, `ar(i)-`, `tippas-` (ACLT poss_adj), `hantawattahi(d)-` (in step with the published tammihi(d)-), `kwi-` (broadening).
- Published entries used here, read against this part's forms. These cover the use as published: `=pa`, `=wa`, `-s`, `=as`, `-nza`, `=ha`, `=du`, `=tta`, `alaman-`, `-za` (covers the nominative), `-i`, `Azzattiwada-`, `-s(sa)`, `-ari`, `-di`, `=mu`, `ami(ya)-`, `harnissa-`, `tama-`, `-ya`, `izzi(ya)-`, `a`, `-ntu`, `-ttu`, `Tarhunza-`, `tanim(a)-`, `-nzi`, `massan(i)-`, `aba-`, `hantawatti-`, `-n`, `appan`, `ta-`, `-sa`.
- units.json, second look: l against the Luwian word order for every unit, and l ↔ i. I checked every grammar label in the notes and morph glosses against ACLT: persons, tenses and moods (present -tti/-i/-ri/-wi, past -ra, imperative -ntu/-ttu), cases (instrumental §63, §71, §72; dative §65; genitive §63, §74, §75; nominative alamanza §61, §74, §75; neuter plural accusative §66, §67, §69, §72b) and gender (hantawattahisa neuter, agreeing with aba). I also checked morph g against the glyphs (ligatures, ri+i, i-zi-i-wa/i, ní-i-pa). No further mismatch was found.

### Refused
- `za-` (published): its list of forms (za, zan, zatti, zassi) does not include this part's zin and zaya. The meaning 'this' covers both forms, and the morph glosses give their cases. Not broadened.
- `alunnamm(a)-` "lust, covetousness": 'covetousness' goes beyond ACLT's 'lust'. It follows the noun's link with alunnazza- 'covet', which the §71 note and its i rely on, and pass 1 accepted it. Kept.
- `haniyattastr(a/i)-` "badness, wickedness": 'wickedness' is a near-synonym that the §72b i uses to tell it apart from attuwalastr(i)-, as its note explains. Kept.
- The published `-wi` "dative ending — 'upon horse'" is pinned to a single line (pilot §8). The rule is that it must be copied whole, so I left it as it is. Rewording the published entry is the orchestrator's call.
