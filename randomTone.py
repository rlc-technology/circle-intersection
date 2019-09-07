import png
import random

r=png.Reader(filename='a.png')
w, h, pixels, metadata = r.read_flat()

t=0
for r1 in range(4):
 for g1 in range(4):
  for b1 in range(4):
   for r2 in range(4):
    for g2 in range(4):
     for b2 in range(4):
      f = open('{:04d}'.format(t)+'.png', 'wb')
      palette=[(0xff,0xff,0xff), (r1*85,g1*85,b1*85), (r2*85,g2*85,b2*85), (0x00,0x00,0x00)]
      wr = png.Writer(w, h, palette=palette, bitdepth=2)
      wr.write_array(f, pixels)
      f.close()
      t+=1
