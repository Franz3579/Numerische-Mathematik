import numpy as np
import Funktionen as fu

# Für schnelles Umschalten der zu zeigenden Plots
y = True
n = False

a = n
b = n
c = n
d = n
e = n

if a:
    x1 = np.linspace(-4, 4, 101)
    x2 = np.linspace(-4, 4, 101)
    X1, X2 = np.meshgrid(x1, x2)
    rosenbrock = 100*(X2-X1**2)**2 + (1-X1)**2
    fu.plotte_Funktion_surf_contf(X1, X2, rosenbrock, "Rosenbrock")

if b:
    x1 = np.linspace(-4, 4, 101)
    x2 = np.linspace(-4, 4, 101)
    X1, X2 = np.meshgrid(x1, x2)
    himmelblau = (X1**2 + X2 - 11)**2 + (X1 + X2**2 -7)**2
    fu.plotte_Funktion_surf_contf(X1, X2, himmelblau, "Himmelblau")

if c:
    x1 = np.linspace(-4, 4, 101)
    x2 = np.linspace(-4, 4, 101)
    X1, X2 = np.meshgrid(x1, x2)
    bazaraa_shetty = (X1 - 2)**4 + (X1 - 2*X2)**2
    fu.plotte_Funktion_surf_contf(X1, X2, bazaraa_shetty, "bazaraa/shetty")

if d:
    x1 = np.linspace(-4, 4, 101)
    x2 = np.linspace(-4, 4, 101)
    X1, X2 = np.meshgrid(x1, x2)
    beale = (1.5 - X1*(1 - X2))**2 + (2.25 - X1*(1 - X2**2))**2 + (2.625 - X1*(1 - X2**2))**2
    fu.plotte_Funktion_surf_contf(X1, X2, beale, "beale")

if e:
    x1 = np.linspace(-4, 4, 101)
    x2 = np.linspace(-4, 4, 101)
    X1, X2 = np.meshgrid(x1, x2)
    spellucci = 2*X1**3 + X2**2 + X1**2*X2**2 + 4*X1*X2 + 3
    fu.plotte_Funktion_surf_contf(X1, X2, spellucci, "spellucci")