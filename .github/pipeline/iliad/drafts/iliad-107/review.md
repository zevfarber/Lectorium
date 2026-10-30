# iliad-107 — review, pass 1 (Iliad 16.777–867, 52 units, 91 lines)

Pass 1 only (units + new-renderings.md). **Pass 2 pending gloss**: `gloss.json` does not exist yet, so no parse was checked against it; odyssey-forms.json was read (18 forms) and agrees with the notes (δάμασσαν, εἴρυσε, καταπρηνεῖ, λύθεν, πιέμεν, στιβαρόν, σχεδόθεν, φέρτεροι, ἐπετέλλετ’, ἐπευχόμενος, ἤκαχε, ἥβην, ἰόντι, ὀλέσσαι, ὀλοή, ὑπέμεινε, ῥηιδίως).

Order followed: (1) every grammatical label and every claim about where a word stands, cross-references, notes against their own `l`/`i`; (2) Greek → `l` word by word; (3) `l` ↔ `i`; (4) remembered English; (5) quotation marks and `mark`. House tables were grepped per word in `iliad/conventions.md` and `odyssey/conventions.md`; published units (iliad-016, -027, -028, -046, -048, -067, -080, -082, -102, odyssey-046, -055, -063) were read for the shared lines. `t` untouched: the 52 units' `t`, joined, equal the 91 packet lines (checked after editing); every unit still has as many `l` lines as `t` lines. JSON loads. Scansion checked with the Odyssey's `scan_hexameter.py` and by hand.

## Changes (line · field · severity · what was wrong · what was done)

| line · unit | field | sev | wrong | done |
|---|---|---|---|---|
| 794–795 (unit 9) | `l`, `i`, `n` | HIGH | αὐλῶπις τρυφάλεια rendered "socketed helm / helmet". The binding Iliad row for αὐλώπιδι τρυφαλείῃ (5.182) is "tubed helm" / "tubed helmet" and names "socketed" among the renderings avoided on purpose; iliad-028, -067, -082 all shipped "tubed". The draft's `new-renderings.md` row presented "socketed" as a new choice. | `l` "the tubed helm", `i` "the tubed helmet"; note now says "tubed" follows the root αὐλός "pipe, tube" without deciding what the tube was (sense still said to be uncertain). The `new-renderings.md` row removed (it is the table's word, not a new one). |
| 779 (1) | `l` | MED | βουλυτὸν δέ = βουλυτόνδε (Odyssey table 9.58): `l` "toward the ox-unyoking time", `i` "toward the time for unyoking oxen"; the table's avoided list says "drop the oxen". `l` had "toward the time of unyoking". | `l` "toward the ox-unyoking time" (`i` already matched). |
| 784 (3) | `l` | MED | θοῷ ἀτάλαντος Ἄρηϊ: table 8.215 and iliad-048/-080 fix `l` "the equal of swift Ares"; draft had "equal to swift Ares" (the table lists "equal to Ares" as avoided). | `l` "the equal of swift Ares". |
| 788 (5) | `l`, `i`, `n` | MED | ἐνὶ κρατερῇ ὑσμίνῃ: table 4.462 is "in strong battle" in both layers (no article); draft "in the strong battle". Also `l` had an added "there" ("For there met you"). | `l` "For met you Phoebus in strong battle,"; `i` "in strong battle"; note quotes the stock phrase. |
| 789–790 (6) | `l`, `n` | MED | ἠέρι πολλῇ: table 3.381 is "thick mist" in both layers and lists "much mist" as avoided; `l` and note had "in much mist". | `l` "for in thick mist wrapped he met him;" note "‘in thick mist’". |
| 796–799 (10) | `n` | MED | False claim about where words stand: the note said "‘a divine man’ and his name Ἀχιλλῆος put after the verb". ἀνδρὸς θείοιο … κάρη … μέτωπον stand before ῥύετ’ (798); only Ἀχιλλῆος follows it (799). | Note now says the object stands before the verb and the name is put after it. |
| 802–803 (13) | `l`, `i`, `n` | MED | τερμιόεσσα: Odyssey table (τερμιόεις, 19.242, odyssey-094) is `l` "with a border", `i` "bordered"; draft `l` "bordered". Also τελαμών is "shield-strap" in `i` (2.388, 12.401). | `l` "fell to the ground, with a border."; `i` "bordered shield with its shield-strap"; note ties to 19.242. `new-renderings.md` row updated (`l` "with a border"). |
| 808 (16) | `l`, `i`, `n` | MED | ἐκέκαστο: table 2.530 and iliad-027 "excelled" (both layers); "surpassed" is reserved for νικάω. Draft "surpassed". | "excelled" in `l`, `i`, note and `new-renderings.md`. |
| 812 (18) | `l`, `i`, `n` | MED | βέλος of a thrown spear rendered "missile". The Iliad table fixes βέλος "shaft" for arrows and spears (1.382, 4.185, 5.18, 13.289, 16.480); "missile" is for stones and mixed missiles (12.458, 14.439, 16.737; 16.668/16.678 for βελέων). The 781 βελέων stays "missiles" (answers 16.668, iliad-105) and 778 is published. | "shaft" in `l`, `i`, and the note. |
| 817 (20) | `l`, `i`, `n` | MED | Line 817 is 3.32 (iliad-016) without δ’; the packet's repeat list did not catch it. Published English is `l` "back to the company of his companions he drew away, death-fate avoiding" / `i` "drew back into the company of his companions, shunning death"; the table (3.32; 6.167 ἀλεείνων "avoiding"/"shunning"; 167 κήρ "doom" reserved for πότμος/μόρος; 2.417 ἑταῖροι "companions") rules out the draft's "was giving ground … comrades … shunning death-fate / shunning his doom". | `l` and `i` now reuse the published wording; note says 817 is 3.32 without the δ’ and gives "companions". `new-renderings.md` row for ἀναχάζομαι · χάζομαι removed. |
| 819 (21) | `l`, `i`, `n` | MED | ἀναχαζόμενον "retreating": table 11.461 keeps the Odyssey's "draw back" for ἀναχάζομαι and lists "retreating" as avoided. | `l` "back, drawing back,", `i` "drawing back"; note likewise. Row removed from `new-renderings.md`. |
| 821 (21) | `l`, `i`, `n` | LOW | νείατον ἐς κενεῶνα already stands in the table (5.857): `l` "to the lowest flank", `i` "into the lowest part of his flank"; draft had "in". The `new-renderings.md` row presented it as new. Note also called οὖτα "the unaugmented οὖτα", a tautology. | `l` "to the lowest flank", `i` "into the lowest part of the flank"; note: "aorist of οὐτάω … (it has no augment)"; row removed. |
| 824 (23) | `l`, `i`, `n` | MED | χάρμῃ rendered "in the fight"; table 4.222/7.218 is "the joy of battle" and lists "the fight" as avoided. | "in the joy of battle" in both layers; note says so. |
| 824 (23) | `n` | LOW | "ὥ τ’ is οἵ τε, the dual relative": ὥ τε is a dual form, not the plural οἵ τε. | "the dual of the relative with τε". |
| 830 (27) | `l`, `i`, `n` | MED | κεραϊξέμεν rendered "sack"; the table's κεραΐζω is "ravage, lay waste" (2.861) and "sack" is reserved for πέρθω/ἐκπέρθω (1.19, 4.53, 4.308). | "ravage" in `l`, `i`, note. |
| 832 (27) | `n` | LOW | Note said "to the dear fatherland", `l` "your dear fatherland" (as in odyssey-003 and -007, same words). | Note says "his own, hence ‘your’ in English". |
| 835 (29) | `i`, `n` | MED | μεταπρέπω `i` "stand out". The Iliad's own rows (2.481, 11.720, 16.596) have `i` "conspicuous"; "stands out among" is listed as avoided at 2.481. `new-renderings.md` claimed the Odyssey's `i` as the reason, which the Iliad table overrides. | `i` "am conspicuous with the spear among the war-loving Trojans"; note and row updated. |
| 836 (29) | `n` | LOW | Note defined ἦμαρ ἀναγκαῖον as "the day of compulsion", the word its own `new-renderings.md` row lists as avoided. | "the day that is forced on a man". |
| 847 (38) | `n` | MED | "τοιοῦτοι … men of the kind that Apollo, Euphorbus and Hector are": Apollo is not a man and cannot be one of "twenty such"; the claim is invented, and "the point is that mortals could not have done it" asserts a reading the line does not state. | Note: "points to men of the sort who have just struck him down; the claim is that mortals alone could not have done it". |
| 847 (38) | `l` | LOW | εἴ πέρ: `i` has "Even if", `l` "But if" (πέρ dropped). | `l` "But even if twenty such as these had met me". |
| 850 (40) | `l`, `n` | MED | ἐξεναρίζεις `l` "strip me of my armour"; the table (4.488, 5.703, 6.417) is `l` "despoil" (`i` "strip of his armour"). The draft's `new-renderings.md` row said it "follows 6.417" while contradicting that row's `l`. | `l` "and you third are despoiling me."; note and row corrected. |
| 861 (47) | `i` | MED | `i` "whether … may not be the first": adds a negative that is not in εἴ κε … φθήῃ (`l` "if … may be first"). | `i` "Who knows whether Achilles … may be the first to lose his life". |
| 862 (48) | `n` | MED | "ὣς ἄρα φωνήσας is the whole-line closing formula": false label — it is a half-line, here opening the line, and the formula that closes a speech (Odyssey table 4.657). | "the formula that closes a speech". |
| 862 (48) | `l` | LOW | λὰξ προσβάς: table 5.620 `l` "stepping on it with his heel"; draft "setting his heel on him" (the `i` "setting his heel on him" is the 6.65 pattern and kept). | `l` "stepping on him with his heel". |
| 789 (6) | `i` | LOW | "met him wrapped in thick mist" can be read as the mist wrapping Patroclus. | "for the god, wrapped in thick mist, met him;". |
| 788 (5) | `n` | LOW | "δεινός … stands alone at the head of the next line": loose; the word begins 789 and ends the sentence. | "begins line 789 by itself … the clause ends with it". |
| 793 (8) | `n` | LOW | "ἀπὸ … βάλε … tmesis" stated flatly; ἀπὸ stands before κρατός and governs it. | "ἀπὸ … κρατός is ‘from the head’; ἀπὸ can also be read with βάλε, ‘cast off’ (tmesis)". |
| 796–799 (10) | `i` | LOW | "horse-plumed helmet": table ἱπποκόμος (12.339) has `i` "with horsehair plumes". | `i` "the helmet with horsehair plumes". |
| 799 (11) | `l`, `n` | LOW | φορέειν `l` "to bear"; table has φορέω "carry" in `l` (2.770, 13.372; `i` "wore" is allowed for a known object). | `l` "to carry"; note says ‘to carry’, ‘to wear’ in the free English. |
| 801 (12) | `i` | LOW | κεκορυθμένον `i` "fitted with its head" adds a gloss; the table keeps κορύσσω "arm" (5.681, 5.699). | `i` "stout, and armed;" (the note already explains "armed with its head"). |
| 806–809 (16) | `n` | LOW | "Euphorbus is named only at the end of the long sentence": the sentence goes on after his name. | "named only after the verb, last of the three phrases that describe him". |
| 810 (17) | `n` | LOW | "ἀφ’ ἵππων … means from their chariots" stated as fact. | "is taken to mean". |
| 813 (19) | `i` | LOW | "would not wait" adds refusal; οὐδ’ ὑπέμεινε is a plain aorist. | "did not wait for Patroclus". |
| 813 (19) | `n` | LOW | "spoken to him in the second a line before": the vocative is at 812, three lines before 815. | "three lines before (812)". |
| 825 (24) | `i` | LOW | ἐθέλουσι `i` "want"; "wish" is the ἐθέλω word (13.347: "want" reserved for βούλομαι). | "wish to drink". |
| 826 (25) | `i`, `n` | LOW | ἐδάμασσε `i` "masters"; the table's δαμάζω `i` is "overcome" (5.106, 5.138, 6.368) and the note said "subdues". | `i` "overcomes", note "‘overcomes’". |
| 839–841 (32) | `i` | LOW | νῆας ἔπι with ἰέναι is motion "to", `i` had "at". | "Do not come to me, to the hollow ships,". |
| 839 (32) | `mark` | LOW | Hector quotes Achilles inside his speech, a speech with its own ‘ ’; the house practice (odyssey-005 "Antinous quotes Penelope") puts a `mark` on the first unit. None given. | `mark` "Hector quotes Achilles" added. |
| 844 (35) | `i` | LOW | ἤδη dropped from `i` ("Now, Hector"), while `l` has "Now already" and the note "even now". | `i` "Even now, Hector, boast greatly;". |
| 844 (36) | `l`, `i` | LOW | ἔδωκε is an aorist (and the note says ‘gave’), `l`/`i` had perfect "has given / have given". | "gave" in both. |
| 848 (38), 854 (42) | `i` | LOW | δαμέντες / δαμέντ’ `i` "brought down"; table `i` is "overcome" (16.326). | "overcome by my spear" and "you will be overcome by the hands of Achilles". |
| 856 (44) | `n` | LOW | "Ἄϊδος δὲ is Ἄϊδόσδε": the text has the genitive Ἄϊδος plus δέ. | "the genitive Ἄϊδος with the ending -δε of motion toward, ‘to (the house of) Hades’". |
| 859 (46) | `n` | LOW | "αἰπύς ‘steep’ here meaning towering, sheer": the table keeps αἰπύς "steep" (11.174). | "the stock phrase; αἰπύς is ‘steep, sheer’". |

Counts: **HIGH 1, MEDIUM 17, LOW 29** (47 changes; 62 fields in 31 units, `t` untouched). `new-renderings.md` edited: three rows removed (αὐλῶπις, ἀναχάζομαι · χάζομαι, νεῖατον κενεών) and four corrected (τερμιόεσσα, μεταπρέπω, ἡλικίην ἐκέκαστο, ἐξεναρίζεις); ἦμαρ ἀναγκαῖον, ὀρωρέχαται and the 866/867 row kept.

## The drafter's open doubts, tested

- **789 ὃ μὲν Patroclus, τὸν ἰόντα Apollo.** Correct: ὃ μὲν (with οὐκ ἐνόησεν) is Patroclus, who does not see the god coming; the participle κεκαλυμμένος and ἀντεβόλησε then belong to the god, and the note says where the subject changes. Kept.
- **835 ὅ.** The printed ὅ with its accent is the neuter relative used as a conjunction ("in that"); ἀμύνω takes ἦμαρ as object and σφιν as dative. Note true. Kept.
- **852 βέῃ.** Second singular of the epic future-sense form of the verb "to live" (cf. βέομαι, 15.194); note's "has the force of a future" is true. Scanner's "correption: βέῃ" is the usual shortening before ἀλλά. Kept.
- **852 χερσὶ δαμέντ’.** δαμέντα elided, accusative singular agreeing with the unexpressed "you" after παρέστηκεν (death and fate stand near you, [you] to be overcome); the note says this. `l` "you to be subdued" matches. Kept.
- **860 φθήῃ … ὀλέσσαι.** φθήῃ is aorist subjunctive of φθάνω after εἴ κε; ὀλέσσαι the aorist infinitive of ὄλλυμι in tmesis with ἀπό (odyssey-forms agrees); τυπείς is the participle. Note true. Only the added "not" in `i` was wrong (fixed above).
- **811 [810] ἀφ’ ἵππων.** The phrase is at 810, not 811. "From chariots" is the usual sense, but the note stated it flatly; hedged ("is taken to mean"). `l`/`i` keep "from their horses".
- **866 `i`.** τὸν = Automedon is the only reading the sense allows (Hector is the subject of ἵετο, 866; Peleus's immortal horses are the ones that carry Automedon out). The departure from iliad-102 (where τὸν = Hector, 16.383) is a different referent, not a different rendering, and `new-renderings.md` records it. Units 50/51 split the published pair differently from iliad-102, so the whole-unit identity rule does not apply; their `l` and the clauses of `i` are the published wording. Kept.
- **857 scansion.** Scanner: `––|–⏑⏑|–⏑‖⏑|–⏑⏑|–⏑⏑|–×` with "closed syllable scanned short: ἀνδροτῆτα" and "correption: καὶ". By hand: ὃν πότ|μον γο|όω|σα λι|ποῦσ’ ἀν|δροτῆ|τα καὶ ἥ|βην is not a valid hexameter without taking ἀν- of ἀνδροτῆτα (closed by ν before δρ) as short and shortening καὶ before ἥ; the irregularity is real and the note's sentence says both things truly. Kept.
- **818-line-start quotation structure.** 818 is a new paragraph (¶) and plain narration (unit 21, `p` true, no quotes); the first speech opens at 830 (unit 27, “ in `l` and `i`, `mark`), Achilles' quoted charge ‘ ’ at 839–841 (units 32–33) sits inside it, Hector's speech closes at 842 (”, unit 33); Patroclus 844–854 (“ unit 35 `mark`, ” unit 42); Hector 859–861 (“ unit 46 `mark`, ” unit 47). Each “ and ” stands in both `l` and `i`. Neighbouring part: the last unit of iliad-106 (775–776, ὃ δ’ ἐν στροφάλιγγι κονίης / κεῖτο μέγας μεγαλωστί) is narrative, no speech runs in; 867 ends Book 16 and no speech runs out.
- **Odyssey-shared lines.** A four-word search of every published Odyssey unit found only: 851 (odyssey-055, -079: identical, English reused ✓), 804 (Od. 8.334 "the lord, the son of Zeus, Apollo" ✓), 832 φίλην ἐς πατρίδα γαῖαν ("your dear fatherland" ✓), 860 τίς δ’ οἶδ’ εἴ (Odyssey `l` "who knows if", `i` "whether" ✓), 862 δόρυ χάλκεον ἐξ ὠτειλῆς (odyssey-046: "the bronze spear out of the wound" ✓), 793 τοῦ δ’ ἀπὸ μὲν (different continuation). 779 (Od. 9.58 βουλυτόνδε) is fixed in the table; no published Odyssey unit carries it.

## Considered and refused

- **777 `i` "stood in the middle of heaven" vs the table's `i` "had reached" (8.68).** The table row is for ἦμος δέ "But when …"; with ὄφρα "As long as …", "had reached" gives wrong English. "stood astride", the word the row avoids, is not used. Left.
- **779 `l` "And when" vs `i` "But when" (δέ).** Both are ordinary renderings of δέ; no rule. Left.
- **Spondaic fifth feet (779, 788, 862).** Real, but the packet flags only 857, and a spondaic fifth is an ordinary licence; no sentence added.
- **788 "imperfect of ἀντάομαι".** Dictionaries differ between ἀντάω and ἀντάομαι; the label "imperfect" is true. Left.
- **826 ἀπηύρα "imperfect" (828) vs ἀπούρας "aorist participle" (831).** Both are the usual classroom labels for the two forms of the one defective verb. Left.
- **837 "was no help to you" for χραίσμησεν.** The row 7.144 (ἔχραισμε "ward off") does not govern an intransitive use with a dative of the person; "help" is the shipped English in iliad-027, -086. Left.
- **839–841 `l` "than that … you have torn" for δαΐξαι.** An infinitive after πρίν rendered as a finite verb in the literal layer; clumsy but accurate. Left.
- **852 `i` "stand close beside you" / `l` "has taken its stand".** Both render the perfect. Left.
- **824–825 "ἐθέλουσι without a contraction" and ἄμφω "dual in sense".** Harmless wording, true of the form. Left.
- **Remembered English.** Searched `i` for phrases that recall a modern version (e.g. "flat of his hand", "steep destruction", "winged words", "day of necessity", "sheer might"): the first three are the house table's own (odyssey-063, 11.174, the ἔπεα πτερόεντα row); "day of necessity" is the literal pair to ἐλεύθερον ἦμαρ "day of freedom" (6.455); "sheer might" is the draft's gloss for βίηφιν. No wording was found that has to be replaced; no translation was consulted.

# Pass 2 — gloss.json (69 novel forms, 17 broadened)

Checked: every parse and meaning against the line in the edited `units.json`; key coverage (the 69 keys equal `novel-forms.json` exactly); novel entries under 230 characters, typographic ’ only (no straight quotes), no line numbers or "here"; Homeric forms name their Attic equivalent; each of the 17 `__broaden__` entries begins with the whole old `known-forms.json` entry followed by " · " (all 17 pass); glosses against the edited `l`/`i`. File loads.

## Changes

| form | sev | wrong | done |
|---|---|---|---|
| χάρμῃ (broadened) | MED | new reading "’in the fury of battle’" for ἐβιήσατο; the unit (and table 4.222/7.218) says "in the joy of battle" | "’in the joy of battle’" |
| κεραϊξέμεν | MED | "sack, ravage, plunder … ’to sack’"; unit now "ravage" (sack is reserved for πέρθω) | "ravage, lay waste … ’to ravage’" |
| κεκορυθμένον | MED | "’fitted (with its head)’" contradicted the edited `i`/`l` "armed" and the table (κορύσσω keeps "arm") | "arm (from κόρυς ’helmet’) … ’armed (with its head)’" |
| πεφνόντα | MED | lemma θείνω with aorist ἔπεφνον; the unit's note and the table (4.397) say φένω | lemma φένω, "’who had killed’" |
| ἀναχαζόμενον | MED | "’retreating’"; table 11.461 and the unit now "drawing back" | "’drawing back’" |
| δαμέντ | LOW | "’(you) brought down’"; `i` now "overcome" | "’(you) overcome’" |
| νήπιε | LOW | "’fool!’"; `l`/`i` "foolish one" | "’foolish one’" |
| ἀναγκαῖον | LOW | "’of compulsion’" (the word the renderings row avoids) | "’of necessity’" |
| ἡλικίην | LOW | "epic -ίη (ἡλικίη)" names no Attic equivalent for the accusative | "(= Attic ἡλικίαν)" |
| ἰόντι | LOW | "’for one going, as he goes’" did not fit the line (agrees with τοι, "as you went") | "agreeing with τοι: ’as you went’" |
| στρεφεδίνηθεν | LOW | lemma στρεφεδινέομαι; note and house use στρεφεδινέω | lemma στρεφεδινέω |
| κεφαλῇ (broadened) | LOW | example "to wear on his own head" vs `l` "to carry" | "to carry on his own head" |

Counts: HIGH 0, MEDIUM 5, LOW 7 (12 edits).

## Considered and refused
- αὐλῶπις is not a form in this file's keys; nothing to fix for "tubed" (gloss has no entry for it; the unit note carries it). βέλος likewise absent (known form).
- τερμιόεσσα "with a border or rim (sense not certain)" agrees with `l` "with a border"; kept.
- στιβαρὸν "’sturdy’" (known entry, broadened shape) vs `i` "stout": the Odyssey entry's gloss; kept.
- ἐπετέλλετ "’kept enjoining’" vs `l` "laid … charges": iterative sense is fair; kept.
- ὅ, μέσον, ᾗ: long broadened lists exempt from the 230 limit; the new readings (ὅ "in that, because"; μέσον οὐρανόν "mid-"; ᾗ possessive with κεφαλῇ) are true of the lines.
- βουλυτὸν, ῥεθέων, ἐνόρουσε "(= Attic ἐνώρουσε)": acceptable.
