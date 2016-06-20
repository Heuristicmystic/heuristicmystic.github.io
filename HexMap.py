# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 08:50:31 2016

@author: ian.weinstock
"""
from __future__ import print_function
from PIL import Image


img_file = "C:\\Users\\ian.weinstock\\Pictures\\megaman4.png"
img = Image.open(img_file)
rgb_img = img.convert("RGB")
width, height = img.size
pix = img.getcolors() # list of tuples (count of color, color number)
x = 0
y = 0
line0 = [] #this will contain the hex color number of the first line of the image
picture = []

row = 0
while y < height:
    x = 0    
    while x < width:
        r,g,b = rgb_img.getpixel((x,y))
        hexno = "#%02X%02X%02X" % (r,g,b)
        if x == 0:
            print(y,",",hexno,",",sep='',end="")
            x +=1
        elif x == width-1:
            print(hexno,)
            x += 1
        else:
            print(hexno,",",end="",sep="")
            x += 1
    picture.append(line0)
    y += 1  
