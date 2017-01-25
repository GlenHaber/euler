"""
10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""
from math import sqrt


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True

def prime_stream():
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1

def nth_prime(n):
    primes = prime_stream()
    for i in range(n-1):
        next(primes)
    return next(primes)

print(nth_prime(6))
print(nth_prime(10001))