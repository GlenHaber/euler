"""Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
from collections import defaultdict
from functools import reduce


def prime_factors(num):
    factors = defaultdict(lambda: 0)
    i = 2
    while num > 1:
        while num % i == 0:
            num //= i
            factors[i] += 1
        i += 1
    return factors


def smallest_multiple(min_factor, max_factor):
    all_factors = defaultdict(lambda: 0)
    for i in range(min_factor, max_factor + 1):
        factors = prime_factors(i)
        for f, count in factors.items():
            all_factors[f] = max(all_factors[f], count)
    return reduce(lambda x, y: x * y, [factor ** count for factor, count in all_factors.items()])


print(smallest_multiple(1, 10))
print(smallest_multiple(1, 20))
