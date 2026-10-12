import json,sys
c=json.load(open('corr.json'))
for a in sys.argv[1:]:
    k,v=a.split('=',1); c[k]=v
json.dump(c,open('corr.json','w'),indent=0)
