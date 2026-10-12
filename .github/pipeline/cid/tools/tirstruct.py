import json,re
seq=json.load(open('prov.json'))
P={p['pn']:p for p in json.load(open('P.json'))}
tir={}; cur=1
tir[1]={'n':1,'lines':[],'pages':set(),'prose':0,'tnum_page':126}
for s in seq:
    if s['k']=='T':
        cur=s['tir']; tir[cur]={'n':cur,'lines':[],'pages':{s['pn']},'prose':0,'tnum_page':s['pn']}
    else:
        t=tir[cur]; t['pages'].add(s['pn'])
        if s['num']=='PROSE': t['prose']+=1
        else: t['lines'].append(s['num'])
out=[]
for k in sorted(tir):
    t=tir[k]
    out.append({'tirada':k,'first':t['lines'][0],'last':t['lines'][-1],'count':len(t['lines']),'prose_bands':t['prose'],'pdf_pages':sorted(t['pages'])})
json.dump(out,open('tiradas.json','w'),indent=0)
for o in out: print(o['tirada'],o['first'],o['last'],o['count'],o['prose_bands'],o['pdf_pages'][0],o['pdf_pages'][-1])
print(sum(o['count'] for o in out))
