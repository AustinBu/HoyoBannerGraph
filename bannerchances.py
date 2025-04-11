import numpy as np

WEAPON_CHANCE = 0.008
CHARACTER_CHANCE = 0.006

i = np.arange(1, 90)
character_chances = np.full_like(i, CHARACTER_CHANCE, dtype=np.float64)
mask = i > 73
character_chances[mask] += ((1 - CHARACTER_CHANCE) / 17) * (i[mask] - 73)

CHARACTER_FAIL_CHANCES = np.empty(91, dtype=np.float64)
CHARACTER_FAIL_CHANCES[0] = 1.0
CHARACTER_FAIL_CHANCES[1:90] = np.cumprod(1 - character_chances)
CHARACTER_FAIL_CHANCES[90] = 0.0

i = np.arange(1, 80)
weapon_chances = np.full_like(i, WEAPON_CHANCE, dtype=np.float64)
mask = i > 65
weapon_chances[mask] += ((1 - WEAPON_CHANCE) / 15) * (i[mask] - 63)

WEAPON_FAIL_CHANCES = np.empty(81, dtype=np.float64)
WEAPON_FAIL_CHANCES[0] = 1.0
WEAPON_FAIL_CHANCES[1:80] = np.cumprod(1 - weapon_chances)
WEAPON_FAIL_CHANCES[80] = 0.0
