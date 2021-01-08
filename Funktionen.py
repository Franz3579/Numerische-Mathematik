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
