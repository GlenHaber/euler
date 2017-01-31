"""
Pandigital products

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example,
the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1
through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""
import math


def check_pandigital(a, b):
    return sorted(''.join([str(a), str(b), str(a * b)])) == list('123456789')


def unique_range(ceil):
    for i in range(ceil):
        if len(set(str(i))) == len(str(i)) and '0' not in str(i):
            yield i

ceiling = math.ceil(math.sqrt(987654321))
print(ceiling)

print(sum({a* b for a in unique_range(ceiling) for b in unique_range(a) if check_pandigital(a, b)}))