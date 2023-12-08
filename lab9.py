from PIL import Image, ImageOps
import numpy as np
import matplotlib.pyplot as plt

#zadanie 1

obraz = Image.open('zeby.png')
print(obraz.mode)
obraz = obraz.convert('L')
print(obraz.mode)

#zadanie 2.1
def histogram_norm(obraz):
    hist = obraz.histogram()
    w, h = obraz.size
    N = w * h
    hist_norm = np.array(hist) / N

    plt.bar(range(256), hist_norm, alpha=0.7)
    plt.title('Histogram')
    plt.xlabel('Wartość pixeli')
    plt.ylabel('Częstotliwość pixeli')
    return plt

#zadanie 2.2
def histogram_norm_array(im):
    hist = im.histogram()
    w, h = im.size
    N = w * h
    hist_norm = np.array(hist) / N
    return hist_norm


def histogram_cumul(obraz):
    histogram = histogram_norm_array(obraz)
    hist_cumulative = [histogram[0]]
    for i in range(1, len(histogram)):
            hist_cumulative.append(hist_cumulative[i - 1] + histogram[i])
    plt.bar(range(256), hist_cumulative, alpha=0.7)
    plt.title('Cumul Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Częstość pixeli')
    return plt


#zadanie 2.3

def histogram_cumul_array(histogram):
    hist_cumulative = [histogram[0]]
    for i in range(1, len(histogram)):
            hist_cumulative.append(hist_cumulative[i - 1] + histogram[i])
    return hist_cumulative

def histogram_equalization(obraz):
    hist_norm = histogram_norm_array(obraz)
    hist_cumulative = histogram_cumul_array(hist_norm)
    im1 = obraz.point(lambda i:  int(255 * hist_cumulative[i]))
    return im1


#zadanie 2.4
plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.bar(range(256), hist_norm, alpha=0.7)
plt.title('Normalized Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Normalized Frequency')

plt.subplot(1, 3, 2)
plt.bar(range(256), hist_cumul, alpha=0.7)
plt.title('Cumulative Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Cumulative Frequency')

plt.subplot(1, 3, 3)
plt.imshow(hist_equalization, cmap='gray')
plt.title('Equalized Image')
plt.axis('off')

plt.tight_layout()
plt.show()
