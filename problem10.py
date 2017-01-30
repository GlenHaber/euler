"""
Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""
from problem3 import is_prime


def prime_sum(ceiling):
    return sum(i for i in range(ceiling) if is_prime(i))


print(prime_sum(10))
print(prime_sum(2000000))
