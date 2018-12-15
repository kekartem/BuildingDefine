import csv

import numpy as np
from PIL import Image, ImageDraw
import cv2

#генерируем cvs файл

image = cv2.imread("dengi01.png", 1)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, image = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY)

cv2.imwrite("dengi01.png", image)

mask1 = Image.open("dengi01.png")

img = np.array(mask1)


image1 = cv2.imread("dengi02.png", 1)
image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
_, image1 = cv2.threshold(image1, 100, 255, cv2.THRESH_BINARY)

cv2.imwrite("dengi02.png", image)

mask1 = Image.open("dengi02.png")

img1 = np.array(mask1)



image2 = cv2.imread("dengi03.png", 1)
image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
_, image2 = cv2.threshold(image2, 100, 255, cv2.THRESH_BINARY)

cv2.imwrite("dengi03.png", image)

mask1 = Image.open("dengi03.png")

img2 = np.array(mask1)

# //img1 = mask11[:,:,0]
print(img1.shape)

def rle_encode(img):
    '''
    img: numpy array, 1 - mask, 0 - background
    Returns run length as string formated
    '''
    pixels = img.flatten()
    pixels = np.concatenate([[0], pixels, [0]])
    runs = np.where(pixels[1:] != pixels[:-1])[0] + 1
    runs[1::2] -= runs[::2]
    return ' '.join(str(x) for x in runs)


result1 = rle_encode(img)
result2 = rle_encode(img1)
result3 = rle_encode(img2)

FILENAME1 = "finalresult.csv"

columns = [
    ["ImageId,EncodedPixels"],
    ["KHSF2T5PXCKI0978.png", result1],
    ["P2MLF2MV9K9XIYUI.png", result2],
    ["ZRYNEEUSVQ213QTY.png", result3]
]

with open(FILENAME1, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(columns)

