from PIL import Image
import numpy as np

#   obr     neg

#1  true    false
#   false   true

#L  a       255-a

#RGB
#   [r,g,b] [255-r,255-g,255-b]

def negatyw(obraz):
    if obraz.mode == "1":
        tab = np.asarray(obraz)
        h, w = tab.shape
        tab_neg = tab.copy()
        for i in range(h):
            for j in range(w):
                if tab_neg[i, j] == True:
                    tab_neg[i, j] = False
                elif tab_neg[i, j] == False:
                    tab_neg[i, j] = True
                else:
                    continue
    elif obraz.mode == "L":
        tab = np.asarray(obraz)
        h, w = tab.shape
        tab_neg = tab.copy()
        for i in range(h):
            for j in range(w):
                tab_neg[i, j] = 255 - tab[i, j]
    elif obraz.mode == "RGB":
        tab = np.asarray(obraz)
        tab_s = obraz.convert("1")
        tab_shape = np.asarray(tab_s)
        h, w = tab_shape.shape
        tab_neg = tab.copy()
        for i in range(h):
            for j in range(w):
                tab_neg[i, j, 0] = 255 - tab[i, j, 0]
                tab_neg[i, j, 1] = 255 - tab[i, j, 1]
                tab_neg[i, j, 2] = 255 - tab[i, j, 2]
    return Image.fromarray(tab_neg)

def rysuj_ramki_kolorowe(w, kolor, zmiana_koloru_r, zmiana_koloru_g, zmiana_koloru_b):
    t = (w, w, 3)
    tab = np.zeros(t, dtype=np.uint8)
    kolor_r = kolor[0]
    kolor_g = kolor[1]
    kolor_b = kolor[2]
    z = w
    for k in range(int(w / 2)):
        for i in range(k, z - k):
            for j in range(k, z - k):
                tab[i, j] = [kolor_r, kolor_g, kolor_b]
        kolor_r = (kolor_r - zmiana_koloru_r) % 256
        kolor_g = (kolor_g - zmiana_koloru_g) % 256
        kolor_b = (kolor_b - zmiana_koloru_b) % 256
    return Image.fromarray(tab)

def rysuj_po_skosie_szare(h,w, a, b):  # formuła zmiany wartości elemntów tablicy a*i + b*j
    t = (h, w) # rysuje kwadratowy obraz
    tab = np.zeros(t, dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            tab[i, j] = (a*i + b*j) % 256
    return Image.fromarray(tab)


skos = rysuj_po_skosie_szare(100, 300, 8, 8)

ramki = rysuj_ramki_kolorowe(200, [0,120,220], 8, 8, -8)

obr = Image.open("gwiazdka.bmp")
a = negatyw(skos)
a.show()