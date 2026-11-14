#!/usr/bin/env python3
"""Reviewer's edits to aeneid-071 units.json (pass 1 and pass 2). Each edit: (unit index, field, old, new);
old must occur exactly once in that field. Only l, i, n are touched. Run once."""
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..')))
import aeneid_lib as A
p = os.path.join(HERE, 'units.json'); D = A.jload(p); U = D['sentences']
E = [
 # M-1 731-733: the subject is not Turnus throughout (lux effulsit, arma sonuere, cristae tremunt)
 (4, 'n', "The subject is Turnus throughout. 'Continuo'",
          "Everything here is Turnus's, his eyes, his armour, his crest, though only 'mittit' has him as its subject. 'Continuo'"),
 (4, 'n', "'oculis', 'from his eyes', ablative of separation.", "'oculis', 'from his eyes'."),
 # L 739: elision list incomplete
 (8, 'n', "Elision 'Castr(a) inimica'.", "Elisions 'Castr(a) inimica', 'null(a) hinc'."),
 # L 743-744: ablative with an adjective, not of description
 (13, 'n', "ablatives of description with 'rudem'.", "ablatives with the adjective 'rudem', 'rough with'."),
 # L 748b: 'is' = such a man, not 'this man'
 (17, 'l', "for not is this man of weapon or wound the author.”", "for not such is of weapon or of wound the author.”"),
 # L 760: ardentem is the object; misquoted connective
 (23, 'l', "but fury, blazing, and of slaughter mad desire\ndrove him at those facing him.",
           "but fury the blazing man, and of slaughter mad desire,\ndrove against those facing him."),
 (23, 'n', "'furor… et… insana cupido'", "'furor… caedisque insana cupido'"),
 # L 765-767: Noemona's syllables and the lengthened -que (scan-fixes 9.767)
 (26, 'n', "'deinde', two syllables.", "'deinde', two syllables; 'Noemona' four, No-e-mo-na, and the '-que' before 'Prytanim' is long, as Homer's 'te' is before 'Prytanin'."),
 # L 768-770a: dexter hedged
 (27, 'n', "'dexter', 'on the right', an adjective doing the work of an adverb.",
           "'dexter', probably 'on the right' (some take it 'with his right hand'), an adjective doing the work of an adverb."),
 # L 792b-796: i rephrased (repetition crowd/crowds; distance from known versions)
 (39, 'i', "As when a crowd of men with hostile weapons crowds in upon a savage lion, and he, alarmed but still fierce and glaring grimly, gives back step by step; his anger and his courage will not let him turn tail, and for all his wish he cannot charge them through the weapons and the men:",
           "As when a throng of men bears hard with hostile weapons on a savage lion, and he, shaken yet still fierce, with a baleful glare, gives ground slowly; anger and courage forbid him to turn tail, yet, much as he longs to, he cannot drive at them through the spears and the men:"),
 (39, 'n', "'Ceu', 'as when'.", "'Ceu… cum', 'as when'."),
 # L 799-800: first 'bis' is not at the head of its clause
 (41, 'n', "'bis… bis', 'twice… twice', repeated at the head of each clause.", "'bis… bis', 'twice… twice', one in each clause."),
 # L 816b-818: i rephrased away from the well-known versions' wording
 (50, 'i', "the river took him as he came on its yellow flood, lifted him up on gentle waves, and returned him, washed clean of the slaughter, rejoicing to his comrades.",
           "the river, with its yellow flood, received him as he came, held him up on gentle waves, and sent him back glad to his comrades, the slaughter rinsed away."),
 (50, 'n', "in Book VIII the same river had welcomed Aeneas as his friend (8.62–64).",
           "in Book VIII the river god had shown himself to Aeneas as his helper (8.62–64)."),
]
E2 = [  # pass 2
]
for k, f, old, new in E + E2:
    s = U[k][f]; c = s.count(old)
    assert c == 1, (k, f, c, old)
    U[k][f] = s.replace(old, new)
A.jdump(D, p)
print('applied', len(E) + len(E2), 'edits')
