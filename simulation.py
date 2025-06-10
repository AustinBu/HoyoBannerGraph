from random import random
from bannerchances import CHARACTER_FAIL_CHANCES, WEAPON_FAIL_CHANCES

CHAR_LOSS = 0.5 + (1/14)
WEP_LOSS = 0.75 + (1/28)

def simulateOne(ff, char_or_wep):
    c = random()
    for i in range(1, 91):
        if c > (CHARACTER_FAIL_CHANCES[i] if char_or_wep else WEAPON_FAIL_CHANCES[i]):
            if (ff and random() > (CHAR_LOSS if char_or_wep else WEP_LOSS)):
                return i + simulateOne(False, char_or_wep)
            else:
                return i
            
def simulateMulti(m, ff, char_or_wep):
    out = []
    total = 0
    for _ in range(m):
        step = simulateOne(ff, char_or_wep)
        total += step
        out.append(total)
    return out

def simulateMany(m):
    out = [[] for _ in range(m)]
    for _ in range(10000):
        l = simulateMulti(m, True, True)
        for i, val in enumerate(l):
            out[i].append(val)
    return [sorted(x) for x in out]

def getChance(out, n):
    low = 0
    high = len(out) - 1

    while low <= high:
        mid = (low + high) // 2
        if out[mid] == n:
            return mid
        elif out[mid] < n:
            low = mid + 1
        else:
            high = mid - 1
    return n
