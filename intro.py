import math as m

xSize = 500
ySize = 500

header = "P3\n%d %d 255\n"%(xSize,ySize)
f = open("image.ppm",'w+')
f.write(header)

for i in range(xSize):
    line = ""
    for j in range(ySize):
        r = m.sin(i * j) % 256;
        g = r**2 % 256;
        b = g**2 % 256;
        line += "%d %d %d "%(r,g,b)
    f.write(line + "\n")

f.close()


