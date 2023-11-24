from PIL import Image
import numpy as np
import math

obraz = Image.open('obraz.jpg')
print("tryb obrazu", obraz.mode)
print("rozmiar", obraz.size)

def rysuj_kwadrat_srednia(obraz, m, n, k):
    obraz1 = obraz.copy()
    pix = obraz.load()
    pix1 = obraz1.load()
    d = int(k / 2)
    temp = [0, 0, 0]
    for a in range(k):
        for b in range(k):
            x = m + a - d
            y = n + b - d
            pixel = pix[x, y]
            temp[0] += pixel[0]
            temp[1] += pixel[1]
            temp[2] += pixel[2]
    for a in range(k):
        for b in range(k):
            x = m + a - d
            y = n + b - d
            pix1[x, y] = (int(temp[0] / k ** 2), int(temp[1] / k ** 2), int(temp[2] / k ** 2))
    return obraz1


obraz1 = obraz.copy()
rysuj_kwadrat_srednia(obraz1, 60, 170, 25).show()

def rysuj_kwadrat_max(obraz, m, n, k):
    obraz1 = obraz.copy()
    pix = obraz.load()
    pix1 = obraz1.load()
    d = int(k / 2)
    temp = [0, 0, 0]

    for a in range(k):
        for b in range(k):
            x = m + a - d
            y = n + b - d
            pixel = pix[x, y]

            temp[0] = max(temp[0], pixel[0])
            temp[1] = max(temp[1], pixel[1])
            temp[2] = max(temp[2], pixel[2])

    for a in range(k):
        for b in range(k):
            x = m + a - d
            y = n + b - d
            pix1[x, y] = (temp[0], temp[1], temp[2])

    return obraz1

rysuj_kwadrat_max(obraz, 50, 100, 101).show()

def rysuj_kwadrat_min(obraz, m, n, k):
    obraz1 = obraz.copy()
    pix = obraz.load()
    pix1 = obraz1.load()
    d = int(k / 2)
    temp = [255, 255, 255]

    for a in range(k):
        for b in range(k):
            x = m + a - d
            y = n + b - d
            pixel = pix[x,y]

            temp[0] = min(temp[0], pixel[0])
            temp[1] = min(temp[1], pixel[1])
            temp[2] = min(temp[2], pixel[2])

    for a in range(k):
        for b in range(k):
            x = m + a - d
            y = n + b - d
            pix1[x, y] = (temp[0], temp[1], temp[2])

    return obraz1

rysuj_kwadrat_min(obraz, 100, 50, 101).show()

#zadanie 2
def zakres(w, h):
    return [(i, j) for i in range(w) for j in range(h)]

def kopiuj_piksele_z_regionu(obraz, m_s, n_s, r, x_src, y_src):
    obraz1 = obraz.copy()
    w, h = obraz.size
    pix = obraz.load()
    pix1 = obraz1.load()

    for i, j in zakres(w, h):
        if (i - m_s) ** 2 + (j - n_s) ** 2 < r ** 2:
            x_src_actual = (i - m_s) + x_src
            y_src_actual = (j - n_s) + y_src

            pix1[i, j] = pix[x_src_actual, y_src_actual]
    return obraz1


kopiuj_piksele_z_regionu(obraz, 20, 150, 50,135,100).show()

#zadanie 3
def odbij_w_pionie(im):
    img = im.copy()
    w, h = im.size
    px = img.load()
    for i in range(w):
        for j in range(h):
            px[i, j] = px[w - 1 - i, j]
    return img

odbij_w_pionie(obraz).show()