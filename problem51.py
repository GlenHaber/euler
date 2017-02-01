"""
Prime digit replacements

By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values are all prime:
13, 23, 43, 53, 73, and 83.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven
primes among the ten generated numbers, yielding the family:
56003, 56113, 56333, 56443, 56663, 56773, and 56993.

Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit is part of an eight prime value family
"""
import time

from problem47 import prime_sieve

primes = prime_sieve(1000000)
prime_set = set(primes)  # For fast lookup


def check(num):
    num_s = str(num)
    digits = set(num_s)
    max_size = 0
    best_value = 0
    for d in digits:
        nums = list(filter(lambda n: n[0] != '0', (num_s.replace(d, r) for r in '0123456789')))
        nums = list(filter(lambda n: n in prime_set, map(int, nums)))
        if len(nums) > max_size:
            max_size = len(nums)
            best_value = min(nums)
    return max_size, best_value


print(check(13))
print(check(56443))

for p in primes:
    size, value = check(p)
    if size >= 8:
        print(value)
        break
