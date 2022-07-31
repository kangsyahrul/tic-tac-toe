import math

def score(x):
    # return x ** 2
    return 1 / (1 + math.exp(-x))

GAME_MATCH = 4
for i in range(GAME_MATCH):
    print(i, score((i)))