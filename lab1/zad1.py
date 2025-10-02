# tryby 1,L,I,RGB,RGBA,CMYK
from PIL import Image
import numpy as np

obraz = Image.open("inicjaly.bmp")
print(obraz.mode)
print(obraz.format)
print(obraz.size)

tablica = np.asarray(obraz)
tab01 = tablica.astype(np.uint8)
inicjaly = open('inicjaly.txt', 'w')
for rows in tab01:
    for item in rows:
        inicjaly.write(str(item) + ' ')
    inicjaly.write('\n')
inicjaly.close()

print(tab01[30,50])
print(tab01[40,90])
print(tab01[0,99])
print(tab01[12,16])

txt = np.loadtxt("inicjaly.txt", dtype=np.bool)
print(tablica.dtype)
print(tablica.shape)
print(tablica.ndim)
print(txt.dtype)
print(txt.shape)
print(txt.ndim)

txt2 = np.loadtxt("inicjaly.txt", dtype=np.uint8)
print(txt2.dtype)
print(txt2.shape)
print(txt2.ndim)

txtobr = Image.fromarray(txt2)

#txtobr.show()
#obraz.show()