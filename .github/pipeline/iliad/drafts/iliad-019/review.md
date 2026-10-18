# iliad-019 (3.264–368) — review

Reviewer: two passes. Pass 1: every note label, position claim and cross-reference; Greek → `l` word by word; `l` ↔ `i`; remembered English; quotation marks; packet-flagged lines; house renderings. Pass 2: re-read of the edited `units.json`, a mechanical check (below), and every parse in `gloss.json` against the line.

Severity scale: **high** = `l` or `i` wrong in sense; **medium** = a note (or gloss entry) says something false about a form, construction or case, or contradicts `l`/`i`/the house table, or a known form's entry does not cover its use here; **low** = imprecision, an English word with nothing under it in the Greek, a cross-reference slip.

`t` was never touched (checked: all 56 `t` strings, joined, equal lines 264–368 of the source; `ln`, `p`, `mark`, `v`, `\n`-count of `l` against `t` all checked by script).

**Counts. units.json: high 0, medium 5, low 13, plus 1 scansion note added. gloss.json: medium 13, low 17. new-renderings.md: 3 rows corrected to match.**

## Mechanical checks passed (no change needed)

- Cross-references in the notes, all checked in `source/iliad-monro-allen1920.json`: 2.45 (= 3.334, verbatim), 2.419 (ὣς ἔφατ’, οὐδ’ ἄρα πώ οἱ ἐπεκραίαινε Κρονίων; the note's "they/for them for he/for him" is exactly the difference), 3.245 (κήρυκες … φέρον ὅρκια πιστά), 3.261 and 3.262 (the last part's tmesis line and the Antenor line), 3.347 (Ἀτρεΐδαο … πάντοσε ἴσην), 346 (πρόσθε), 332 (ἔδυνεν), 334, 316–317 (lots, "which first let fly"), 286/288 (τιμήν), 266 = 341, 297 = 319, 276/298/320 (κύδιστε μέγιστε), 351 (τίσασθαι), 338. Rows of `new-renderings.md` cite 3.256, 3.259, 3.28, 3.183, 2.771, 3.240, 2.11, 2.342, 2.368, 2.743, 1.13, 1.122, 1.159, 1.181, 1.199, 1.478, 1.602: all exist and contain the word cited, except 2.137 (the word is at 2.138; corrected in the row).
- Repeated lines. 3.312: `l` and `i` identical to iliad-018's unit at 262 (script). 3.266 = 3.341: identical English in both units. 3.276 = 3.320 (first line of each speech): identical. 3.297 = 3.319: identical. 3.336–337 = odyssey-107 (the Iliad cuts the Odyssey's unit at the ano teleia after ἵππουριν; wording is the Odyssey's, verified against `odyssey-107.json`). 3.338 = odyssey-082 (`l` identical; `i` adds "he", needed because the sentence begins here, and the note and the renderings row say so). 3.365 = odyssey-100 plus the opening quotation mark only. 3.277 is the second-person form of the Odyssey half-line (odyssey-052 and -060: "who oversees all things and listens to all things" / "sees everything and hears everything"); the Iliad's `l`/`i` follow it.
- Quotation marks. Speeches open at 276, 298, 304, 320, 351, 365 (each first unit has `mark` and “ in both `l` and `i`); close at 291, 301, 309, 323, 354, 368 (” in both). No unit carries an unbalanced mark. iliad-018's last unit (3.263) is narration and no speech runs into this part; iliad-020 opens at 369 (ἦ καὶ ἐπαΐξας), narration, so 368 really ends Menelaus' speech.
- Paragraph marks `p`: exactly the units that begin at 264, 292, 302, 310, 324, 340, 355 (the ¶ lines of the packet).
- Epithets against the house table (Odyssey and Iliad tables): πουλυβότειρα "much-nourishing" / "that feeds so many"; ἀγαυός "noble"; ἀρηΐφιλος Μενέλαος "Ares-loved" / "dear to Ares"; ἰσόθεος φώς; ἐϋκνήμιδες; ἱππόδαμος "horse-taming" / "tamer of horses"; κορυθαίολος; ξανθός; ἄναξ ἀνδρῶν; πολύμητις; ποντοπόρος "sea-crossing"; ἰφθίμῳ "mighty"; ἄλκιμον ἔγχος "sturdy"; δολιχόσκιον "long-shadowed"; χαλκήρης "bronze-fitted"; μένος "might"; αἰειγενέτης "forever-born"/"everlasting"; ἦ (ῥα) καί "He spoke, and"/"So he said, and"; ἐστιχόωντο (men: "marching"); λαοί "people"/"troops"; ὣς ἔφαν; ᾤμωξεν "cried out"; ἀλεύατο "avoided"; θώρηξ "breastplate"; κακότης "baseness" (the Iliad row, 2.368); ἠΰκομος "fine-haired". All agree with the table. Departures (τιμή "recompense", ποινή "requital", ὅρκια πιστὰ θεῶν, ἀερσίποδες, φάλος) are in `new-renderings.md` with reasons.
- Remembered English: none found. Phrases that might arrive fully formed were rebuilt from the Greek: "may their brain run out on the ground like this wine" (ῥέοι, χαμάδις, ὡς ὅδε οἶνος), "Hear me, Trojans and well-greaved Achaeans" (κέκλυτέ μευ), "three pieces and four" (τριχθά τε καὶ τετραχθά, the idiom's two numbers), "the black spirit of death" (table). None needed changing.

## Changes — units.json

| line · field | severity | what was wrong | what was done |
|---|---|---|---|
| 271 · n | low | "the same word names Menelaus from 347 on": at 347 the form is Ἀτρεΐδαο, not Ἀτρεΐδης (Ἀτρεΐδης first at 350) | now says "the same name is used of Menelaus later (Ἀτρεΐδαο at 347, Ἀτρεΐδης at 350)" |
| 271 · n | low | ἄωρτο glossed "had been hung" while `l`/`i` say "always hung" | now "‘had been hung up’, so ‘was hanging’" |
| 275 · i | low | "On behalf of them all": "all" has nothing under it (τοῖσιν = the leaders served with the hairs) | "On their behalf" |
| 284 · i | low | `i` dropped καί of ἥ τε καὶ ἐσσομένοισι (`l` has "as well") | added "as well" to `i`; row in new-renderings.md updated |
| 288 · l and i | low | "I myself": αὐτάρ ἐγώ has no αὐτός; "myself" added an emphasis the Greek does not make | removed "myself" from both layers |
| 297 · n | medium | εἴπεσκεν called "an iterative imperfect"; it is the iterative formed on the aorist stem of εἶπον (the Odyssey and Iliad glossaries already say "iterative aor.") | "an iterative past tense built on the aorist stem of εἶπον" |
| 298 · n | medium | "The three verbs πημήνειαν, ῥέοι and δαμεῖεν are optatives of wish (‘may they do harm …’)": πημήνειαν stands in the relative clause (ὁππότεροι … πημήνειαν) and `l`/`i` rightly render it "do harm"/"does harm", not as a wish; the note contradicted its own `l`/`i` | ῥέοι and δαμεῖεν are the wishes; πημήνειαν is the optative in the relative clause that goes with them (‘whichever of the two should do harm’) |
| 298 · n | low | last sentence ("ἐγκέφαλος ‘brain’, and ἄλοχοι ‘wives’ made subject … means taken over …") had no sensible construction | rewritten: ἐγκέφαλος singular; ἄλοχοι … δαμεῖεν says the wives are to be made subject to others |
| 304 · n | medium | κέκλυτε called "the perfect imperative" of κλύω; it is the reduplicated aorist imperative (both glossaries say so) | corrected |
| 305 · i | low | "with my own eyes": "own" not in ἐν ὀφθαλμοῖσιν (`l` has "with my eyes") | "with my eyes" |
| 310 · n | medium | "ἂν δ’ ἄρ’ ἔβαιν’ … κατὰ δ’ … τεῖνεν … both without the augment": ἔβαιν’ = ἔ-βαινε keeps its augment; only τεῖνεν lacks it | "the augment is kept in ἔβαιν’ (ἔ-βαινε) but absent in τεῖνεν; the same tmesis stands at 261" |
| 313 · l | low | `l` "returning, back to Ilios": "back" has no word of its own (ἄψορροι is already "returning") | removed "back" |
| 314 · n | low | "χαλκήρης being a stock epithet of helmets and spears": only a helmet is called so in this part; the note may not claim more than the part shows | "χαλκήρης ‘bronze-fitted’ is the word for the helmet here" |
| 334 · n | low | "The same line stands at 2.45, with the same English": `l` is the same, `i` has the words in a different order | "…and `l` has the same English there" |
| 337 · n | medium | "ἔνευεν … without the augment": ἔνευεν = ἔ-νευεν has the augment (the final ν is movable; the glossary says so) | corrected |
| 344 · n | low | "at spear-throw distance": the Greek says only ἐγγύς, "near" | "close together" |
| 355 · l and i | low | repeated half-line προΐει δολιχόσκιον ἔγχος had "his" at 346 and "the" at 355, while the note said "with the same English" | 355 now "his long-shadowed spear" in both layers (new-renderings.md row updated) |
| 357 · n | low | ἠρήρειστο glossed "had been driven" while `l`/`i` say "was driven" | "‘was driven in’" |
| 357 · n | scansion (real) | packet flag, see below | added one sentence: "The line is metrically irregular as transmitted: it scans only if the short ι of διὰ is lengthened in the first foot." |

Packet scansion flag, line 357: διὰ μὲν ἀσπίδος ἦλθε φαεινῆς ὄβριμον ἔγχος. By hand: –⏑⏑ | –⏑⏑ | –⏑⏑ | –– | –⏑⏑ | –×, that is διὰ μὲν (δῑ-ὰ μὲν) | ἀσπίδος | ἦλθε φα- | -εινῆς | ὄβριμον | ἔγχος, with ει a diphthong and ὄ long before βρ. The first foot cannot be filled without lengthening the naturally short ι of διά (the scanner reports the same: "metrical lengthening: διὰ [longum of foot 1]"; there is no other irregularity). 358 (not flagged) has διὰ short in a dactyl (καὶ διὰ θώρηκος), so the lengthening is specific to 357. Real, so the sentence was added.

## Changes — gloss.json (second pass)

Every one of the 196 novel entries and the 14 broadenings was read against its line(s). All lengths are under 230, only ’ is used, and each `__broaden__` entry still begins with the old entry whole plus " · ".

| form · entry | severity | what was wrong | what was done |
|---|---|---|---|
| κουλεόν | medium | "neut. nom. sg."; it is the accusative after πὰρ (the subject of ἄωρτο is ἥ, the knife) | "neut. acc. sg., … after παρά" |
| πὰρ (broaden) | medium | added "prep. + gen., ’beside’ (πὰρ ξίφεος ’beside the sword’)": ξίφεος depends on κουλεόν; πὰρ takes the accusative, which the old entry already covers | clause removed; the adverb reading (πὰρ δέ οἱ …) stays |
| κασιγνήτοιο | medium | "in apposition to οἷο"; οἷο agrees with it as the possessive adjective | "with οἷο agreeing" |
| παλάμηφιν | medium | "in or by the hand" only; at 368 it is ἐκ … παλάμηφιν, "from the palm" | covers dative and ablative, both senses |
| φάλον | medium | stated a definite sense ("ridge or boss … the socket holding the crest"); the meaning is disputed and the note says so | "usually taken as the ridge that carried the plume; the sense is not certain" |
| ἐπίορκον | medium | "acc. sg. used adverbially: ’falsely’", contrary to `l`/`i` ("swears a false oath") and the renderings row, which turns "swears falsely" down | "neut. acc. sg., as cognate object of ὄμνυμι: ’a false (oath)’" |
| ἠΐχθη | medium | ’was hurled’ (passive) against `l`/`i` "darted" | "aor. pass. 3 sg. with active sense: ’darted’" |
| ὁρᾶσθαι | medium | "’to be seen, to look’": here it is "to look at" (middle, object μαρνάμενον … υἱόν) | corrected |
| ξίφος (broaden, new) | medium | known entry covers the accusative only; 367 ξίφος ἄγη has it as subject | added nominative reading |
| τέλος (broaden, new) | medium | known entry covers the nominative only; 291 τέλος πολέμοιο κιχείω has it as object | added accusative reading |
| τιν (broaden, new) | medium | known entry "masc. acc. sg."; ἥν τιν’ ἔοικεν is feminine, agreeing with τιμήν | added the feminine reading |
| ὡς (broaden, new) | medium | known entry has no comparison; ὡς ὅδε οἶνος is "like this wine" | added |
| ἀτρεΐδαο (broaden, new) | medium | known entry "i.e. Agamemnon"; 347 and 356 use the genitive of Menelaus (356 Πριαμίδαο is the mirror) | added "also … Menelaus" |
| δαρδανίδης | low | "of Priam: ’the Dardanian’" (pinned to a line, and "the Dardanian" is the rendering turned down in the renderings row) | "descendant of Dardanus, ancestor of the Trojan royal house (patronymic); masc. nom. sg." |
| δεινὸν | low | ’terribly’ (turned down in the row; the unit says "dreadfully"/"fearsomely") | ’dreadfully, fearsomely’ |
| δερκόμενοι | low | "glare" / ’glaring’ (turned down: "glaring"); δέρκομαι is "look" | ’looking’ |
| διάμησε | low | ’slit’ / "slice open", not `l`'s "cut through" | "cut through" |
| πημήνειαν | low | ’should wrong, violate’ ("wrong" is turned down in the row; the unit says "do harm") | ’should do harm’ |
| ποινῆς | low | "recompense" / ’for the recompense’: the house gives "recompense" to τιμή and "requital" to ποινή | "requital, payment exacted …" / ’for the requital’ |
| ποντοπόροισιν | low | "sea-faring" (the table keeps "seafaring" for another word) | "sea-crossing" only |
| τίνυσθον | low | "pres. 2 dual": 2nd and 3rd dual share the ending and the clause is relative | "pres. dual mid. (2nd and 3rd person share the ending): ’the two punish’" |
| ἀερσίποδες | low | gave the sense as certain; the note says it is not quite certain | "the usual explanation, sense not quite certain" |
| ἀραρυίας | low | "Attic ἠρηρυῖα": an Attic equivalent I cannot support | "epic reduplicated -υῖα, no Attic prose equivalent: ’fitted’" |
| ἀργυρέοισιν | low | "masc. dat. pl." though it agrees with neuter ἐπισφυρίοις | "masc./neut." |
| ἀφείη | low | ’should hurl’ ("hurl" turned down for ἀφίημι; the unit says "let fly") | "let go, let fly" / ’should let fly’ |
| ἄψορροι | low | ’turning back’ (turned down in the row; the unit says "returning") | ’returning’ |
| ἐφάμην | low | "epic uncontracted": the form is not an uncontracted one | "impf. mid. 1 sg. (= Attic ἔφην)" |
| ἰφθίμῳ | low | meaning order "stout, mighty" ("stout" belongs to στιβαρός) | "mighty, stout" |
| ἔχεν (broaden) | low | example translated ’amazement seized’ against the unit's "wonder held" | ’wonder held (them)’ |
| τ (broaden, new) | low | known entry lacks ἦ τε (366 ἦ τ’ ἐφάμην) | added |

## Findings considered and refused

- **οἷο (333) "the possessive pronoun in the genitive"** (note and gloss). Suspected a wrong label (genitive of the pronoun ἕ). Refused: οἷο agrees with κασιγνήτοιο in -οιο and is the possessive ὅς, ἥ, ὅν; the Odyssey glossary has the same entry.
- **ἵκοντο "a past tense of ἱκνέομαι"** (264). Vague (it is the unaugmented aorist), but true; the glossary entry names the aorist. Left.
- **ἄψορροι "agreeing with" the dual τώ** (313). Plural adjective with a dual pronoun is ordinary Greek; "agreeing" is not false. Left.
- **τίνυσθον "two powers below are meant, unnamed"** (276). Kept: the verb is dual, which is all the note claims.
- **αὐτῷ in ἀμφὶ δ’ ἄρ’ αὐτῷ (362) "means about the helmet"**. The antecedent could be argued (helmet or its ridge), but `i` says "around it" after "the ridge of the helmet", which fits either; not hedged further.
- **"stock epithet" for ὄβριμον, φαεινῆς, εὐρύς, ἀρήϊος (357, 364, 339).** The part cannot show the stock use; weakest claims of the notes. Left because the convention names these as epithets and the renderings table already carries them; flagged here for the owner.
- **334 `i` word order against iliad-007** ("slung about his shoulders the silver-studded sword, a bronze one", published: "slung the silver-studded sword about his shoulders"). The apposition χάλκεον would sit oddly after "shoulders"; `l` is identical. Left, note softened.
- **"ἐκλίνθη … ‘swerved aside’" (360 `i`) and "rising to the blow" (361 `i`)**: both follow the table (κῆρα μέλαιναν; Odyssey ἀνασχόμενος), not remembered English.
- **δῖος Ἀλέξανδρος in Menelaus' mouth (351)**: kept "heavenly" by the stock-epithet rule; the note says so ("even of the man he hates").
- **ἔκχεον (295)**, impf. or aor.: the form is the same and the note does not say which. No change.
- **Unit 24 `l` "were going away" against the note's "go back"**: ἀπονέομαι is "go back"; `l` keeps ἀπο- as "away" and "returning" for ἄψορροι. Left.
- **Line 358** (scanner: "spondaic fifth", not packet-flagged): ἠρήρειστο ends the line with –– in the fifth foot, which is the ordinary spondaic line. Not a note matter.
- **The validator warning on 365** (English differs from odyssey-100 by the opening quotation mark): expected, recorded in new-renderings.md.
- **gloss.json "ἐρυσσάμενος ’having drawn (a sword)’"**: used here of a knife as well; the parenthesis reads as an example. Left.
- **gloss.json ὅδε/ὅτις/ἧός/πόσις and the other 150-odd novel entries** read against the line and found correct in lemma, case, number and tense; no change.
