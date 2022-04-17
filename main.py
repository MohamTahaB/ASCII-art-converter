import os

from PIL import Image

liste = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`\'. ")

print("type the  path of the image : ")
aux = str(input())
im = Image.open(aux)
maxx, maxy = im.width , im.height

im_rgb = im.convert("RGB")
for i in range(maxy):
    for j in range(maxx):
        aux = im_rgb.getpixel((j, i))
        print(liste[(aux[0] + aux[1] + aux[2])//11] , end='')
    print("")
