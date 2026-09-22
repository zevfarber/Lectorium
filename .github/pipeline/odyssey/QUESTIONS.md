# Odyssey pipeline — open questions

## 1.47 ὡς (raised at the pilot, 2026-09-20)
The archive prints unaccented ὡς with the optative of wish ἀπόλοιτο. The text is left as printed and the
note says how it is taken. Worth one look at the printed Loeb page; no second witness is wired.

## τῷ's "therefore" sense cannot be added within the 230-character glossary cap (raised at odyssey-003, 2026-09-22)
At 1.239 τῷ is used inferentially ("in that case, therefore"), a sense the shipped glossary entry for τῷ
does not carry (it covers the pronoun, the relative, and the instrumental relative). The shipped entry is
already 227 characters, and conventions.md's rules — every entry under 230 characters, broadenings are
additions-only and must never shorten the existing text — leave no room to append even the shortest honest
addition. Decided meanwhile: left unbroadened. The unit's own note at 1.239 states the sense correctly, so
a reader is not misled, only unaided by the glossary entry itself. Closing this needs an owner decision:
either raise the per-entry cap for heavily-used forms, or permit compacting an old entry's wording (which
the current rule forbids, to keep old readings intact). `build_odyssey.py` does not enforce the 230-char
cap on broadenings (only on new entries), so a fix could technically pass the gate; the pipeline chose not
to rely on that gap.

## 1.277 ἔεδνα / οἱ δέ: whose people prepare the gifts, stated without a hedge (raised at odyssey-003, 2026-09-22)
"οἱ δὲ γάμον τεύξουσι καὶ ἀρτυνέουσιν ἔεδνα" (1.277) is rendered with οἱ δέ taken as Penelope's father's
household preparing the wedding-gifts — the majority reading — while ἔεδνα itself is glossed neutrally
("wedding-gifts") because the word's usual lexicon sense (a suitor's gifts to a bride's family) sits
awkwardly with its use here. Some commentators take οἱ δέ as the suitors instead. The reviewer judged a
second caveat in an already-double-hedged note would overload it, and left the unit committed to the
majority reading without flagging the alternative in the note itself. Decided meanwhile: left as is;
flagged here in case a future part's cross-reference or the owner's own reading disagrees.
