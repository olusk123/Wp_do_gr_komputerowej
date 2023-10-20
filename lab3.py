import numpy as np
from PIL import Image


# Zadanie 1
def rysuj_ramke_w_ramce(w, h, grub, kolor):  # grub grubość ramki w pikselach
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8)
    for k in range(min(w, h)):
        tab[k * grub:h - k * grub, k * grub:w - k * grub] = (k + kolor) % 256
    return tab


def rysuj_pasy_pionie(w, h, grub, kolor):
    t = (h, w)  # rozmiar tablicy-
    tab = np.ones(t, dtype=np.uint8)
    ile = int(w / grub)
    for k in range(ile):
        for g in range(grub):
            j = k * grub + g
            for i in range(h):
                tab[i, j] = (k + kolor) % 256
    return Image.fromarray(tab)


def negatyw_szare(obraz):
    tab = np.asarray(obraz)
    h, w = tab.shape
    tab_neg = tab.copy()
    for i in range(h):
        for j in range(w):
            tab_neg[i, j] = 255 - tab[i, j]
    return Image.fromarray(tab_neg)


tab = rysuj_ramke_w_ramce(300, 300, 5, 100)
obr1 = Image.fromarray(tab)
obr1.save('obraz1_1.jpg')
obr1.save('obraz1_1.png')
obr1_N = negatyw_szare(obr1)
obr1_N.save('obraz1_1N.jpg')
obr1_N.save('obraz1_1N.png')

obr2 = rysuj_pasy_pionie(600, 300, 5, 50)
obr2.save('obraz1_2.png')
obr2.save('obraz1_2.jpg')
obr2_N = negatyw_szare(obr2)
obr2_N.save('obraz1_2N.png')
obr2_N.save('obraz1_2N.jpg')


# Zadanie 2
def rysuj_ramke_w_ramce_rgb(w, h, grub):  # grub grubość ramki w pikselach
    t = (h, w, 3)
    tab = np.zeros(t, dtype=np.uint8)
    for k in range(min(w, h)):
        if k % 3 == 0:
            tab[k * grub:h - k * grub, k * grub:w - k * grub] = [255, 0, 0]
        elif k % 3 == 1:
            tab[k * grub:h - k * grub, k * grub:w - k * grub] = [0, 255, 0]
        else:
            tab[k * grub:h - k * grub, k * grub:w - k * grub] = [0, 0, 255]
    return tab


def rysuj_pasy_pionie_rbg(w, h, grub):
    t = (h, w, 3)  # rozmiar tablicy-
    tab = np.ones(t, dtype=np.uint8)
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


def negatyw_szare_rgb(obraz):
    tab = np.asarray(obraz)
    h, w, d = tab.shape
    tab_neg = tab.copy()
    for i in range(h):
        for j in range(w):
            tab_neg[i, j, 0] = 255 - tab[i, j, 0]
            tab_neg[i, j, 1] = 255 - tab[i, j, 1]
            tab_neg[i, j, 2] = 255 - tab[i, j, 2]
    return Image.fromarray(tab_neg)


tab3 = rysuj_ramke_w_ramce_rgb(300, 300, 5)
obr3 = Image.fromarray(tab3)
obr3.save('obraz2_1.jpg')
obr3.save('obraz2_1.png')
obr3_N = negatyw_szare_rgb(obr3)
obr3_N.save('obraz2N_1.jpg')
obr3_N.save('obraz2N_1.png')

obr4 = rysuj_pasy_pionie_rbg(600, 300, 5)
obr4.save('obraz2_2.png')
obr4.save('obraz2_2.jpg')
obr4_N = negatyw_szare_rgb(obr4)
obr4_N.save('obraz2_2N.png')
obr4_N.save('obraz2_2N.jpg')


# zadanie 3
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


obraz = Image.open('../lab2/inicjaly.bmp')
obr5 = inicjaly_paski_rbg(5, obraz)
obr5.show()
