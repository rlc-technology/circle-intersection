import png
import random

pageWidth=15360
pageHeight=8640

logoWidth=int(pageWidth/12)
logoHeight=int(pageHeight/18)

r=png.Reader(filename='a.png')
w, h, p, metadata = r.read_flat()

if w!=logoWidth or h!=logoHeight:
    exit()

pixels=[0]*pageWidth*pageHeight

for y in range(logoHeight):
 for x in range(logoWidth):
  t=1
  colorIndex=p[y*logoWidth+x]
  for j in range(18):
   for i in range(12):
    t+=1
    pixels[(j*logoHeight+y)*pageWidth+i*logoWidth+x]=colorIndex
    if colorIndex>1:
     pixels[(j*logoHeight+y)*pageWidth+i*logoWidth+x]=t

palette=[(0,0,0)]*256

t=1
for r in range(6):
 for g in range(6):
  for b in range(6):
   t+=1
   palette[t]=(r*51,g*51,b*51)

t=0
for r in range(6):
 for g in range(6):
  for b in range(6):
   f = open('{:03d}'.format(t)+'.png', 'wb')
   palette[1]=(r*51,g*51,b*51)
   wr = png.Writer(pageWidth, pageHeight, palette=palette, bitdepth=8)
   wr.write_array(f, pixels)
   f.close()
   t+=1
