""" 
Digital Image Filtration program
Written by: Brandon Engholm
Class: CST 205
Purpose: to combine images into one image, removing unwanted stuff.
"""

import PIL
from PIL import Image
import glob

def findMedian( k ):
    median = 0
    sort = 0
    sort = sorted(k)
    median = (int)((len(k)-1)/2) + 1
    if ( len(sort) <= 1 ):
        return sort[0]
    return sort[median]

finalImage = Image.open('finalImage\\fwImage.png');
newImage=finalImage.load()
width, height = finalImage.size

image_list = [] #array of images

for filename in glob.glob('sampleImages\*.png'):
    im=Image.open(filename)
    px=im.load()
    image_list.append(px)

#may not actually be neccesary
#if (width > height):
 #   temp = height
  #  height = width
   # width = temp

r = []
g = []
b = []
red = green = blue = 0
progress = 0

for y in range(0,height):
    for x in range(0,width):
        for anImage in image_list:
            pixel = anImage[x,y]
            if (type(pixel) is tuple):
                if (len(pixel) > 3):
                    red, green, blue, alpha = pixel
                else:
                    red, green, blue = pixel
            if (type(pixel) is int):
                red = green = blue = pixel
            r.append(red)
            g.append(green)
            b.append(blue)
        newImage[x,y] = (findMedian(r), findMedian(g), findMedian(b));
        del r[:],g[:],b[:]
        red = green = blue = 0;    
    progress = (int)(100 / height * y)
    if ( progress % 5 == 0 ):
        print ('Job: ', progress, '% complete'); 
        
finalImage.save('finalImage\\finalImage.png')
print ("I'm done!");
