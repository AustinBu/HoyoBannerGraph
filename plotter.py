import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import math
from simulation import *

def createPlot(copies):
    out = simulateMany(copies)

    plt.figure(figsize=(10, 6), dpi=120)
    plt.xticks(range(0, out[-1][-1], 10 * math.ceil(copies/2)))
    plt.yticks(range(0, 110, 10))
    for x in range(copies):
        chances = list((out[x][i-1], i//(100)) for i in range(1, 10001, 100))
        x, y = zip(*chances)
        plt.plot(x, y)

    plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)
    plt.savefig("plot.png")
    plt.close()

createPlot(7)