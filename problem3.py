"""
Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
"""
from math import sqrt


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True


def prime_factors(num):
    for i in range(2, num // 2 + 1):
        if not is_prime(i):
            continue
        while num % i == 0:
            num //= i
            yield i
        if num == 1:
            break


print(max(prime_factors(600851475143)))
