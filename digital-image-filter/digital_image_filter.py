""" 
Digital Image Filtration program
Written by: Brandon Engholm
Class: CST 205
Purpose: to combine images into one image, removing unwanted stuff.
"""



import PIL
from PIL import Image
import glob
import statistics

image_list = [] #array of images
for filename in glob.glob('sampleImages\*.png'):
    im=Image.open(filename)
    width, height = im.size
    px=im.load()
    image_list.append(px)

#im = Image.open('sampleImages\one.png')
#px = im.load()
#image_list[1].show()
#print(len(image_list));

if (width > height):
    temp = height
    height = width
    width = temp

r = []
g = []
b = []
newImage = []
for y in range(0,height):
    for x in range(0,width):
        for anImage in image_list:
            red, green, blue = anImage[x,y]
            r.append(red)
            g.append(green)
            b.append(blue)
        statistics.median(r)
        

print ("I'm done!");