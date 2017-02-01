"""
Square root convergence

It is possible to show that the square root of two can be expressed as an infinite continued fraction:

    sqrt(2) = 1 + 1/(2 + 1/(2 + 1/(2 + 1/( + ... ))) = 1.414213

By expanding this for the first four iterations, we get:

    1 + 1/2 = 3/2
    1 + 1/(2 + 1/2) = 7/5
"""
from math import log10, floor

from sympy import Rational


def simplify(depth):
    base = Rational(1, 2)
    for _ in range(depth):
        base = Rational(1, 2 + base)
    return base + 1


expansions = [simplify(d) for d in range(1000)]
print(len(list(filter(lambda r: floor(log10(r.p)) > floor(log10(r.q)), expansions))))
# It turns out every 5th then 8th expansion has len(n) > len(d). So...
print(2 * 1000 // 13)
