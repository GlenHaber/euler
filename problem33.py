"""
Digit cancelling fractions

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly
believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits
in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""
import math
from functools import reduce
from operator import mul


def simplify(num, denom):
    factor = math.gcd(num, denom)
    return num // factor, denom // factor


def check(num, denom):
    num_digits = [num // 10, num % 10]
    den_digits = [denom // 10, denom % 10]
    cancel = list(set(num_digits).intersection(den_digits))
    if cancel == [0]:
        return False
    if cancel:
        num_digits.remove(cancel[0])
        den_digits.remove(cancel[0])
        return simplify(num, denom) == simplify(num_digits[0], den_digits[0])
    return False


results = set()
for n in range(10, 100):
    for d in range(n + 1, 100):
        if check(n, d):
            results.add(simplify(n, d))

n = reduce(mul, [r[0] for r in results])
d = reduce(mul, [r[1] for r in results])
print(simplify(n, d)[1])
