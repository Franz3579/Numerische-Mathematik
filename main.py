import matplotlib
import math as m


def getErgebnisse(mxland, mxwasser, vland, vwasser, iterationen):
    """
    Mit dieser Funktion sollen die Ergebnisse xland, xwasser und Zeit des Problems "Rette Mensch in Wasser"
    in einer Liste gespeichert werden.
    unsere Variablen sind xland und xwasser. Die Zeit soll minimiert werden.

    xland/vland + xwasser/vwasser = zeit
    N.B. xwasser = sqrt(mxwasser^2 + (mxland - xland)^2)
    => zeit = xland/vland + sqrt(mxwasser^2 + (mxland - xland)^2)/vwasser
    """
    ergebnisse = []
    iterationenlist = list(range(iterationen))

    for i in iterationenlist:
        # Berechne Werte
        xland = i * mxland/(iterationen-1)
        xwasser = m.sqrt(m.pow(mxwasser, 2) + m.pow((mxland - xland), 2))
        zeit = xland/vland + m.sqrt(m.pow(mxwasser, 2) + m.pow((mxland - xland), 2))/vwasser

        # Trage Werte in Liste ein
        ergebnisse.append([xland, xwasser, zeit])

    return ergebnisse


def dastellenErgebnisse(ergebnisse):
    """Mit dieser Funktion sollen die Ergebnisse des Problems "Rette Mensch in Wasser" dargestellt werden"""

    return

def getBestTime(ergebnisse):
    pass

if __name__ == '__main__':
    print(getErgebnisse(100, 50, 5, 2, 10))