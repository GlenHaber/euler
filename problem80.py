"""
Square root digital expansion

It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal
expansion of such square roots is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits
for all the irrational square roots.
"""

from time import time

from problem16 import digital_sum

start = time()


def expand_root(c):
    p = 0
    for _ in range(100):
        x = 9
        while x * (20 * p + x) > c:
            x -= 1
        y = x * (20 * p + x)
        p = 10 * p + x
        c = (c - y) * 100
        if c == 0:
            return None
    return digital_sum(p)


sums = map(expand_root, range(2, 100))
print(sum(s for s in sums if s))
print(time() - start)
