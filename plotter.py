import matplotlib.pyplot as plt
import math
from simulation import *

# number of trials (not pulls)
n = 100000
# number of copies
m = 5
# True for fifty fifties, False to not include (or for Wuthering waves)
ff = True
# True for char, False for wep (or for Wuthering waves)
char_or_wep = False

out = simulateMany(n, m, ff, char_or_wep)

plt.figure(figsize=(10, 6), dpi=120)
plt.xticks(range(0, out[-1][-1], 10 * math.ceil(m/2)))
plt.yticks(range(0, 110, 10))

for x in range(m):
    chances = list((out[x][i-1], i//(n//100)) for i in range(1, n+1, n//100))
    x, y = zip(*chances)
    plt.plot(x, y)

plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)
plt.show()
