"""
Triangular, pentagonal, and hexagonal

Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

Triangle	Tn=n(n+1)/2		1, 3, 6, 10, 15, ...
Pentagonal	Pn=n(3n−1)/2	1, 5, 12, 22, 35, ...
Hexagonal	Hn=n(2n−1)		1, 6, 15, 28, 45, ...
It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
"""
from math import sqrt

from problem12 import triangle_numbers
from problem44 import is_pentagonal


def is_hexagonal(num):
    return ((1 + sqrt(1 + 8 * num)) / 4).is_integer()

if __name__ == '__main__':
    for t in triangle_numbers():
        if is_pentagonal(t) and is_hexagonal(t):
            print(t)
            if t > 40755:
                break
