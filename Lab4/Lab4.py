from PIL import Image
import numpy as np

def rysuj_ramki_szare(w, h, grub, kolor_ramki, kolor, ilosc): #kolor od 0 do 255
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    tab[:] = kolor_ramki
    tab[grub:h - grub, grub:w - grub] = kolor
    for i in range(1,ilosc):
        tab[grub*(i*i+1):h - grub*(i*i+1), grub*(i*i+1):w - grub*(i*i+1)] = kolor_ramki
        tab[grub*(i*i+2):h - grub*(i*i+2), grub*(i*i+2):w - grub*(i*i+2)] = kolor
    return Image.fromarray(tab)

def rysuj_pasy_pionowe_szare(w, h, grub, zmiana_koloru):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    ile = int(w / grub)
    for k in range(ile):
        for g in range(grub):
            i = k * grub + g
            for j in range(h):
                tab[j, i] = (k + zmiana_koloru) % 256
    return Image.fromarray(tab)


im_paski = rysuj_pasy_pionowe_szare(1024, 64, 1, 10)
im_paski.show()

im_ramka = rysuj_ramki_szare(3000, 2000, 50 , 100, 200, 6)
#im_ramka.show()