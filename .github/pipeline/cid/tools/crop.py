import pymupdf,sys
d=pymupdf.open('/home/claude/lectorium/.github/pipeline/cid/source/raw/pidal1923_text.pdf')
pn=int(sys.argv[1]); y0=float(sys.argv[2]); y1=float(sys.argv[3]); z=float(sys.argv[4]) if len(sys.argv)>4 else 1.3
x0=float(sys.argv[5]) if len(sys.argv)>5 else 100; x1=float(sys.argv[6]) if len(sys.argv)>6 else 1080
p=d[pn-1]; pix=p.get_pixmap(matrix=pymupdf.Matrix(z,z),clip=pymupdf.Rect(x0,y0,x1,y1)); pix.save(f'c{pn}_{int(y0)}.png'); print(f'c{pn}_{int(y0)}.png')
