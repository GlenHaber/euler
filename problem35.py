"""
Circular primes

The number, 197 is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""
from problem3 import is_prime


def rotations(n):
    s = str(n)
    rs = set()
    for i in range(len(s)):
        rs.add(int(s[i:] + s[:i]))
    return rs

def circular_prime(n):
    return all(is_prime(x) for x in rotations(n))

print(len(list(filter(circular_prime, range(2, 100)))))
print(len(list(filter(circular_prime, range(2, 1000000)))))