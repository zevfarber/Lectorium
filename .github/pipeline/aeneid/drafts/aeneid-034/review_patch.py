#!/usr/bin/env python3
"""Reviewer's patch for aeneid-034 (pass 1 and 2). Edits l / i / n of units.json by exact-substring replacement; never touches t.
Run after make_units.py (which regenerates units.json from draft.py)."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(HERE, 'units.json')
D = json.load(open(P, encoding='utf8')); S = D['sentences']; log = []
def rep(idx, field, old, new):
    s = S[idx][field]
    if s.count(old) != 1: sys.exit(f'unit {idx} {field}: {old[:50]!r} occurs {s.count(old)} times')
    S[idx][field] = s.replace(old, new); log.append((idx, field))
T0 = [u['t'] for u in S]
# U0 (286-289)
rep(0,'l',"To this, pious Aeneas","After this, pious Aeneas")
rep(0,'n',"'Hoc' looks back to the end of the race: 'after this'.","'Hoc' looks back to the end of the race: 'after this', 'hereupon' (an adverbial use; whether it is an ablative or an accusative of time is not settled).")
rep(0,'n',"'collibus… curvis' is an ablative of place for the curving hills on which the woods stand.","'collibus… curvis' is most simply an ablative of place, 'on the curving hills' where the woods stand (some take it as means, 'with hills').")
# U1 (289-290)
rep(1,'l',"to where with many thousands the hero himself\nto the middle of the gathering carried himself, and on the built-up seat sat down.","to where himself with many thousands the hero\nin the gathering, in the middle, carried, and on the built-up seat sat down.")
rep(1,'n',"'medium' agrees with the subject, 'heros', 'in the middle of the crowd'.","'medium' is accusative and agrees with 'se', 'himself (as the one) in the middle'; it cannot agree with the subject 'heros', which would be 'medius'.")
# U2 (291-292)
rep(2,'l',"Here, those who by chance may wish to contend in swift running,\nhe invites with prizes in spirit, and rewards sets out.","Here, such as by chance may wish to contend in swift running,\nhe invites with prizes the spirits, and rewards sets out.")
rep(2,'i',"Here he calls on any who may care to race in a swift run, tempting their hearts with prizes, and he sets the awards out where all can see.","Here he calls on whoever may care to race in a swift run, tempting their hearts with prizes, and sets out the awards.")
rep(2,'n',"in the sense 'any who may wish'; its antecedent ('eos', 'those') is left out and 'animos' stands for the persons whose spirits he invites.","'such as may wish', placed ahead of its antecedent, 'animos', so that the sentence reads 'he invites with prizes the spirits (that) may by chance wish…'; 'animos' stands for the men whose spirits they are.")
# U3 (293-296)
rep(3,'n',"'Nisus amore pio' repeats 'insignis' by zeugma, 'Nisus (marked out) by loyal love',","In 'Nisus amore pio' 'insignis' is understood from the line before, 'Nisus (marked out) by loyal love',")
# U4
rep(4,'n',"and 'de stirpe Priami' 'from the stock of Priam' with 'egregia' put between to frame the line.","'egregia… de stirpe' is 'from outstanding stock', with 'Priami' tucked inside it, so that the adjective and its noun frame the genitive.")
# U5
rep(5,'n',"'Simul et' joins the two names, 'both together'.","'Simul' is 'together', and 'et' joins the two names.")
rep(5,'n',"'Acarnan' is a Greek nominative ('Acarnas'), a man from Acarnania","'Acarnan' is a Greek nominative, 'an Acarnanian', a man from Acarnania")
# U8
rep(8,'i',"In the midst of these Aeneas then spoke, and spoke thus:","In the midst of these Aeneas then spoke in these words:")
# U11
rep(11,'n',"'Gnosia' is 'of Cnossus', and so 'Cretan' (the Latin Library prints 'Cnosia'); the Cretans were famous archers and iron-workers.","'Gnosia' is 'of Cnossus', and so 'Cretan'; the Cretans were famous archers, and 'spicula' (sharp points) may be arrow-heads or dart-heads as well as spear-points.")
rep(11,'n',"'Levato ferro' is an ablative of quality, with 'levato' from 'levo', 'make smooth', here 'polished', not 'lifted'.","'Levato ferro' is an ablative going with 'lucida' ('bright with polished iron'), with 'levato' from 'levo', 'make smooth', here 'polished' (the usual reading), not 'lifted'.")
rep(11,'i',"two bright Cretan spearheads with burnished iron","two Cretan spear-points, bright with burnished iron")
# U12
rep(12,'i',"This is the single honour for all.","This shall be the one honour for all.")
# U15
rep(15,'l',"an Amazonian quiver and one full of arrows","an Amazonian quiver and full of arrows")
rep(15,'n',"'Plenamque' ('que' joins 'pharetram' and 'plenam') is 'and full'.","'Plenamque' is 'and full': 'que' joins the two adjectives 'Amazoniam' and 'plenam', both agreeing with 'pharetram'.")
rep(15,'n',"is spelled with a diaeresis to show it has three syllables.","is spelled with a diaeresis to show that the e and the i are sounded separately (Thre-i-ci-is, four syllables).")
# U16
rep(16,'n',"'Hac' points at the helmet: Aeneas is holding it up.","'Hac' points at the helmet, so Aeneas is evidently showing it.")
# U17
rep(17,'l',"together the farthest marks they eye.","together the farthest points they mark.")
rep(17,'i',"streaming out like a rain-cloud","pouring forth like a rain-cloud let loose")
rep(17,'n',"The scene is closely built on the foot race of Iliad XXIII, where the runners also 'pour' away from the line.","The scene is modelled on the foot race in the funeral games of Iliad XXIII.")
# U18
rep(18,'n',"held back to the end of the second line;","held back to the end of the line;")
rep(18,'i',"swifter than the winds and than the wings of the lightning;","outstripping the winds, quicker than lightning on the wing;")
# U19
rep(19,'n',"next, yes, but only just in order.","next in order, yes, but far behind.")
# U22
rep(22,'n',"usually read as a dative: Diores is pressing on Helymus's shoulder.","usually read as a dative: Diores is pressing on Helymus's shoulder (some take 'umero' as an ablative, 'with his shoulder').")
rep(22,'n',"'Ambiguum' is a neuter noun, 'a doubtful matter', and 'ambiguumque' perhaps means 'or at least'.","'Ambiguum' is a neuter adjective used as a noun, 'what is undecided', so 'relinquat' is 'might leave it open'; the 'que' joins the two verbs, but the sense is nearly 'or' ('pass him, or at least leave it in doubt'; the English version reads it so, and the Latin does not say 'at least').")
# U23
rep(23,'l',"end they were approaching, when on slippery blood Nisus","end they were approaching, with slippery blood Nisus")
rep(23,'i',"had been spilled when the bullocks were slaughtered and had soaked the ground and the green grass above it.","had been poured on the ground when the bullocks were slaughtered, and had soaked the green grass over it.")
rep(23,'n',"'Cum… labitur' is the 'inverse cum', with the main action in the cum-clause. 'Levi… sanguine' is an ablative of means with 'labitur' ('glides', 'slips'); 'levis' is 'smooth', 'slippery'.","'Levi cum sanguine' is 'on (literally with) the slippery blood': 'cum' is a preposition, set after its adjective, and there is no 'when' in the Latin, only the imperfect 'adventabant' followed by the vivid present 'labitur' ('glides', 'slips'); 'levis' is 'smooth', 'slippery'.")
rep(23,'n',"(the blood spilled when the bullocks were slain, an ablative absolute); 'humum' is an accusative of the place over which; 'viridisque super herbas' puts the preposition after its noun ('-is' is Greenough's accusative plural), and","(the blood spilled when the bullocks were slain; 'caesis iuvencis' is an ablative absolute); 'humum' is an accusative of the place to which, 'poured on the ground'; 'super' is an adverb, 'on top' (or a preposition cut off from 'herbas' by the verb), so 'viridisque super… herbas' is 'and the green grass above' ('-is' is Greenough's accusative plural), and")
# U24
rep(24,'l',"but headlong in the very\nfilth fell, and the unclean dung and the sacred blood.","but headlong in the very\nfell, in unclean dung and in sacred blood.")
rep(24,'n',"'In ipso immundoque fimo sacroque cruore' is 'in the very foul dung and sacred blood' (the double 'que… que', and 'ipso' agrees with 'fimo');","'In ipso… immundoque fimo sacroque cruore' is 'in the very (place): in the unclean dung and the sacred blood'; 'ipso' is most simply taken with 'fimo' ('in the very dung'), with 'immundo… sacro' joined by 'que… que', but the grammar is loose and editors differ on what 'ipso' agrees with;")
# U30
rep(30,'i',"fills the whole vast bank of seats with his shouting","fills the whole assembly of the vast theatre with his shouting")
# U31
rep(31,'i',"and a courage all the more welcome for coming in a form so fair.","and a courage that pleases the more because it comes in a handsome body.")
# U35
rep(35,'n',"'Fatus' is the perfect participle of the deponent 'for', 'speak', with 'est' omitted.","'Fatus' is the perfect participle of the deponent 'for', 'speak': 'sic fatus' is 'having so spoken' (no verb is left out).")
rep(35,'i',"heavy with its shaggy mane","heavy with its shaggy hair")
# U36
rep(36,'i',"who earned the first crown by his running","who earned the first crown by his merit")
rep(36,'n',"There is an irony here: it was Nisus himself who sent Salius sprawling.","There is dark humour here: it was Nisus himself who sent Salius sprawling, though he now speaks of hostile fortune as what felled them both.")
# U37
rep(37,'l',"his face he displayed and with wet\nfoul limbs with dung.","his face he displayed and wet\nfoul limbs with dung.")
# U38
rep(38,'i',"which the Danaans had torn from the sacred doorpost of Neptune;","which the Danaans had taken down from the sacred doorpost of Neptune;")
# U41
rep(41,'n'," Greenough spells 'brachia'; the Latin Library 'bracchia'.","")
# U51
rep(51,'n',"Greenough prints the closing mark one space late,","The text as printed has the closing mark one space late,")
rep(51,'n',"which is a misprint of its position","which is a misplacement")
assert [u['t'] for u in S] == T0
json.dump(D, open(P, 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print(len(log), 'edits applied; t untouched')
