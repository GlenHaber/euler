"""
Pandigital prime

We shall say than an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example,
2143 is a p-digit pandigital and is also prime.
"""
from itertools import permutations, chain

from problem3 import is_prime


def gen_pandigitals(length):
    digits = reversed('123456789'[:length])
    for c in permutations(digits):
        yield int(''.join(c))


pangen = chain.from_iterable([gen_pandigitals(n) for n in range(9, 0, -1)])
for p in pangen:
    if is_prime(p):
        print(p)
        break
