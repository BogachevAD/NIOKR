from scipy.ndimage import correlate
from PIL import Image
import cv2
import numpy

img1 = Image.open('DN_alfa1_0_alfa2_0_alfa3_0_n_0_a_0.bmp')

img2 = Image.open('DN_alfa1_0_alfa2_0_alfa3_0_n_0_a_0.bmp')

cor = correlate(img1, img2)
cor.tofile('output.txt', sep = ' ')

with open('output.txt') as f:
    s = f.read()

mylist = s.split()
mylist2 = list(map(int, mylist))

print(mylist2)