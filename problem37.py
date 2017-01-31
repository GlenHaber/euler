"""
Truncatable primes

The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left
to right, and remain prime at each stage: 3797, 797, 97, and 7
"""
import math

from problem3 import is_prime


def is_truncatable(n):
    a = n  # For truncating the left
    b = n  # For truncating the right
    while is_prime(a):
        a %= 10 ** math.floor(math.log10(a))
    while is_prime(b):
        b //= 10
    return a == 0 and b == 0


print(is_truncatable(3797))
primes = set()
i = 21
while len(primes) < 11:
    i += 2
    if is_truncatable(i):
        primes.add(i)
print(sum(primes))
