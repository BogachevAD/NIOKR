from PIL import Image
import numpy

img1 = Image.open("DN_alfa1_5_alfa2_2_alfa3_7_n_0_a_9.bmp")
np_img1 = numpy.array(img1)
np_img1.tofile('array1.txt', sep = ' ')

with open('array1.txt') as f:
    s1 = f.read()
mylist1 = s1.split()
mylist11 = list(map(int, mylist1))

img2 = Image.open("DN_alfa1_5_alfa2_2_alfa3_7_n_0_a_9.bmp")
np_img2 = numpy.array(img2)
np_img2.tofile('array2.txt', sep = ' ')

with open('array2.txt') as f:
    s2 = f.read()
mylist2 = s2.split()
mylist22 = list(map(int, mylist2))

corr = numpy.correlate(mylist11, mylist22, )
corr2 = corr / (len(mylist11) * numpy.std(mylist11) * numpy.std(mylist22))
my_rounded_list = [round(elem, 3) for elem in corr2]
print(list(corr))
print(list(my_rounded_list))
#print(mylist11)
