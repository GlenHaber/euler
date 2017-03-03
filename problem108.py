"""
Diaphantine reciprocals I

In the following equation x, y, and n are positive integers.

    1/x + 1/y = 1/n

For n = 4 there are exactly three distinct solutions:

    1/5 + 1/20 = 1/4
    1/6 + 1/12 = 1/4
    1/8 + 1/8 = 1/4

What is the least value of n for which the number of distinct solutions exceeds one-thousand?
"""
# 1/x + 1/y = 1/n; let x=n+r, y=n+s
#   1/(n+r) + 1/(n+s) = 1/n
#     n(n+s) + n(n+r) = (n+r)(n+s)
# n^2 + ns + n^2 + nr = n^2 + nr + ns + rs
#                 n^2 = rs
from functools import reduce
from operator import mul
from time import time

from problem47 import prime_sieve


def count_solutions(n):
    count = 0
    for i in range(1, n + 1):
        if n ** 2 % i == 0:
            count += 1
    return count


primes = list(prime_sieve(20))


def count_factors(n):
    # This is much faster
    exps = []
    for p in primes:
        a = 0
        while n % p == 0:
            a += 1
            n //= p
        exps.append(a)
    return reduce(mul, [x + 1 for x in exps])


if __name__ == '__main__':
    start = time()
    i = 1
    while (count_factors(i ** 2) + 1) / 2 <= 1000:
        i += 1
    print('Answer:', i)
    print(time() - start)

    # Slower version!
    # i = 1
    # while True:
    #     solutions = count_solutions(i)
    #     if i % 10000 == 0:
    #         print(i, solutions)
    #     if solutions > 1000:
    #         break
    #     i += 1
