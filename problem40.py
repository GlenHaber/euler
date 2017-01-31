"""
Champernowne's constant

An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If d(n) represents the nth digit of the fractional part, find the value of the following expression.

d(1) × d(10) × d(100) × d(1000) × d(10000) × d(100000) × d(1000000)
"""
from math import log10


def digits(n):
    return list(map(int, str(n)))

def champernowne():
    i = 0
    while True:
        i += 1
        for d in digits(i):
            yield d

c = champernowne()
product = 1
for i in range(1, 1000001):
    value = next(c)
    if log10(i).is_integer():
        product *= value
print(product)