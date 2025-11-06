from PIL import Image
import numpy as np
from PIL import ImageChops
from PIL import ImageStat as stat
import matplotlib.pyplot as plt

def statystyki(im):
    s = stat.Stat(im)
    print("extrema ", s.extrema)  # max i min
    print("count ", s.count)  # zlicza
    print("mean ", s.mean)  # srednia
    print("rms ", s.rms)  # pierwiastek średniokwadratowy
    print("median ", s.median)  # mediana
    print("stddev ", s.stddev)  # odchylenie standardowe

def rysuj_histogram_RGB(obraz):
    hist = obraz.histogram()
    plt.title("histogram  ")
    plt.bar(range(256), hist[:256], color='r', alpha=0.5)
    plt.bar(range(256), hist[256:2 * 256], color='g', alpha=0.4)
    plt.bar(range(256), hist[2 * 256:], color='b', alpha=0.3)
    plt.show()

def rysuj_histogram_L(obraz):
    hist = obraz.histogram()
    plt.title("histogram  ")
    plt.bar(range(256), hist[:])
    plt.show()

def zlicz_piksele(obraz, kolor):
    wynik = 0
    histo = obraz.histogram()
    wynik += histo[kolor[0]]
    wynik += histo[kolor[1]+256]
    wynik += histo[kolor[2]+2*256]
    return wynik

Im = Image.open("dragon.png")
statystyki(Im) # obraz jest zrównoważony i jasny ponieważ rms jest większy od mean

rysuj_histogram_RGB(Im)

r, g, b = Im.split()

rysuj_histogram_L(r)
rysuj_histogram_L(g)
rysuj_histogram_L(b)

hist = Im.histogram()
print("kanał r ", hist[155])
print("kanał g ", hist[155+256])
print("kanał b ", hist[155+2*256] )

print(zlicz_piksele(Im,[155,155,155]))


w,h = Im.size
