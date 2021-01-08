import matplotlib.pyplot as plt
import numpy as np


# Praktikum 1
def plotte_Funktion_surf_contf(X1, X2, funktion, name):
    fig = plt.figure()
    ax = fig.add_subplot(1, 2, 1, projection='3d')
    ax.set_title(name)
    ax.plot_surface(X1, X2, funktion)
    ax = fig.add_subplot(1, 2, 2)
    ax.contourf(X1, X2, funktion, levels=100)
    plt.show()


def rosenbrock(x):
    rosenbrock = 100 * (x[1] - x[0] ** 2) ** 2 + (1 - x[0]) ** 2
    return rosenbrock


def himmelblau(x):
        himmelblau = (x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 -7)**2
        return himmelblau


def bazaraa_shetty(x):
        bazaraa_shetty = (x[0] - 2)**4 + (x[0] - 2*x[1])**2
        return bazaraa_shetty


def beale(x):
        beale = (1.5 - x[0]*(1 - x[1]))**2 + (2.25 - x[0]*(1 - x[1]**2))**2 + (2.625 - x[0]*(1 - x[1]**3))**2
        return beale


def spellucci(x):
        spellucci = 2*x[0]**3 + x[1]**2 + x[0]**2*x[1]**2 + 4*x[0]*x[1] + 3
        return spellucci
