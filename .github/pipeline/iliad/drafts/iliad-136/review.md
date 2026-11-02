# iliad-136 (21.400–501) — review

Two passes: units.json (pass 1), then gloss.json (pass 2). `t` untouched (re-checked equal to the archive, lines 400–501). Totals: 0 high, 15 medium, 17 low. No scansion flags in the packet. Nothing run through the build.

Boundaries checked. Last unit of iliad-135 (21.396–399) closes Ares' speech with ” on 399, so `ὣς εἰπών` at 400 is correctly outside any speech, and no ” is owed here. Hermes' speech ends at 501: source line 502 opens a new paragraph with `ὣς ἄρ᾽ ἔφη, Λητὼ δὲ συναίνυτο …` ("So he spoke"), so the closing ” on the 500–501 unit is right and iliad-137 begins outside a speech. Quote marks otherwise balanced: Athena 410–414, Hera 420–422, Athena 428–433, Poseidon 436–460, Apollo 462–467, Artemis 472–477, Hera 481–488, Hermes 498–501; `mark` and `p` present on every speech start and every ¶.

## Pass 1: units.json

| line · field | sev | was wrong | done |
|---|---|---|---|
| 400 · l, n | medium | `l` "he wounded at the aegis"; table row οὔτησε κατ’ ἀσπίδα (11.434) says a thrust that lands on the shield wounds no one, so "wounded" is false | `l` "he thrust at the aegis"; note says the thrust lands on the aegis and wounds no one |
| 402 · l, i, n | medium | same: "Ares wounded her" / "stabbed her" makes Athena wounded, which the next unit contradicts | `l` "There at her Ares thrust"; `i` "stabbed at her"; note adds that the spear does not wound her |
| 410 · l, n | medium | ἰσοφαρίζεις `l` "match yourself"; table row ἰσοφαρίζει (21.194) is `l` "compares himself", `i` "matches" | `l` "compare yourself"; `i` already "match yourself with me"; note says so |
| 420 · i | medium | βροτολοιγὸν Ἄρηα `i` "mortal-ruining Ares"; table (13.298, 11.295) has `i` "Ares, the ruin of mortals" | `i` changed |
| 435 · n | medium | "προσέφη is the unaugmented aorist": false, ἔ-φη carries the augment | note now "aorist of πρόσφημι (the augment sits between πρός and the stem)", as in iliad-104 |
| 455 · l, n | medium | στεῦτο `l` "claimed"; table (2.597, 5.832, Odyssey 17.525) is `l` "declared", `i` "claimed" | `l` "declared"; note "declared, claimed" |
| 475–477 · l, i, n | medium | ἐναντίβιον rendered "face to face … with force opposed"; table (8.255, 10.451) fixes "head-on" and reserves "face to face" for ἀντίον ηὔδα | `l` "opposite Poseidon head-on to fight"; `i` "fight Poseidon head-on"; note rewritten |
| 474 · i | medium | αὔτως `i` "for no reason"; table (2.342) keeps `i` "to no purpose" and lists "for no reason" as avoided | `i` "to no purpose" |
| 482 · l, i, n | medium | `l` "to set myself against" has the wrong person (the one who opposes is "you", not "I"), and ἀντιφέρεσθαι is the table's 1.589 verb, `l` "to oppose", `i` "stand against" | `l` "to oppose"; `i` "to stand against"; note |
| 487 · l, i, n | medium | φερτέρη "mightier"; every shipped φέρτερος (2.201, 6.158, 10.557, 21.264) is "stronger" | "stronger" in `l`, `i`, note. (Now κρείσσοσιν at 486 is also "stronger"; the table already has both words as "stronger", so this is conformity, not a new clash) |
| 489 · l, i, n | medium | ἦ ῥα, καί `l`/`i` "So she spoke, and"; table (1.219, 14.214) is `l` "She spoke, and", `i` "So she said, and", and keeps ὣς φάτο apart | `l` "She spoke, and"; `i` "So she said, and"; note |
| 500–501 · l, i, n | medium | πρόφρασσα `l` "very readily" (table: `l` "ready-minded"); εὔχεσθαι `l` "claim" (table `l` "declare"); νικῆσαι "beaten/beat" (table νικάω `l` "prevailed over", `i` "defeated") | `l` "but, very ready-minded, … declare yourself to have prevailed over me"; `i` "… that you defeated me"; note |
| 472 · i | low | vocative ἑκάεργε `i` "far-working one"; table (7.34) `i` "you who work from afar" | `i` "you who work from afar" |
| 481 · i | low | κύον ἀδεές `i` "you fearless dog"; the Iliad's own row (iliad-050, 8.423) is `l` "dog, fearless one", `i` "you fearless one" | `i` "you dog, you fearless one" (resolution below) |
| 466 · n | low | "subjunctive with the epic long vowel": the subjunctive ω is ordinary; the epic feature is the ending -μεσθα | "epic ending -μεσθα (Attic παυώμεθα)" |
| 495 · n | low | ἁλώμεναι called "aorist passive infinitive"; ἑάλων is a second-aorist (active form), passive in sense | "aorist infinitive … (passive in sense)" |
| 497 · n | low | "the meaning of διάκτορος ('the guide') is unknown" contradicts giving a sense | "is not known ('the guide' is the usual rendering)" |
| 450 · l, n | low | ἐξέφερον is imperfect (the note says "were bringing it out") but `l` "brought out" | `l` "were bringing out" |
| 418–419 · n | low | note calls the introduction "winged words he spoke" for a feminine subject | "she spoke" |
| 475 · n | low | note quotes ὡς τὸ πρίν; the printed word is πρὶν | corrected |
| 487 · i | low | `i` "learn what war is" adds a reading to πολέμοιο δαήμεναι | "learn about war" |

## Pass 2: gloss.json (all 103 novel forms and 21 broadenings read against the line; every broadening begins with the old entry whole; no ASCII apostrophe, no line number, all under 230)

| form | sev | was wrong | done |
|---|---|---|---|
| νικῆσαι | medium | "(that I) beat": ἐμέ is the object, the subject is the understood "you" (Leto) | "(that you) beat (me)", with ἐμέ named as object |
| εὔχεσθαι (broaden) | medium | example "declare that I beat" has the same error | "declare that you beat me", noting the imperative use |
| κυνάμυια (broaden added) | medium | old entry "fem. voc. sg."; 421 ἡ κυνάμυια ἄγει is nominative, subject | broadened: nominative with ἡ |
| διέσταμεν | low | "= Attic διέσταμεν" is the same form | "= Attic διεστήκαμεν" |
| κίομεν | low | "= Attic ἐκίομεν" invents an Attic form | "the augmented form is ἐκίομεν" |
| μέτελθε | low | "= μετάελθε" garbled | "accent thrown back in the compound (μετά + ἔλθε)" |
| πειρᾷ | low | "+ gen." not true of this line | "+ an indirect question" |
| χαλεπή | low | gloss "hard (to match)" not the sense of ἀντιφέρεσθαι | "hard (to oppose)" |
| ἴρηκος | low | "gen. of the agent" overstates ὑπ’ ἴρηκος | "gen. after ὑπό, of the pursuer" |
| τοῦ (broaden) | low | example "τοῦ … χάριν 'for his sake'" misdescribes the line (χάριν is the object of φέρεις) | example quotes τοῦ δὴ νῦν … φέρεις χάριν |
| ἄντα (broaden added) | low | old entry says "following its noun"; 477 ἄντα Ποσειδάωνος precedes it | broadened |
| παράκοιτις (broaden added) | low | old entry says "predicate"; 479 it is the subject in apposition | broadened |

## Doubtful points resolved

- κύον ἀδεές (481). The shipped Iliad row (iliad-050, 8.423) fixes `l` "dog, fearless one" and `i` "you fearless one"; the shipped Odyssey (odyssey-092, 19.91) has "unafraid dog" / "you unafraid dog". The Iliad follows its own row, so `l` stays and `i` becomes "you dog, you fearless one". The new-renderings row now says this. The note already carries the vocative-or-adverb doubt.
- ὕπερθε (453–454, "above"). Kept: the Greek does not say what is above what, and every shipped treatment (13.61, 17.541) keeps the word and says so in the note. Any English that decides ("over our heads", "from above", "all over") would be a guess. The note already says it is unclear. Left as drafted.

## Findings considered and refused

- 423 `l` "rushing upon her": ἐπιεισαμένη has no object in the Greek, but `l` needs one in English and the note already says the object is unstated and τῆς in the next line supplies it.
- 456 `l` "with a resentful heart" against `i` "hearts": θυμῷ is singular and distributive; the plural is the natural English for "we two" and is recorded in new-renderings.
- 435–437 ἀρξάντων ἑτέρων "now that others have begun": the standing reading; the other possible reading (a condition) is weaker against ἔοικεν. Kept.
- 441 `ὡς` exclamatory "how": the known entry's headline "as, how, that" covers it; no broadening needed.
- Scansion: packet flags none; nothing hand-scanned.
- Sole-source: no modern translation consulted.

## Left open

Nothing blocking. The table itself uses "stronger" for both φέρτερος and κρείσσων (and "mightier" is given as the φέρτερος rendering in one old row, 16.688); this part follows the shipped uses.
