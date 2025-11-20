from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def zakres(w, h):  # funkcja, która uprości podwójna petle for
    return [(i, j) for i in range(w) for j in range(h)]

def wstaw_inicjaly(obraz, inicjaly, m, n, kolor):
    obrazc = obraz.copy()
    w, h = obraz.size
    w0, h0 = inicjaly.size
    for i, j in zakres(w0, h0):
        if inicjaly.getpixel((i, j)) == 0:
            p = obraz.getpixel((i + m, j + n))
            obrazc.putpixel((i + m, j + n), (p[0] + kolor[0], p[1]+kolor[1], p[2]+kolor[2]))
    return obrazc

def wstaw_inicjaly_maska(obraz, inicjaly, m, n):
    obrazc = obraz.copy()
    w, h = obraz.size
    w0, h0 = inicjaly.size
    for i, j in zakres(w0, h0):
        if inicjaly.getpixel((i, j)) == 0:
            p = obraz.getpixel((i + m, j + n))
            obrazc.putpixel((i + m, j + n), (255-p[0], 255-p[1], 255-p[2]))
    return obrazc

obraz = Image.open("dragon.jpg")
inicjaly = Image.open("inicjaly.bmp")

copy = obraz.copy()

obraz1 = wstaw_inicjaly(copy,inicjaly,142,184,[255,0,0])
obraz1.save("obraz1.jpg")

obraz2 = wstaw_inicjaly_maska(copy,inicjaly,142,184)
obraz2.save("obraz2.jpg")
obraz2.show()