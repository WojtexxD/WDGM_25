from PIL import Image
import numpy as np


def rysuj_ramke_w_obrazie(obraz, grub):
    tab_obraz = np.asarray(obraz).astype(np.uint8)
    h, w = tab_obraz.shape
    tab_obraz[0:grub, 0:w] = 0
    tab_obraz[h - grub:h, 0:w] = 0
    tab_obraz[0:h, 0:grub] = 0
    tab_obraz[0:h, w - grub:w] = 0

    tab = tab_obraz.astype(bool)
    return Image.fromarray(tab)


def rysuj_ramki(w, h, grub):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    x = 0
    y = 1

    tab[grub*x:y*grub, grub*x:w-grub*x] = 0
    tab[h - grub*y:h - x*grub, x*grub:w-grub*x] = 0
    tab[x*grub:h-x*grub, x*grub:y*grub] = 0
    tab[x*grub:h-grub*x, w - grub*y:w-x*grub] = 0


    tab1 = tab.astype(np.bool_)
    return Image.fromarray(tab1)


inicjaly = Image.open("bs.bmp")

print("tryb", inicjaly.mode)
print("format", inicjaly.format)
print("rozmiar", inicjaly.size)

t_inicjaly = np.asarray(inicjaly)
print("typ danych tablicy", t_inicjaly.dtype)
print("rozmiar tablicy", t_inicjaly.shape)

# inicjaly.show()
a = rysuj_ramke_w_obrazie(inicjaly, 4)
print("tryb", a.mode)
print("format", a.format)
print("rozmiar", a.size)
# a.show()

b = rysuj_ramki(200, 100, 10)
b.show()
