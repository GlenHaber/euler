"""
Counting summations

It is possible to write five as a sum in exactly six different ways:

4+1
3+2
3+1+1
2+2+1
2+1+1+1
1+1+1+1+1

How many different ways can one hundred be written as a sum of at least two positive integers?
"""
# This problem refers to the partition function, minus the trivial case of one term.
from math import sqrt
from time import time

known = {0: 1}


def pentagonal(k):
    return k * (3 * k - 1) // 2


def p(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif n not in known:
        max_k = int((1 + sqrt(1 + 24 * n)) / 6) * 2
        total = 0
        for k in range(1, max_k):
            total += (-1) ** (k - 1) * p(n - pentagonal(k))
            total += (-1) ** (-k - 1) * p(n - pentagonal(-k))
        total = int(total)
        known[n] = total
    return known[n]

start = time()
print(p(100)-1)
print(time() - start)