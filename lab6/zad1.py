from PIL import Image
import numpy as np
from PIL import ImageChops
from PIL import ImageStat as stat
import matplotlib.pyplot as plt

def ocen_czy_identyczne(obraz1, obraz2):
    a1 = obraz1.mode
    b1 = obraz2.mode
    a2 = obraz1.format
    b2 = obraz2.format
    a3 = obraz1.size
    b3 = obraz2.size
    count = 0
    if a1 != b1:
        print("obrazy nie są identyczne, bo mają różne tryby")
    elif a2 != b2:
        print("obrazy nie są identyczne, bo mają różne formaty")
    elif a3 != b3:
        print("obrazy nie są identyczne, bo mają różne rozmiary")
    else:
        if a2 == "BMP":
            t_obraz1 = np.asarray(obraz1)
            t_obraz2 = np.asarray(obraz2)
            h, w = t_obraz1.shape
            for i in range(h):
                for j in range(w):
                    if t_obraz1[i,j] != t_obraz2[i,j]:
                        count += 1
        else:
            t_obraz1 = np.asarray(obraz1)
            t_obraz2 = np.asarray(obraz2)
            h, w, d = t_obraz1.shape
            for i in range(h):
                for j in range(w):
                    for k in range(0,3):
                        if t_obraz1[i,j,k] != t_obraz2[i,j,k]:
                            count += 1
    if count != 0:
        print("obrazy nie są identyczne, bo mają różne wartości pikseli")
    else:
        print("obrazy są identyczne")

a = Image.open("kod.bmp")
b = Image.open("kod2.bmp")

ocen_czy_identyczne(a,b)