"""
Coin partitions

Let p(n) represent the number of different ways in which n coins can be separated into piles.
"""
from math import sqrt
from time import time

# Use the same method as problem 76, but mod numbers by 1000000 before storing

known = {0: 1}


def pentagonal(k):
    return k * (3 * k - 1) // 2


def p(n):
    if n < 0:
        return 0
    if n not in known:
        max_k = int((1 + sqrt(1 + 24 * n)) / 6) * 2
        total = 0
        for k in range(1, max_k):
            total += (-1) ** (k - 1) * p(n - pentagonal(k))
            total += (-1) ** (-k - 1) * p(n - pentagonal(-k))
            total %= 1000000
        known[n] = int(total)
    return known[n]


start = time()

n = 0
pn = 1
while pn != 0:
    n += 1
    pn = p(n)
print(n)

print(time() - start)
