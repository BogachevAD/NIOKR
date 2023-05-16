from PIL import Image
from PIL import ImageOps
import math

pict_num = 7
spisok = [[] for i in range(int(pict_num))]
#spisok = [[] for i in range(int(input(f"Введите количество альфа 1: ")))]
print(spisok)
topor_spisok = []

for k in range(0, pict_num):
    for l in range(0, 21):
        for m in range(0, 21):

            img1 = ImageOps.flip(Image.open(f"13.bmp"))
            #img1 = Image.open(f"13.bmp").rotate(180, expand=True)
            #img1 = Image.open(f"DN_alfa1_3_alfa2_11_alfa3_11.bmp")

            img2 = Image.open(f"DN_alfa1_{k}_alfa2_{l}_alfa3_{m}.bmp")

            def coef_corr(Image1, Image2):
                im1 = Image1.load()
                im2 = Image2.load()
                # Введем переменные для расчета
                # Среднее значение яркости пикселей первого изображения avg_pix_br_1
                Summ1 = 0

                # Среднее значение яркости пикселей второго изображения
                Summ2 = 0

                # Cумма в числителе
                Summ_ch = 0

                # Cумма в знаменателе
                Summ_zn_1 = 0
                Summ_zn_2 = 0

                if (Image1.size == Image2.size):
                    x1, y1 = Image1.size
                    for x in range(0, x1):
                        for y in range(0, y1):
                            Summ1 = Summ1 + im1[x, y]
                            Summ2 = Summ2 + im2[x, y]
                else:
                    print("Размер изображений не совпадают!")

                avg_pix_br_1 = Summ1 / (x1 * y1)
                # print(Summ1, avg_pix_br_1)

                avg_pix_br_2 = Summ2 / (x1 * y1)
                # print(Summ2, avg_pix_br_2)

                if (Image1.size == Image2.size):
                    x1, y1 = Image1.size
                    for x in range(0, x1):
                        for y in range(0, y1):
                            Summ_ch = Summ_ch + ((im1[x, y] - avg_pix_br_1) * (im2[x, y] - avg_pix_br_2))
                            Summ_zn_1 = Summ_zn_1 + (im1[x, y] - avg_pix_br_1) ** 2
                            Summ_zn_2 = Summ_zn_2 + (im2[x, y] - avg_pix_br_2) ** 2
                else:
                    print("Размер изображений не совпадают!")

                Pirsons_coef = Summ_ch / math.sqrt(Summ_zn_1 * Summ_zn_2)

                return round(Pirsons_coef, 5)


            topor_spisok.append(coef_corr(img1, img2))

        spisok[k].append(topor_spisok)
        topor_spisok = []

print(f'Коэффициенты корреляции для тестовых изображений: {spisok}')