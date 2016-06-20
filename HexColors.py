# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 08:50:31 2016

@author: ian.weinstock
"""

from PIL import Image

img_file = "C:\\Users\\ian.weinstock\\Pictures\\megaman.gif"
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
    line0 = [y]
    while x < width:
        r,g,b = rgb_img.getpixel((x,y))
        hexno = "#%02X%02X%02X" % (r,g,b)
        line0.append(hexno)
        x += 1
    picture.append(line0)
    y += 1  


number_colors = []  #this should pull out only color numbers in one list
i = 0
while i < len(pix):
    number_colors.append(pix[i][1])
    i += 1
    
all_hexes = []
j = 0

while j < len(picture):   #this loop gives you all unique hex colors in the order they appear
    color_num = 1
    while color_num < x:
        if picture[j][color_num] not in all_hexes:
            all_hexes.append(picture[j][color_num])  
        color_num += 1
    j += 1
    
print zip(number_colors,all_hexes) # creates a list of tuples, matching color number to hex
