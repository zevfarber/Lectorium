# Run lead's corrections to the Sonnet glosser's gloss.json (aeneid-090); see gloss-corrections.md.
import json
p='gloss.json'; g=json.load(open(p,encoding='utf-8'))
g['obustis']='obūrō, -ere, -ussī, -ustum — to burn round, char at the end, fire-harden (perf. pass. part., f. abl. pl., with sudibus)'
g['quadrupedumque']='quadrupēs, -pedis (m./f.) — four-footed; as noun, horse, steed (gen. pl.) + -que, and'
g['hibero']='Hibērus, -a, -um — Iberian, Spanish, of the far west (m. abl. sg.)'
g['laurentiaque']='Laurentius, -a, -um — of Laurentum, Laurentine (n. nom./acc. pl.) + -que, and'
b=g['__broaden__']; old=b['opis'].split(' · ')[0]
b['opis']=old+' · also Ōpis, -is (f.) — Opis, a nymph of Diana, sent to guard and avenge Camilla (nom. sg.)'
for k,v in g.items():
    if k!='__broaden__': assert len(v)<230,k
for k,v in b.items(): assert len(v)<230,k
json.dump(g,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=1); open(p,'a').write('\n')
