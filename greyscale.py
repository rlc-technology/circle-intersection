import png
import random
t=17 #1,3,5,15,17,51,85
w=1920
h=1080
a = [0]*w*h
dur=False

for i in range(99999):
    if dur:
        break
    b=random.randint(h/3,2*h/3)
    c=random.randint(h/3,w-h/3)
    d=random.randint(1,h/3)
    for x in range(h):
        for y in range(w):
            if (x-b)*(x-b)+(y-c)*(y-c)<d*d:
                a[x*w+y]+=t
                if a[x*w+y]==255:
                    dur=True

f = open('test.png', 'wb')
w = png.Writer(w, h,greyscale=True)
w.write_array(f, a)
f.close()
