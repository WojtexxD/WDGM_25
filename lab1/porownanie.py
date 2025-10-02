from PIL import Image
import numpy as np

obraz1 = Image.open("inicjaly.bmp")
print(obraz1.mode)
print(obraz1.format)
print(obraz1.size)

obraz2 = Image.open("inicjaly.png")
print(obraz2.mode)
print(obraz2.format)
print(obraz2.size)

obraz3 = Image.open("inicjaly.jpg")
print(obraz3.mode)
print(obraz3.format)
print(obraz3.size)

obraz4 = Image.open("inicjaly.gif")
print(obraz4.mode)
print(obraz4.format)
print(obraz4.size)

print("\n")

tablica1 = np.asarray(obraz1)
print(tablica1.dtype)
print(tablica1.shape)
print(tablica1.ndim)
tablica2 = np.asarray(obraz2)
print(tablica2.dtype)
print(tablica2.shape)
print(tablica2.ndim)
tablica3 = np.asarray(obraz3)
print(tablica3.dtype)
print(tablica3.shape)
print(tablica3.ndim)
tablica4 = np.asarray(obraz4)
print(tablica4.dtype)
print(tablica4.shape)
print(tablica4.ndim)

#obraz1.show()
#obraz2.show()
#obraz3.show()
#obraz4.show()