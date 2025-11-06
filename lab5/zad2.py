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

Im2 = Image.open("dragon.jpg")
Im1 = Image.open("dragon.png")

statystyki(Im2) # ponieważ są zapisywane w innym formacie które się różnią w niwielkim stopniu odczytywaniem nasycenia kolorów i jpg pogarsza ich kolorystyke

diff = ImageChops.difference(Im1,Im2)
#statystyki(diff) # zmniejszył się zasięg kolorów pikseli z 0,255 do 0,123 (maksymanlna wartość z RGB) i mean z rms są o wiele mniejsze w okolicach 10-krotnie i mediana tez sie zmniejszyla wraz z stddev wynika to, ze obraz jest ubogi w kolory i zakres ich jest o wiele mniejszy
diff.save("diff.jpg")
Im2.save("im.jpg")
Im3 = Image.open("im.jpg")
Im3.save("im.jpg")
Im4 = Image.open("im.jpg")
statystyki(Im4)