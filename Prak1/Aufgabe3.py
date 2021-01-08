import numpy as np
import Funktionen as fu


# Startwerte
funktion = fu.spellucci
anzahl_it = 1000
startpunkt = [0, 0]
sigma = 0.5

x = startpunkt
k = 0
xarray = []
while k < anzahl_it:
    r = np.random.rand(2)
    v = x + sigma*(r - 0.5)
    xfun = funktion(x)
    vfun = funktion(v)
    if vfun < xfun:
        x = v
    k += 1

print(x)
