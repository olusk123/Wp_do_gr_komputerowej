import numpy as np
from PIL import Image
# 1
inicjaly = Image.open("obraz.bmp")
inicjaly.show()

# 2
print("---------- informacje o obrazie")
print("tryb:", inicjaly.mode)
print("format:", inicjaly.format)
print("rozmiar:", inicjaly.size)
print(" ")

# 3
dane_obrazka = np.asarray(inicjaly)

dane_obrazka1 = dane_obrazka * 1
ob_d1 = Image.fromarray(dane_obrazka1)

inicjaly_text = open('inicjaly.txt', 'w')

t2_text = open('inicjaly.txt', 'w')
for rows in dane_obrazka1:
    for item in rows:
        t2_text.write(str(item) + ' ')
    t2_text.write('\n')
t2_text.close()

#4a
t1 = np.loadtxt("inicjaly.txt")
print("typ danych tablicy inicjaly:", t1.dtype)
print("rozmiar tablicy inicjaly :", t1.shape)
print("rozmiar tablicy inicjaly :", t1.size)
print("wymiar tablicy inicjaly :", t1.ndim)
print("rozmiar wyrazu wyrazu :", t1.itemsize)
print("=============================")

#4b
print("pierwszy:", t1[30][50])
print("drugi:", t1[40][90])
print("trzeci:", t1[0][99])
print("============================")

t2 = np.loadtxt("inicjaly.txt", dtype=np.bool_)
t3 = np.loadtxt("inicjaly.txt", dtype=np.uint8)


print("informacje o tablicy bool:")
print("==========================")
print("typ danych tablicy inicjaly:", t2.dtype)
print("rozmiar tablicy inicjaly :", t2.shape)
print("rozmiar tablicy inicjaly :", t2.size)
print("wymiar tablicy inicjaly :", t2.ndim)
print("rozmiar wyrazu wyrazu :", t2.itemsize)
print("=========================")
print("informacje o tablicy uint8:")
print("=========================")
print("typ danych tablicy inicjaly:", t3.dtype)
print("rozmiar tablicy inicjaly :", t3.shape)
print("rozmiar tablicy inicjaly :", t3.size)
print("wymiar tablicy inicjaly :", t3.ndim)
print("rozmiar wyrazu wyrazu :", t3.itemsize)
print("========================")
