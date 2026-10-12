import json,re
seq=json.load(open('prov.json'))
P={p['pn']:p for p in json.load(open('P.json'))}
def clean(s):
    le=s['le']; ws=[]
    for x0,x1,w in s['words']:
        if x1<=le-6: continue          # margin label word
        if x0<le-14 and x1>le:          # label glued to first word
            n=round((le-x0)/max(1,(x1-x0))*len(w)); w=w[n:]
            w=re.sub(r'^[\d\W_]+(?=[^\W\d_]|["”“’\'])','',w) if re.match(r'^[\d»«•*>.,;:\-]',w) else w
        if not ws and x0<le-10 and (re.search(r'\d',w) or not re.search(r'[A-Za-záéíóúñÁÉÍÓÚÑ]{2,}',w)) and not re.match(r'^["”“\'’]?[aeoyiAEOYI]$',w):
            continue
        ws.append(w)
    t=' '.join(ws)
    t=re.sub(r'\s+',' ',t).strip()
    return t
lines=[]; tir=1
for s in seq:
    if s['k']=='T': tir=s['tir']; continue
    lines.append({'tir':tir,'num':s['num'],'pn':s['pn'],'t':clean(s),'ital':s.get('ital',False),'over':s.get('over',False),'idx':s['idx']})
json.dump(lines,open('lines.json','w'),ensure_ascii=False)
