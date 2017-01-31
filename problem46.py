"""
Goldbach's other conjecture

It was proposed by Christian Goldbach that every odd composite
number can be written as the sum of a prime and twice a square.

    9 = 7 + 2×1^2
    15 = 7 + 2×2^2
    21 = 3 + 2×3^2
    25 = 7 + 2×3^2
    27 = 19 + 2×2^2
    33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""
from math import sqrt

from problem3 import is_prime


def odd_composites():
    n = 9
    while True:
        if not is_prime(n):
            yield n
        n += 2


def check(n):
    squares = [i for i in range(1, n//2) if sqrt(i).is_integer()]
    return any(is_prime(n-2*s) for s in squares)

for i in odd_composites():
    if not check(i):
        break
print(i)