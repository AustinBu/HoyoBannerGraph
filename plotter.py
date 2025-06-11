import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import math
from simulation import *

def createPlot(copies, pulls):
    out = simulateMany(7)
    chance = 0

    plt.figure(figsize=(10, 6), dpi=120)
    plt.xticks(range(0, pulls+1, 5 * math.ceil(pulls//100)))
    plt.yticks(range(0, 110, 10))
    for z in range(copies):
        chances = list((out[z][i-1], i//(100)) for i in range(1, 10001, 100))
        if (z == copies-1):
            for (a, b) in chances:
                if a > pulls:
                    chance = b
                    break
        x, y = zip(*chances)
        plt.plot(x, y)

    plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)
    plt.xlim(left=0)
    plt.xlim(xmax=pulls+10)
    plt.savefig("plot.png")
    plt.close()
    return chance

createPlot(7, 600)