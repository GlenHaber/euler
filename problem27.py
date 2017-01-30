"""
Quadratic primes

Euler discovered the remarkable quadratic formula:

n^2+n+41

It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39.
However, when n=40,402+40+41=40(40+1)+41n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when
n=41,412+41+41 is clearly divisible by 41.

The incredible formula n2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79.
The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n^2+an+b, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4|
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes
for consecutive values of n, starting with n=0.

"""
from problem3 import is_prime


def count_quadratic_primes(a, b):
    def func(n):
        return n ** 2 + a * n + b

    i = 0
    while is_prime(func(i)):
        i += 1
    return i


print(count_quadratic_primes(1, 41))
print(count_quadratic_primes(-79, 1601))
a, b = max(((a, b) for a in range(-999, 1000) for b in range(-1000, 1001)),
           key=lambda pair: count_quadratic_primes(pair[0], pair[1]))
print(a * b)
