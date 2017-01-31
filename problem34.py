"""
Digit factorials

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""
from math import factorial


def is_curious(n):
    digits = map(int, str(n))
    return n == sum(map(factorial, digits))

print(is_curious(145))

print(sum(i for i in range(3, 10**8) if is_curious(i)))