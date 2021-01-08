import numpy as np
import Funktionen as fu
import scipy.optimize as sc
import matplotlib.pyplot as plt

# Für schnelles Umschalten der zu zeigenden Plots
y = True
n = False

a = y
b = y
c = y
d = y
e = y

startwerte = [2, 0]

if a:
    def rosenbrock(x):
        rosenbrock = 100*(x[1]-x[0]**2)**2 + (1-x[0])**2
        return rosenbrock
    guess = np.array(startwerte)
    min = sc.minimize(rosenbrock, guess, method='Nelder-Mead')
    print("Minimum bei x1 = {}, x2 = {} mit dem Wert f(x1,x2) = {}"
          .format(round(min.x[0], 4), round(min.x[1], 4), min.fun))

    # Darstellung
    x1 = np.linspace(-4, 4, 101)
    x2 = np.linspace(-4, 4, 101)
    X1, X2 = np.meshgrid(x1, x2)
    funktionswerte = rosenbrock([X1, X2])
    plt.contourf(X1, X2, funktionswerte, levels=100)
    plt.title("Rosenbrock Minimum")
    plt.plot(min.x[0], min.x[1], 'go')
    plt.text(min.x[0], min.x[1], "Minimum")
    plt.plot(guess[0], guess[1], 'ro')
    plt.text(guess[0], guess[1], "Startwert")
    plt.show()

if b:
    def himmelblau(x):
        himmelblau = (x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 -7)**2
        return himmelblau
    guess = np.array(startwerte)
    min = sc.minimize(himmelblau, guess, method='Nelder-Mead')
    print("Minimum bei x1 = {}, x2 = {} mit dem Wert f(x1,x2) = {}"
          .format(round(min.x[0], 4), round(min.x[1], 4), min.fun))

    # Darstellung
    x1 = np.linspace(-4, 4, 101)
    x2 = np.linspace(-4, 4, 101)
    X1, X2 = np.meshgrid(x1, x2)
    funktionswerte = himmelblau([X1, X2])
    plt.contourf(X1, X2, funktionswerte, levels=100)
    plt.title("himmelblau Minimum")
    plt.plot(min.x[0], min.x[1], 'go')
    plt.text(min.x[0], min.x[1], "Minimum")
    plt.plot(guess[0], guess[1], 'ro')
    plt.text(guess[0], guess[1], "Startwert")
    plt.show()

if c:
    def bazaraa_shetty(x):
        bazaraa_shetty = (x[0] - 2)**4 + (x[0] - 2*x[1])**2
        return bazaraa_shetty
    guess = np.array(startwerte)
    min = sc.minimize(bazaraa_shetty, guess, method='Nelder-Mead')
    print("Minimum bei x1 = {}, x2 = {} mit dem Wert f(x1,x2) = {}"
          .format(round(min.x[0], 4), round(min.x[1], 4), min.fun))

    # Darstellung
    x1 = np.linspace(-4, 4, 101)
    x2 = np.linspace(-4, 4, 101)
    X1, X2 = np.meshgrid(x1, x2)
    funktionswerte = bazaraa_shetty([X1, X2])
    plt.contourf(X1, X2, funktionswerte, levels=100)
    plt.title("bazaraa_shetty Minimum")
    plt.plot(min.x[0], min.x[1], 'go')
    plt.text(min.x[0], min.x[1], "Minimum")
    plt.plot(guess[0], guess[1], 'ro')
    plt.text(guess[0], guess[1], "Startwert")
    plt.show()

if d:
    def beale(x):
        beale = (1.5 - x[0]*(1 - x[1]))**2 + (2.25 - x[0]*(1 - x[1]**2))**2 + (2.625 - x[0]*(1 - x[1]**3))**2
        return beale
    guess = np.array(startwerte)
    min = sc.minimize(beale, guess, method='Nelder-Mead')
    print("Minimum bei x1 = {}, x2 = {} mit dem Wert f(x1,x2) = {}"
          .format(round(min.x[0], 4), round(min.x[1], 4), min.fun))

    # Darstellung
    x1 = np.linspace(-4, 4, 101)
    x2 = np.linspace(-4, 4, 101)
    X1, X2 = np.meshgrid(x1, x2)
    funktionswerte = beale([X1, X2])
    plt.contourf(X1, X2, funktionswerte, levels=100)
    plt.title("beale Minimum")
    plt.plot(min.x[0], min.x[1], 'go')
    plt.text(min.x[0], min.x[1], "Minimum")
    plt.plot(guess[0], guess[1], 'ro')
    plt.text(guess[0], guess[1], "Startwert")
    plt.show()

if e:
    def spellucci(x):
        spellucci = 2*x[0]**3 + x[1]**2 + x[0]**2*x[1]**2 + 4*x[0]*x[1] + 3
        return spellucci
    guess = np.array(startwerte)
    min = sc.minimize(spellucci, guess, method='Nelder-Mead')
    print("Minimum bei x1 = {}, x2 = {} mit dem Wert f(x1,x2) = {}"
          .format(round(min.x[0], 4), round(min.x[1], 4), min.fun))

    # Darstellung
    x1 = np.linspace(-4, 4, 101)
    x2 = np.linspace(-4, 4, 101)
    X1, X2 = np.meshgrid(x1, x2)
    funktionswerte = spellucci([X1, X2])
    plt.contourf(X1, X2, funktionswerte, levels=100)
    plt.title("spellucci Minimum")
    plt.plot(min.x[0], min.x[1], 'go')
    plt.text(min.x[0], min.x[1], "Minimum")
    plt.plot(guess[0], guess[1], 'ro')
    plt.text(guess[0], guess[1], "Startwert")
    plt.show()