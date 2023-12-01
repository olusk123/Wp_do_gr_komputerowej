from PIL import Image
from PIL import ImageFilter
import matplotlib.pyplot as plt

im = Image.open('zima.jpg')
print("tryb obrazu", im.mode)
print("rozmiar", im.size)

#zadanie 1
def filtruj(obraz, kernel, scale):
    half_size_x, half_size_y = len(kernel) // 2, len(kernel[0]) // 2
    wynik_obraz = Image.new('RGB', obraz.size)

    for x in range(half_size_x, obraz.width - half_size_x):
        for y in range(half_size_y, obraz.height - half_size_y):
            suma = [0, 0, 0]

            for i in range(len(kernel)):
                for j in range(len(kernel[0])):
                    pixel = obraz.getpixel((x - half_size_x + i, y - half_size_y + j))
                    waga = kernel[i][j]
                    suma[0] += pixel[0] * waga
                    suma[1] += pixel[1] * waga
                    suma[2] += pixel[2] * waga

            pixel_wynik = (
                int(suma[0] / scale),
                int(suma[1] / scale),
                int(suma[2] / scale)
            )

            wynik_obraz.putpixel((x, y), pixel_wynik)

    return wynik_obraz

kernel_edge_detection = (-1, -1, -1,-1,  8, -1,-1, -1, -1)
kernel_edge_detection2 = [
    [-1, -1, -1],
    [-1,  8, -1],
    [-1, -1, -1]
]
laplacian_kernel = [
    [0, 1, 0],
    [1, -4, 1],
    [0, 1, 0]
    ]
sharpen_kernel = [
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
    ]
emboss_kernel = [
    [-2, -1, 0],
    [-1, 1, 1],
    [0, 1, 2]]
gaussian_kernel = [
    [1/16, 2/16, 1/16],
    [2/16, 4/16, 2/16],
    [1/16, 2/16, 1/16]
]

custom_blur_kernel = [[1/13, 1/13, 1/13],
                    [1/13, 5/13, 1/13],
                    [1/13, 1/13, 1/13]]
scale_box_blur = 1

filtruj(im, laplacian_kernel, scale_box_blur).show()
filtruj(im, sharpen_kernel, scale_box_blur).show()
filtruj(im, emboss_kernel, scale_box_blur).show()
filtruj(im, gaussian_kernel, scale_box_blur).show()
filtruj(im, custom_blur_kernel, scale_box_blur).show()

im.filter(ImageFilter.BLUR).show()