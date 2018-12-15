import numpy as np
import cv2
from PIL import Image
#В этом скрипте делаем маску
#С помощью манипуляций с opencv создаем два файла
#первый - с контрастными крышами, второй - с выделенными дорогами
#затем - используя второй файл, убираем дороги с первого
image = "ZRYNEEUSVQ213QTY.png"

input = cv2.imread(image)

_, th = cv2.threshold(input, 130, 160, cv2.THRESH_TOZERO)

cv2.imwrite("th.png", th)

image = "th.png"
img = cv2.imread(image)

lower = np.array([0, 1, 1])
upper = np.array([0, 255, 255])
mask = cv2.inRange(img, lower, upper)
roads = cv2.bitwise_and(img, img, mask=mask)

height = int(np.size(img, 0))
width = int(np.size(img, 1))

for h in range(1, 500):
    for w in range(1, 500):
        color = str(roads[w, h])
        if color != "[0, 145, 153]":
            pass
        else:
            roads[h, w] = [0, 0, 255]

cv2.imwrite("roads.png", roads)

mask = Image.open("roads.png")
mask1 = Image.open("th.png")

for i in range (1, 6528):
    for j in range (1, 7733):
        if mask1.getpixel((i,j))[0] != 0 or mask1.getpixel((i,j))[1] != 0 or \
                mask1.getpixel((i,j))[2] != 0:
            mask1.putpixel((i, j), (255, 255, 255))
        if (mask.getpixel((i, j))[0] != 0) or (mask.getpixel((i, j))[1] != 0) or (mask.getpixel((i, j))[2] != 0):
            mask1.putpixel((i, j), (0, 0, 0))
mask1.save("dengi3.jpg", "JPEG")