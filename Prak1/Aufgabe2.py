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
    guess = np.array(startwerte)
    min = sc.minimize(fu.rosenbrock, guess, method='Nelder-Mead')
    print("Minimum bei x1 = {}, x2 = {} mit dem Wert f(x1,x2) = {}"
          .format(round(min.x[0], 4), round(min.x[1], 4), min.fun))

    # Darstellung
    x1 = np.linspace(-4, 4, 101)
    x2 = np.linspace(-4, 4, 101)
    X1, X2 = np.meshgrid(x1, x2)
    funktionswerte = fu.rosenbrock([X1, X2])
    plt.contourf(X1, X2, funktionswerte, levels=100)
    plt.title("Rosenbrock Minimum")
    plt.plot(min.x[0], min.x[1], 'go')
    plt.text(min.x[0], min.x[1], "Minimum")
    plt.plot(guess[0], guess[1], 'ro')
    plt.text(guess[0], guess[1], "Startwert")
    plt.show()

if b:
    guess = np.array(startwerte)
    min = sc.minimize(fu.himmelblau, guess, method='Nelder-Mead')
    print("Minimum bei x1 = {}, x2 = {} mit dem Wert f(x1,x2) = {}"
          .format(round(min.x[0], 4), round(min.x[1], 4), min.fun))

    # Darstellung
    x1 = np.linspace(-4, 4, 101)
    x2 = np.linspace(-4, 4, 101)
    X1, X2 = np.meshgrid(x1, x2)
    funktionswerte = fu.himmelblau([X1, X2])
    plt.contourf(X1, X2, funktionswerte, levels=100)
    plt.title("himmelblau Minimum")
    plt.plot(min.x[0], min.x[1], 'go')
    plt.text(min.x[0], min.x[1], "Minimum")
    plt.plot(guess[0], guess[1], 'ro')
    plt.text(guess[0], guess[1], "Startwert")
    plt.show()

if c:
    guess = np.array(startwerte)
    min = sc.minimize(fu.bazaraa_shetty, guess, method='Nelder-Mead')
    print("Minimum bei x1 = {}, x2 = {} mit dem Wert f(x1,x2) = {}"
          .format(round(min.x[0], 4), round(min.x[1], 4), min.fun))

    # Darstellung
    x1 = np.linspace(-4, 4, 101)
    x2 = np.linspace(-4, 4, 101)
    X1, X2 = np.meshgrid(x1, x2)
    funktionswerte = fu.bazaraa_shetty([X1, X2])
    plt.contourf(X1, X2, funktionswerte, levels=100)
    plt.title("bazaraa_shetty Minimum")
    plt.plot(min.x[0], min.x[1], 'go')
    plt.text(min.x[0], min.x[1], "Minimum")
    plt.plot(guess[0], guess[1], 'ro')
    plt.text(guess[0], guess[1], "Startwert")
    plt.show()

if d:
    guess = np.array(startwerte)
    min = sc.minimize(fu.beale, guess, method='Nelder-Mead')
    print("Minimum bei x1 = {}, x2 = {} mit dem Wert f(x1,x2) = {}"
          .format(round(min.x[0], 4), round(min.x[1], 4), min.fun))

    # Darstellung
    x1 = np.linspace(-4, 4, 101)
    x2 = np.linspace(-4, 4, 101)
    X1, X2 = np.meshgrid(x1, x2)
    funktionswerte = fu.beale([X1, X2])
    plt.contourf(X1, X2, funktionswerte, levels=100)
    plt.title("beale Minimum")
    plt.plot(min.x[0], min.x[1], 'go')
    plt.text(min.x[0], min.x[1], "Minimum")
    plt.plot(guess[0], guess[1], 'ro')
    plt.text(guess[0], guess[1], "Startwert")
    plt.show()

if e:
    guess = np.array(startwerte)
    min = sc.minimize(fu.spellucci, guess, method='Nelder-Mead')
    print("Minimum bei x1 = {}, x2 = {} mit dem Wert f(x1,x2) = {}"
          .format(round(min.x[0], 4), round(min.x[1], 4), min.fun))

    # Darstellung
    x1 = np.linspace(-4, 4, 101)
    x2 = np.linspace(-4, 4, 101)
    X1, X2 = np.meshgrid(x1, x2)
    funktionswerte = fu.spellucci([X1, X2])
    plt.contourf(X1, X2, funktionswerte, levels=100)
    plt.title("spellucci Minimum")
    plt.plot(min.x[0], min.x[1], 'go')
    plt.text(min.x[0], min.x[1], "Minimum")
    plt.plot(guess[0], guess[1], 'ro')
    plt.text(guess[0], guess[1], "Startwert")
    plt.show()