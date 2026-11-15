#!/usr/bin/env python3
"""Reviewer's edits to aeneid-081 units.json (pass 1). Each edit: (unit index, field, old, new); old must occur
exactly once in that field. Only l, i, n are touched; t, ln, p, v and the top-level fields never. Run once
(it refuses if the file has already been edited: the first old string must still be present)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..')))
import aeneid_lib as A
p = os.path.join(HERE, 'units.json'); D = A.jload(p); U = D['sentences']
before = [(u['t'], u['ln'], u.get('p'), u.get('v')) for u in U]
top = {k: D[k] for k in ('title', 'titleEn', 'part', 'about')}

def PRINT(a, b):
    return (f"The print has '{a} ”{b}', the closing speech mark joined to the next word, a misprint for "
            f"'{a}” {b}', corrected here: the speech ends with '{a[:-1]}'. ")
def CLOSE(who):
    return f"The closing speech mark printed at the head of this unit belongs to {who} speech (see the note before)."

E = [
 # ---- rule-5b placement, made the same as 077, 078 and 080: the print's reading opens the note of the unit
 #      where the speech closes; the next unit (whose t begins with the stray mark) points back to it.
 (8, 'n', "'moriture',", PRINT('tua.', 'Nec') + "'moriture',"),
 (8, 'n', " The closing speech mark is printed joined to the next word; see the next unit.", ""),
 (9, 'n', "The print has 'tua. ”Nec', with the closing speech mark joined to the next word, a misprint for 'tua.” Nec', corrected here: the speech ends with 'tua'.", CLOSE("Aeneas's")),
 (16, 'n', "'Hoc', explained", PRINT('cadis.', 'Increpat') + "'Hoc', explained"),
 (16, 'n', " On the closing speech mark, see the next unit.", ""),
 (17, 'n', "The print has 'cadis. ”Increpat', with the closing speech mark joined to the next word, a misprint for 'cadis.” Increpat', corrected here: the speech ends with 'cadis'.", CLOSE("Aeneas's")),
 (32, 'n', "'Sed linquam', 'but", PRINT('linquam.', 'Simul') + "'Sed linquam', 'but"),
 (32, 'n', " On the closing speech mark, see the next unit.", ""),
 (33, 'n', "The print has 'linquam. ”Simul', with the closing speech mark joined to the next word, a misprint for 'linquam.” Simul', corrected here: the speech ends with 'linquam'.", CLOSE("Mezentius's")),
 (49, 'n', "'Desine', 'stop'", PRINT('prius.', 'Dixit') + "'Desine', 'stop'"),
 (49, 'n', " On the closing speech mark, see the next unit.", ""),
 (50, 'n', "The print has 'prius. ”Dixit', with the closing speech mark joined to the next word, a misprint for 'prius.” Dixit', corrected here: the speech ends with 'prius'.", CLOSE("Mezentius's")),
 (56, 'n', "'Advolat', 'flies to'", PRINT('animi?', 'Contra') + "'Advolat', 'flies to'"),
 (56, 'n', " On the closing speech mark, see the next unit.", ""),
 (57, 'n', "The print has 'animi? ”Contra', with the closing speech mark joined to the next word, a misprint for 'animi?” Contra', corrected here: the speech ends with 'animi'.", CLOSE("Aeneas's")),

 # ---- elision lists (medium)
 (2, 'n', "'iamqu(e) adsurgentis', 'Aenea(e) subiit', 'mucron(em) ipsumque'.", "'iamqu(e) adsurgentis', 'mucron(em) ipsumque'."),
 (5, 'n', "Elisions 'agricol(a) et', 'arc(e) viator'.", "Elision 'agricol(a) et'; 'arce viator' does not elide, since v is a consonant."),

 # ---- false labels / claims (medium)
 (24, 'n', "'corpore inhaeret', 'clings to the body', dative with the compound.", "'corpore inhaeret', 'clings to the body', 'corpore' ablative ('inhaereo' takes the dative or the ablative)."),
 (11, 'n', "The word order sets 'Aeneas' at the head of the line beside 'iuvenem', the grown warrior and the boy.", "The word order sets 'Aeneas' inside the phrase 'per medium… iuvenem', the grown warrior and the boy locked together."),

 # ---- hypermetric 895 (scansion finding M3; the notes now say so)
 (55, 'n', "Both armies see that the fight is decided. Elision 'Clamor(e) incendunt'.",
           "Both armies see that the fight is decided. The line is hypermetric: the final '-que' of 'Latinique' is elided into 'Advolat', the first word of the next line (as at 781). Elisions 'Clamor(e) incendunt', 'Latiniqu(e) Advolat' (across the line-end)."),
 (56, 'n', "Elision 'vaginaqu(e) eripit'.", "Elision 'vaginaqu(e) eripit'; 'Advolat' also takes in the elided '-que' of 895."),

 # ---- low: labels, wording, attributions
 (2, 'n', "Aeneas rising on his toes to bring down a blow.", "Aeneas rising up to bring down a blow."),
 (5, 'n', "the repeated 'omnis' (anaphora) emptying the fields.", "the repeated 'omnis' (anaphora) emptying the fields; 'diffugit' is perfect (the metre needs a long u), of what always happens."),
 (14, 'n', "Aeneas speaks to the dead boy.", "Aeneas speaks to the dying boy."),
 (16, 'n', "'infelix', 'unlucky one', in effect a vocative.", "'infelix', 'unlucky one', nominative with the 'you' of 'solabere', where English would use a vocative."),
 (19, 'n', "adjective and noun spread across the line.", "adjective and noun split across the line-end."),
 (24, 'n', "'both palms', framing the line-end,", "'both palms', split across the line-end,"),
 (39, 'n', "'sharp javelins', framing the second half of the line.", "'sharp javelins', enclosing the verb."),
 (21, 'n', "'multumque remittit / qui revocent', 'and sends many (messengers) to call him back', a relative clause of purpose with the subjunctive; 'multum' for 'multos' is unusual, and some take it as an adverb, 'again and again'.",
           "'multumque remittit / qui revocent', 'and again and again sends (men) to call him back', 'multum' an adverb, 'much, often', with the antecedent of 'qui' left out; 'qui revocent' is a relative clause of purpose with the subjunctive. Some take 'multum' loosely for 'multos', 'many (messengers)'."),
 (21, 'l', "Many things about Lausus he keeps asking, and many he sends\nwho should call him back", "Many things about Lausus he keeps asking, and often he sends\nmen who should call him back"),
 (21, 'i', "and sent man after man to call him back", "and sent messengers time after time to call him back"),
 (27, 'n', "Many editors read 'exilium'", "Some editors read 'exilium'"),
 (53, 'n', "strikes one of Nestor's horses in the head and brings his chariot down (Iliad 8.81–86).", "strikes one of Nestor's horses in the head, and its plunging throws the team into confusion (Iliad 8.81–86)."),
 (17, 'i', "Then he went further and called on the boy's hesitating comrades, and himself raised Lausus", "Then, unprompted, he rebuked the boy's comrades for hanging back, and himself raised Lausus"),

 # ---- echo recasts in i (low)
 (8, 'i', "“Where are you running to your death, daring more than your strength can carry? Your love for your father is blinding you to the danger.”",
          "“Doomed boy, where are you rushing, attempting what is beyond your strength? Your devotion deceives you, and you are off your guard.”"),
 (12, 'i', "then his life withdrew sorrowing through the air to the shades and left the body behind.",
           "then his life, grieving, slipped away through the air to the shades and forsook the body."),
 (13, 'i', "But when the son of Anchises saw the look on the dying boy's face, that face growing pale in ways so strange, he groaned deeply in pity and stretched out his hand, as the picture of his own love for his father came into his mind.",
           "But when Anchises' son saw the dying boy's features, those features turning so strangely and wonderfully pale, he groaned deeply in pity and held out his hand, and there rose in his mind the image of his own devotion to his father."),
 (14, 'i', "“What can dutiful Aeneas give you now, poor boy, for such glorious deeds — what gift worthy of so noble a spirit?",
           "“Pitiable boy, what can Aeneas the dutiful offer you now for glory like yours? What gift is worthy of so great a heart?"),
 (15, 'i', "Keep the arms you took such pride in, for they are yours; and I give you back to the shades and ashes of your fathers, if that is any concern to the dead.",
           "The armour that was your delight, keep it; it is yours. And you yourself I return to the shades and the ashes of your fathers, if such things are any care to the dead."),
 (31, 'i', "As it is, I am alive, and still I do not leave mankind and the light of day.",
           "And here I am, alive, not yet gone from mankind and the daylight."),
 (32, 'i', "But I shall leave them.”", "But go I will.”"),
 (36, 'i', "“Rhaebus, we have lived a long time, if anything at all can be called long for mortal creatures.",
           "“Rhaebus, our life has been a long one, if any mortal thing can be said to last long."),
 (47, 'i', "This was the only way by which you could destroy me.", "There was one road only to my ruin, and you have taken it."),
 (48, 'i', "I have no dread of death, and I spare none of the gods.", "Death does not frighten me, and there is no god I spare."),
 (59, 'i', "There is no wrong in killing; I did not come to battle on such terms, nor did my Lausus make any such bargain with you for me.",
           "Killing is no sin. I did not come to the fight on terms like these, and my Lausus struck no such bargain with you on my behalf."),
 (60, 'i', "This one thing I beg of you, by whatever mercy is left for beaten enemies: let my body be covered with earth.",
           "I make one plea, by whatever grace a beaten enemy may still claim: allow my body to be laid under the earth."),
 (61, 'i', "I know that my own people's bitter hatred is all around me: shield me, I beg you, from their fury, and let me share my son's tomb.”",
           "I know how bitterly my own people hate me and how close that hatred stands: protect me, I beg you, from their fury, and grant that I may lie with my son, his companion in the grave.”"),
 (62, 'i', "So he spoke, and took the sword in his throat, knowing well what he did, and poured out his life over the fields in a stream of blood.",
           "So he spoke, and, knowing what he did, took the sword into his throat; his life went streaming out over the fields with the welling blood."),
]

for k, f, old, new in E:
    s = U[k][f]
    assert s.count(old) == 1, (k, f, old[:60], s.count(old))
    U[k][f] = s.replace(old, new)

# guards
assert [(u['t'], u['ln'], u.get('p'), u.get('v')) for u in U] == before
assert {k: D[k] for k in ('title', 'titleEn', 'part', 'about')} == top
for k, u in enumerate(U):
    assert u['l'].count('\n') == u['t'].count('\n'), k
    assert '\n' not in u['i'], k
    n = len(u['n'].split()); assert 15 <= n <= 139, (k, n)
for lay in ('l', 'i'):
    o = sum(u[lay].count('“') for u in U); c = sum(u[lay].count('”') for u in U)
    assert o == c == 8, (lay, o, c)
A.jdump(D, p)
print('applied', len(E), 'edits')
