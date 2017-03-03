"""
Diophantine reciprocals II

In the following equation x, y, and n are positive integers.

    1/x + 1/y = 1/n

It can be verified that when n = 1260 there are 113 distinct solutions and this is the least value of n for which the
total number of distinct solutions exceeds one hundred.

What is the least value of n for which the number of distinct solutions exceeds four million?
"""
from functools import reduce
from operator import mul
from time import time
from timeit import timeit

from problem108 import count_factors
from problem47 import prime_sieve

primes = list(prime_sieve(50))


def slow_solve(n):
    i = 1
    while (count_factors(i ** 2) + 1) / 2 <= n:
        i += 1
    return i


def factors(n):
    exps = []
    for p in primes:
        a = 0
        while n % p == 0:
            a += 1
            n //= p
        exps.append(a)
    return exps


def value(exponents):
    return reduce(mul, [p ** e for p, e in zip(primes, exponents)])


exp = factors(1310400)
assert value(exp) == 1310400


def set_twos(exponents, limit):
    # Require (sum(2exp+1 for each exp)+1)/2 > limit
    limit = 2 * limit - 1
    others = reduce(mul, [2 * e + 1 for e in exponents[1:]])
    twos = (limit // others - 1) // 2
    while (2 * twos + 1) * others < limit:
        twos += 1
    exponents[0] = twos
    return exponents


def fast_solve(n):
    exponents = [0] * (len(primes) + 1)
    i = 1
    best = value([1] * len(primes))
    while i < len(primes):
        set_twos(exponents, n)
        if exponents[0] < exponents[1]:
            i += 1
        else:
            # Check
            i = 1
            v = value(exponents)
            if v < best:
                best = v
            pass
        exponents[i] += 1
        for j in range(i):
            exponents[j] = exponents[i]
    return best


if __name__ == '__main__':
    start = time()
    # print(slow_solve(100))
    # print(timeit('slow_solve(100)', 'from __main__ import slow_solve', number=100) / 100)
    print(fast_solve(4000000))
    # print(timeit('fast_solve(100)', 'from __main__ import fast_solve', number=100) / 100)
    print(time() - start)
