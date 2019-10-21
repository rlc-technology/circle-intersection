import png
import random

pageWidth=10240
pageHeight=3840

logoWidth=int(pageWidth/8)
logoHeight=int(pageHeight/8)

r=png.Reader(filename='a.png')
w, h, p, metadata = r.read_flat()

if w!=logoWidth or h!=logoHeight:
    exit()

pixels=[0]*pageWidth*pageHeight

for y in range(logoHeight):
 for x in range(logoWidth):
  t=1
  colorIndex=p[y*logoWidth+x]
  for j in range(8):
   for i in range(8):
    t+=1
    pixels[(j*logoHeight+y)*pageWidth+i*logoWidth+x]=colorIndex
    if colorIndex>1:
     pixels[(j*logoHeight+y)*pageWidth+i*logoWidth+x]=t

palette=[(255,255,255)]*256

t=1
for r in range(4):
 for g in range(4):
  for b in range(4):
   t+=1
   palette[t]=(r*85,g*85,b*85)

t=0
for r in range(4):
 for g in range(4):
  for b in range(4):
   f = open('{:02d}'.format(t)+'.png', 'wb')
   palette[1]=(r*85,g*85,b*85)
   wr = png.Writer(pageWidth, pageHeight, palette=palette, bitdepth=8)
   wr.write_array(f, pixels)
   f.close()
   t+=1
