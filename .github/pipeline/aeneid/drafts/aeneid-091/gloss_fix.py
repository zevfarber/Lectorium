import json
p='gloss.json'; g=json.load(open(p,encoding='utf-8'))
g['flagrantis']="flagrāns, -antis — blazing, burning, aflame (pres. part. of flagrō as adj., m./f. acc. pl., = flagrantēs; also gen. sg.)"
g['orithyia']="Ōrīthyia, -ae (f.) — Orithyia, daughter of Erechtheus of Athens, carried off by Boreas (nom. sg., Greek name)"
g['adscire']="adsciō (asciō), -īre — to take to oneself, admit, adopt (as allies); akin to adscīscō (pres. inf.)"
json.dump(g,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
