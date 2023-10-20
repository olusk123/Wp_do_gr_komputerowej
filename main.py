from PIL import Image
import numpy as np


#zadanie 1




def foo3(w, h, m, n,grub,kolor,kolor1):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8) * 255
    ile = int(w / grub)
    for k in range(ile):
        for i in range(n):
            for j in range(m):
                tab[i][j] = (k + kolor) % 256
        for i in range(n,h):
            for j in range(m,w):
                tab[i][j] = (k + kolor1) % 256
        return Image.fromarray(tab)

obraz313 = foo3(480, 320, 100, 50,10,100,0)
obraz313.save("obraz313.bmp")
obraz313.show()

def negatyw_szare(obraz):
    tab = np.asarray(obraz)
    h, w = tab.shape
    tab_neg = tab.copy()
    for i in range(h):
        for j in range(w):
            tab_neg[i, j] = 255 - tab[i, j]
    return Image.fromarray(tab_neg)

obr_N = negatyw_szare(obraz313)
obr_N.show()

def inicjaly_paski_rbg(grub, obraz):
    tab = np.asarray(obraz) * 255
    h, w = tab.shape
    ile = int(w / grub)
    for k in range(ile):
        for g in range(grub):
            j = k * grub + g
            for i in range(h):
                if k % 3 == 0:
                    tab[i, j] = [255, 0, 0]
                elif k % 3 == 1:
                    tab[i, j] = [0, 255, 0]
                else:
                    tab[i, j] = [0, 0, 255]
    return Image.fromarray(tab)


obraz = Image.open('inicjaly.bmp')
obr5 = inicjaly_paski_rbg(5, obraz)
obr5.show()

