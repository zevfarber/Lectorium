import json,re
P=json.load(open('P.json'))
MAP=str.maketrans({'I':'1','l':'1','i':'1','|':'1','!':'1','O':'0','o':'0','S':'5','s':'5','$':'5','z':'2','Z':'2','B':'8','g':'9','q':'9','J':'1','t':'1','T':'7'})
def labtext(p,b):
    le=p['le']; out=[]
    for x0,x1,w in b['words']:
        if x0<le-12:
            if x1<=le+4: out.append(w)
            else:
                # merged: take leading non-letter-ish chars
                m=re.match(r"^[\d\W_IlioOSsz$]{1,5}",w)
                frac=(le-x0)/max(1,(x1-x0)); n=max(1,round(frac*len(w)))
                out.append(w[:n])
    return ''.join(out)
def parse(t):
    t2=t.translate(MAP)
    digs=re.sub(r'[^0-9b]','',t2)
    m=re.match(r'^(\d{1,4})(b?)',digs)
    return (int(m.group(1)),m.group(2)) if m else (None,'')
if __name__=='__main__':
    seq=[]
    for p in P:
        for b in p['bands']:
            if b['k'] in('verse','tnum','turn','center','rub'):
                seq.append((p,b))
    json.dump(None,open('/dev/null','w'))
    # walk
    n=0; rows=[]
    for p,b in seq:
        if b['k']!='verse': rows.append({'pn':p['pn'],'k':b['k'],'y':b['y0'],'t':' '.join(w[2] for w in b['words'])}); continue
        exp=n+1
        lt=labtext(p,b) if b['lab'] else None
        num,suf=parse(lt) if lt else (None,'')
        flag=''
        if b['lab']:
            if num is not None and (num==exp or (num%1000==exp%1000) or (num%100==exp%100 and abs(num-exp)<50)):
                pass
            elif num is not None:
                flag=f'LABEL {lt!r}->{num}{suf} exp {exp}'
            else:
                flag=f'LABEL? {lt!r} exp {exp}' if exp%5 else ''
            if exp%5 and not flag: flag=f'LABEL at non5 exp {exp} ({lt!r})'
        else:
            if exp%5==0: flag=f'NOLABEL exp {exp}'
        n=exp
        rows.append({'pn':p['pn'],'k':'verse','y':b['y0'],'n':exp,'lab':lt,'flag':flag,'t':' '.join(w[2] for w in b['words'])})
    json.dump(rows,open('rows.json','w'),ensure_ascii=False)
    fl=[r for r in rows if r.get('flag')]
    print(n,len(fl))
    for r in fl[:80]: print(r['pn'],r['y'],r['n'],r['flag'],'|',r['t'][:50])
    
