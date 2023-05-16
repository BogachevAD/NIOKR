from PIL import Image
import math
from PIL import ImageOps
import math

k = 20

#img1 = ImageOps.flip(Image.open(f"{k}.bmp"))

img1 = Image.open(f"{k}.bmp").rotate(180, expand=True)

img2 = Image.open(f"ver_1_num_pict_{k}.bmp")

img3 = Image.open(f"ver_2_num_pict_{k}.bmp")

img4 = Image.open(f"ver_3_num_pict_{k}.bmp")

img5 = Image.open(f"ver_4_num_pict_{k}.bmp")

img6 = Image.open(f"ver_5_num_pict_{k}.bmp")

a = [img1, img2, img3, img4, img5, img6]

def MSE(Image1, Image2):

    im1 = Image1.load()
    im2 = Image2.load()

    i = 0
    SUM = 0

    if (Image1.size == Image2.size):
        x1, y1 = Image1.size
        k = 1 / (x1 * y1)
        for x in range(0, x1):
            for y in range(0, y1):
                SUM = SUM + (im1[x, y] - im2[x, y]) ** 2
                if im1[x, y] != im2[x, y]:
                    i = i + 1
        print(f"Количество разных пикселей: {i}")
    else:
        print("Размер изображений не совпадают!")

    MSE = math.sqrt(k * SUM)

    return round(MSE, 5)

d = {}

for i in range(1, 6):
    d[f'img{i+1}'] = MSE(img1, a[i])
print(f'Коэффициенты корреляции для 5 тестовых изображений: {d}')

try:
    with open("out.txt", "a") as file:
        file.write(f'MSE{k}: {d}\n')
except:
    print(f"Ошибка")
finally:
    file.close()