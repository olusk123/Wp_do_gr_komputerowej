from PIL import Image
import numpy as np
from PIL import ImageChops
from PIL import ImageStat as stat
import matplotlib.pyplot as plt
from random import randint

im3_jpg = Image.open('im3.jpg')
im3_png = Image.open('im3.png')

im_diff = ImageChops.difference(im3_jpg, im3_png)
im_diff.save('immage_diff.jpg')

def statystyki(im):
    s = stat.Stat(im)
    print("extrema ", s.extrema)  # max i min
    print("count ", s.count)  # zlicza
    print("mean ", s.mean)  # srednia
    print("median ", s.median)  # mediana
    print("stddev ", s.stddev)  # odchylenie standardowe

statystyki(im_diff)

def rysuj_histogram_RGB(obraz):
    hist = obraz.histogram()
    plt.title("histogram  ")
    plt.bar(range(256), hist[:256], color='r', alpha=0.5)
    plt.bar(range(256), hist[256:2 * 256], color='g', alpha=0.4)
    plt.bar(range(256), hist[2 * 256:], color='b', alpha=0.3)
    plt.show()
#rysuj_histogram_RGB(im_diff)

def zlicz_roznice_srednia_RGB(obraz, wsp):
    t_obraz = np.asarray(obraz)
    h, w, d = t_obraz.shape
    zlicz = 0
    for i in range(h):
        for j in range(w):
                if np.mean(t_obraz[i, j, :]) > wsp:
                    zlicz = zlicz + 1
    procent = zlicz/(h*w)
    return zlicz, procent

def zlicz_roznice_suma_RGB(obraz, wsp):
    t_obraz = np.asarray(obraz)
    h, w, d = t_obraz.shape
    zlicz = 0
    for i in range(h):
        for j in range(w):
                if sum(t_obraz[i, j, :]) > wsp:
                # if (t_obraz[i, j, 0] + t_obraz[i, j, 1] + t_obraz[i, j, 2]) > wsp:
                # if t_obraz[i, j, 0] > wsp or  t_obraz[i, j, 1] > wsp or t_obraz[i, j, 2] > wsp:
                    zlicz = zlicz + 1
    procent = zlicz/(h*w)
    return zlicz, procent

#print(zlicz_roznice_srednia_RGB(im_diff,2))
#print(zlicz_roznice_srednia_RGB(im_diff,10))

#print(zlicz_roznice_suma_RGB(im_diff,2))
#print(zlicz_roznice_suma_RGB(im_diff,10))


obraz1 = Image.open('obraz.jpg')
obraz1.save('obraz1.jpg')
obraz2 = Image.open('obraz1.jpg')
obraz2.save('obraz2.jpg')
obraz3 = Image.open('obraz2.jpg')
obraz3.save('obraz3.jpg')
obraz4 = Image.open('obraz3.jpg')
obraz4.save('obraz4.jpg')
obraz5 = Image.open('obraz4.jpg')
obraz5.save('obraz5.jpg')

print('obraz1')
statystyki(obraz1)
print('obraz5')
statystyki(obraz5)
print('obraz4')
statystyki(obraz4)

def odkoduj(obraz1, obraz2):

    # Uzyskaj wymiary obrazów
    width, height = obraz1.size

    # Utwórz nowy obraz w trybie "L" (greyscale)
    diff_image = Image.new("L", (width, height), color=255)

    # Konwertuj obrazy na tablice NumPy
    arr1 = np.array(obraz1)
    arr2 = np.array(obraz2)

    # Porównaj obrazy piksel po pikselu
    for i in range(height):
        for j in range(width):
            if not np.array_equal(arr1[i, j], arr2[i, j]):
                # Jeśli piksele są różne, ustaw w nowym obrazie na czarno
                diff_image.putpixel((j, i), 0)

    return diff_image



jesien = Image.open('jesien.jpg')
zakodowany = Image.open('zakodowany1.bmp')
zakodowany1 = Image.open('zakodowany2.bmp')
odkoduj(jesien,zakodowany).show()
odkoduj(jesien,zakodowany1).show()