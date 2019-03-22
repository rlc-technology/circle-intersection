import random
w=1920
h=1080
a = [0]*w*h
f = open('test.yuv', 'wb')
for i in range(180):
    b=random.randint(h/3,2*h/3)
    c=random.randint(h/3,w-h/3)
    d=random.randint(1,h/3)
    for x in range(h):
        for y in range(w):
            if (x-b)*(x-b)+(y-c)*(y-c)<d*d:
                a[x*w+y]+=5
            if a[x*w+y]>255:
                a[x*w+y]=255
            f.write(bytes([a[x*w+y]]))
    for x in range(h):
        for y in range(w):
            f.write(bytes([128,128]))

f.close()
