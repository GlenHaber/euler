"""
Amicable numbers

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

from math import sqrt, ceil


def proper_divisors(n):
    divisors = set()
    for i in range(1, ceil(sqrt(n))+1):
        if n % i == 0:
            divisors.update({i, n // i})
    return divisors - {n}


def d(n):
    return sum(proper_divisors(n))


def is_amicable(n):
    return d(n) != n and d(d(n)) == n

if __name__ == '__main__':
    print(sum(n for n in range(10000) if is_amicable(n)))
