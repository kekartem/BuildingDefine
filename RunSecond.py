from PIL import Image
#чистим от шумов (не методом, котрый чистит от шумов, а собственным алгоритмом по пикселям)
mask = Image.open("dengi3.jpg")
mask1 = Image.open("black.png")

for i in range(6, 6523):
    for j in range(6, 7728):
        count = 0
        if mask.getpixel((i,j)) == (255, 255, 255):
            for u in range (i - 5, i + 5):
                for v in range (j - 5, j + 5):
                    if mask.getpixel((u, v)) == (255, 255, 255):
                        count += 1
            if count >= 85:
                for u in range(i - 5, i + 5):
                    for v in range(j - 5, j + 5):
                        mask1.putpixel((u, v), (255, 255, 255))
    print(i)
    print()
mask1.save("dengi_clear3.png", "png")

