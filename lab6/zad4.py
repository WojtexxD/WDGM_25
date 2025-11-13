from PIL import Image
import numpy as np
from PIL import ImageChops
from PIL import ImageStat as stat
import matplotlib.pyplot as plt

def odkoduj(obraz1, obraz2):
    t_obraz1 = np.asarray(obraz1)
    t_obraz2 = np.asarray(obraz2)
    h,w,d = t_obraz1.shape
    t = (h,w)
    odkodowany = np.zeros(t, dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            for k in range(0,3):
                if t_obraz1[i,j,k] == t_obraz2[i,j,k]:
                    odkodowany[i,j] = 0
                else:
                    odkodowany[i,j] = 255
    return Image.fromarray(odkodowany)

a = Image.open("zakodowany1.bmp")
b = Image.open("jesien.jpg")

c = odkoduj(a,b)
c.save("kod2.bmp")
c.show()